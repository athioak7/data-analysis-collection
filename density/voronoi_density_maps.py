import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.spatial import Voronoi, voronoi_plot_2d

'''
Version 1 for voronoi

There are different ways for density map calculations but here,
as the density changes, the cells need to be self-adaptive.
According to the study of \citep{adacells} for our star data set,
what works best in our case is a tesselation method.
This prevails the other methods(Cloud in a Cell, kernels etc),
as it is entirely self-adaptive without relying on any imposed parameters,
which make the other methods "fail" .
The grids are estimated through the Voronoi estimation. 
In our case each star will be a point of coordinates, eg $x_1$,
and its corresponding Voronoi cell will consist of every other star/point
in the plane whose distance to $x_1$ is less than or equal
to its distance to any other $x_n$.

INPUT: the header of fits image w/ coordinates x,y
'''


hdu = fits.open('Astroimage.fits')
img = hdu[0].data
img1=img[10000:10010, 10000:10010]

#Image DATA array stored in the Primary header
data_array = img1

#converting to coordinate form
coords_data = np.argwhere(data_array > 0)
print(coords_data[0])

#Making Voronoi plot
vor = Voronoi(coords_data)

#Plotting Voronoi
voronoi_plot_2d(vor)
plt.show()

