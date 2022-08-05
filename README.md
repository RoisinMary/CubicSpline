# CubicSpline
A simple tool for computing the cubic spline of one-dimensional data.

Execute.py will prompt the user for 3 inputs - the first should be a .npy file containing a 2xn array representing x and y values. These represent the function to be fit. The 2nd is a .npy file containing a 1xm array representing a grid which speicifies where the user would like the spline evaluate. The third is a file name where the result of the program will be written as a .npy file containing a 3xm array, where the three components are the evalute spline, the first derivative and the second derivative respectively.
