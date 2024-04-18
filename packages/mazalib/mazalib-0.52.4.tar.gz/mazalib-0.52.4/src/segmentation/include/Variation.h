#pragma once

#include "DynamicArray.h"
#include "Grid.h"
#include "LogFile.h"
#include "Point.h"
#include "util.h"


enum VariogramType { 
  Semivariogram,
  Covariance
};


class Variogram : public DynamicArray<double> {
public:
  Variogram(size_t max_distance = 1UL, double distance_step = 1.0)
      : DynamicArray<double>(max_distance + 1UL, 0.0), distance_step_(distance_step), variogram_type_(VariogramType::Semivariogram) {}
  Variogram(const Variogram &v)
      : DynamicArray<double>(v), distance_step_(v.distance_step_), variogram_type_(v.variogram_type_) {}

  double Variance() const { return (*this)[0]; }
  
  double UnitLag() const { return distance_step_; };

  int MaxDistance() const { return static_cast<int>(size()) - 1; };

  VariogramType Type() const { return variogram_type_; };

  double operator()(const double x) const;

  template <class Iterator>
  void Compute(Iterator image_data_itr, const Grid &grid) {
    fill(this->begin(), this->end(), 0.0);

    int size_x = grid.n_x();
    int size_y = grid.n_y();
    int size_z = grid.n_z();

    int max_dist = MaxDistance();

    const int size_ = static_cast<int>(this->size());
    std::vector<double> partial_variogram(size_, 0.0);
    std::vector<double> norm(size_, 0.0);
    std::vector<double> norm_cumulative(size_, 0.0);

    typedef typename Iterator::value_type T;

    size_t total_n_voxels = (size_t)size_x * size_y * size_z;

    // Subsample 1 of 1000
    const size_t denominator = 1000;
    size_t n_samples = total_n_voxels / denominator;

    // Do not subsample for small images
    size_t stride = total_n_voxels / n_samples;
    if (n_samples < denominator) {
      n_samples = total_n_voxels;
      stride = 1UL;
    }

    try {
      // Subsampling
      for (size_t index = 0UL; index < total_n_voxels - stride; index += stride) {
        ComputePartialVariogramAtPoint(image_data_itr, partial_variogram, norm, size_x, size_y, size_z, index, max_dist);
        for (int h = 1; h < size_; ++h) {
          (*this)[h] += partial_variogram[h];
          norm_cumulative[h] += norm[h]; 
        }
      }

      // Normalization
      for (size_t h = 1; h <= max_dist; ++h) {
        (*this)[h] *= 0.5 / norm_cumulative[h];
      }

    } catch (std::exception &e) {
      std::cerr << "Something wrong in variogram computation" << std::endl;
    }

    this->front() = Utils::variance(image_data_itr, image_data_itr + grid.size());
  }

  void TransformToCovariance() {
    // change to covariance by var-gamma(r)
    if (variogram_type_ != VariogramType::Semivariogram) {
      return;
    }
    variogram_type_ = VariogramType::Covariance;
    double variance = front();
    for (auto i = 1; i < size(); ++i) {
      (*this)[i] = variance - (*this)[i];
    }
  }

private:

  template <class Iterator>
  void ComputePartialVariogramAtPoint(Iterator image_data_itr,
                                      std::vector<double> &partial_variogram,
                                      std::vector<double> &norm,
                                      int size_x, int size_y, int size_z,
                                      size_t sample_index,
                                      int max_distance) {
    const int slice_size = size_y * size_x;

    const int z = static_cast<int>(sample_index / slice_size);
    const size_t rest_of_slices = sample_index - z * slice_size;
    const int y = static_cast<int>(rest_of_slices / size_x);
    const int x = static_cast<int>(rest_of_slices % size_x);
    double center_value = static_cast<double>(*(image_data_itr + sample_index));

    for (size_t h = 0; h <= max_distance; ++h)
    {
      partial_variogram[h] = 0.0;
      norm[h] = 0.0;
    }

    for (int h = -max_distance; h <= max_distance; ++h)
    {
      if (h == 0) { continue; }
      size_t current_lag = static_cast<size_t>(abs(h));

      // Offset in X
      int current_x = x + h;
      if (current_x >= 0 && current_x < size_x) {
        size_t current_idx = z * slice_size + y * size_x + current_x;
        double current_value = static_cast<double>(*(image_data_itr + current_idx));
        double delta = current_value - center_value;
        partial_variogram[current_lag] += delta * delta;
        norm[current_lag] += 1.0;
      }

      // Offset in Y
      int current_y = y + h;
      if (current_y >= 0 && current_y < size_y) {
        size_t current_idx = z * slice_size + current_y * size_x + x;
        double current_value = static_cast<double>(*(image_data_itr + current_idx));
        double delta = current_value - center_value;
        partial_variogram[current_lag] += delta * delta;
        norm[current_lag] += 1.0;
      }

      // Offset in Z
      int current_z = z + h;
      if (current_z >= 0 && current_z < size_z) {
        size_t current_idx = current_z * slice_size + y * size_x + x;
        double current_value = static_cast<double>(*(image_data_itr + current_idx));
        double delta = current_value - center_value;
        partial_variogram[current_lag] += delta * delta;
        norm[current_lag] += 1.0;
      }
    }
  }

  double distance_step_;
  VariogramType variogram_type_;
};