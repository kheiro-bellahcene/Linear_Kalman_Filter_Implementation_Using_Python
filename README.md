Regarding the comment on 2D vehicle tracking using the Linear Kalman filter :

Our estimation (blue) by the Kalman filter effectively converges towards
the current state (red) of the vehicle. The uncertainty ellipse is reduced, 
indicating precise estimation. Additionally, as illustrated in the second figure, our 
system also converges in terms of position and velocity, with errors converging towards
zero and remaining bounded within the ±3 sigma band. The values displayed at the end of
the video in the terminal indicate that the Mean Squared Error (MSE) for position and 
velocity is 27.65 m^2 and 2.68 (m/s)^2 respectively. Concerning the last figure on innovation
(difference between prediction and measurement), the values are well bounded with standard deviations
of 10.34 m and 11.16 m for measurements in X and Y respectively, and the innovation has a mean equal to zero.
In conclusion, our linear Kalman filter demonstrates its effectiveness in this case.





