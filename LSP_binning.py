# -*- coding: utf-8 -*-
"""
LSP_binning.py

Extracting Droplet Information and Binning

DMK
25/02/2018
"""

import sys
from os import walk
import fnmatch
import numpy as np
import scipy.io as sio
from LSPData_class import LSPData

#Macros:
LSP_FLAGS = ()
E_FLAGS = ()


#get filepath
LSP_files_path = input('LSP files path:\n')
E_files_path = input('Eulerian files path:\n')
Mat_files_path = input('Matlab output files path:\n')

#get lsp filenames
(_, _, LSP_filename_vec) = walk(LSP_files_path).next()
LSP_filename_vec = fnmatch.filter(LSP_filename_vec,'*.plt')
#get corresponding Eulerian filenames
(_, _, E_filename_vec) = walk(E_files_path).next()
E_filename_vec = fnmatch.filter(E_filename_vec,'*.plt')

#Loop over all files
for LSP_filename,E_filename in zip(LSP_filename_vec,E_filename_vec):
    #print filename for progress tracking purposes
    print ('Processing file:') + LSP_filename
    
    #import data from lsp .plt file
    myData = LSPData(LSP_files_path,LSP_filename,LSP_FLAGS) #no Wb flag
    
    #interpolate data from Eulerian .plt to lsp field
    myData.interp_Eulerian(E_files_path,E_filename,E_FLAGS)
    
    sio.savemat('{:s}'.format(Mat_files_path + '/' + LSP_filename),\
                {'XP':myData.dataset.zone(0).values('X').as_numpy_array(),\
                'YP':myData.dataset.zone(0).values('Y').as_numpy_array(),\
                'ZP':myData.dataset.zone(0).values('Z').as_numpy_array(),\
                'TP':myData.dataset.zone(0).values('TP').as_numpy_array(),\
                'MP':myData.dataset.zone(0).values('MP').as_numpy_array(),\
                'DP':myData.dataset.zone(0).values('DP').as_numpy_array(),\
                'UP_X':myData.dataset.zone(0).values('UP-X').as_numpy_array(),\
                'UP_Y':myData.dataset.zone(0).values('UP-Y').as_numpy_array(),\
                'UP_Z':myData.dataset.zone(0).values('UP-Z').as_numpy_array(),\
                'RHO':myData.dataset.zone(0).values('RHO').as_numpy_array(),\
                'Z_GAS':myData.dataset.zone(0).values('Z-scalar').as_numpy_array(),\
                'CSRC':myData.dataset.zone(0).values('CSRC').as_numpy_array(),\
                'T':myData.dataset.zone(0).values('T').as_numpy_array(),\
                'Y_N_C12H26':myData.dataset.zone(0).values('Y_N-C12H26').as_numpy_array(),\
                'Y_OH':myData.dataset.zone(0).values('Y_OH').as_numpy_array(),\
                'Y_OHD_OH':myData.dataset.zone(0).values('Y_OHD-OH').as_numpy_array(),\
                'hr':myData.dataset.zone(0).values('hr').as_numpy_array(),\
                'U_X':myData.dataset.zone(0).values('U-X').as_numpy_array(),\
                'U_Y':myData.dataset.zone(0).values('U-Y').as_numpy_array(),\
                'U_Z':myData.dataset.zone(0).values('U-Z').as_numpy_array()})
    
    
    
print 'Processing complete. Matlab output files saved at: ',Mat_files_path
