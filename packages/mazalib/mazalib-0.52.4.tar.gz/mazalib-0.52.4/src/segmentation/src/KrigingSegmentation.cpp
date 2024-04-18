#include "KrigingSegmentation.h"

const int grid_dim = 3;

KrigingProcessor::KrigingProcessor(KrigingSettings &settings,
                                   const DataDescription &dimensions)
    : LatticeModel(2) {
  threshold.Setup(settings.ThresholdParams);

  Point L(0.0, 0.0, 0.0);
  Point U(static_cast<double>(dimensions.W), static_cast<double>(dimensions.H),
          static_cast<double>(dimensions.D));

  int size[grid_dim] = {dimensions.W, dimensions.H, dimensions.D};
  grid.set(grid_dim, L, U, size, 0, 0);

  this->settings = settings;
  this->dimensions = dimensions;
}

void KrigingProcessor::BuildCDFs(const ContainerType &input_image,
                                 CDF &phase_0_cdf, CDF &phase_1_cdf) {
  const int histogram_length = 256;
  Histogram hist(input_image, histogram_length);
  phase_0_cdf = CDF(hist);
  phase_1_cdf = CDF(hist);

  this->StatsNL(input_image, threshold.HighThresholds(),
                threshold.LowThresholds(), this->means, this->vars);

  double middle_threshold_point = 0.0;
  if (abs(this->vars[0] + this->vars[1]) < EPS_THINY) {
    middle_threshold_point = threshold.HighThresholds()[0];
  } else {
    middle_threshold_point =
        threshold.HighThresholds()[0] +
        (this->vars[0]) / (this->vars[0] + this->vars[1]) *
            (threshold.LowThresholds()[1] - threshold.HighThresholds()[0]);
  }

  FillCDF(phase_0_cdf, threshold.HighThresholds()[0], middle_threshold_point);
  FillCDF(phase_1_cdf, middle_threshold_point, threshold.LowThresholds()[1]);
}

void KrigingProcessor::BuildVariograms(const ContainerType &input_image,
                                       ContainerType &segmented_image,
                                       const CDF &cdf_of_phase_0,
                                       const CDF &cdf_of_phase_1,
                                       Variogram &var_phase_0,
                                       Variogram &var_phase_1) {
  // Create float version of input image
  const auto data_size = input_image.size();
  std::vector<float> float_image(data_size);
  for (size_t idx = 0UL; idx < data_size; ++idx) {
    if (segmented_image[idx] == PHASE_0) {
      float_image[idx] = 1.0;
    } else if (segmented_image[idx] == PHASE_1) {
      float_image[idx] = 0.0;
    } else {
      auto input_value = static_cast<double>(input_image[idx]);
      float_image[idx] = static_cast<float>(cdf_of_phase_0.F(input_value));
    }
  }
  var_phase_0.Compute(float_image.begin(), grid);

  for (size_t idx = 0UL; idx < data_size; ++idx) {
    if (segmented_image[idx] == UNDEFINED) {
      auto input_value = static_cast<double>(input_image[idx]);
      float_image[idx] = static_cast<float>(cdf_of_phase_1.F(input_value));
    }
  }
  var_phase_1.Compute(float_image.begin(), grid);

  var_phase_0.TransformToCovariance();
  var_phase_1.TransformToCovariance();
}

void KrigingProcessor::Proceed(const ContainerType &input_image,
                               ContainerType &segmented_image) {
  size_t data_size = input_image.size();
  for (auto &segm_value : segmented_image) {
    segm_value = PHASE_0;
  }
  size_t unsegmented_voxels_count =
      InitSeedRegions(input_image, segmented_image);
  if (unsegmented_voxels_count == 0UL) {
    return;
  }

  CDF cdf_of_phase_0, cdf_of_phase_1;
  BuildCDFs(input_image, cdf_of_phase_0, cdf_of_phase_1);

  const int radius = settings.Radius;
  const int variogram_length = int(sqrt(double(grid_dim)) * 2 * radius);
  Variogram var_phase_0(variogram_length, 1.0);
  Variogram var_phase_1(variogram_length, 1.0);
  BuildVariograms(input_image, segmented_image, cdf_of_phase_0, cdf_of_phase_1,
                  var_phase_0, var_phase_1);

  Point *neighborhood = new Point[ipow(2 * radius + 1, grid_dim)];
  size_t kriging_vector_len = BuildNeighborhood(neighborhood);

  DynamicArray<double> kriging_matrix_phase_0;
  DynamicArray<double> kriging_matrix_phase_1;
  DynamicArray<double> kriging_coeffs_phase_0;
  DynamicArray<double> kriging_coeffs_phase_1;

  SolveOrdinaryKriging(kriging_matrix_phase_0, kriging_coeffs_phase_0,
                       kriging_vector_len, var_phase_0, neighborhood);
  SolveOrdinaryKriging(kriging_matrix_phase_1, kriging_coeffs_phase_1,
                       kriging_vector_len, var_phase_1, neighborhood);
  delete[] neighborhood;

  ApplyKrigingModel(input_image, segmented_image, kriging_vector_len,
                    cdf_of_phase_0, cdf_of_phase_1, kriging_coeffs_phase_0,
                    kriging_coeffs_phase_1);
}

void KrigingProcessor::ApplyKrigingModel(
    const ContainerType &input_image, ContainerType &segmented_image,
    size_t kriging_vector_len, const CDF &cdf_of_phase_0,
    const CDF &cdf_of_phase_1, const DynamicArray<double> &rhs_phase_0,
    const DynamicArray<double> &rhs_phase_1) {
  DynamicArray<double> intermediate_data_phase_0(kriging_vector_len);
  DynamicArray<double> intermediate_data_phase_1(kriging_vector_len);

  ContainerType presegmented_image(segmented_image.size());
  std::copy(segmented_image.begin(), segmented_image.end(),
            presegmented_image.begin());

  for (size_t idx = 0; idx < segmented_image.size(); ++idx) {
    if (segmented_image[idx] != UNDEFINED) {
      continue;
    }

    if (input_image[idx] < threshold.LowThresholds()[0] ||
        input_image[idx] > threshold.LowThresholds()[1]) {
      continue;
    }
    CollectValuesFromNeighborhood(input_image, presegmented_image, idx,
                                  intermediate_data_phase_0.begin_pointer(),
                                  cdf_of_phase_0);
    CollectValuesFromNeighborhood(input_image, presegmented_image, idx,
                                  intermediate_data_phase_1.begin_pointer(),
                                  cdf_of_phase_1);

    double phase_0_prob = std::inner_product(
        rhs_phase_0.begin(), rhs_phase_0.begin() + kriging_vector_len,
        intermediate_data_phase_0.begin(), 0.0);
    double phase_1_prob = std::inner_product(
        rhs_phase_1.begin(), rhs_phase_1.begin() + kriging_vector_len,
        intermediate_data_phase_1.begin(), 0.0);

    if (phase_0_prob > 1.0 - phase_1_prob) {
      segmented_image[idx] = PHASE_0;
    } else {
      segmented_image[idx] = PHASE_1;
    }
  }
}

size_t KrigingProcessor::InitSeedRegions(const ContainerType &input_image,
                                         ContainerType &segmented_image) {
  size_t unsegmented_voxels_count = 0UL;
  const size_t size = input_image.size();
  for (size_t i = 0; i < size; ++i) {
    auto float_image_value = static_cast<double>(input_image[i]);
    if (float_image_value <= threshold.HighThresholds()[0] - EPS_THINY) {
      segmented_image[i] = PHASE_0;
    } else if (float_image_value >= threshold.LowThresholds()[1] + EPS_THINY) {
      segmented_image[i] = PHASE_1;
    } else {
      ++unsegmented_voxels_count;
      segmented_image[i] = UNDEFINED;
    }
  }
  return unsegmented_voxels_count;
}

void KrigingProcessor::SolveOrdinaryKriging(
    DynamicArray<double> &matrix_data, DynamicArray<double> &kriging_weights,
    size_t kriging_vector_len, Variogram &variogram,
    const Point *neighborhood) {
  size_t rank = kriging_vector_len + 1;
  matrix_data.resize(rank * rank);
  kriging_weights.resize(rank);

  SetupOrdinaryKriging(matrix_data, kriging_vector_len, variogram,
                       neighborhood);

  Eigen::MatrixXd mat(rank, rank);
  Eigen::VectorXd rhs_vec(rank);

  for (size_t row = 0UL; row < kriging_vector_len; ++row) {
    rhs_vec[row] = variogram(neighborhood[row].abs());
  }
  rhs_vec[kriging_vector_len] = 1.0;

  for (size_t col = 0; col < rank; col++) {
    for (size_t row = 0; row < rank; row++) {
      size_t plain_idx = row * rank + col;
      mat(col * rank + row) = matrix_data[plain_idx];
    }
  }

  Eigen::VectorXd result(rank);
  result = mat.fullPivHouseholderQr().solve(rhs_vec);

  for (int i = 0; i < kriging_weights.size(); i++) {
    kriging_weights[i] = result[i];
  }

  double sum =
      std::accumulate(kriging_weights.begin(),
                      kriging_weights.begin() + kriging_vector_len, 0.0);
  if ((fabs(sum - 1.0) > EPS_THINY)) {
    std::cout << "Ordinary kriging system solution does not converge"
              << std::endl;
  }
  CoerceNegativeWeights(kriging_weights.begin_pointer(), kriging_vector_len,
                        variogram, neighborhood);
}

void KrigingProcessor::CoerceNegativeWeights(double *weights,
                                             size_t kriging_vector_len,
                                             const Variogram &covariance,
                                             const Point *neighborhood) {
  DynamicArray<int64_t> index(kriging_vector_len);
  size_t neg_index = 0;
  double average_neg_weight = 0.0;
  double average_covariance_of_neg = 0.0;
  for (size_t i = 0; i < kriging_vector_len; ++i) {
    if (weights[i] < 0.0) {
      average_neg_weight -= weights[i];
      average_covariance_of_neg += covariance(neighborhood[i].abs());
      index[neg_index++] = i;
    }
  }
  if (neg_index == 0UL) {
    return;
  }

  size_t n_negative = neg_index;
  average_neg_weight /= n_negative;
  average_covariance_of_neg /= n_negative;
  double stat_sum = 0.0;
  for (size_t i = 0; i < kriging_vector_len; ++i) {
    if (weights[i] < 0.0) {
      weights[i] = 0.0;
    } else if (covariance(neighborhood[i].abs()) < average_covariance_of_neg &&
               weights[i] < average_neg_weight) {
      weights[i] = 0.0;
    }
    stat_sum += weights[i];
  }
  for (size_t i = 0; i < kriging_vector_len; ++i) {
    weights[i] /= stat_sum;
  }
}

void KrigingProcessor::FillCDF(CDF &cdf, double lower_boundary,
                               double upper_boundary) {
  double inner_lower_boundary = cdf.x_0();
  double inner_upper_boundary = cdf.x_n();
  double step = cdf.delta();

  if (lower_boundary < inner_lower_boundary) {
    lower_boundary = inner_lower_boundary;
  }
  if (upper_boundary > inner_upper_boundary) {
    upper_boundary = inner_upper_boundary;
  }

  double lower_value = cdf.F(lower_boundary);
  double upper_value = cdf.F(upper_boundary);

  double x = inner_lower_boundary;
  for (size_t idx = 0; idx < cdf.size(); ++idx, x += step) {
    if (x < lower_boundary) {
      cdf[idx] = 1.0;
    } else if (x < upper_boundary) {
      cdf[idx] = (upper_value - cdf[idx]) / (upper_value - lower_value);
    } else {
      cdf[idx] = 0.0;
    }
  }
}

void KrigingProcessor::SetupOrdinaryKriging(std::vector<double> &mat,
                                            size_t kriging_vector_len,
                                            const Variogram &covariance,
                                            const Point *neighborhood) {
  size_t rank = kriging_vector_len + 1;

  for (size_t row = 0; row < kriging_vector_len; ++row) {
    for (size_t col = 0; col < row; ++col) {
      double gamma = covariance(dist(neighborhood[row], neighborhood[col]));
      mat[row * rank + col] = gamma;
      mat[rank * col + row] = gamma;
    }
    mat[row * rank + row] = 0.0;
  }

  for (int i = 0; i < kriging_vector_len; ++i) {
    mat[kriging_vector_len * rank + i] = 1.0;
    mat[(i + 1) * rank - 1] = 1.0;
  }
  mat[rank * rank - 1] = 0.0;
}

size_t KrigingProcessor::BuildNeighborhood(Point *neighborhood) {
  size_t neighborhood_volume = 0UL;
  const int radius = settings.Radius;
  const int squared_radius = radius * radius;

  for (int k = -radius; k <= radius; ++k) {
    for (int j = -radius; j <= radius; ++j) {
      for (int i = -radius; i <= radius; ++i) {
        int squared_dist = k * k + j * j + i * i;
        if (squared_dist > squared_radius)
          continue;
        if (k == 0 && j == 0 && i == 0)
          continue;
        neighborhood[neighborhood_volume] = Point(i, j, k);
        ++neighborhood_volume;
      }
    }
  }
  return neighborhood_volume;
}

void KrigingProcessor::CollectValuesFromNeighborhood(
    const ContainerType &input_image, ContainerType &segmented_image,
    size_t plain_idx, double *intermediate_data, const CDF &cdf) {
  int radius = settings.Radius;
  int depth = grid.n_z();
  int rows = grid.n_y();
  int cols = grid.n_x();

  const int cz = static_cast<int>(plain_idx / (cols * rows));
  const int cy = static_cast<int>((plain_idx - cz * cols * rows) / cols);
  const int cx = static_cast<int>((plain_idx - cz * cols * rows) % cols);

  size_t data_index = 0UL;
  for (int64_t z = cz - radius; z <= cz + radius; ++z) {
    for (int64_t y = cy - radius; y <= cy + radius; ++y) {
      for (int64_t x = cx - radius; x <= cx + radius; ++x) {
        if ((z - cz) * (z - cz) + (y - cy) * (y - cy) + (x - cx) * (x - cx) >
            radius * radius) {
          continue;
        }
        if ((z == cz) && (y == cy) && (x == cx)) {
          continue;
        }

        if (z < 0 || z >= depth || y < 0 || y >= rows || x < 0 || x >= cols) {
          intermediate_data[data_index] = 0.5;
        } else {
          size_t index = (z * rows + y) * cols + x;
          ElemType pi = segmented_image[index];
          if (pi == PHASE_0) {
            intermediate_data[data_index] = 1.0;
          } else if (pi == PHASE_1) {
            intermediate_data[data_index] = 0.0;
          } else {
            double value = input_image[index];
            intermediate_data[data_index] = cdf.F(value);
          }
        }
        data_index++;
      }
    }
  }
}
