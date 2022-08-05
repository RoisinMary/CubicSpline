#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Set up the linear equation which will define the cubic spline. 
Returns the coefficients of the piecewise cubic polynomials specifying the spline.
b is the linear component, c the quadratic and d the cubic coefficients.
"""
import numpy as np

def cubic_spline_coeffs(x,y):
    
    n=x.shape[0]
    
    "define the linear system"
    
    delta_x=np.diff(x)
    delta_y=np.diff(y)
    
    lin_sys_mat=np.zeros([n,n])
    lin_sys_mat[0,0]=1
    lin_sys_mat[-1,-1]=1
    
    diag=2*(delta_x[1:]+delta_x[:-1])
    
    for i in range(1,n-1):
        lin_sys_mat[i,i]=diag[i-1]
        lin_sys_mat[i,i-1]=delta_x[i-1]
        lin_sys_mat[i,i+1]=delta_x[i]

    lin_sys_sol=3*((delta_y[1:]/delta_x[1:])-(delta_y[:-1]/delta_x[:-1]))
    
    lin_sys_sol=np.concatenate(([0],lin_sys_sol,[0]))
    
    "solve the quadratic coefficents"
    
    c=np.linalg.solve(lin_sys_mat,lin_sys_sol)

    "solve for the linear and cubic coefficents"

    d=(c[1:]-c[:-1])/(3*delta_x)
    b=(delta_y/delta_x)-(delta_x/3)*(2*c[:-1]+c[1:])
    
    return (b,c,d)
    

