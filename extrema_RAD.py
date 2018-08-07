#!/usr/bin/python
# -*- coding: latin-1 -*-
import pandas as pd
import numpy as np
import os
import sys
import time
import datetime
import math

real_t = 'float64'




    #***************************************************************** Pressure Spline:
in_file_path1 = "/data/PDS_Python/PDS_out/3_Splines/Pspline/"


 # ***************************************************************** lowest Air Temperature:
    ####################### nominal acquisitions:
in_file_path8 = "/data/PDS_Python/PDS_out/2_MEAN/Mean5/Out_lowest_Temp/"

    ####################### nominal and extended acquisitions:
in_file_path2 = "/data/PDS_Python/PDS_out/2_MEAN/Mean1/Out_Lowest_Temp/"

############### means GTS, sigma GTS, sigma RHSurf:
in_file_path3 = "/data/PDS_Python/PDS_out/4_RH/RHSurface6/"

# ***************************************************************** RH air at 1.5m:
in_file_path4 = "/data/PDS_Python/PDS_out/4_RH/RHSurface5/"

# ***************************************************************** Global, diffuse and direct irradiance:
in_file_path5 = "/data/PDS_Python/PDS_out/5_UV/"

# ***************************************************************** Derivative Spline GTS
in_file_path6 = "/data/PDS_Python/PDS_out/6_HEA_COO/splineGTS/"

# ***************************************************************** Difference AirTemp, GTS
in_file_path7 = "/data/PDS_Python/PDS_out/7_AirGround_Tdiff/"

# ***************************************************************** u*rho*(Tg-Ta)
in_file_path9 = "/data/PDS_Python/PDS_out/2_MEAN/Mean5/Out_mean_P_Tg_Ta_rho/"


# ***************************************************************** ENV & MOD from FMT V.6 (RDR_03.07.2015) para temperatura booms y UV temp
in_file_path10 = "/data/PDS_Python/PDS_out/1_AWK/CLEAN_ALL/MD_CLEAN/"
in_file_path11 = "/data/PDS_Python/PDS_out/1_AWK/CLEAN_ALL/NV_CLEAN/"
    
    
# ***************************************************************** ADR from FMT V.7 (RDR_18.02.2016) topography files
sun_topo_file_path = "/data/PDS_Python/PDS_out/1_AWK/CLEAN_ALL/ADR_CLEAN/"


#in_file_path12 = "/data/PDS_Python/PDS_out/Other_files/"
#in_file_path12 = "/data/PDS_Python/PDS_out/Other_files/"
in_file_path12 = "/data/PDS_Python/Code_Python/Other_files/"
#in_file_path12 = "/data/PDS_Python/PDS_out/Other_files/"

in_file_path13 = "/data/PDS_Python/PDS_out/TOA/"

in_file_path14 = "/data/PDS_Python/PDS_out/9_VMR_GTS/VMR_GTS_P_MAX/"

in_file_path15 = "/data/PDS_Python/PDS_out/10_ATS/ATS_Boom1_Global/"

in_file_path16 = "/data/PDS_Python/PDS_out/10_ATS/ATS_Boom2_Global/"

in_file_path17 = "/data/RAD/PDS_out/2_MEAN_MAX_MIN/"






out_dir1 = "/data/PDS_Python/PDS_out/8_Extrema/"




#Time #Pressure #Air Temperature #Ground Temperature #RH Temperature #RH 1.5m #Mass Mixing Ratio y Volumen Mixing Ratio #RH Surface
#RH Subsurface # 45-62Global Irradiance #63-81Diffuse Irradiance # 82-89 DerivativeGTS # 90-96 max min Sensb_HeatFlux #Difference AirTemp-GTS
# Diurnal mean and rms air Temp # Diurnal mean and rms ground Temp # Diurnal mean and rms Sensb_HeatFlux # TOA, tauUV
# max absolute Diffence T1-T2 # max & min UV Temperature
headerOut_extrema = "[1]Sol [2]ls [3]sunrise [4]sunset " \
"[5]LMST_maxP [6]SZA_maxP [7]maxP [8]err_maxP [9]LMST_minP [10]SZA_minP [11]minP [12]err_minP "\
"[13]LMST_maxTa [14]SZA_maxTa [15]maxTa [16]err_maxTa [17]LMST_minTa [18]SZA_minTa [19]minTa [20]err_minTa " \
"[21]LMST_maxGTS [22]SZA_maxGTS [23]maxGTS [24]Std.err_maxGTS [25]LMST_minGTS [26]SZA_minGTS [27]minGTS [28]Std.err_minGTS "\
"[29]LMST_minRHSTemp [30]SZA_minRHSTemp [31]minRHSTemp [32]err_minRHSTemp "\
"[33]LMST_maxRH [34]SZA_maxRH [35]maxRH [36]err_maxRH "\
"[37]maxMR [38]maxVMR "\
"[39]LMST_maxRH_Surf [40]SZA_maxRH_Surf [41]maxRH_Surf [42]Std.err_maxRH_Surf "\
"[43]maxRH_Sub_Surf [44]err_maxRH_Sub_Surf "\
"[45]LMST_maxUV_global_A [46]SZA_maxUV_global_A [47]maxUV_global_A "\
"[48]LMST_maxUV_global_B [49]SZA_maxUV_global_B [50]maxUV_global_B "\
"[51]LMST_maxUV_global_C [52]SZA_maxUV_global_C [53]maxUV_global_C "\
"[54]LMST_maxUV_global_ABC [55]SZA_maxUV_global_ABC [56]maxUV_global_ABC "\
"[57]LMST_maxUV_global_D [58]SZA_maxUV_global_D [59]maxUV_global_D "\
"[60]LMST_maxUV_global_E [61]SZA_maxUV_global_E [62]maxUV_global_E "\
"[63]LMST_maxUV_diffuse_A [64]SZA_maxUV_diffuse_A [65]maxUV_diffuse_A "\
"[66]LMST_maxUV_diffuse_B [67]SZA_maxUV_diffuse_B [68]maxUV_diffuse_B "\
"[69]LMST_maxUV_diffuse_C [70]SZA_maxUV_diffuse_C [71]maxUV_diffuse_C "\
"[72]LMST_maxUV_diffuse_ABC [73]SZA_maxUV_diffuse_ABC [74]maxUV_diffuse_ABC "\
"[75]LMST_maxUV_diffuse_D [76]SZA_maxUV_diffuse_D [77]maxUV_diffuse_D "\
"[78]LMST_maxUV_diffuse_E [79]SZA_maxUV_diffuse_E [80]maxUV_diffuse_E [81]err_UV "\
"[82]LMST_maxDerivGTS [83]SZA_maxDerivGTS [84]maxDerivGTS [85]err_1Deriv "\
"[86]LMST_minDerivGTS [87]SZA_minDerivGTS [88]minDerivGTS [89]err_1Deriv "\
"[90]LMST_maxSensb_HeatFlux [91]SZA_maxSensb_HeatFlux [92]maxSensb_HeatFlux "\
"[93]LMST_minSensb_HeatFlux [94]SZA_minSensb_HeatFlux [95]minSensb_HeatFlux [96]err_Sensb_HeatFlux "\
"[97]diurnalMean_Vertical_Thermal_Gradient [98]diurnalRMS_Vertical_Thermal_Gradient "\
"[99]diurnalMean_Ta [100]diurnalRMS_Ta "\
"[101]diurnalMean_Tg [102]diurnalRMS_Tg "\
"[103]diurnalMean_Sensb_HeatFlux [104]diurnalRMS_Sensb_HeatFlux "\
"[105]TOA [106]tauUV "\
"[107]LMST_maxAbsDiff(T1-T2) [108]SZA_maxAbsDiff(T1-T2) [109]maxAbsDiff(T1-T2) [110]Boom_T1 [111]Boom_T2 "\
"[112]LMST_maxUV_Temp [113]SZA_maxUV_Temp [114]UV_Temp [115]LMST_minUV_Temp [116]SZA_minUV_Temp [117]minUV_Temp "\
"[118]VMR_MAX_21 [119]Time_21 [120]GT_AVG_21 [121]P_AVG_21 [122]VMR_MAX_22 [123]Time_22 [124]GT_AVG_22 [125]P_AVG_22 "\
"[126]VMR_MAX_23 [127]Time_23 [128]GT_AVG_23 [129]P_AVG_23 [130]VMR_MAX_24 [131]Time_24 [132]GT_AVG_24 [133]P_AVG_24 "\
"[134]VMR_MAX_01 [135]Time_01 [136]GT_AVG_01 [137]P_AVG_01 [138]VMR_MAX_02 [139]Time_02 [140]GT_AVG_02 [141]P_AVG_02 "\
"[142]VMR_MAX_03 [143]Time_03 [144]GT_AVG_03 [145]P_AVG_03 [146]VMR_MAX_04 [147]Time_04 [148]GT_AVG_04 [149]P_AVG_04 "\
"[150]VMR_MAX_05 [151]Time_05 [152]GT_AVG_05 [153]P_AVG_05 [154]VMR_MAX_06 [155]Time_06 [156]GT_AVG_06 [157]P_AVG_06 "\
"[158]VMR_MAX_07 [159]Time_07 [160]GT_AVG_07 [161]P_AVG_07"\
"[162]VMR_MAX_08 [163]Time_08 [164]GT_AVG_08 [165]P_AVG_08 [166]Time_m_max_B1 [167]m_max_B1 [168]Pressure_m_max_B1 [169]Tf_m_max_B1 "\
"[170]Time_m_min_B1 [171]m_min_B1 [172]Pressure_m_min_B1 [173]Tf_m_min_B1 [174]Wind_Speed_max_B1 [175]Avg_Wind_Direction_B1 "\
"[176]v_max_with_orientation_B1 [177]Wind_Orientation_v_max_B1 [178]Time_m_max_B2 [179]m_max_B2 [180]Pressure_m_max_B2 "\
"[181]Tf_m_max_B2 [182]Time_m_min_B2 [183]m_min_B2 [184]Pressure_m_min_B2 [185]Tf_m_min_B2 [186]Wind_Speed_max_B2 "\
"[187]Avg_Wind_Direction_B2 [188]v_max_with_orientation_B2 [189]Wind_Orientation_v_max_B2"\
"[190]AVG_B [191]LMST_MAX_B [192]MAX_B [193]LMST_MIN_B [194]MIN_B [195]AVG_E [196]LMST_MAX_E [197]MAX_E [198]LMST_MIN_E [199]MIN_En"\



final = "# Pressure[Pa]: 1 second spline from 300 seconds pressure averaged nominal acquisitions. "\
     "# err_P[Pa]: 0.75, nominal value."\
    '--'    \
     "# Ta[K]: 300 seconds lowest air temperature between TB1 and TB2 nominal and extended acquisitions. "\
     "# err_Ta[K]: 5, nominal value."\
    '--'\
     "# GTS[K]: 300 seconds averaged nominal acquisitions. "\
     "# Std.err_minGTS[K]: 300 seconds GTS averaged nominal acquisitions. "\
    '--'\
     "# RHSTemp[K]: Relative Humidity Sensor Temperature at 1.5 m, 6 first seconds nominal acquisitions."\
     "# err_minRHSTemp[%]: 10, nominal value."\
     "# RH[%]: Relative Humidity at 1.5 m, 6 first seconds nominal acquisitions."\
     "# err_maxRH[%]: 10, nominal value."\
     "# MR[g H2O/ kg dry air]: Mass Mixing Ratio at maxRH. MR = Mw/Md * RH/100 * esat/(P - RH/100 * esat) * 1000, "\
    "where esat = ew(RHSTemp)."\
     "# VMR[ppmv]: Volumen Mixing Ratio at maxRH. VMR = Md/Mw * MR * 1e3."\
     "# RH_Surf[%]: from Richardson's formula ew = 6.11 * EXP(22.5 * (1. - TK/ T)) and mean_RH_Temp, mean_RH, "\
    "mean_GTS, mean_P."\
     "# Std.err_maxRH_Surf[%]: Std.err_maxRH_Surf(mean_GTS) = abs(derv_RH_Surf(mean_GTS)) * Std.err_minGTS, "\
    "where derv_RH_Surf(mean_GTS) = - mean_RHSurf * 22.5 * 273.14159/mean_GTS**2."\
     "# RH_Sub_Surf[%]: from Richardson's formula ew = 6.11 * EXP(22.5 * (1. - TK/ T)) and minRHSTemp, maxRH, "\
    "Sub_Temp, maxP, where Sub_Temp = minGTS + (maxGTS - minGTS)/2.3."\
     "# err_maxRH_Sub_Surf: ......"\
    '--'\
     "# UV_global[W/m**2]: global irradiance (SZA 0-30) and rover still."\
     "# UV_diffuse[W/m**2]: pure diffuse irradiance or global irradiance in shadow, where "\
    "SZA = FoV and rover still for both cases."\
     "# err_UV[%]: 10, nominal value."\
    '--'\
     "# maxDerivGTS[K/s]: 60 secs spline step time GTS 1 derivative value "\
    "from 1000 secs spline step time from averaged nominal acquisitions. Maximum Heating Rate."\
     "# minDerivGTS[K/s]: 60 secs spline step time GTS 1 derivative value "\
    "from 1000 secs spline step time from averaged nominal acquisitions. Maximum Cooling Rate."\
    '--'\
     "# Sensb_HeatFlux: u*rho*(Tg-Ta), "\
    "where u = 1 wind speed, Ta = 300 seconds lowest air temperature between TB1 and TB2, "\
    "Tg = 300 seconds averaged GTS, rho = P/R/Ta, where P = 300 seconds averaged pressure. Nominal acquisitions."\
    '--'\
     "# diurnalMean_Vertical_Thermal_Gradient[K]: diurnal mean of the difference between "\
    "lowest_Air_Temp and mean_GTS (Ta-Tg) from 300 seconds averaged nominal acquisitions."\
     "# diurnalRMS_Vertical_Thermal_Gradient[K]: diurnal rms of the difference between "\
    "lowest_Air_Temp and mean_GTS (Ta-Tg) from 300 seconds averaged nominal acquisitions."\
     "# diurnalMean_Ta[K]: diurnal mean of the lowest_Air_Temp "\
    "from 300 seconds nominal acquisitions."\
     "# diurnalRMS_Ta[K]: diurnal rms of the lowest_Air_Temp "\
    "from 300 seconds nominal acquisitions."\
     "# diurnalMean_Tg[K]: diurnal mean of the GTS "\
    "from 300 seconds averaged GTS nominal acquisitions."\
     "# diurnalRMS_Tg[K]: diurnal rms of the GTS "\
    "from 300 seconds averaged GTS nominal acquisitions."\
    '--'\
     "# diurnalMean_Sensb_HeatFlux: diurnal mean of u*rho*(Tg-Ta). "\
     "# diurnalRMS_Sensb_HeatFlux: diurnal rms of u*rho*(Tg-Ta). "\
    '--'\
     "# TOA[W/m2]: ABC1_TOA. "\
     "# tauUV: =-log { [ maxUV_global_ABC/cos(SZA_maxUV_global_ABC)-maxUV_diffuse_ABC ]/ ABC_TOA }"\
    "*cos(SZA_maxUV_global_ABC). "\
    '--'\
     "# AbsDiff[K]: maximum of fabs(T1-T2) from MOD. "\
     "# Boom_T1, Boom_T2[K]: Boom_T1, Boom_T2 values when fabs(T1-T2) is maximum. "\
     "# UV_Temp[K]: UV_Temp maximum from NV. "\
    '--'\
     "# MODs & ENVs RDR_03.07.2015 FMT V.6."\
     "# -1 = invalid value."\
     "# ############## scrREMS/8_Extrema"\
     
    
    
#print(headerOut_extrema)

sec_per_hour = 3600
sec_per_minute = 60


def getSeconds(LocalTime):
    
    hour = str(LocalTime)[0:2]
    hour = int(hour)
    minutes = str(LocalTime)[3:5]
    minutes = int(minutes)
    seconds = str(LocalTime)[6:8]
    seconds = int(seconds)
    totalSec = hour*sec_per_hour + minutes*sec_per_minute + seconds
    #print(totalSec)

    return totalSec

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
def sunset_Sunrise():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, fileSuns in os.walk(in_file_path12):
        
        sun_Arr = []
       
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileSun in fileSuns:
                
            array1=[]
            array2=[]
            array3=[]
            array4=[]
            
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileSun.endswith('.dat') and not fileSun.startswith('f'):
            
                sizeP = (len(open(in_file_path12+fileSun).readlines()))
                with open(in_file_path12 + 'msl_ls_sunrise_sunset_sol_0_to_7299_v_2_msl_sclk_v_13.dat','r') as input_fileSun:
                    for i in input_fileSun:
                        
                        colSUN=(i.split())

                        
                        if len(colSUN) < 3:
                            continue
                        else:
                            sol_ls=colSUN[0]
                            sun_Arr.append(sol_ls)
                            ls=(colSUN[2])
                            array2.append(ls)
                            time1 = (colSUN[3])
                            array3.append(time1)
                            time2 = (colSUN[4])
                            array4.append(time2)

    
                


    return sun_Arr, array2, array3, array4
def absoluteMax_Numpy(y):
    
    abs_max=max(y)
    pos_abs_max=y.tolist().index(abs_max)
    return float(abs_max), pos_abs_max

def absoluteMax(y):
    if not y:
        abs_max = -1.00
        pos_abs_max= 0
        return float(abs_max), pos_abs_max
    else:
    
        abs_max=max(y)
        pos_abs_max=y.index(abs_max)
        return float(abs_max), pos_abs_max

def absoluteMinP(y):
    if not y:
        abs_min = -1.00
        pos_abs_min= 0
        return float(abs_min), pos_abs_min
    else:
        a=[]
        
        for i in y:
            if i==-1:
                continue
            else:
                a.append(i)

        
        #abs_min = min(a)
        
        if (not a):
            abs_min=-1 
            pos_abs_min = 0 
        else:
            abs_min = min(a)
            pos_abs_min = y.index(abs_min)
            if abs_min < 200:
                abs_min=-1 
                pos_abs_min = 0 

        return float(abs_min), pos_abs_min

def absoluteMin(y):
    if not y:
        abs_min = -1.00
        pos_abs_min= 0
        return float(abs_min), pos_abs_min
    else:
        a=[]
        
        for i in y:
            if i == -1 or i == -1.0:
                continue
            else:
                a.append(i)
            
        if (not a):
            abs_min=-1
            pos_abs_min = 0
        else:
            

            abs_min = min(a)
            pos_abs_min = y.index(abs_min)
        
    

        return float(abs_min), pos_abs_min


def RAD_AVG_MAX_MIN():
    for base, dirs, files in os.walk(in_file_path17):
        sun_Arr=[]
        array1=[]
        
        for file in files:
            
            if file.endswith('.dat'):
                
                sun = file[16:21]
                with open(in_file_path17 + 'AVERAGE_MAX_MIN_' + sun + '.dat','r') as input_file:
                    for i in input_file:
                        col = i.split()
                        array1.append(i)
                sun_Arr.append(sun)
                
    return sun_Arr, array1



def Extrema_VMR_GTS_P_MAX():
    for base, dirs, filesVMR in os.walk(in_file_path14):
        sun_Arr=[]
        array1=[]
        
        for fileVMR in filesVMR:
            
            if fileVMR.endswith('.dat'):
                
                sunVMR = fileVMR[14:19]
                with open(in_file_path14 + 'VMR_GTS_P_MAX_' + sunVMR + '.dat','r') as input_fileVMR:
                    for i in input_fileVMR:
                        colVMR = i.split()
                        array1.append(i)
                sun_Arr.append(sunVMR)
                
    return sun_Arr, array1  



def Extrema_Boom1_Global():
    for base, dirs, filesVMR in os.walk(in_file_path15):
        sun_Arr=[]
        array1=[]
        
        for fileVMR in filesVMR:
            
            if fileVMR.endswith('.dat'):
                
                sunVMR = fileVMR[29:34]
                with open(in_file_path15 + 'ATS_Boom1_m_max_m_min_global_' + sunVMR + '.dat','r') as input_fileVMR:
                    for i in input_fileVMR:
                        colVMR = i.split()
                        array1.append(i)
                sun_Arr.append(sunVMR)
                
    return sun_Arr, array1  

def Extrema_Boom2_Global():
    for base, dirs, filesVMR in os.walk(in_file_path16):
        sun_Arr=[]
        array1=[]
        
        for fileVMR in filesVMR:
            
            if fileVMR.endswith('.dat'):
                
                sunVMR = fileVMR[29:34]
                with open(in_file_path16 + 'ATS_Boom2_m_max_m_min_global_' + sunVMR + '.dat','r') as input_fileVMR:
                    for i in input_fileVMR:
                        colVMR = i.split()
                        array1.append(i)
                sun_Arr.append(sunVMR)
                
    return sun_Arr, array1  

    
def ExtremaP():

    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesPS in os.walk(in_file_path1):
        
        abs_maxP_Arr = []
        TIME_abs_maxP_Arr = []

        sun_Arr = []

        abs_minP_Arr = []
        TIME_abs_minP_Arr = []

        max_SZA_Arr = []
        min_SZA_Arr = []
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for filePS in filesPS:
            array1=[]
            array2=[]
            array3=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if filePS.endswith('.dat') and not filePS.startswith('f'):
            
                sunPS = filePS[20:25]
                #print("sunPS " + sunPS)
                sizeP = (len(open(in_file_path1+filePS).readlines()))
                with open(in_file_path1 + 'pressure_spline_sol_' + sunPS + '.dat','r') as input_filePS:
                    for i in input_filePS:
                        
                        colPS=(i.split())
                        
                        if len(colPS) < 3:
                            continue
                        else:
                            segP=colPS[0]
                            array1.append(segP)
                            timeLMST_P=colPS[1]
                            array2.append(timeLMST_P)
                            P = float(colPS[2])
                            array3.append(P)
                sun_Arr.append(sunPS)
                
                abs_maxP, pos_abs_maxP = absoluteMax(array3)
                abs_maxP_Arr.append(abs_maxP)

                if abs_maxP == -1.00:
                    TIME_abs_maxP_Arr.append("00:00:00")
                else:   

                    TIME_abs_maxP_Arr.append(array2[pos_abs_maxP])

                abs_minP, pos_abs_minP = absoluteMinP(array3)
                abs_minP_Arr.append(abs_minP)
                
                if abs_minP == -1.00:
                    TIME_abs_minP_Arr.append("00:00:00")
                else:
                    TIME_abs_minP_Arr.append(array2[pos_abs_minP])

                if abs_maxP == -1:
                    max_SZA_P = -1.00
                    min_SZA_P = -1.00
                    max_SZA_Arr.append(max_SZA_P)
                    min_SZA_Arr.append(min_SZA_P)
                else:
                    max_SZA_P, min_SZA_P = max_min_SZA(sunPS, array2[pos_abs_maxP], array2[pos_abs_minP])
                    
                    if str(max_SZA_P).isdigit() and str(min_SZA_P).isdigit():
                        o = 1
                    
                        if float(max_SZA_P) > 100.0:
                            max_SZA_P = '******'

                        if float(min_SZA_P) > 100.0:
                            min_SZA_P = '******'

                    max_SZA_Arr.append(max_SZA_P)
                    min_SZA_Arr.append(min_SZA_P)
                

    return sun_Arr, abs_maxP_Arr, TIME_abs_maxP_Arr, abs_minP_Arr, TIME_abs_minP_Arr, max_SZA_Arr, min_SZA_Arr


def ExtremaLT():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesLT in os.walk(in_file_path2):
        
        abs_maxT_Arr = []
        TIME_abs_maxT_Arr = []

        sun_Arr = []

        abs_minT_Arr = []
        TIME_abs_minT_Arr = []

        max_SZA_Arr = []
        min_SZA_Arr = []

        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileLT in filesLT:
            array1=[]
            array2=[]
            array3=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileLT.endswith('.dat') and not fileLT.startswith('f'):
            
                sunLT = fileLT[16:21]
                #print("sunLT " + sunLT)
                
                sizeT = (len(open(in_file_path2+fileLT).readlines()))

                with open(in_file_path2 + 'lowest_temp_sol_' + sunLT + '.dat','r') as input_fileLT:
                    for i in input_fileLT:
                        
                        colLT=(i.split())
                        
                        if len(colLT) < 3:
                            continue
                        else:
                            segT=colLT[0]
                            array1.append(segT)
                            timeLMST_T=colLT[1]
                            array2.append(timeLMST_T)
                            T = float(colLT[2])
                            array3.append(T)

                sun_Arr.append(sunLT)
                
                abs_maxT, pos_abs_maxT = absoluteMax(array3)
                abs_maxT_Arr.append(abs_maxT)
               
                if abs_maxT == -1.0:
                    TIME_abs_maxT_Arr.append("00:00:00")
                else:                    
                    TIME_abs_maxT_Arr.append(array2[pos_abs_maxT])

                abs_minT, pos_abs_minT = absoluteMin(array3)
                abs_minT_Arr.append(abs_minT)

                if abs_minT == -1.0:
                    TIME_abs_minT_Arr.append("00:00:00")
                else:                    
                    TIME_abs_minT_Arr.append(array2[pos_abs_minT])

                if abs_maxT == -1.00:
                    max_SZA_T = -1.00
                    min_SZA_T = -1.00
                    max_SZA_Arr.append(max_SZA_T)
                    min_SZA_Arr.append(min_SZA_T)
                else:

                    max_SZA_T, min_SZA_T = max_min_SZA(sunLT, array2[pos_abs_maxT], array2[pos_abs_minT])
                    
                    if str(max_SZA_T).isdigit() and str(min_SZA_T).isdigit():
                        o = 1
                    
                        if float(max_SZA_T) > 100.0:
                            max_SZA_T = '******'

                        if float(min_SZA_T) > 100.0:
                            min_SZA_T = '******'

                    max_SZA_Arr.append(max_SZA_T)
                    min_SZA_Arr.append(min_SZA_T)

    return sun_Arr, abs_maxT_Arr, TIME_abs_maxT_Arr, abs_minT_Arr, TIME_abs_minT_Arr, max_SZA_Arr, min_SZA_Arr
    

def ExtremaNOMINAL():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesNOMINAL in os.walk(in_file_path8):
        sun_Arr = []
        rms_Arr = []
        mean_Arr = []

        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileNOMINAL in filesNOMINAL:
            array1=[]
            array2=[]
            array3=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileNOMINAL.endswith('.dat') and not fileNOMINAL.startswith('f'):
            
                sunNOMINAL = fileNOMINAL[16:21]
                #print("sunNOMINAL "+sunNOMINAL)

                sizeNOMINAL = (len(open(in_file_path8+fileNOMINAL).readlines()))
                

                with open(in_file_path8 + 'lowest_temp_sol_' + sunNOMINAL + '.dat','r') as input_fileNOMINAL:
                    for i in input_fileNOMINAL:
                        
                        colNOMINAL=(i.split())
                        
                        if len(colNOMINAL) < 3:
                            continue
                        else:
                            segTa_nominal=colNOMINAL[0]
                            array1.append(segTa_nominal)
                            timeLMST_Ta_nominal=colNOMINAL[1]
                            array2.append(timeLMST_Ta_nominal)
                            Ta_nominal = float(colNOMINAL[2])
                            array3.append(Ta_nominal)

                rms, mean = means_rms(array3, sizeNOMINAL)
                rms_Arr.append(rms)
                mean_Arr.append(mean)

                sun_Arr.append(sunNOMINAL)


    return sun_Arr, rms_Arr, mean_Arr


def TOA():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, fileSuns in os.walk(in_file_path13):
        sun_Arr = []
        array2=[]
        
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileSun in fileSuns:
            
            
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileSun.endswith('.dat') and not fileSun.startswith('f'):
            
                sizeP = (len(open(in_file_path13+fileSun).readlines()))
                with open(in_file_path13 + 'sol_Ls_ABC1_TOA.dat','r') as input_fileSun:
                    for i in input_fileSun:
                        
                        colSUN=(i.split())

                        if len(colSUN) < 3:
                            continue
                        else:
                            sol_TOA=colSUN[0]
                            sun_Arr.append(sol_TOA)
                            ABC1_TOA=float(colSUN[2])
                            array2.append(ABC1_TOA)


    return sun_Arr, array2


def ExtremaGTS_RHSurf_Sigmas():
    
    abs_maxT_Arr = []
    TIME_abs_maxT_Arr = []
    sun_Arr = []

    abs_max_RH_Surf_Arr = []
    TIME_abs_max_RH_Surf_Arr = []

    abs_minGTS_Arr = []
    TIME_abs_minGTS_Arr = []

    max_SZA_Arr = []
    min_SZA_Arr = []

    max_SZA_RH_Surf_Arr = []

    rms_Arr = []
    mean_Arr = []
    st_Dev_GTS_Max_Arr = []
    st_Dev_GTS_Min_Arr = []
    st_Dev_RH_Surf_Max_Arr = []
    

    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesGTS_RHSurf_Sigmas in os.walk(in_file_path3):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileGTS_RHSurf_Sigmas in filesGTS_RHSurf_Sigmas:
            array1=[]
            array2=[]
            array3=[]
            array4=[]
            array5=[]
            array6=[]
            Tg_nominal=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileGTS_RHSurf_Sigmas.endswith('.dat') and not fileGTS_RHSurf_Sigmas.startswith('f'):
            
                sunGTS_RHSurf_Sigmas = fileGTS_RHSurf_Sigmas[36:41]
                #print("sunGTS_RHSurf_Sigmas " + sunGTS_RHSurf_Sigmas)
                
                sizeGTS = (len(open(in_file_path3+fileGTS_RHSurf_Sigmas).readlines()))
                
                with open(in_file_path3 + 'means_RH_RHSurf_Temps_UV_sigmas_sol_' + sunGTS_RHSurf_Sigmas + '.dat','r') as input_fileGTS_RHSurf_Sigmas:
                    for i in input_fileGTS_RHSurf_Sigmas:
                        
                        colGTS=(i.split())
                        
                        if len(colGTS) < 6:
                            continue
                        else:
                            segGTS = colGTS[0]
                            array1.append(segGTS)
                            timeLMST_GTS = colGTS[1]
                            array2.append(timeLMST_GTS)
                            GTS = float(colGTS[4])
                            array3.append(GTS)
                            Tg_nominal.append(GTS)
                            st_Dev_GTS = float(colGTS[5])
                            array4.append(st_Dev_GTS)
                            RH_Surf = float(colGTS[6])
                            array5.append(RH_Surf)
                            st_Dev_RH_Surf = float(colGTS[7])
                            array6.append(st_Dev_RH_Surf)

                sun_Arr.append(sunGTS_RHSurf_Sigmas)
                
                abs_maxRHSurf, pos_abs_maxRHSurf = absoluteMax(array5)
                abs_max_RH_Surf_Arr.append(abs_maxRHSurf)

                if abs_maxRHSurf == -1.0:
                    TIME_abs_max_RH_Surf_Arr.append("00:00:00")
                else:                    
                    TIME_abs_max_RH_Surf_Arr.append(array2[pos_abs_maxRHSurf])

                abs_maxT, pos_abs_maxT = absoluteMax(array3)
                abs_maxT_Arr.append(abs_maxT)

                if abs_maxT == -1.0:
                    TIME_abs_maxT_Arr.append("00:00:00")
                else:                    
                    TIME_abs_maxT_Arr.append(array2[pos_abs_maxT])

                abs_minGTS, pos_abs_minGTS = absoluteMin(array3)
                abs_minGTS_Arr.append(abs_minGTS)

                if abs_minGTS == -1.0:
                    TIME_abs_minGTS_Arr.append("00:00:00")
                else:                    
                    TIME_abs_minGTS_Arr.append(array2[pos_abs_minGTS])

                if abs_maxT == -1.0:
                    st_Dev_GTS_Max_Arr.append(-1.00)
                    
                else:
                    st_Dev_GTS_Max_Arr.append(array4[pos_abs_maxT])

                if abs_minGTS == -1.0:
                    st_Dev_GTS_Min_Arr.append(-1.00)
                else:
                    st_Dev_GTS_Min_Arr.append(array4[pos_abs_minGTS])


                if abs_maxRHSurf == -1.0:
                    st_Dev_RH_Surf_Max_Arr.append(-1.00)
                else:
                    st_Dev_RH_Surf_Max_Arr.append(array6[pos_abs_maxRHSurf])

                if abs_maxT == -1.00:
                    max_SZA_GTS = -1.00
                    min_SZA_GTS = -1.00
                    max_SZA_Arr.append(max_SZA_GTS)
                    min_SZA_Arr.append(min_SZA_GTS)
                else:
                    
                
                    max_SZA_GTS, min_SZA_GTS = max_min_SZA(sunGTS_RHSurf_Sigmas, array2[pos_abs_maxT], array2[pos_abs_minGTS])

                    if str(max_SZA_GTS).isdigit() and str(min_SZA_GTS).isdigit():
                        o = 1
                    
                    
                        if float(max_SZA_GTS) > 100.0:
                            max_SZA_GTS = '******'

                        if float(min_SZA_GTS) > 100.0:
                            min_SZA_GTS = '******'

                    max_SZA_Arr.append(max_SZA_GTS)
                    min_SZA_Arr.append(min_SZA_GTS)
                
                if abs_maxRHSurf == -1.0:
                    max_SZA_RH_Surf = -1.00
                    residuo = -1.00
                    max_SZA_RH_Surf_Arr.append(max_SZA_RH_Surf)
                    
                else:

                    max_SZA_RH_Surf, residuo = max_min_SZA(sunGTS_RHSurf_Sigmas, array2[pos_abs_maxRHSurf], array2[pos_abs_minGTS])
                    if str(max_SZA_RH_Surf).isdigit():
                        o = 1

                        if float(max_SZA_RH_Surf) > 100.0:
                            max_SZA_RH_Surf = '******'

                    max_SZA_RH_Surf_Arr.append(max_SZA_RH_Surf)
                
                rms, mean = means_rms(Tg_nominal, sizeGTS)
                rms_Arr.append(rms)
                mean_Arr.append(mean)

    return sun_Arr, abs_maxT_Arr, TIME_abs_maxT_Arr, abs_max_RH_Surf_Arr, TIME_abs_max_RH_Surf_Arr, abs_minGTS_Arr, TIME_abs_minGTS_Arr, max_SZA_Arr, min_SZA_Arr, max_SZA_RH_Surf_Arr, rms_Arr, mean_Arr, st_Dev_GTS_Max_Arr, st_Dev_GTS_Min_Arr, st_Dev_RH_Surf_Max_Arr


def ExtremaRH():
    
   
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesRH in os.walk(in_file_path4):
        
        sun_Arr = []
        
        abs_maxRH_Arr = []
        TIME_abs_maxRH_Arr = []

        abs_minRH_Temp_Arr = []
        TIME_abs_minRH_Temp_Arr = []

        max_SZA_Arr = []
        min_SZA_Arr = []

        MR_Arr =[]
        VMR_Arr = []

        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileRH in filesRH:
            array1=[]
            array2=[]
            array3=[]
            array4=[]
            array5=[]
            array6=[]
            
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileRH.endswith('.dat') and not fileRH.startswith('f'):
                sunRH = fileRH[20:25]
                #print(sunRH)
                sizeRH = (len(open(in_file_path4+fileRH).readlines()))
                

                with open(in_file_path4 + 'RH_Surf_SubSurf_sol_' + sunRH + '.dat','r') as input_fileRH:
                    for i in input_fileRH:

                        colRH=(i.split())

                        if len(colRH) < 3:
                            continue

                        else:
                            
                            segRH = colRH[0]
                            array1.append(segRH)
                            timeLMST_RH = colRH[1]
                            array2.append(timeLMST_RH)
                            RH_Temp = float(colRH[3])
                            array3.append(RH_Temp)
                            RH = float(colRH[5])
                            array4.append(RH)
                            MR = colRH[7]
                            array5.append(MR)
                            VMR = colRH[8]
                            array6.append(VMR)
                           

                sun_Arr.append(sunRH)
                
                abs_maxRH, pos_abs_maxRH = absoluteMax(array4)
                abs_maxRH_Arr.append(abs_maxRH)
                if abs_maxRH == -1.00:
                    TIME_abs_maxRH_Arr.append("00:00:00")
                    MR_Arr.append("-1.00")
                    VMR_Arr.append("-1.00")
                else:
                    TIME_abs_maxRH_Arr.append(array2[pos_abs_maxRH])
                    MR_Arr.append(array5[pos_abs_maxRH])
                    VMR_Arr.append(array6[pos_abs_maxRH])

                abs_minRH_Temp, pos_abs_minRH_Temp = absoluteMin(array3)
                abs_minRH_Temp_Arr.append(abs_minRH_Temp)
                if abs_minRH_Temp == -1.00:
                    TIME_abs_minRH_Temp_Arr.append("00:00:00")
                else:
                    TIME_abs_minRH_Temp_Arr.append(array2[pos_abs_minRH_Temp])

                
                if abs_maxRH == -1.00:
                    max_SZA_RH = -1.00
                    min_SZA_RH_Temp = -1.00
                    max_SZA_Arr.append(max_SZA_RH)
                    min_SZA_Arr.append(min_SZA_RH_Temp)
                else:
                    
                    max_SZA_RH, min_SZA_RH_Temp = max_min_SZA(sunRH, array2[pos_abs_maxRH], array2[pos_abs_minRH_Temp])

                    if str(max_SZA_RH).isdigit() and str(min_SZA_RH_Temp).isdigit():
                        o = 1

                        if float(max_SZA_RH) > 100.0:
                            max_SZA_RH = '******'

                        if float(min_SZA_RH_Temp) > 100.0:
                            min_SZA_RH_Temp = '******'

                    max_SZA_Arr.append(max_SZA_RH)
                    min_SZA_Arr.append(min_SZA_RH_Temp)

    return sun_Arr, abs_maxRH_Arr, TIME_abs_maxRH_Arr, abs_minRH_Temp_Arr, TIME_abs_minRH_Temp_Arr, max_SZA_Arr, min_SZA_Arr, VMR_Arr, MR_Arr


def ExtremaUV():
    
    sun_Arr = []
    
    abs_maxUV_global_A_Arr = []
    TIME_abs_maxUV_global_A_Arr = []

    abs_maxUV_global_B_Arr = []
    TIME_abs_maxUV_global_B_Arr = []

    abs_maxUV_global_C_Arr = []
    TIME_abs_maxUV_global_C_Arr = []

    abs_maxUV_global_ABC_Arr = []
    TIME_abs_maxUV_global_ABC_Arr = []

    abs_maxUV_global_D_Arr = []
    TIME_abs_maxUV_global_D_Arr = []

    abs_maxUV_global_E_Arr = [] 
    TIME_abs_maxUV_global_E_Arr = []

    abs_maxUV_diffuse_A_Arr = []
    TIME_abs_maxUV_diffuse_A_Arr = []

    abs_maxUV_diffuse_B_Arr = []
    TIME_abs_maxUV_diffuse_B_Arr = []

    abs_maxUV_diffuse_C_Arr = []
    TIME_abs_maxUV_diffuse_C_Arr = []

    abs_maxUV_diffuse_ABC_Arr = []
    TIME_abs_maxUV_diffuse_ABC_Arr = []

    abs_maxUV_diffuse_D_Arr = []
    TIME_abs_maxUV_diffuse_D_Arr = []

    abs_maxUV_diffuse_E_Arr = []
    TIME_abs_maxUV_diffuse_E_Arr = []

    max_SZA_Arr_global_A = []
    max_SZA_Arr_global_B = []
    max_SZA_Arr_global_C = []
    max_SZA_Arr_global_ABC = []
    max_SZA_Arr_global_D = []
    max_SZA_Arr_global_E = []


    max_SZA_Arr_diffuse_A = []
    max_SZA_Arr_diffuse_B = []
    max_SZA_Arr_diffuse_C = []
    max_SZA_Arr_diffuse_ABC = []
    max_SZA_Arr_diffuse_D = []
    max_SZA_Arr_diffuse_E = []
    
    current_ABC1_TOA_Arr = []

    tau_UV_Arr = []


    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesUV in os.walk(in_file_path5):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileUV in filesUV:
            array1=[]
            array2=[]
            array3=[]
            array4=[]
            array5=[]
            array6=[]
            array7=[]
            array8=[]
            array9=[]
            array10=[]
            array11=[]
            array12=[]
            array13=[]
            array14=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileUV.endswith('.dat') and not fileUV.startswith('f'):
            
                sunUV = fileUV[18:23]
                #print("sunUV "+sunUV)

                sizeGTS = (len(open(in_file_path5+fileUV).readlines()))

                with open(in_file_path5 + 'irradiance_UV_sol_' + sunUV + '.dat','r') as input_fileUV:
                    for i in input_fileUV:
                        
                        colUV=(i.split())
                        
                        if len(colUV) < 3:
                            continue
                        else:
                            segUV = colUV[0]
                            array1.append(segUV)

                            timeLMST_UV = colUV[1]
                            array2.append(timeLMST_UV)

                            UV_global_A = float(colUV[2])
                            array3.append(UV_global_A)

                            UV_diffuse_A = float(colUV[3])
                            array4.append(UV_diffuse_A)

                            UV_global_B = float(colUV[5])
                            array5.append(UV_global_B)

                            UV_diffuse_B = float(colUV[6])
                            array6.append(UV_diffuse_B)

                            UV_global_C = float(colUV[8])
                            array7.append(UV_global_C)

                            UV_diffuse_C = float(colUV[9])
                            array8.append(UV_diffuse_C)

                            UV_global_ABC = float(colUV[11])
                            array9.append(UV_global_ABC)

                            UV_diffuse_ABC = float(colUV[12])
                            array10.append(UV_diffuse_ABC)

                            UV_global_D = float(colUV[14])
                            array11.append(UV_global_D)

                            UV_diffuse_D = float(colUV[15])
                            array12.append(UV_diffuse_D)

                            UV_global_E = float(colUV[17])
                            array13.append(UV_global_E)

                            UV_diffuse_E = float(colUV[18])
                            array14.append(UV_diffuse_E)

                sun_Arr.append(sunUV)
                
                abs_maxUV_global_A, pos_abs_maxUV_global_A = absoluteMax(array3)
                abs_maxUV_global_A_Arr.append(abs_maxUV_global_A)
                if abs_maxUV_global_A == -1.00:
                    TIME_abs_maxUV_global_A_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_global_A_Arr.append(array2[pos_abs_maxUV_global_A])

                abs_maxUV_global_B, pos_abs_maxUV_global_B = absoluteMax(array5)
                abs_maxUV_global_B_Arr.append(abs_maxUV_global_B)
                if abs_maxUV_global_B == -1.00:
                    TIME_abs_maxUV_global_B_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_global_B_Arr.append(array2[pos_abs_maxUV_global_B])

                abs_maxUV_global_C, pos_abs_maxUV_global_C = absoluteMax(array7)
                abs_maxUV_global_C_Arr.append(abs_maxUV_global_C)
                if abs_maxUV_global_C == -1.00:
                    TIME_abs_maxUV_global_C_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_global_C_Arr.append(array2[pos_abs_maxUV_global_C])

                abs_maxUV_global_ABC, pos_abs_maxUV_global_ABC = absoluteMax(array9)
                abs_maxUV_global_ABC_Arr.append(abs_maxUV_global_ABC)
                if abs_maxUV_global_ABC == -1.00:
                    TIME_abs_maxUV_global_ABC_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_global_ABC_Arr.append(array2[pos_abs_maxUV_global_ABC])

                abs_maxUV_global_D, pos_abs_maxUV_global_D = absoluteMax(array11)
                abs_maxUV_global_D_Arr.append(abs_maxUV_global_D)
                if abs_maxUV_global_D == -1.00:
                    TIME_abs_maxUV_global_D_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_global_D_Arr.append(array2[pos_abs_maxUV_global_D])

                abs_maxUV_global_E, pos_abs_maxUV_global_E = absoluteMax(array13)
                abs_maxUV_global_E_Arr.append(abs_maxUV_global_E)
                if abs_maxUV_global_E == -1.00:
                    TIME_abs_maxUV_global_E_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_global_E_Arr.append(array2[pos_abs_maxUV_global_E])

                abs_maxUV_diffuse_A, pos_abs_maxUV_diffuse_A = absoluteMax(array4)
                abs_maxUV_diffuse_A_Arr.append(abs_maxUV_diffuse_A)
                if abs_maxUV_diffuse_A == -1.00:
                    TIME_abs_maxUV_diffuse_A_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_diffuse_A_Arr.append(array2[pos_abs_maxUV_diffuse_A])

                abs_maxUV_diffuse_B, pos_abs_maxUV_diffuse_B = absoluteMax(array6)
                abs_maxUV_diffuse_B_Arr.append(abs_maxUV_diffuse_B)
                if abs_maxUV_diffuse_B == -1.00:
                    TIME_abs_maxUV_diffuse_B_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_diffuse_B_Arr.append(array2[pos_abs_maxUV_diffuse_B])

                abs_maxUV_diffuse_C, pos_abs_maxUV_diffuse_C = absoluteMax(array8)
                abs_maxUV_diffuse_C_Arr.append(abs_maxUV_diffuse_C)
                if abs_maxUV_diffuse_C == -1.00:
                    TIME_abs_maxUV_diffuse_C_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_diffuse_C_Arr.append(array2[pos_abs_maxUV_diffuse_C])

                abs_maxUV_diffuse_ABC, pos_abs_maxUV_diffuse_ABC = absoluteMax(array10)
                abs_maxUV_diffuse_ABC_Arr.append(abs_maxUV_diffuse_ABC)
                if abs_maxUV_diffuse_ABC == -1.00:
                    TIME_abs_maxUV_diffuse_ABC_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_diffuse_ABC_Arr.append(array2[pos_abs_maxUV_diffuse_ABC])

                abs_maxUV_diffuse_D, pos_abs_maxUV_diffuse_D = absoluteMax(array12)
                abs_maxUV_diffuse_D_Arr.append(abs_maxUV_diffuse_D)
                if abs_maxUV_diffuse_D == -1.00:
                    TIME_abs_maxUV_diffuse_D_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_diffuse_D_Arr.append(array2[pos_abs_maxUV_diffuse_D])

                abs_maxUV_diffuse_E, pos_abs_maxUV_diffuse_E = absoluteMax(array14)
                abs_maxUV_diffuse_E_Arr.append(abs_maxUV_diffuse_E)
                if abs_maxUV_diffuse_E == -1.00:
                    TIME_abs_maxUV_diffuse_E_Arr.append("00:00:00")
                else:
                    TIME_abs_maxUV_diffuse_E_Arr.append(array2[pos_abs_maxUV_diffuse_E])

                if abs_maxUV_global_A == -1.00:
                    max_SZA_global_A = -1.00
                    max_SZA_Arr_global_A.append(max_SZA_global_A)
                    
                else:

                    max_SZA_global_A  = max_SZA(sunUV, array2[pos_abs_maxUV_global_A])

                    if str(max_SZA_global_A).isdigit():
                        o = 1

                        if float(max_SZA_global_A) > 100.0:
                            max_SZA_global_A = '******'

                    max_SZA_Arr_global_A.append(max_SZA_global_A)

                if abs_maxUV_global_B == -1.00:
                    max_SZA_global_B = -1.00
                    max_SZA_Arr_global_B.append(max_SZA_global_B)
                    
                else:

                    max_SZA_global_B  = max_SZA(sunUV, array2[pos_abs_maxUV_global_B])

                    if str(max_SZA_global_B).isdigit():
                        o = 1

                        if float(max_SZA_global_B) > 100.0:
                            max_SZA_global_B = '******'

                    max_SZA_Arr_global_B.append(max_SZA_global_B)

                if abs_maxUV_global_C == -1.00:
                    max_SZA_global_C = -1.00
                    max_SZA_Arr_global_C.append(max_SZA_global_C)
                    
                else:

                    max_SZA_global_C  = max_SZA(sunUV, array2[pos_abs_maxUV_global_C])

                    if str(max_SZA_global_C).isdigit():
                        o = 1

                        if float(max_SZA_global_C) > 100.0:
                            max_SZA_global_C = '******'

                    max_SZA_Arr_global_C.append(max_SZA_global_C)

                if abs_maxUV_global_ABC == -1.00:
                    max_SZA_global_ABC = -1.00
                    max_SZA_Arr_global_ABC.append(max_SZA_global_ABC)
                    
                else:

                    max_SZA_global_ABC  = max_SZA(sunUV, array2[pos_abs_maxUV_global_ABC])

                    if str(max_SZA_global_ABC).isdigit():
                        o = 1

                        if float(max_SZA_global_ABC) > 100.0:
                            max_SZA_global_ABC = '******'

                    max_SZA_Arr_global_ABC.append(max_SZA_global_ABC)

                if abs_maxUV_global_D == -1.00:
                    max_SZA_global_D = -1.00
                    max_SZA_Arr_global_D.append(max_SZA_global_D)
                    
                else:
                    max_SZA_global_D  = max_SZA(sunUV, array2[pos_abs_maxUV_global_D])

                    if str(max_SZA_global_D).isdigit():
                        o = 1

                        if float(max_SZA_global_D) > 100.0:
                            max_SZA_global_D = '******'

                    max_SZA_Arr_global_D.append(max_SZA_global_D)

                if abs_maxUV_global_E == -1.00:
                    max_SZA_global_E = -1.00
                    max_SZA_Arr_global_E.append(max_SZA_global_E)
                    
                else:

                    max_SZA_global_E  = max_SZA(sunUV, array2[pos_abs_maxUV_global_E])

                    if str(max_SZA_global_E).isdigit():
                        o = 1

                        if float(max_SZA_global_E) > 100.0:
                            max_SZA_global_E = '******'

                    max_SZA_Arr_global_E.append(max_SZA_global_E)

                if abs_maxUV_diffuse_A == -1.00:
                    max_SZA_diffuse_A = -1.00
                    max_SZA_Arr_diffuse_A.append(max_SZA_diffuse_A)
                    
                else:

                    max_SZA_diffuse_A  = max_SZA(sunUV, array2[pos_abs_maxUV_diffuse_A])

                    if str(max_SZA_diffuse_A).isdigit():
                        o = 1

                        if float(max_SZA_diffuse_A) > 100.0:
                            max_SZA_diffuse_A = '******'

                    max_SZA_Arr_diffuse_A.append(max_SZA_diffuse_A)

                if abs_maxUV_diffuse_B == -1.00:
                    max_SZA_diffuse_B = -1.00
                    max_SZA_Arr_diffuse_B.append(max_SZA_diffuse_B)
                    
                else:

                    max_SZA_diffuse_B  = max_SZA(sunUV, array2[pos_abs_maxUV_diffuse_B])

                    if str(max_SZA_diffuse_B).isdigit():
                        o = 1

                        if float(max_SZA_diffuse_B) > 100.0:
                            max_SZA_diffuse_B = '******'

                    max_SZA_Arr_diffuse_B.append(max_SZA_diffuse_B)

                if abs_maxUV_diffuse_C == -1.00:
                    max_SZA_diffuse_C = -1.00
                    max_SZA_Arr_diffuse_C.append(max_SZA_diffuse_C)
                    
                else:
                    max_SZA_diffuse_C  = max_SZA(sunUV, array2[pos_abs_maxUV_diffuse_C])

                    if str(max_SZA_diffuse_C).isdigit():
                        o = 1

                        if float(max_SZA_diffuse_C) > 100.0:
                            max_SZA_diffuse_C = '******'

                    max_SZA_Arr_diffuse_C.append(max_SZA_diffuse_C)

                if abs_maxUV_diffuse_ABC == -1.00:
                    max_SZA_diffuse_ABC = -1.00
                    max_SZA_Arr_diffuse_ABC.append(max_SZA_diffuse_ABC)
                    
                else:

                    max_SZA_diffuse_ABC  = max_SZA(sunUV, array2[pos_abs_maxUV_diffuse_ABC])

                    if str(max_SZA_diffuse_ABC).isdigit():
                        o = 1

                        if float(max_SZA_diffuse_ABC) > 100.0:
                            max_SZA_diffuse_ABC = '******'

                    max_SZA_Arr_diffuse_ABC.append(max_SZA_diffuse_ABC)

                if abs_maxUV_diffuse_D == -1.00:
                    max_SZA_diffuse_D = -1.00
                    max_SZA_Arr_diffuse_D.append(max_SZA_diffuse_D)
                    
                else:

                    max_SZA_diffuse_D  = max_SZA(sunUV, array2[pos_abs_maxUV_diffuse_D])

                    if str(max_SZA_diffuse_D).isdigit():
                        o = 1

                        if float(max_SZA_diffuse_D) > 100.0:
                            max_SZA_diffuse_D = '******'

                    max_SZA_Arr_diffuse_D.append(max_SZA_diffuse_D)

                if abs_maxUV_diffuse_E == -1.00:
                    max_SZA_diffuse_E = -1.00
                    max_SZA_Arr_diffuse_E.append(max_SZA_diffuse_E)
                    
                else:
                    max_SZA_diffuse_E  = max_SZA(sunUV, array2[pos_abs_maxUV_diffuse_E])

                    if str(max_SZA_diffuse_E).isdigit():
                        o = 1

                        if float(max_SZA_diffuse_E) > 100.0:
                            max_SZA_diffuse_E = '******'

                    max_SZA_Arr_diffuse_E.append(max_SZA_diffuse_E)


                sol_TOA, ABC1_TOA= TOA()

                if sunUV in sol_TOA:
                    #print(sunUV)
                    
                    i = sol_TOA.index(sunUV)
                    i2 = sun_Arr.index(sunUV)

                    current_ABC1_TOA = ABC1_TOA[i]

                    current_ABC1_TOA_Arr.append(current_ABC1_TOA)

                    if is_number(abs_maxUV_global_ABC_Arr[i2]) and is_number(abs_maxUV_diffuse_ABC_Arr[i2]) and is_number(max_SZA_Arr_global_ABC[i2]) and is_number(ABC1_TOA[i]):
                        o = 1

                        if ((float(abs_maxUV_global_ABC_Arr[i2]) != -1.0) and (float(abs_maxUV_global_ABC_Arr[i2]) > 0.0) and (float(abs_maxUV_diffuse_ABC_Arr[i2]) != -1.0) and (float(abs_maxUV_diffuse_ABC_Arr[i2]) > 0.0) and (float(max_SZA_Arr_global_ABC[i2]) != -1.0) and (float(max_SZA_Arr_global_ABC[i2]) > 0.0) and (float(ABC1_TOA[i]) != -1.0) and (float(ABC1_TOA[i]) > 0.0)):

                            tau_UV = -np.log(((abs_maxUV_global_ABC_Arr[i2]/np.cos(np.deg2rad(max_SZA_Arr_global_ABC[i2])) - abs_maxUV_diffuse_ABC_Arr[i2])/ABC1_TOA[i]).astype(np.float64)) * np.cos(np.deg2rad(max_SZA_Arr_global_ABC[i2]))
                            tau_UV_Arr.append(tau_UV)
                        
                        else:
                            #print("Entra 1 else")
                            tau_UV = -1.00
                            tau_UV_Arr.append(tau_UV)
                    else:
                        # print(abs_maxUV_global_ABC_Arr[i2])
                        # print(abs_maxUV_diffuse_ABC_Arr[i2])
                        # print(max_SZA_Arr_global_ABC[i2])
                        # print(ABC1_TOA[i2])
                        
                        tau_UV = -1.00
                        tau_UV_Arr.append(tau_UV)
            
                
                
        return sun_Arr, abs_maxUV_global_A_Arr, TIME_abs_maxUV_global_A_Arr, abs_maxUV_global_B_Arr, TIME_abs_maxUV_global_B_Arr, abs_maxUV_global_C_Arr, TIME_abs_maxUV_global_C_Arr, abs_maxUV_global_ABC_Arr, TIME_abs_maxUV_global_ABC_Arr, abs_maxUV_global_D_Arr, TIME_abs_maxUV_global_D_Arr, abs_maxUV_global_E_Arr, TIME_abs_maxUV_global_E_Arr, abs_maxUV_diffuse_A_Arr, TIME_abs_maxUV_diffuse_A_Arr, abs_maxUV_diffuse_B_Arr, TIME_abs_maxUV_diffuse_B_Arr, abs_maxUV_diffuse_C_Arr, TIME_abs_maxUV_diffuse_C_Arr, abs_maxUV_diffuse_ABC_Arr, TIME_abs_maxUV_diffuse_ABC_Arr, abs_maxUV_diffuse_D_Arr, TIME_abs_maxUV_diffuse_D_Arr, abs_maxUV_diffuse_E_Arr, TIME_abs_maxUV_diffuse_E_Arr, max_SZA_Arr_global_A, max_SZA_Arr_global_B, max_SZA_Arr_global_C, max_SZA_Arr_global_ABC, max_SZA_Arr_global_D, max_SZA_Arr_global_E, max_SZA_Arr_diffuse_A, max_SZA_Arr_diffuse_B, max_SZA_Arr_diffuse_C, max_SZA_Arr_diffuse_ABC, max_SZA_Arr_diffuse_D, max_SZA_Arr_diffuse_E, current_ABC1_TOA_Arr, tau_UV_Arr



def ExtremaDerivGTS():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesDerivGTS in os.walk(in_file_path6):
        abs_maxDerivGTS_Arr = []
        TIME_abs_maxDerivGTS_Arr = []

        sun_Arr = []

        abs_minDerivGTS_Arr = []
        TIME_abs_minDerivGTS_Arr = []

        max_SZA_Arr = []
        min_SZA_Arr = []

        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileDerivGTS in filesDerivGTS:
            array1=[]
            array2=[]
            array3=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileDerivGTS.endswith('.dat') and not fileDerivGTS.startswith('f'):
            
                sunDerivGTS = fileDerivGTS[33:38]
                #print("sunDerivGTS "+sunDerivGTS)

                sizeT = (len(open(in_file_path6+fileDerivGTS).readlines()))

                with open(in_file_path6 + '1_2_3_4_derivativeGTS_spline_sol_' + sunDerivGTS + '.dat','r') as input_fileDerivGTS:
                    for i in input_fileDerivGTS:
                        
                        colDerivGTS=(i.split())
                        
                        if len(colDerivGTS) < 3:
                            continue
                        else:
                            segDerivGTS=colDerivGTS[0]
                            array1.append(segDerivGTS)
                            timeLMST_DerivGTS=colDerivGTS[1]
                            array2.append(timeLMST_DerivGTS)
                            DerivGTS = float(colDerivGTS[3])
                            array3.append(DerivGTS)
                sun_Arr.append(sunDerivGTS)
                
                abs_maxDerivGTS, pos_abs_maxDerivGTS= absoluteMax(array3)
                abs_maxDerivGTS_Arr.append(abs_maxDerivGTS)
                if abs_maxDerivGTS == -1.00:
                    TIME_abs_maxDerivGTS_Arr.append("00:00:00")
                else:
                    TIME_abs_maxDerivGTS_Arr.append(array2[pos_abs_maxDerivGTS])

                abs_minDerivGTS, pos_abs_minDerivGTS= absoluteMin(array3)
                abs_minDerivGTS_Arr.append(abs_minDerivGTS)
                if abs_minDerivGTS == -1.00:
                    TIME_abs_minDerivGTS_Arr.append("00:00:00")
                else:
                    
                    TIME_abs_minDerivGTS_Arr.append(array2[pos_abs_minDerivGTS])

                if abs_maxDerivGTS == -1.00:
                    max_SZA_DerivGTS = -1.00
                    min_SZA_DerivGTS = -1.00
                    max_SZA_Arr.append(max_SZA_DerivGTS)
                    min_SZA_Arr.append(min_SZA_DerivGTS)
                else:
                    
                    max_SZA_DerivGTS, min_SZA_DerivGTS = max_min_SZA(sunDerivGTS, array2[pos_abs_maxDerivGTS], array2[pos_abs_minDerivGTS])

                    if str(max_SZA_DerivGTS).isdigit() and str(min_SZA_DerivGTS).isdigit():
                        o = 1

                        if float(max_SZA_DerivGTS) > 100.0:
                            max_SZA_DerivGTS = '******'

                        if float(min_SZA_DerivGTS) > 100.0:
                            min_SZA_DerivGTS = '******'

                    max_SZA_Arr.append(max_SZA_DerivGTS)
                    min_SZA_Arr.append(min_SZA_DerivGTS)

    return sun_Arr, abs_maxDerivGTS_Arr, TIME_abs_maxDerivGTS_Arr, abs_minDerivGTS_Arr, TIME_abs_minDerivGTS_Arr, max_SZA_Arr, min_SZA_Arr


def ExtremaHeatFlux():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesDerivGTS in os.walk(in_file_path9):
        abs_maxSensb_HeatFlux_Arr = []
        TIME_abs_maxSensb_HeatFlux_Arr = []
        sun_Arr = []

        abs_minSensb_HeatFlux_Arr = []
        TIME_abs_minSensb_HeatFlux_Arr = []

        max_SZA_Arr = []
        min_SZA_Arr = []

        rms_Arr = []
        mean_Arr = []

        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileDerivGTS in filesDerivGTS:
            array1=[]
            array2=[]
            array3=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileDerivGTS.endswith('.dat') and not fileDerivGTS.startswith('f'):
            
                sunDerivGTS = fileDerivGTS[27:32]
                #print("ExtremaHeatFlux "+sunDerivGTS)

                sizeT = (len(open(in_file_path9+fileDerivGTS).readlines()))

                with open(in_file_path9 + 'mean_P_Tg_Ta_tGrad_rho_sol_' + sunDerivGTS + '.dat','r') as input_fileDerivGTS:
                    for i in input_fileDerivGTS:
                        
                        colDerivGTS=(i.split())
                        
                        if len(colDerivGTS) < 3:
                            continue
                        else:
                            segSensb_HeatFlux=colDerivGTS[0]
                            array1.append(segSensb_HeatFlux)
                            timeLMST_Sensb_HeatFlux=colDerivGTS[1]
                            array2.append(timeLMST_Sensb_HeatFlux)
                            Sensb_HeatFlux = float(colDerivGTS[7])
                            array3.append(Sensb_HeatFlux)

                sun_Arr.append(sunDerivGTS)
                
                abs_maxSensb_HeatFlux, pos_abs_maxSensb_HeatFlux= absoluteMax(array3)
                abs_maxSensb_HeatFlux_Arr.append(abs_maxSensb_HeatFlux)

                if abs_maxSensb_HeatFlux == -1.00:
                    TIME_abs_maxSensb_HeatFlux_Arr.append("00:00:00")
                else:
                    TIME_abs_maxSensb_HeatFlux_Arr.append(array2[pos_abs_maxSensb_HeatFlux])

                abs_minSensb_HeatFlux, pos_abs_minSensb_HeatFlux= absoluteMin(array3)
                abs_minSensb_HeatFlux_Arr.append(abs_minSensb_HeatFlux)

                if abs_minSensb_HeatFlux == -1.00:
                    TIME_abs_minSensb_HeatFlux_Arr.append("00:00:00")
                else:
                    TIME_abs_minSensb_HeatFlux_Arr.append(array2[pos_abs_minSensb_HeatFlux])

                if abs_maxSensb_HeatFlux == -1.00:
                    max_SZA_Sensb_HeatFlux = -1.00
                    min_SZA_Sensb_HeatFlux = -1.00
                    max_SZA_Arr.append(max_SZA_Sensb_HeatFlux)
                    min_SZA_Arr.append(min_SZA_Sensb_HeatFlux)
                else:
                    max_SZA_Sensb_HeatFlux, min_SZA_Sensb_HeatFlux = max_min_SZA(sunDerivGTS, array2[pos_abs_maxSensb_HeatFlux], array2[pos_abs_minSensb_HeatFlux])

                    if str(max_SZA_Sensb_HeatFlux).isdigit() and str(min_SZA_Sensb_HeatFlux).isdigit():
                        o = 1
                        if float(max_SZA_Sensb_HeatFlux) > 100.0:
                            max_SZA_Sensb_HeatFlux = '******'

                        if float(min_SZA_Sensb_HeatFlux) > 100.0:
                            min_SZA_Sensb_HeatFlux = '******'

                    max_SZA_Arr.append(max_SZA_Sensb_HeatFlux)
                    min_SZA_Arr.append(min_SZA_Sensb_HeatFlux)

                rms, mean = means_rms(array3, sizeT)
                rms_Arr.append(rms)
                mean_Arr.append(mean)



    return sun_Arr, abs_maxSensb_HeatFlux_Arr, TIME_abs_maxSensb_HeatFlux_Arr, abs_minSensb_HeatFlux_Arr, TIME_abs_minSensb_HeatFlux_Arr, max_SZA_Arr, min_SZA_Arr, rms_Arr, mean_Arr


#call openFile(u7, sun_topo_path, error_openFile)

def ExtremaFileDiff():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesPS in os.walk(in_file_path7):

        sun_Arr = []
        rms_Arr = []
        mean_Arr = []
        
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for filePS in filesPS:
            array1=[]
            array2=[]
            array3=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if filePS.endswith('.dat') and not filePS.startswith('f'):
            
                sunDiff = filePS[27:32]
                #print("sunDiff "+sunDiff)
                
                sizeDiff = (len(open(in_file_path7+filePS).readlines()))
                with open(in_file_path7 + 'difference_AirTemp_GTS_sol_' + sunDiff + '.dat','r') as input_filePS:
                    for i in input_filePS:
                        
                        colDiff=(i.split())
                        
                        if len(colDiff) < 3:
                            continue
                        else:
                            segDifference=colDiff[0]
                            array1.append(segDifference)
                            timeLMST_Diff=colDiff[1]
                            array2.append(timeLMST_Diff)
                            Difference = float(colDiff[4])
                            array3.append(Difference)

                rms, mean = means_rms(array3, sizeDiff)
                rms_Arr.append(rms)
                mean_Arr.append(mean)

                sun_Arr.append(sunDiff)

    return sun_Arr, rms_Arr, mean_Arr





#call openFile(u8, ls_file_path, error_openFile)

#call openFile(u12, TOA_file_path, error_openFile)


def ExtremaMDB1B2():
    
    sun_Arr=[]
    absDiff_Arr = []
    TIME_abs_maxDiff_Arr=[]

    max_SZA_Arr = []

    T1_Arr = []
    T2_Arr = []

    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesMDB1B2 in os.walk(in_file_path10):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileMDB1B2 in filesMDB1B2:
            array1=[]
            array2=[]
            array3=[]
            array4=[]
            array5=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileMDB1B2.endswith('.dat') and not fileMDB1B2.startswith('f'):
            
                sunMDB1B2 = fileMDB1B2[3:8]
                #print("sunMDB1B2 " + sunMDB1B2)
                
                sizeT = (len(open(in_file_path10+fileMDB1B2).readlines()))
                # print(sunMDB1B2)
                # print(sizeT)
                with open(in_file_path10 + 'MD_' + sunMDB1B2 + '.dat','r') as input_fileMDB1B2:
                    for i in input_fileMDB1B2:
                        
                        colMDB1B2=(i.split())
                        if len(colMDB1B2) < 3:
                            continue
                        else:
                            segT1T2=colMDB1B2[0]
                            array1.append(segT1T2)
                            timeLMST_T1T2=colMDB1B2[1][0:8]
                            array2.append(timeLMST_T1T2)
                            T1 = float(colMDB1B2[8])
                            array3.append(T1)
                            T2 = float(colMDB1B2[10])
                            array4.append(T2)

                absDiff = absoluteDifference(array3,array4,sizeT)

                abs_maxDiff, pos_maxDiff = absoluteMax_Numpy(absDiff)

                absDiff_Arr.append(abs_maxDiff)
                sun_Arr.append(sunMDB1B2)
                TIME_abs_maxDiff_Arr.append(array2[pos_maxDiff])

                max_SZA_T1T2  = max_SZA(sunMDB1B2, array2[pos_maxDiff])

                if str(max_SZA_T1T2).isdigit():
                    o = 1
                    if float(max_SZA_T1T2) > 100.0:
                        max_SZA_T1T2 = '******'

                max_SZA_Arr.append(max_SZA_T1T2)

                T1_Arr.append(array3[pos_maxDiff])
                T2_Arr.append(array4[pos_maxDiff])


                

    return sun_Arr, absDiff_Arr, TIME_abs_maxDiff_Arr, max_SZA_Arr, T1_Arr, T2_Arr


def ExtremaNV():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, filesNV in os.walk(in_file_path11):
        
        abs_maxUV_Temp_Arr = []
        TIME_abs_maxUV_Temp_Arr = []

        sun_Arr = []
        
        abs_minUV_Temp_Arr = []
        TIME_abs_minUV_Temp_Arr = []

        max_SZA_Arr = []
        min_SZA_Arr = []
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileNV in filesNV:
            array1=[]
            array2=[]
            array3=[]
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileNV.endswith('.dat') and not fileNV.startswith('f'):
            
                sunNV = fileNV[3:8]
                #print("sunNV "+sunNV)
                sizeT = (len(open(in_file_path11+fileNV).readlines()))

                with open(in_file_path11 + 'NV_' + sunNV + '.dat','r') as input_fileNV:
                    for i in input_fileNV:
                        
                        colNV=(i.split())
                        
                        if len(colNV) < 3:
                            continue
                        else:
                            seg_UV_Temp=colNV[0]
                            array1.append(seg_UV_Temp)
                            timeLMST_UV_Temp=colNV[1][0:8]
                            array2.append(timeLMST_UV_Temp)
                            UV_Temp = float(colNV[8])
                            array3.append(UV_Temp)
                
                sun_Arr.append(sunNV)
                
                abs_maxUV_Temp, pos_abs_maxUV_Temp = absoluteMax(array3)
                abs_maxUV_Temp_Arr.append(abs_maxUV_Temp)
                TIME_abs_maxUV_Temp_Arr.append(array2[pos_abs_maxUV_Temp])

                abs_minUV_Temp, pos_abs_minUV_Temp = absoluteMin(array3)
                abs_minUV_Temp_Arr.append(abs_minUV_Temp)
                TIME_abs_minUV_Temp_Arr.append(array2[pos_abs_minUV_Temp])

                SZA_maxUV_Temp, SZA_minUV_Temp = max_min_SZA(sunNV, array2[pos_abs_maxUV_Temp], array2[pos_abs_minUV_Temp])
                
                if str(SZA_maxUV_Temp).isdigit() and str(SZA_minUV_Temp).isdigit():
                    o = 1

                    if float(SZA_maxUV_Temp) > 100.0:
                        SZA_maxUV_Temp = '******'

                    if float(SZA_minUV_Temp) > 100.0:
                        SZA_minUV_Temp = '******'

                max_SZA_Arr.append(SZA_maxUV_Temp)
                min_SZA_Arr.append(SZA_minUV_Temp)
                            

    return sun_Arr, abs_maxUV_Temp_Arr, TIME_abs_maxUV_Temp_Arr, abs_minUV_Temp_Arr, TIME_abs_minUV_Temp_Arr, max_SZA_Arr, min_SZA_Arr


def Extrema():
    
    # for base, dirs, filesNV in os.walk(in_file_path11):
    #     ##Read each file name
    #     #variable file is the name of the file with the extension and we put it as the file name 
    #     for fileNV in filesNV:
    #         #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
    #         if fileNV.endswith('.dat') and not fileNV.startswith('f'):
            
    #             sunNV = fileNV[3:8]
    err_maxP = "0.75"
    err_minP = "0.75"
    err_maxTa = "5"
    err_minTa = "5"
    err_minRHTemp = "10"
    err_maxRH = "10"
    err_maxRH_Sub_Surf = "0.0"
    err_UV = "10"
    err_1Deriv = "0.0014"
    err_Sensb_HeatFlux = "0.0000"

    with open(out_dir1 + 'extrema_press_lowestTemp_GTS_RH_MR_UV_Rate_TherGrad_HeatFlux_TOA_absBoomDiff_sol_00010_02027.dat','w') as output_file_Extrema:
        
        output_file_Extrema.write(str(headerOut_extrema) +'\n')                        
        
        sun0, abs_maxDiff, time_abs_maxDiff, SZA_abs_maxDiff, T1, T2 = ExtremaMDB1B2()
        sun1, abs_maxP, time_abs_maxP, abs_minP, time_abs_minP, SZA_maxP, SZA_minP = ExtremaP()  
        sun2, abs_maxT, Time_abs_maxT, abs_minT, Time_abs_minT,SZA_maxT, SZA_minT = ExtremaLT()  
        sun3, abs_maxGTS, time_abs_maxGTS, abs_maxRH_Surf, Time_abs_maxRH_Surf, abs_minGTS, time_abs_minGTS, SZA_maxGTS, SZA_minGTS, SZA_maxRH_Surf, rms_Tg_nominal, mean_Tg_nominal, st_Dev_GTS_Max, st_Dev_GTS_Min, st_Dev_RH_Surf_Max = ExtremaGTS_RHSurf_Sigmas()  
        sun4, abs_maxRH, time_abs_maxRH, abs_minRH_Temp, Time_abs_minRH_Temp, SZA_maxRH, SZA_minRH_Temp, VMR, MR = ExtremaRH()  
        sun5, abs_maxUV_global_A, timeLMST_UV_global_A, abs_maxUV_global_B, timeLMST_UV_global_B, abs_maxUV_global_C, timeLMST_UV_global_C, abs_maxUV_global_ABC, timeLMST_UV_global_ABC, abs_maxUV_global_D, timeLMST_UV_global_D, abs_maxUV_global_E, timeLMST_UV_global_E, abs_maxUV_diffuse_A, timeLMST_UV_diffuse_A, abs_maxUV_diffuse_B, timeLMST_UV_diffuse_B, abs_maxUV_diffuse_C, timeLMST_UV_diffuse_C, abs_maxUV_diffuse_ABC, timeLMST_UV_diffuse_ABC, abs_maxUV_diffuse_D, timeLMST_UV_diffuse_D, abs_maxUV_diffuse_E, timeLMST_UV_diffuse_E, max_SZA_Arr_global_A, max_SZA_Arr_global_B, max_SZA_Arr_global_C, max_SZA_Arr_global_ABC, max_SZA_Arr_global_D, max_SZA_Arr_global_E, max_SZA_Arr_diffuse_A, max_SZA_Arr_diffuse_B, max_SZA_Arr_diffuse_C, max_SZA_Arr_diffuse_ABC, max_SZA_Arr_diffuse_D, max_SZA_Arr_diffuse_E, current_ABC1_TOA, tau_UV = ExtremaUV()
        sun6, abs_maxUV_Temp, Time_abs_maxUV_Temp, abs_minUV_Temp, Time_abs_minUV_Temp, SZA_maxUV_Temp, SZA_minUV_Temp = ExtremaNV()
        sun7, abs_maxDerivGTS, Time_abs_maxDerivGTS, abs_minDerivGTS, Time_abs_minDerivGTS, SZA_maxDerivGTS, SZA_minDerivGTS = ExtremaDerivGTS()
        sun8, abs_maxSensb_HeatFlux, Time_abs_maxSensb_HeatFlux, abs_minSensb_HeatFlux, Time_abs_minSensb_HeatFlux, SZA_maxSensb_HeatFlux, SZA_minSensb_HeatFlux, rms_Sensb_HeatFlux, mean_Sensb_HeatFlux = ExtremaHeatFlux()
        sun9, rms_Difference, mean_Difference = ExtremaFileDiff()
        sun10, rms_Ta_nominal, mean_Ta_nominal = ExtremaNOMINAL()
        sun11, ls, sunriseTime, sunsetTime = sunset_Sunrise()
        sun12, EXTREMA_VMR_GTS = Extrema_VMR_GTS_P_MAX()
        sun13, EXTREMA_boom1 = Extrema_Boom1_Global()
        sun14, EXTREMA_boom2 = Extrema_Boom2_Global()
        sun15, AVERAGE_MAX_MIN = RAD_AVG_MAX_MIN()

        print("0")
        print(sorted(sun0))
        print("1")
        print(sorted(sun1))
        print("2")
        print(sorted(sun2))
        print("3")
        print(sorted(sun3))
        print("4")
        print(sorted(sun4))
        print("5")
        print(sorted(sun5))
        print("6")
        print(sorted(sun6))
        print("7")
        print(sorted(sun7))
        print("8")
        print(sorted(sun8))
        print("9")
        print(sorted(sun9))
        print("10")
        print(sorted(sun10))
        print("11")
        print(sorted(sun11))
        print("12")
        print(sorted(sun12))
        print("13")
        print(sorted(sun13))
        print("14")
        print(sorted(sun14))
        print("15")
        print(sorted(sun15))
        


        
        
        sun_aux = sorted(sun1)
        # print("Inicializando SUN_AUX")
        # print(len(ls))

        for i in sun_aux:
            if str(i) == "00000" or str(i) == "00001" or str(i) == "00002" or str(i) == "00003" or str(i) == "00004" or str(i) == "00005" or str(i) == "00006" or str(i) == "00007" or str(i) == "00008" or str(i) == "00009":
                continue
            else:
                #print("Sun in Extrema: "+ str(i))
                for a in sun1:
                    if a == i:
                        pos1 = sun1.index(a)
        
                        for b in sun2:
                            if b == a:
                                pos2 = sun2.index(b)
                                
                                for c in sun3:
                                    if c==b:
                                        pos3 = sun3.index(c)

                                        for d in sun0:
                                            if d == c:
                                                pos0 = sun0.index(d)

                                                for e in sun4:
                                                    if e == d:
                                                        pos4 = sun4.index(e)

                                                        for f in sun5:
                                                            if f == e:
                                                                pos5 = sun5.index(f)

                                                                for g in sun6:
                                                                    if g == f:
                                                                        pos6 = sun6.index(g)

                                                                        for h in sun7:
                                                                            if h == g:
                                                                                pos7 = sun7.index(h)

                                                                                for j in sun8:
                                                                                    if j == h:
                                                                                        pos8 = sun8.index(j)

                                                                                        for k in sun9:
                                                                                            if k == j:
                                                                                                pos9 = sun9.index(k)

                                                                                                for l in sun10:
                                                                                                    if l == k:
                                                                                                        pos10 = sun10.index(l)

                                                                                                        for m in sun11:
                                                                                                            if m == l:
                                                                                                                pos11 = sun11.index(m)
                                                                                                                for n in sun12:
                                                                                                                    if n == m:
                                                                                                                        pos12 = sun12.index(n)
                                                                                                                        for o in sun13:
                                                                                                                            if o == n:
                                                                                                                                pos13 = sun13.index(o)
                                                                                                                                for p in sun14:
                                                                                                                                    if p == o:
                                                                                                                                        pos14 = sun14.index(p)
                                                                                                                                        for q in sun15:
                                                                                                                                            if q == p:
                                                                                                                                                print(str(q))
                                                                                                                                                pos15 = sun15.index(q)

                                                                                                                                                Sub_Temp = (abs_minGTS[pos3]) + (abs_maxGTS[pos3] - abs_minGTS[pos3])/2.3

                                                                                                                                                # # Surface RH:
                                                                                                                                                abs_maxRH_Sub_Surf = calling_subroutines((abs_maxRH[pos4]), (abs_minRH_Temp[pos4]), abs_maxP[pos1], Sub_Temp)

                                                                                                                                                abs_maxDiff[pos0] = round(abs_maxDiff[pos0], 2)
                                                                                                                                                abs_maxDerivGTS[pos7] = round(abs_maxDerivGTS[pos7], 6)
                                                                                                                                                abs_minDerivGTS[pos7] = round(abs_minDerivGTS[pos7], 6)
                                                                                                                                                abs_maxRH_Sub_Surf = round(abs_maxRH_Sub_Surf, 3)
                                                                                                                                                mean_Difference[pos9] = round(mean_Difference[pos9], 2)
                                                                                                                                                rms_Difference[pos9] = round(rms_Difference[pos9], 2)
                                                                                                                                                mean_Ta_nominal[pos10] = round(mean_Ta_nominal[pos10], 2)
                                                                                                                                                rms_Ta_nominal[pos10] = round(rms_Ta_nominal[pos10], 2)
                                                                                                                                                # print("len(ls)")
                                                                                                                                                # print(len(ls))
                                                                                                                                                # print("pos11 "+str(pos11))
                                                                                                                                                ls[pos11] = round(float(ls[pos11]), 3)
                                                                                                                                                mean_Tg_nominal[pos3] = round(mean_Tg_nominal[pos3], 2)
                                                                                                                                                rms_Tg_nominal[pos3] = round(rms_Tg_nominal[pos3], 2)
                                                                                                                                                mean_Sensb_HeatFlux[pos8] = round(mean_Sensb_HeatFlux[pos8], 4)
                                                                                                                                                rms_Sensb_HeatFlux[pos8] = round(rms_Sensb_HeatFlux[pos8], 4)
                                                                                                                                                tau_UV[pos5] = round(tau_UV[pos5], 3)
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                output_file_Extrema.write(str(sun1[pos1]) +'   ' + str(ls[pos11])+'   '+ str(sunriseTime[pos11])+'   '+ str(sunsetTime[pos11])+'   '+ str(time_abs_maxP[pos1])+'   '+ str(SZA_maxP[pos1])+'   '+str(abs_maxP[pos1])+'   '+str(err_maxP)+'   '+ str(time_abs_minP[pos1])+'   '+ str(SZA_minP[pos1])+'   '+str(abs_minP[pos1])+'   '+str(err_minP)+'   '+ str(Time_abs_maxT[pos2])+'   '+ str(SZA_maxT[pos2])+'   '+str(abs_maxT[pos2])+'   '+str(err_maxTa)+'   '+ str(Time_abs_minT[pos2])+'   '+ str(SZA_minT[pos2])+'   '+str(abs_minT[pos2])+'   '+str(err_minTa)+'   '+ str(time_abs_maxGTS[pos3])+'   '+ str(SZA_maxGTS[pos3])+'   '+str(abs_maxGTS[pos3])+'   '+str(st_Dev_GTS_Max[pos3])+'   '+ str(time_abs_minGTS[pos3])+'   '+ str(SZA_minGTS[pos3])+'   '+str(abs_minGTS[pos3])+'   '+str(st_Dev_GTS_Min[pos3])+ '   '+ str(Time_abs_minRH_Temp[pos4])+ '   '+ str(SZA_minRH_Temp[pos4]) + '   '+ str(abs_minRH_Temp[pos4])+'   '+str(err_minRHTemp)+ '   '+ str(time_abs_maxRH[pos4])+ '   '+ str(SZA_maxRH[pos4]) + '   '+ str(abs_maxRH[pos4]) +'   '+str(err_maxRH) + '   '+ str(MR[pos4])+ '   '+ str(VMR[pos4]) +
                                                                                                                                                '   '+ str(Time_abs_maxRH_Surf[pos3])+ '   '+ str(SZA_maxRH_Surf[pos3]) + '   '+ str(abs_maxRH_Surf[pos3]) + '   '+ str(st_Dev_RH_Surf_Max[pos3])+ '   '+ str(abs_maxRH_Sub_Surf)+ '   '+ str(err_maxRH_Sub_Surf)+ '   '+ str(timeLMST_UV_global_A[pos5])+ '   '+ str(max_SZA_Arr_global_A[pos5]) + '   '+ str(abs_maxUV_global_A[pos5])+ '   '+ str(timeLMST_UV_global_B[pos5])+ '   '+ str(max_SZA_Arr_global_B[pos5]) + '   '+ str(abs_maxUV_global_B[pos5])+ '   '+ str(timeLMST_UV_global_C[pos5])+ '   '+ str(max_SZA_Arr_global_C[pos5]) + '   '+ str(abs_maxUV_global_C[pos5])+ '   '+ str(timeLMST_UV_global_ABC[pos5])+ '   '+ str(max_SZA_Arr_global_ABC[pos5]) + '   '+ str(abs_maxUV_global_ABC[pos5])+ '   '+ str(timeLMST_UV_global_D[pos5])+ '   '+ str(max_SZA_Arr_global_D[pos5]) + '   '+ str(abs_maxUV_global_D[pos5])+ '   '+ str(timeLMST_UV_global_E[pos5])+ '   '+ str(max_SZA_Arr_global_E[pos5]) + '   '+ str(abs_maxUV_global_E[pos5])+ 
                                                                                                                                                '   '+ str(timeLMST_UV_diffuse_A[pos5]) + '   '+ str(max_SZA_Arr_diffuse_A[pos5]) + '   '+ str(abs_maxUV_diffuse_A[pos5])+ '   '+ str(timeLMST_UV_diffuse_B[pos5])+ '   '+ str(max_SZA_Arr_diffuse_B[pos5]) + '   '+ str(abs_maxUV_diffuse_B[pos5])+ '   '+ str(timeLMST_UV_diffuse_C[pos5])+ '   '+ str(max_SZA_Arr_diffuse_C[pos5]) + '   '+ str(abs_maxUV_diffuse_C[pos5])+ '   '+ str(timeLMST_UV_diffuse_ABC[pos5])+ '   '+ str(max_SZA_Arr_diffuse_ABC[pos5]) + '   '+ str(abs_maxUV_diffuse_ABC[pos5])+ '   '+ str(timeLMST_UV_diffuse_D[pos5])+ '   '+ str(max_SZA_Arr_diffuse_D[pos5]) + '   '+ str(abs_maxUV_diffuse_D[pos5])+ '   '+ str(timeLMST_UV_diffuse_E[pos5]) + '   '+ str(max_SZA_Arr_diffuse_E[pos5])+ '   '+ str(abs_maxUV_diffuse_E[pos5])+ '   '+ str(err_UV)+ '   '+ str(Time_abs_maxDerivGTS[pos7])+ '   '+ str(SZA_maxDerivGTS[pos7]) + '   '+ str(abs_maxDerivGTS[pos7])+ '   '+ str(err_1Deriv)+
                                                                                                                                                '   '+ str(Time_abs_minDerivGTS[pos7])+ '   '+ str(SZA_minDerivGTS[pos7]) + '   '+ str(abs_minDerivGTS[pos7])+ '   '+ str(err_1Deriv)+ '   '+ str(Time_abs_maxSensb_HeatFlux[pos8])+ '   '+ str(SZA_maxSensb_HeatFlux[pos8]) + '   '+ str(abs_maxSensb_HeatFlux[pos8])+ '   '+ str(Time_abs_minSensb_HeatFlux[pos8]) + '   '+ str(SZA_minSensb_HeatFlux[pos8])+ '   '+ str(abs_minSensb_HeatFlux[pos8])+ '   '+ str(err_Sensb_HeatFlux)+ '   '+ str(mean_Difference[pos9]) + '   '+ str(rms_Difference[pos9])+ '   '+ str(mean_Ta_nominal[pos10])+ '   '+ str(rms_Ta_nominal[pos10])+ '   '+ str(mean_Tg_nominal[pos3])+ '   '+ str(rms_Tg_nominal[pos3])+ '   '+ str(mean_Sensb_HeatFlux[pos8])+ '   '+ str(rms_Sensb_HeatFlux[pos8])+ '   '+ str(current_ABC1_TOA[pos5])+ '   '+ str(tau_UV[pos5])+ '   '+ str(time_abs_maxDiff[pos0])+ '   '+ str(SZA_abs_maxDiff[pos0])+ '   '+str(abs_maxDiff[pos0])+ '   '+str(T1[pos0])+ '   '+str(T2[pos0])+ '   '+ str(Time_abs_maxUV_Temp[pos6])+ '   '+ str(SZA_maxUV_Temp[pos6])+ '   '+str(abs_maxUV_Temp[pos6])+ '   '+ str(Time_abs_minUV_Temp[pos6])+ '   '+ str(SZA_minUV_Temp[pos6])+ 
                                                                                                                                                '   '+str(abs_minUV_Temp[pos6]) + '   ' + str(EXTREMA_VMR_GTS[pos12])+ '   ' + str(EXTREMA_boom1[pos13])+ '   ' + str(EXTREMA_boom2[pos14]) + '   ' + str(AVERAGE_MAX_MIN[pos15]) + '\n')               
                                                                                                                                            




        output_file_Extrema.write(str(final.encode(encoding='utf_8')))





def calling_subroutines(RH, T_RH, P, T):
    RH=float(RH) 
    T_RH=float(T_RH)
    P=float(P)
    T=float(T)


    hP = (P)/10**2 # pressure in hPa
    # Convert relative humidity (%) into mixing ratio given Temperature and Pressure at 1.5m:
    esat1 = (es(T_RH))
  
    W, VMR= rh2mr(RH, hP, esat1)

    # Convert mixing ratio (g H2O per kg of dry air) at given temperature (GTS) and pressure into relative humidity (%):
    esat2 = es(T)
    RH_out = mr2rh(hP, W, esat2)

    return RH_out

def rh2mr(RH, P, esat):
    
    
    Mw = 18.0160 # molecular weight of water
    Md = 43.3400 # molecular weight of dry air on Mars 
    
    #        #This is the mixing ratio

    W = Mw/Md * RH/100. * esat/(P - RH/100. * esat) * 1000.

    VMR = Md/Mw * W * 1e3
    
    return W, VMR


def mr2rh(P, W, esat):
    

        Mw = 18.0160 # molecular weight of water
        Md = 43.3400 # molecular weight of dry air on Mars 
        
        fact = W/1000.0 * Md/Mw

        # This is the Relative Humidity (%)
        RH_out = P/esat * fact/(1 + fact) * 100.0

        if (RH_out > 100.0):
            RH_out = 100.0


        return RH_out



def es(T):
  
    e1 = 1013.250
    TK = 273.14159
    es = 6.11 * np.exp(22.5 * (1. - TK/ T)) # saturation vapor pressure in Pa ??????.
    return es
   


def means_rms(dta, size):
    
    add = 0
    square = 0
    n = 0

    if not dta:
        rms = -1.00
        mean = -1.00
        return rms, mean
        
    else:

        for i in range(size):
            
            if (dta[i] != -1):
                add = add + dta[i]
                square = square + (dta[i])**2
                n = n + 1
            
        
        if (n != 0):
            mean = add/n
            rms = np.sqrt(square/n)            
            return rms, mean
        else:
            mean = -1.00
            rms = -1.00 
            return rms, mean


# --------------------------------------------------------------------
# MODULE  MyTrigonometricFunctions:
#    This module provides the following functions and constants
#    (1) RadianToDegree()     - converts its argument in radian to
#                               degree
#    (2) DegreeToRadian()     - converts its argument in degree to
#                               radian
#    (3) MySIN()              - compute the sine of its argument in
#                               degree
#    (4) MyCOS()              - compute the cosine of its argument
#                               in degree
# --------------------------------------------------------------------

# def RadianToDegree(Radian):
#     PI = 3.1415926
#     Degree180 = 180.0
#     R_to_D = Degree180/PI

#     Rad2Deg = Radian * R_to_D
#     return Rad2Deg



# def DegreeToRadian(Degree):
#     PI = 3.1415926
#     Degree180 = 180.0
#     D_to_R = PI/Degree180  

#     Deg2Rad = Degree * D_to_R
#     return Deg2Rad

# def sin(x):
    
#       MySIN = np.sin(np.deg2rad(x))
#       return MySIN

# def cos(x):
    
#       MyCOS = np.cos(np.deg2rad(x))
#       return MyCOS


def absoluteDifference(dat1, dat2, size):
    
    tempMin = 218.0
    absDiff=np.zeros(size)
    dat1=(dat1)
    dat2=(dat2)
    # print(dat1)
    # print(dat2)

    for i in range(size):
        
        if (float(dat2[i]) < tempMin):
            #print('hola')
            absDiff[i] = '-1'
            continue # (-55C). Cuando la temperatura en el boom 2 sea menor que tempMin esta se descarta
        else:
            #print(i)
            absDiff[i] = float(dat1[i]) - float(dat2[i])

            if (absDiff[i] < 0):
                absDiff[i] = ((absDiff[i])*(-1)) 

    #print(absDiff)

    return absDiff

def max_min_SZA(sun, timeLMST_max,timeLMST_min):

    time_min = timeLMST_min
    it_min = getSeconds(timeLMST_min)

    time_max = timeLMST_max
    it_max = getSeconds(timeLMST_max)
    countMAX = 0
    countMIN = 0
    minfound = False
    maxfound = False
    SZA_max = '******'
    SZA_min = '******'
    
    # if os.stat(sun_topo_file_path + 'ADR_' + sun + '.dat').st_size != 0 or not(sun_topo_file_path + 'ADR_' + sun + '.dat'):
        
    #     SZA_max = -1.00
    #     SZA_min = -1.00
        
    #     return SZA_max, SZA_min

    if os.path.isfile(sun_topo_file_path + 'ADR_' + sun + '.dat') == False:
        
        return SZA_max, SZA_min

    with open(sun_topo_file_path + 'ADR_' + sun + '.dat','r') as input_fileLT:
        for i in input_fileLT:
            
            colLT=(i.split())
            
            if len(colLT) < 3:
                continue
            else:
                LMST = colLT[1][0:8]
                sza = float(colLT[2])
                
                itime = getSeconds(LMST)
                #print("soy itime) "+ str(itime))
                
                if it_max == itime:
                    
                    SZA_max = sza
                    #print("soy sza" +str(sza))
                    
                    maxfound = True

                elif (itime > it_max):
                    countMAX = countMAX + 1
                    if countMAX == 1 and maxfound == False:
                        SZA_max = sza
                        #print("soy sza" +str(sza))
                        
                if (itime == it_min):
                    SZA_min = sza
                    #print("soy sza" +str(sza))
                    
                    minfound = True
                    
                elif (itime > it_min):
                    countMIN = countMIN + 1
                    if countMIN == 1 and minfound == False:
                        SZA_min = sza
                        #print("soy sza" +str(sza))

                # if float(SZA_max) > 100.0:
                #     SZA_max = '******'

                # if float(SZA_min) > 100.0:
                #     SZA_min = '******'

        return SZA_max, SZA_min


def max_SZA(sun, timeLMST_max):
    
    

    time_max = timeLMST_max
    it_max = getSeconds(timeLMST_max)
    countMAX = 0
    maxfound = False
    SZA_max = '******'
    if os.path.isfile(sun_topo_file_path + 'ADR_' + sun + '.dat') == False:
        
        return SZA_max



    with open(sun_topo_file_path + 'ADR_' + sun + '.dat','r') as input_fileLT:
        for i in input_fileLT:
            
            colLT=(i.split())
            
            if len(colLT) < 3:
                continue
            else:
                LMST = colLT[1][0:8]
                sza = float(colLT[2])
                
                itime = getSeconds(LMST)
                #print("soy itime) "+ str(itime))
                
                if it_max == itime:
                    
                    SZA_max = sza
                    #print("soy sza" +str(sza))
                    
                    maxfound = True

                elif (itime > it_max):
                    countMAX = countMAX + 1
                    if countMAX == 1 and maxfound == False:
                        SZA_max = sza
                        #print("soy sza" +str(sza))
                        
                

        return SZA_max


print("EXTREMA FINAL ... STARTING")

Extrema()
print("EXTREMA FINAL ... COMPLETED")


ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)