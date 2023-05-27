#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import numpy as np

from astropy.io import fits

path = '/path/to/fits/files/'
fits_dir = os.path.join(path + 'data')
#fits_dir = '/Users/danielhenningsen/Desktop/ASU/skysurf/F275W_fits'

#with open(os.path.join(path + 'newlist_WFC3uvis2_F275W_missing_image_list.txt') as file:
#    for line in file.readlines():
#        if line 

outfile = open('/path/to/output.txt', 'w')

for fits_files in os.listdir(fits_dir):
    if fits_files.endswith(".fits.gz"):
        outfile.write(fits_files)
        fits_name = str(fits_files)
        f = fits.open(os.path.join(fits_dir + "/" + fits_name))
        outfile.write(f[0].header['FILTER'])
        outfile.write(f[0].header['DETECTOR'])
        outfile.write('\n')


# In[ ]:




