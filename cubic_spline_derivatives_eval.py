#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
takes in the coefficients provided by cubic spline and gives back 
the first and second derivatives at the specified grid
"""

import numpy as np

def cubic_spline_derivatives_eval(x,y,b,c,d,grid):
    
    grid_evals_1=[]
    grid_evals_2=[]
    j=1
    
    
    for point in grid:
        
        while point>x[j] and j<x.shape[0]-1:
            j=j+1

        diff=point-x[j-1]
        val_1=b[j-1]+2*c[j-1]*diff+3*d[j-1]*diff**2             
        grid_evals_1.append(val_1)
        val_2=2*c[j-1]+6*d[j-1]*diff            
        grid_evals_2.append(val_2)
        
    return(grid_evals_1,grid_evals_2)
