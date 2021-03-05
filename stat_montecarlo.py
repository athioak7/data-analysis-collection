import numpy as np
import random
import scipy.stats as stats
import matplotlib.pyplot as plt

'''
Statistical Monte Carlo method for a gaussian function
for 2 lambda values: 5 and 15
'''


lambda1=5
lambda2=15

def calcHist(data):
    # The number of counts N of events will be distributed
    # as a Poissonian distribution if we sum up the time differences

    sum = 0
    N = 0
    h = []
    for x in data:
        sum += x
        N += 1
        if sum >= 1:
            h.append(N)
            sum = 0
            N = 0
            
    return h

# part1
# montecarlo simulation for different values of lambda 
# applying it to random generated times that follow an exponential distribution 
x1 = np.random.exponential(scale=0.2, size=1000)
x2 = np.random.exponential(scale=0.0666666, size=1000)

plt.hist([x1,x2], bins=25, histtype='bar', color=['pink','skyblue'], edgecolor='lightgrey')
plt.legend([('lambda = 5'),('lambda = 15')])
plt.title('Exponential distributions')
plt.show()

# part2
# The number of counts N of events will be distributed
# as a Poissonian distribution if we sum up the time differences
h1 = calcHist(x1)
h2 = calcHist(x2)

# part3
plt.hist([h1,h2], bins=25, histtype='bar', color=['pink','skyblue'], edgecolor='lightgrey')
plt.legend([('lambda = 5'),('lambda = 15')])
plt.title('Histograms of N')
plt.show()

# part4
x_fit = np.arange(0,30,1.)

plt.hist(h1, bins=25, histtype='bar', density=True, color='pink', edgecolor='lightgrey')
plt.plot(x_fit, stats.poisson.pmf(x_fit, 5), linestyle='dashed', color='grey')
plt.title('Poisson fit of lambda = 5')
plt.show()

plt.hist(h2, bins=25, histtype='bar', density=True, color='skyblue', edgecolor='lightgrey')
plt.plot(x_fit, stats.poisson.pmf(x_fit, 15), linestyle='dashed', color='grey')
plt.title('Poisson fit of lambda = 15')
plt.show()


