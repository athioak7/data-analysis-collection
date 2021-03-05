import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt
from astropy.io import fits
import freud
from scipy.spatial import Voronoi

'''
Version 2 for voronoi

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

# save to csv file
savetxt('data.csv', coords_data, delimiter='')

points = coords_data
plt.scatter(points[:,0], points[:,1])
plt.title('Points')
plt.show()

# We must add a z=0 component to this array for freud
points = np.hstack((points, np.zeros((points.shape[0], 1))))

L = 20
box = freud.box.Box.square(L)
voro = freud.locality.Voronoi()

cells = voro.compute((box, points)).polytopes

plt.figure()
ax = plt.gca()
voro.plot(ax=ax, cmap='RdBu')
ax.scatter(points[:, 0], points[:, 1], s=10, c='k')
plt.show()

