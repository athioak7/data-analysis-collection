#First Part 
#I generate 2000 random coordinates (x,y,z)  that I use for the simulation of the pdf in the first part
import random as rd
#the range between which we cant to have them randomnly
rangeX = (0, 3)
rangeY = (0, 3)


qty = 2000  
for i in range(1,2):
    f = open("random_"+str(i)+"txt","w+")

    for j in range(qty):
        x = rd.uniform(*rangeX)
        y = rd.uniform(*rangeY)
        f.write(str(x))
        f.write(" ")
        f.write(str(y))
        f.write("\n")    

    f.close()

#Second Part using the previous data set and creating a code for the Gibbs implementation


#question b
import os
from sys import*
from math import *
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit as cf
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy import stats
from astropy.io import ascii

# This makes plots beautiful
try: plt.style.use('./mc_notebook.mplstyle')
except: pass
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

np.seterr(divide='ignore', invalid='ignore')    #ignore warnings from div 0

catIn2=open('random.dat','r')

x,y = np.loadtxt(catIn2, dtype='float', usecols=(0,1), unpack=True )

pdf1=np.exp( -( (x[1]**2) * (y**2) + (x[1]**2)-9*x[1])/2)
pdf2=np.exp( -( (x**2) * (y[1]**2) + (x**2)-9*x)/2)

plt.figure(1) 
plt.plot()

plt.scatter(y, pdf1, s = 50, c = 'palevioletred', marker = '*', label='stable x, various y ' )
plt.title('plotting the pdf for different values of y with stable x', fontsize=10)
plt.ylabel('pdf')
plt.xlabel('x,y')
plt.legend()
plt.show()


plt.figure(2) 
plt.plot()
plt.scatter(x,pdf2, s = 50, c = 'teal', marker = '*', label='stable y, various x')
plt.title('plotting the pdf for different values of x with stable y', fontsize=10)
plt.ylabel('pdf')
plt.xlabel('x,y')
plt.legend()
plt.show()

#question c
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(521)
X1 = np.random.uniform(size = 1000)
X2 = np.random.uniform(size = 1000)
R = np.sqrt(-2 * np.log(X1))
Theta = 2 * np.pi * X2
z1 = R * np.cos(Theta)
z2 = R * np.sin(Theta)

plt.figure(1)
x1_fit = np.arange(0,6)
plt.hist(z1, bins=25, histtype='bar', density=True, color = "palevioletred")
plt.plot(x1_fit, stats.poisson.pmf(x1_fit, 0.95), linestyle='dashed',
color='teal')
plt.plot(-x1_fit, stats.poisson.pmf(x1_fit, 0.95), linestyle='dashed',
color='teal')
plt.title("z1")
plt.show()

plt.figure(2)
x2_fit = np.arange(0,6)
plt.hist(z2, bins=25, histtype='bar', density=True, color = "palevioletred")
plt.plot(x2_fit, stats.poisson.pmf(x2_fit, 0.95), linestyle='dashed',
color='teal')
plt.plot(-x2_fit, stats.poisson.pmf(x2_fit, 0.95), linestyle='dashed',
color='teal')
plt.title("z2")
plt.show()
