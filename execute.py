#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
takes in arguments to fit and the grid and returns the cubic spine
"""
import sys
import numpy as np
import cubic_spline_coeffs, cubic_spline_eval, cubic_spline_derivatives_eval

"takes .npy files as inputs, one 2xn array for x,y values and one 1xm array as a grid"

(x,y)=np.load(input('Provide an input file\n'))

grid=np.load(input('Specify grid\n'))

name_output=input('Give a file name for output file.\n')

(b,c,d)=cubic_spline_coeffs.cubic_spline_coeffs(x, y)
eval_spline=cubic_spline_eval.cubic_spline_eval(x,y,b,c,d,grid)
(eval_deriv_1,eval_deriv_2)=cubic_spline_derivatives_eval.cubic_spline_derivatives_eval(x,y,b,c,d,grid)


"saves the result as a 2xm array in an npy file which gives the spline and the derivatives evaluated on the grid"
eval_package=np.array([eval_spline,eval_deriv_1,eval_deriv_2])

np.save(name_output, eval_package)
