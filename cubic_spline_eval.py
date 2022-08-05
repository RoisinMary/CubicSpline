#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creates a linear system using linear_system.py, solves using Jacobi.py. 
Returns the cubic spline evaluated at points in the grid.
"""
import numpy as np

def cubic_spline_eval(x,y,b,c,d,grid):
    
    grid_evals=[]
    j=1
    
    
    for point in grid:
        
        while point>x[j] and j<x.shape[0]-1:
            j=j+1

        diff=point-x[j-1]
        val=y[j-1]+b[j-1]*diff+c[j-1]*diff**2+d[j-1]*diff**3             
        grid_evals.append(val)
        
    return(grid_evals)