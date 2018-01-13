# -*- coding: utf-8 -*-
"""
Created on Jan 02 2018

@author: Danyal Mohaddes Khorassani
"""

import numpy as np
import scipy.io as sio
from matplotlib import pyplot as plt

#STATION = 0
#LIM = 000.0

D = 0.025 #m
Ub = 17.1 #m/s

EXP_PATH = 'C:\Users\Danyal\Box Sync\Stanford\Research\LES\Mastorakos_spray\DD1S2 Exp Data'
LSP_PATH = input('LSP_DATA PATH:\n')
MAT_PATH_FILE = input('MAT FILE PATH/NAME:\n')

#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_1\SOLUT_LSP'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_2\SOLUT_LSP'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_3\SOLUT_LSP'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_4\SOLUT_LSP'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\1_DD1S2_OH_SMD37'
#LSP_PATH = 'C:\Users\Danyal\Documents\University Documents\Stanford University\Research\Mastorakos_Spray\DD1S2_OH_PL_V2\DD1S2_OH_PL_1\SOLUT_LSP\Steady'

LSP_data = np.load(LSP_PATH + '\LSP_data_processed_az_rad.npz')
sum_DP3_mat = LSP_data['DP3_mat']
sum_DP2_mat = LSP_data['DP2_mat']
sum_UP_X_mat = LSP_data['UP_X_mat']
sum_UP_R_mat = LSP_data['UP_R_mat']
#sum_UP_Y_mat = LSP_data['UP_Y_mat']
NP_mat = LSP_data['NP_mat']
x_bins = LSP_data['x_bins']
r_bins = LSP_data['r_bins']
LSP_data.close()

SMD_mat = (sum_DP3_mat/sum_DP2_mat)*1000000
UP_X_mat = sum_UP_X_mat/NP_mat
UP_R_mat = sum_UP_R_mat/NP_mat
#UP_Y_mat = sum_UP_Y_mat/NP_mat

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

#must add UP_R_EXP
UP_R_EXP_z0 = EXP_data['VMeanradial'][EXP_data['z_0']-1]
UP_R_EXP_z1 = EXP_data['VMeanradial'][EXP_data['z_1']-1]
UP_R_EXP_z2 = EXP_data['VMeanradial'][EXP_data['z_2']-1]
UP_R_EXP_z3 = EXP_data['VMeanradial'][EXP_data['z_3']-1]
UP_R_EXP_LIST = [UP_R_EXP_z0,UP_R_EXP_z1,UP_R_EXP_z2,UP_R_EXP_z3]


EXP_SMD_vec = np.array([])
EXP_UP_X_vec = np.array([])
EXP_UP_R_vec = np.array([])
EXP_r_vec = np.array([])
EXP_vec_lens = np.array([1]) #for matlab indexing

#remove points with too few droplets
SMD_plot_mat = SMD_mat
UP_X_plot_mat = UP_X_mat
UP_R_plot_mat = UP_R_mat

for i in range(np.shape(SMD_plot_mat)[0]):
    for j in range(np.shape(SMD_plot_mat)[1]):
        if i == 0:
            LIM = 0.0
        else:
            LIM = 1000.0
        if NP_mat[i,j] < LIM:
            SMD_plot_mat[i,j] = np.nan
            UP_X_plot_mat[i,j] = np.nan
            UP_R_plot_mat[i,j] = np.nan
    

for STATION in range(0,4):

    st = STATION

    st_array = np.array([0.01,0.02,0.03,0.04])/0.025
    
    #SMD Figure
    plt.figure(0,figsize=(8,7))
#    plt.figure(figsize=(5,2))
    NUM = 414 - st
    plt.subplot(NUM)
    plt.plot(r_bins/D,SMD_plot_mat[st,:],'r')
    plt.plot(-r_bins/D,SMD_plot_mat[st,:],'r')
    plt.plot(np.squeeze(EXP_data['r_vec'][EXP_data['z_'+str(st)]-1])/D,np.squeeze(SMD_EXP_LIST[st]),'o')
#    plt.xlim([0.0,1.4])
    plt.xlim([-1.6,1.6])
#    plt.subplot(NUM).text(0,0.5,'x/D = {:f}'.format(st_array[STATION]),ha='left')
    plt.ylim([0.0,120.0])
#    plt.xlabel('r/D')
    plt.ylabel('SMD [$\mu$m]')
    
    #U_X Figure
    plt.figure(1,figsize=(8,7))
#    plt.figure(figsize=(5,2))
    plt.subplot(NUM)
    plt.plot(r_bins/D,UP_X_plot_mat[st,:]/Ub,'r')
    plt.plot(-r_bins/D,UP_X_plot_mat[st,:]/Ub,'r')
    plt.plot(np.squeeze(EXP_data['r_vec'][EXP_data['z_'+str(st)]-1])/D,np.squeeze(UP_X_EXP_LIST[st])/Ub,'o')
#    plt.xlim([0.0,1.4])
    plt.xlim([-1.6,1.6])
    plt.ylim([-0.15,0.55])
#    plt.xlabel('r/D')
    plt.ylabel('Ux/Ub')
    
    #U_R Figure
    plt.figure(2,figsize=(8,7))
#    plt.figure(figsize=(5,2))
    plt.subplot(NUM)
    plt.plot(r_bins/D,UP_R_plot_mat[st,:]/Ub,'r')
    plt.plot(-r_bins/D,UP_R_plot_mat[st,:]/Ub,'r')
    plt.plot(np.squeeze(EXP_data['r_vec'][EXP_data['z_'+str(st)]-1])/D,np.abs(np.squeeze(UP_R_EXP_LIST[st])/Ub),'o')
#    plt.xlim([0.0,1.4])
    plt.xlim([-1.6,1.6])
    plt.ylim([0.0,0.7])
#    plt.xlabel('r/D')
    plt.ylabel('Ur/Ub')
    
    #Make EXP matrices for use with .mat output
    EXP_SMD_vec = np.append(EXP_SMD_vec,np.squeeze(SMD_EXP_LIST[st]),axis=0)
    EXP_UP_X_vec = np.append(EXP_UP_X_vec,np.squeeze(UP_X_EXP_LIST[st]),axis=0)
    EXP_UP_R_vec = np.append(EXP_UP_R_vec,np.squeeze(UP_R_EXP_LIST[st]),axis=0)
    EXP_r_vec = np.append(EXP_r_vec,np.squeeze(EXP_data['r_vec'][EXP_data['z_'+str(st)]-1]),axis=0)
    EXP_vec_lens = np.append(EXP_vec_lens,EXP_vec_lens[-1]+len(np.squeeze(EXP_data['r_vec'][EXP_data['z_'+str(st)]-1])))

for i in range(3):
    plt.figure(i).text(0.15,0.2,'x/D = {:1.1f}'.format(st_array[0]))
    plt.figure(i).text(0.15,0.4,'x/D = {:1.1f}'.format(st_array[1]))
    plt.figure(i).text(0.15,0.6,'x/D = {:1.1f}'.format(st_array[2]))
    plt.figure(i).text(0.15,0.8,'x/D = {:1.1f}'.format(st_array[3]))  
   
plt.show

sio.savemat('{:s}'.format(MAT_PATH_FILE),{'UP_X_plot_mat':UP_X_plot_mat,'UP_R_plot_mat':UP_R_plot_mat,\
            'SMD_plot_mat':SMD_plot_mat,'Ub':Ub,'r_bins':r_bins,'D':D,\
            'EXP_r_vec':EXP_r_vec,\
            'EXP_UP_X_vec':EXP_UP_X_vec,'EXP_UP_R_vec':EXP_UP_R_vec,'EXP_SMD_vec':EXP_SMD_vec,'EXP_vec_lens':EXP_vec_lens})