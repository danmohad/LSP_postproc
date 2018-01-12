# -*- coding: utf-8 -*-
"""
LSP Data Extraction
For Mastorakos Cambridge dodecane spray case

02.12.2017
Danyal Mohaddes Khorassani

"""

import sys
import os
import tecplot as tp
import numpy as np
from os import walk

#Data binning - volumes from Yuan thesis for LDA/PDA measurements, sec. 2.3.1
#Axial binning
#dx = 0.00015
dx = 0.001
x_bins = np.array([0.01,0.02,0.03,0.04])

#Radial binning
y_bins,dy = np.linspace(-0.036,0.036,73,retstep=True)

#Swirl binning
#dz = 0.0034
dz = 0.001
z_bin = np.array([0.0])

#Prepare for outer loop
NP_mat = np.zeros([len(x_bins),len(y_bins)])
TP_mat = np.zeros([len(x_bins),len(y_bins)])
MP_mat = np.zeros([len(x_bins),len(y_bins)])
DP_mat = np.zeros([len(x_bins),len(y_bins)])
DP2_mat = np.zeros([len(x_bins),len(y_bins)])
DP3_mat = np.zeros([len(x_bins),len(y_bins)])
UP_X_mat = np.zeros([len(x_bins),len(y_bins)])
UP_Y_mat = np.zeros([len(x_bins),len(y_bins)])
UP_Z_mat = np.zeros([len(x_bins),len(y_bins)])

#get path to LSP files
LSP_files_path = sys.argv[1]
print 'Processing LSP files at path:'
print LSP_files_path
#get filenames
#(_, _, LSP_filename_vec) = walk('C:\Users\Danyal\Box Sync\Stanford\Research\LES\Mastorakos_spray\LSP Data Extraction').next()
(_, _, LSP_filename_vec) = walk(LSP_files_path).next()

#Loop over all files
for LSP_filename in LSP_filename_vec:
    #print filename for progress tracking purposes
    print 'Processing file:' + LSP_filename
    
    #import data from lsp .plt file
    dataset = tp.data.load_tecplot(LSP_files_path + '/' + LSP_filename)
    
    #convert dataset to numpy arrays
    x_array = dataset.zone(0).values('X').as_numpy_array()
    y_array = dataset.zone(0).values('Y').as_numpy_array()
    z_array = dataset.zone(0).values('Z').as_numpy_array()
    TP_array = dataset.zone(0).values('TP').as_numpy_array()
    MP_array = dataset.zone(0).values('MP').as_numpy_array()
    DP_array = dataset.zone(0).values('DP').as_numpy_array()
    NPAR_array = dataset.zone(0).values('NPAR').as_numpy_array()
    UP_X_array = dataset.zone(0).values('UP-X').as_numpy_array()
    UP_Y_array = dataset.zone(0).values('UP-Y').as_numpy_array()
    UP_Z_array = dataset.zone(0).values('UP-Z').as_numpy_array()
    
    #Total number of droplets in domain:
    NPAR_TOT = x_array.size
    
    #Loop over all droplets in file
    #Assume NPAR_array is all ones (i.e. all parcels only have 1 droplet each)    
    for i in xrange(NPAR_TOT):
        #Determine if droplet is in a bin
        if z_array[i] < dz and z_array[i] > -dz:
            if y_array[i] < y_bins.max() + dy and y_array[i] > y_bins.min() - dy:
                if x_array[i] < x_bins.max() + dx and x_array[i] > x_bins.min() - dx:
                    if any(np.equal(x_array[i] < x_bins + dx,x_array[i] > x_bins - dx)):
                        idx_x = np.equal(x_array[i] < x_bins + dx,x_array[i] > x_bins - dx).argmax()
                        idx_y = np.argmin(np.abs(y_bins - y_array[i]))
                        #Update droplet stats
                        NP_mat[idx_x,idx_y] += 1
                        TP_mat[idx_x,idx_y] += TP_array[i]
                        MP_mat[idx_x,idx_y] += MP_array[i]
                        DP_mat[idx_x,idx_y] += DP_array[i]
                        DP2_mat[idx_x,idx_y] += DP_array[i]**2
                        DP3_mat[idx_x,idx_y] += DP_array[i]**3
                        UP_X_mat[idx_x,idx_y] += UP_X_array[i]
                        UP_Y_mat[idx_x,idx_y] += UP_Y_array[i]
                        UP_Z_mat[idx_x,idx_y] += UP_Z_array[i]
    #delete dataset object
    del dataset
    
#Save data to .npz
outfile_name = LSP_files_path + '/' + 'LSP_data_processed.npz'             
with open(outfile_name,'wb') as outfile:
    np.savez(outfile,NP_mat=NP_mat,TP_mat=TP_mat,MP_mat=MP_mat,DP_mat=DP_mat,\
             DP2_mat=DP2_mat,DP3_mat=DP3_mat,UP_X_mat=UP_X_mat,UP_Y_mat=UP_Y_mat,\
             UP_Z_mat=UP_Z_mat,x_bins=x_bins,y_bins=y_bins)

#Print completion message
#cwd = os.getcwd()
print 'Processing complete.\nData saved at ' + outfile_name

    



