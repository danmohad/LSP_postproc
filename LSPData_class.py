# -*- coding: utf-8 -*-
"""
LSPData Class Constructor
V2

For extraction of individual instantaneous LSP data and interpolation of
instantaneous Eulerian information

12/01/2018
Danyal Mohaddes Khorassani
"""

import tecplot as tp
import numpy as np

class LSPData():
    def __init__(self,LSP_FILEPATH,LSP_FILENAME,FLAGS=()):
        tp.new_layout()        
        #Zone 0:
        self.dataset = tp.data.load_tecplot(LSP_FILEPATH + '/' + LSP_FILENAME)
        
        if 'WB' in FLAGS:
            self.WB_P_array = self.dataset.zone(0).values('WB').as_numpy_array()
        if 'RE_P' in FLAGS:
            self.RE_P_array = self.dataset.zone(0).values('RE_P').as_numpy_array()
        if 'Z_GAS_P' in FLAGS:
            self.Z_GAS_P_array = self.dataset.zone(0).values('Z_GAS_P').as_numpy_array()
        
    def interp_Eulerian(self,E_FILEPATH,E_FILENAME,FLAGS=()):
        #Zone 1:
        tp.data.load_tecplot(E_FILEPATH + '/' + E_FILENAME)
        
        frame = tp.active_frame()
        plot = frame.plot(tp.constant.PlotType.Cartesian3D)
        plot.activate()
        #Interpolate TO LSP FROM Eulerian:
        tp.data.operate.interpolate_linear(0,1,[self.dataset.variable('RHO'),\
                                                self.dataset.variable('P'),\
                                                self.dataset.variable('Z-scalar'),\
                                                self.dataset.variable('Q'),\
                                                self.dataset.variable('C'),\
                                                self.dataset.variable('CSRC'),\
                                                self.dataset.variable('T'),\
                                                self.dataset.variable('Y_N-C12H26'),\
                                                self.dataset.variable('Y_CO2'),\
                                                self.dataset.variable('Y_OH'),\
                                                self.dataset.variable('Y_N-C12H26'),\
                                                self.dataset.variable('Y_OHD-OH'),\
                                                self.dataset.variable('hr'),\
                                                self.dataset.variable('U-X'),\
                                                self.dataset.variable('U-Y'),\
                                                self.dataset.variable('U-Z'),\
                                                ])
        
        
        
