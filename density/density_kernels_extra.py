import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy.stats as st
from astropy.io import fits 

'''
This code creates the density maps using kernels.
In the first two it creatse the density maps for each of the two populations 1,2
and then it devides the populations one over the other to show how much one "completes" the other.
Here we also added a random map to estimate how trustable are our results

INPUT: three catalogues of coordinates(x1,y1 and x2,y2 and x_r,y_r)
'''

# SOURCES
# initial plotting code from: https://towardsdatascience.com/simple-example-of-2d-density-plots-in-python-83b83b934f67
# transparent color map from: https://kbkb-wx-python.blogspot.com/2015/12/python-transparent-colormap.html
# no ravel : Return a contiguous flattened array.
# A 1-D array, containing the elements of the input, is returned. A copy is made only if needed


def calcDensity(x1, y1, x2, y2, name):
    print(name)
    
    # Define the borders
    deltaX = (max(x1) - min(x1))/7
    deltaY = (max(y1) - min(y1))/7
    xmin = min(x1) - deltaX
    xmax = max(x1) + deltaX
    ymin = min(y1) - deltaY
    ymax = max(y1) + deltaY
    # Create meshgrid
    xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j] #here we create the grids used for gauss

    positions = np.vstack([xx.ravel(), yy.ravel()])
    
    values1 = np.vstack([x1, y1])
    values2 = np.vstack([x2, y2])
    valuer_r = np.vstack([x_r, y_r])
    kernel1 = st.gaussian_kde(values1)
    kernel2 = st.gaussian_kde(values2)
    kernel_r = st.gaussian_kde(valuer_r)
    f1 = np.reshape(kernel1(positions).T, xx.shape)
    f2 = np.reshape(kernel2(positions).T, xx.shape)
    f_r = np.reshape(kernel_r(positions).T, xx.shape)

    # Make custom transparent cmap
    colors = [(0,1,1,c) for c in np.linspace(0,1,10000)]
    cmapred = mcolors.LinearSegmentedColormap.from_list('mycmap', colors, N=100)
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca()
    ax.set_alpha(.5)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    pos = ax.imshow(np.rot90(f_r), cmap='BuPu', extent=[xmin, xmax, ymin, ymax]) 
    cbar = plt.colorbar(pos, ax=ax)
    plt.scatter(x_r, y_r, s=10, facecolors='none', edgecolors='k', alpha=1)
    #plt.scatter(x1, y1, s=10, c='b', alpha=0.5)
    plt.show()
    plt.savefig(name + '.png')
    plt.close(fig)

    pos = ax.imshow(np.rot90(f2), cmap=cmapred,  extent=[xmin, xmax, ymin, ymax]) 
    cbar = fig.colorbar(pos, ax=ax)
    plt.show()
    plt.savefig('astro_grid/' + name + '.png', transparent=True)
    plt.close(fig)
    return f_r, f2, xmin, xmax, ymin, ymax


if __name__ == '__main__':
    x1, y1, _ = np.loadtxt('Population1.cat', skiprows=0, unpack=True)
    _, x2, y2 = np.loadtxt('Population2.cat', skiprows=0, unpack=True)
    x_r, y_r  = np.loadtxt('random.txt', skiprows=0, unpack=True)
    
    f1, f2, xmin1, xmax1, ymin1, ymax1 = calcDensity(x1, y1, x2, y2, 'image1')
    comp1 = np.array(f1/f2)

    hdu = fits.PrimaryHDU(comp)  #at this part the image will be saved as an astrophysical fits image
    hdu.writeto('comp1.fits') 
