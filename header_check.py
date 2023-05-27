#!/usr/bin/env python
# coding: utf-8

import os
import sys
import numpy as np
from astropy.io import fits
#create list of all fits files in directory
path = '/path/to/fits/files/'
fits_dir = os.path.join(path + 'data')

#open a txt file to write output to
outfile = open('/path/to/output.txt', 'w')

#iterate through files and write out the file name, filter, detector/camera info
for fits_files in os.listdir(fits_dir):
    if fits_files.endswith(".fits.gz"):
        outfile.write(fits_files)
        fits_name = str(fits_files)
        f = fits.open(os.path.join(fits_dir + "/" + fits_name))
        outfile.write(f[0].header['FILTER'])
        outfile.write(f[0].header['DETECTOR'])
        outfile.write('\n')

