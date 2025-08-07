import numpy as np
from kfsims.tracker2d import run_sim
from kfsims.kfmodels import KalmanFilterBase

# Simulation Options
sim_options = {'time_step': 0.01,
               'end_time': 120,
               'measurement_rate': 1,
               'measurement_noise_std': 10,
               'motion_type': 'straight',
               'start_at_origin': True,
               'start_at_random_speed': True,
               'start_at_random_heading': True,
               'draw_plots': True,
               'draw_animation': True} 

# Kalman Filter Model
class KalmanFilterModel(KalmanFilterBase):
    
    def initialise(self, time_step):

        # Set Initial State and Covariance
        init_pos_std = 0
        init_vel_std = 5
        self.state = np.array([0, 0, 0, 0])
        self.covariance = np.diag(np.array([init_pos_std*init_pos_std,
                                            init_pos_std*init_pos_std,
                                            init_vel_std*init_vel_std,
                                            init_vel_std*init_vel_std]))

        # Setup the Model F Matrix
        dt = time_step
        self.F = np.array([[1, 0, dt, 0],
                           [0, 1, 0, dt],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])

        # Set the Q Matrix
        accel_std = 0.1
        self.Q = np.diag(np.array([(0.5*dt*dt), (0.5*dt*dt), dt, dt]) * (accel_std*accel_std))

        # Setup the Model H Matrix
        self.H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])

        #Set the R Matrix

        meas_std = 10.0
        self.R = np.diag([(meas_std*meas_std), (meas_std*meas_std)])
        
        return

    def prediction_step(self):
        # Make Sure Filter is Initialised
        if self.state is not None:
            x = self.state
            P = self.covariance

            # Calculate Kalman Filter Prediction
            x_predict = np.matmul(self.F, x) 
            P_predict = np.matmul(self.F, np.matmul(P, np.transpose(self.F))) + self.Q

            # Save Predicted State
            self.state = x_predict
            self.covariance = P_predict

        return

    def update_step(self, measurement):

        # Make Sure Filter is Initialised
        if self.state is not None and self.covariance is not None:
            x = self.state
            P = self.covariance

            # Calculate Kalman Filter Update
            z = np.array([measurement[0], measurement[1]])

            # Predicted Measurement: z_hat = H * x
            z_hat = np.matmul(self.H, x)

            # Innovation: y = z - z_hat
            y = z - z_hat

            # Innovation Covariance: S = H * P * H' + R
            S = np.matmul(np.matmul(self.H, P), self.H.transpose()) + self.R

            # Kalman Gain: K = P * H' * S^-1
            K = np.matmul(np.matmul(P, self.H.transpose()), np.linalg.inv(S))

            # Kalman State Update: x_update = x + K*y
            x_update = x + np.matmul(K, y)

            # Kalman Covariance Update: P_update = (I - K*H)*P
            H = self.H
            KH = np.matmul(K, H)
            KH_dim = np.shape(KH)[0]
            In = np.eye(KH_dim)
            P_update = np.matmul((In - KH), P)

            # Save Updated State
            self.innovation = y
            self.innovation_covariance = S
            self.state = x_update
            self.covariance = P_update

        return 


# Run the Simulation
run_sim(KalmanFilterModel, sim_options, {})

