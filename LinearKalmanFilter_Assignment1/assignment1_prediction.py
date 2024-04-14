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
               'start_at_random_speed': False,
               'start_at_random_heading': False,
               'draw_plots': True,
               'draw_animation': True} 

# Kalman Filter Model


class KalmanFilterModel(KalmanFilterBase):

    def initialise(self, time_step):

        # Define a np.array 4x1 with the initial state (px,py,vx,vy)
        self.state = np.array([[0], [0], [7.07], [7.07]])

        # Define a np.array 4x4 for the initial covariance
        self.covariance = np.diag([0, 0, 0, 0])

        # Setup the Model F Matrix
        dt = time_step
        self.F = np.array([[1, 0, dt, 0],
                           [0, 1, 0, dt],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
        accel_std = 0.1
        # Set the Q Matrix
        self.Q =  np.diag(np.array([(0.5*dt*dt), (0.5*dt*dt), dt, dt]) * (accel_std*accel_std))
        
        return
    
    def prediction_step(self):
        # Make Sure Filter is Initialised
        if self.state is not None:
            x = self.state
            P = self.covariance
            F = self.F
            Q = self.Q
            # Calculate Kalman Filter Prediction
            
            # State Prediction: x_predict = F * x
            x_predict = np.matmul(F, x)

            # Covariance Prediction: P_predict = F * P * F' + Q
            P_predict = (np.matmul(np.matmul(F, P), np.transpose(F))) + Q

            # Save Predicted State
            self.state = x_predict
            self.covariance = P_predict

        return

    def update_step(self, measurement):
        return 


# Run the Simulation
run_sim(KalmanFilterModel, sim_options, {})
