#!/usr/bin/env python3
""" A first template for a PID controller """


class PID():
    """ Computes proportional, derivative, and integral terms for a PID controller """
    def __init__(self, gain_kp=1.0, gain_kd=1.0, gain_ki=1.0):
        """Initializes gains and internal state (previous error and integral error)"""
        self.gain_kp = gain_kp
        self.gain_kd = gain_kd
        self.gain_ki = gain_ki

        self.error_signal_previous = None
        self.error_signal_integral = 0

    def proportional(self, error_signal):
        """ Compute proportional term (with gain) """
        #TODO: This is a stub. Write your code here.
        return -self.gain_kp * error_signal
        return control_p

    def integral(self, error_signal, time_delay):
        """ Compute integral term (with gain) """
        #TODO: This is a stub. Write your code here.
        self.error_signal_integral += error_signal * time_delay
        return -self.gain_ki * self.error_signal_integral
        return control_i

    def derivative(self, error_signal, time_delay):
        """ Compute derivative term (with gain) """
        #TODO: This is a stub. Write your code here.
        error_signal_derivative = (error_signal - self.error_signal_prev) / time_delay
        self.error_signal_prev = error_signal
        return -self.gain_kd * error_signal_derivative
        return control_d
