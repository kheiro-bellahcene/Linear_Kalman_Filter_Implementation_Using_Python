# 2D Vehicle Tracking Using Linear Kalman Filter

## Simulation and Results

![Kalman Tracking GIF](images/kalman_tracking.gif)

This project demonstrates the use of a Linear Kalman Filter to track a vehicle’s position and velocity in 2D space.

## Summary

- The Kalman filter estimation (blue) converges effectively towards the true vehicle state (red).
- The uncertainty ellipse decreases over time, indicating increasing precision in the estimates.
- Position and velocity errors converge towards zero and remain bounded within the ±3 sigma confidence interval, as shown in the second figure.
- The Mean Squared Error (MSE) values at the end of the simulation are:
  - Position MSE: 27.65 m²
  - Velocity MSE: 2.68 (m/s)²
- Innovation (the difference between prediction and measurement) is well-behaved:
  - Standard deviations of innovation are 10.34 m (X) and 11.16 m (Y).
  - The innovation mean is approximately zero, indicating unbiased estimates.

## Conclusion

The Linear Kalman Filter proves effective for 2D vehicle tracking, providing accurate and reliable state estimation.
