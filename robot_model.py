#!/usr/bin/env python3

from math import cos, sin

import numpy as np



def model_parameters():
    param_k=1.0
    param_d=0.5
    """Returns two constant model parameters"""
    return param_k, param_d


def system_matrix(theta):
    """Returns a numpy array with the A(theta) matrix for a differential drive robot"""
    return a_matrix


def system_field(z, u):
    """Computes the field at a given state for the dynamical model"""
    return dot_z


def euler_step(z, u, stepSize):
    """Integrates the dynamical model for one time step using Euler's method"""
    return z_next
