#include "Variation.h"
#include "threshold.h"


double Variogram::operator()(const double distance_accurate) const
{
	int dist = int(distance_accurate/distance_step_);

	if (dist == 0) {
	    if( variogram_type_ == VariogramType::Covariance ) {
		  return linear_interpolate(distance_accurate, 0, distance_step_, front(), (*this)[1]);
		}
	    else {
		  return linear_interpolate(distance_accurate, 0, distance_step_, 0.0, (*this)[1]);
		}
	}

	if (dist < MaxDistance())
	{
		return linear_interpolate(distance_accurate,
		                          dist * distance_step_,
								  (dist + 1) * distance_step_,
								  (*this)[dist],
								  (*this)[dist + 1]);
	}

	if (dist == MaxDistance()) {
		return linear_interpolate(distance_accurate,
		                          dist * distance_step_,
				                  (dist + 1) * distance_step_,
							      (*this)[dist],
							      front());
	}
    return (variogram_type_ == VariogramType::Covariance) ? 0.0 : front();
}
