#!/usr/bin/env python
# coding: utf-8

# In[29]:


import matplotlib.pyplot as plt
import numpy as np
from astropy.wcs import WCS
from astropy.io import fits
plt.rcParams["font.family"] = "Times New Roman"
'''
Comments are entered here
This is a mock jupyter notebook file for github testing purposes
Best way is to save in github desktop directory and just commit and push

This is a quick display of 12CO Tmb map from the FCRAO survey
'''
hdu = fits.open(r'C:\Users\kphall\Documents\Research\PerA_12coFCRAO_F_map.fits')
co_data = hdu[0].data
fwcs = WCS(hdu[0].header)

fig = plt.figure()
ax = fig.add_subplot((111), projection = fwcs)#.dropaxis(2))#cube.wcs.dropaxis(2)) Commented out the commands for the HI brightness temperature map
im = ax.imshow(co_data.squeeze(), cmap = 'afmhot')#, vmin=0, vmax=60) More commands for the Brightness temp map
ax.invert_yaxis()
ax.invert_xaxis()

ax.set_ylabel('Declination', fontsize=14)
ax.set_xlabel('Right Ascension', fontsize=14)
ax.tick_params(which='both', direction='in', labelsize=10)


# In[ ]:




