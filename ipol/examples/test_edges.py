from scipy.misc import imread,imresize
import matplotlib.pyplot as plt
import numpy as np
import ipol
from ipol.thirdparties import netpbmfile
plt.ion()

im_file =ipol.path+'/csources/lsd_1.6/chairs.pgm'

#image =imread(im_file)# does not work with the provided pgm file :(

image=netpbmfile.imread(im_file)
plt.imshow(image,cmap=plt.cm.Greys_r)

edges=ipol.edges_sobel(image.astype(np.float32),0.1,2)
plt.imshow(edges)

