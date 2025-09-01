# 🚗📡 2D Vehicle Tracking Using Linear Kalman Filter 

## 🎯 Simulation and Results

![Kalman Tracking GIF](demo/kalman_tracking.gif) 

This project demonstrates the use of a **Linear Kalman Filter** to track a vehicle’s position and velocity in 2D space.

---

## 📋 Summary

- The **Kalman filter estimation** (🔵 blue) converges effectively towards the **true vehicle state** (🔴 red).  
- The **uncertainty ellipse** shrinks over time, indicating increasing precision in the estimates.  
- **Position and velocity errors** converge towards zero and remain within the ±3 sigma confidence interval, as shown in the second figure.  
- **Mean Squared Error (MSE)** at the end of the simulation:  
  - Position MSE: **27.65 m²**  
  - Velocity MSE: **2.68 (m/s)²**  
  - Innovation** (difference between prediction and measurement) is well-behaved:  
  - Standard deviations: **10.34 m (X)** and **11.16 m (Y)**  
  - Innovation mean ≈ **0**, indicating unbiased estimates.

---

## Conclusion

The **Linear Kalman Filter** proves highly effective for 🚗 vehicle tracking in 2D space, delivering **accurate** 📏 and **reliable** 🔒 state estimation.
