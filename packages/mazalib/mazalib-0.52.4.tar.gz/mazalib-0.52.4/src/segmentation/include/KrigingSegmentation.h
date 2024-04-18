#ifndef SEGMENT_H
#define SEGMENT_H
#include "DynamicArray.h"
#include <Eigen/Dense.h>

#include "Grid.h"
#include "LatticeModel.h"
#include "Variation.h"
#include "threshold.h"
#include <cstring>

struct DataDescription {
  int W;
  int H;
  int D;
};

struct KrigingSettings {
  KrigingSettings() : Radius(3) {}

  int Radius;
  int SegMethod;
  ThresholdSettings ThresholdParams;
};

class KrigingProcessor : public LatticeModel {
  using ElemType = int;
  using ContainerType = typename std::vector<ElemType>;
  using LatticeIterator = typename std::vector<ElemType>::iterator;
  using LatticeConstIterator = typename std::vector<ElemType>::const_iterator;

  const ElemType PHASE_0 = static_cast<ElemType>(0);
  const ElemType PHASE_1 = static_cast<ElemType>(1);
  const ElemType UNDEFINED = static_cast<ElemType>(50);

public:
  KrigingProcessor(KrigingSettings &sp, const DataDescription &dd);
  void ComputeVriogramBetweenThresholds() {}
  void SolveOrdinaryKriging(DynamicArray<double> &matrix_data,
                            DynamicArray<double> &kriging_weights,
                            size_t kriging_vector_len, Variogram &variogram,
                            const Point *neighborhood);
  void CoerceNegativeWeights(double *weights, size_t kriging_vector_len,
                             const Variogram &covariance,
                             const Point *neighborhood);
  void Proceed(const ContainerType &input_image,
               ContainerType &segmented_image);
  size_t InitSeedRegions(const ContainerType &input_image,
                         ContainerType &segmented_image);
  void BuildCDFs(const ContainerType &input_image, CDF &phase_0_cdf,
                 CDF &phase_1_cdf);
  void FillCDF(CDF &cdf, double lower_boundary, double upper_boundary);
  void BuildVariograms(const ContainerType &input_image,
                       ContainerType &segmented_image,
                       const CDF &cdf_of_phase_0, const CDF &cdf_of_phase_1,
                       Variogram &var_phase_0, Variogram &var_phase_1);
  void ApplyKrigingModel(const ContainerType &input_image,
                         ContainerType &segmented_image, size_t n_of_data,
                         const CDF &cdf_of_phase_0, const CDF &cdf_of_phase_1,
                         const DynamicArray<double> &rhs_phase_0,
                         const DynamicArray<double> &rhs_phase_1);
  void SetupOrdinaryKriging(std::vector<double> &mat, size_t kriging_vector_len,
                            const Variogram &covariance,
                            const Point *neighborhood);
  size_t BuildNeighborhood(Point *neighborhood);
  void CollectValuesFromNeighborhood(const ContainerType &input_image,
                                     ContainerType &segmented_image,
                                     size_t plain_idx,
                                     double *intermediate_data, const CDF &cdf);

private:
  Grid grid;
  Threshold<ElemType> threshold;
  DataDescription dimensions;
  KrigingSettings settings;
};

#endif
