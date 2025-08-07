# 2D Vehicle Tracking Using Linear Kalman Filter

This project demonstrates the application of a Linear Kalman Filter for tracking a vehicle's position and velocity in 2D space.

## Overview

- The Kalman filter's estimated state (blue) converges to the actual vehicle state (red).
- The uncertainty ellipse decreases over time, reflecting increasing confidence in the estimates.
- Position and velocity errors converge to zero and remain within the ±3 sigma bounds, showing stable and reliable tracking.

## Results



| Metric            | Value | Unit   |
|-------------------|-------|--------|
| Position MSE      | 27.65 | m²     |
| Velocity MSE      | 2.68  | (m/s)² |
| Innovation Std (X)| 10.34 | m      |
| Innovation Std (Y)| 11.16 | m      |


- The innovation (difference between predicted and measured values) has a mean near zero, indicating unbiased estimates.

## Conclusion

The Linear Kalman Filter effectively estimates the vehicle’s state with good accuracy and stable error behavior, making it suitable for 2D vehicle tracking applications.

---

Feel free to explore the code and visualization in this repository for more details.
