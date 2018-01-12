# -*- coding: utf-8 -*-
"""
Created on Sat Dec 02 18:36:07 2017

@author: Danyal Mohaddes Khorassani
"""

import numpy as np
from matplotlib import pyplot as plt

STATION = 0

D = 0.025 #m
Ub = 17.1 #m/s

EXP_PATH = 'C:\Users\Danyal\Box Sync\Stanford\Research\LES\Mastorakos_spray\DD1S2 Exp Data'
LSP_PATH = input('LSP_DATA PATH:\n')

#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_1\SOLUT_LSP'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_2\SOLUT_LSP'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_3\SOLUT_LSP'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_4\SOLUT_LSP'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\1_DD1S2_OH_SMD37'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_V2\DD1S2_OH_PL_1\SOLUT_LSP\Steady'

LSP_data = np.load(LSP_PATH + '\LSP_data_processed.npz')
sum_DP3_mat = LSP_data['DP3_mat']
sum_DP2_mat = LSP_data['DP2_mat']
sum_UP_X_mat = LSP_data['UP_X_mat']
sum_UP_Y_mat = LSP_data['UP_Y_mat']
NP_mat = LSP_data['NP_mat']
x_bins = LSP_data['x_bins']
y_bins = LSP_data['y_bins']
LSP_data.close()

SMD_mat = (sum_DP3_mat/sum_DP2_mat)*1000000
UP_X_mat = sum_UP_X_mat/NP_mat
UP_Y_mat = sum_UP_Y_mat/NP_mat

EXP_data = np.load(EXP_PATH + '\EXP_PDA_DD1S2.npz')
SMD_EXP_z0 = EXP_data['SMD'][EXP_data['z_0']-1]
SMD_EXP_z1 = EXP_data['SMD'][EXP_data['z_1']-1]
SMD_EXP_z2 = EXP_data['SMD'][EXP_data['z_2']-1]
SMD_EXP_z3 = EXP_data['SMD'][EXP_data['z_3']-1]
SMD_EXP_LIST = [SMD_EXP_z0,SMD_EXP_z1,SMD_EXP_z2,SMD_EXP_z3]

UP_X_EXP_z0 = EXP_data['UMeanaxial'][EXP_data['z_0']-1]
UP_X_EXP_z1 = EXP_data['UMeanaxial'][EXP_data['z_1']-1]
UP_X_EXP_z2 = EXP_data['UMeanaxial'][EXP_data['z_2']-1]
UP_X_EXP_z3 = EXP_data['UMeanaxial'][EXP_data['z_3']-1]
UP_X_EXP_LIST = [UP_X_EXP_z0,UP_X_EXP_z1,UP_X_EXP_z2,UP_X_EXP_z3]

st = STATION
st_array = np.array([0.01,0.02,0.03,0.04])/0.025
plt.figure(figsize=(5,2))
plt.plot(y_bins/D,SMD_mat[st,:],'rx')
plt.plot(np.squeeze(EXP_data['r_vec'][EXP_data['z_'+str(st)]-1])/D,np.squeeze(SMD_EXP_LIST[st]),'o')
#plt.xlim([-0.6,0.6])
plt.ylim([0.0,120.0])
plt.xlabel('r/D')
plt.ylabel('SMD [microns]')
#plt.title('x/D = '+str(st_array[st]))
#plt.axes().set_aspect(adjustable='box',aspect=0.003)
plt.figure(figsize=(5,2))
plt.plot(y_bins/D,UP_X_mat[st,:]/Ub,'rx')
plt.plot(np.squeeze(EXP_data['r_vec'][EXP_data['z_'+str(st)]-1])/D,np.squeeze(UP_X_EXP_LIST[st])/Ub,'o')
plt.ylim([-0.2,0.7])
#plt.xlim([-0.6,0.6])
plt.xlabel('r/D')
plt.ylabel('Ux/Ub')
#plt.title('x/D = '+str(st_array[st]))
#plt.axes().set_aspect(adjustable='box',aspect=0.003)
