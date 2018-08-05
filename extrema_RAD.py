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
# Variables Declaration
# Path from where I am reading
in_dir = "/data/PDS_Python/PDS_out_release/1_AWK/RAW_ALL/MD_RAW/"
# path where I will put the results
out_dir = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"
#NV path
in_dir2 = "/data/PDS_Python/PDS_out_release/1_AWK/RAW_ALL/NV_RAW/"
# path where I will put the results
out_dir2 = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/NV_CLEAN/"

in_dir3 = "/data/PDS_Python/PDS_out_release/1_AWK/RAW_ALL/ADR_RAW/"
# path where I will put the results
out_dir3 = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/ADR_CLEAN/"

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')




print("MD_Clean... STARTING")

print(st)


def read_clean_MD():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.TAB'):
                #if file.find(file_md) != -1.00:
                md_file = file
                
                sun = "0"+md_file[16:20]
                w_file = "MD_"+sun+".dat"
                with open(in_dir+md_file) as textfile1, open(out_dir+w_file, 'w+') as output_file:
                    output_file.truncate()
                    for y in (textfile1):
                        y = y.split(",")
                        if len(y)<9:
                            continue
                        else:
                            output_file.write(y[0].strip('\"').replace('UNK','-1.00') + ' ' + y[1].strip('\"').replace(sun+'M','') + ' ' + y[30].strip('\"').replace('UNK','-1.00') + ' ' + y[31].strip('\"').replace('UNK','-1.00') + ' ' + y[33].strip('\"').replace('NULL','-1.00') +
                                                ' ' + y[37].strip('\"').replace('UNK','-1.00') + ' ' + y[7].strip('\"').replace('UNK','-1.00') + ' ' + y[10].strip('\"').replace('UNK','-1.00') + ' ' + y[11].strip('\"').replace('UNK','-1.00') + ' ' + y[12].strip('\"').replace('UNK','-1.00') +
                                                ' ' + y[13].strip('\"').replace('UNK','-1.00') + ' ' + y[14].strip('\"').replace('UNK','-1.00')+ ' ' + y[15].strip('\"').replace('UNK','-1.00')+ ' ' + y[16].strip('\"').replace('UNK','-1.00')+ ' ' + y[3].strip('\"').replace('UNK','-1.00')+ ' ' + y[5].strip('\"').replace('UNK','-1.00')+ ' ' + y[6].strip('\"').replace('UNK','-1.00') +'\n')
                #print (w_file + ' Completed!')

                #read_clean_MD([0,1,30,31,33,37,7,10,11,12,13,14,15,16,03,05,06])
                #read_clean_MD([0,1,02,03,04,05,6,07,08,09,10,11,12,13,14,15,16])

read_clean_MD()

print("MD_Clean... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


print("NV_Clean... STARTING")


def read_clean_NV():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir2):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.TAB'):
                #if file.find(file_md) != -1.00:
                nv_file = file
                
                sun = "0"+nv_file[16:20]
                w_file = "NV_"+sun+".dat"
                with open(in_dir2 + nv_file) as textfile1, open(out_dir2 + w_file, 'w+') as output_file:
                    output_file.truncate()
                    for y in (textfile1):
                        y = y.split(",")
                        if len(y)<9:
                            continue
                        else:
                            output_file.write(y[0].strip('\"').replace('UNK','-1.00') + ' ' + y[1].strip('\"').replace(sun+'M','') + y[41].strip('\"').replace('UNK','-1.00') + ' ' + y[42].strip('\"').replace('UNK','-1.00') + ' ' + y[43].strip('\"').replace('UNK','-1.00') +
                                                ' ' + y[44].strip('\"').replace('UNK','-1.00') + ' ' + y[45].strip('\"').replace('UNK','-1.00') + ' ' + y[46].strip('\"').replace('UNK','-1.00') + ' ' + y[53].strip('\"').replace('UNK','-1.00') + ' ' + y[54].strip('\"').replace('UNK','-1.00') +
                                                ' ' + y[27].strip('\"').replace('UNK','-1.00') + ' ' + y[33].strip('\"').replace('UNK','-1.00')+ ' ' + y[34].strip('\"').replace('UNK','-1.00')+ ' ' + y[40].strip('\"').replace('UNK','-1.00')+ ' ' + y[28].strip('\"').replace('UNK','-1.00') +
                                                ' ' + y[29].strip('\"').replace('UNK','-1.00') + ' ' + y[66].strip('\"').replace('UNK','-1.00')+ ' ' + y[67].strip('\"').replace('UNK','-1.00')+ ' ' + y[35].strip('\"').replace('UNK','-1.00')+ ' ' + y[36].strip('\"').replace('UNK','-1.00')
                                                + ' ' + y[30].strip('\"').replace('UNK','-1.00')+ ' ' + y[31].strip('\"').replace('UNK','-1.00')+ ' ' + y[32].strip('\"').replace('UNK','-1.00')+ ' ' + y[37].strip('\"').replace('UNK','-1.00')+ ' ' + y[38].strip('\"').replace('UNK','-1.00')+ ' ' + y[39].strip('\"').replace('UNK','-1.00')+'\n')
                #print (w_file + ' Completed!')

# read_clean_NV([0,1,41,42,43,44,45,46,53,54,27,33,34,40,28,29,66,67,35,36,30,31,32,37,38,39])    
# read_clean_NV([0,1,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])

read_clean_NV()

print("NV_Clean... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


#This function transforms degrees to radians

def deg2rad(angle):
    #pi=3.14159265358979323846
    deg2rad=((np.pi/180)*angle)

    return deg2rad


#This function transforms radians to degrees

def rad2deg(angle):
    #pi=3.14159265358979323846
    rad2deg=(180/np.pi)*angle
    return rad2deg

#This function creates a rotation matrix about the 1-axis (or the X-axis)

def RX(angle):
    radang=deg2rad(angle)
    p22=np.cos(radang)
    p23=np.sin(radang)
    p32=-(np.sin(radang))
    p33=np.cos(radang)
    text = [[1, 0, 0, 0,p22, p23, 0, p32, p33]]
    #text=(text*(-1))
    text = (np.array(text,dtype=object))
    return(text[0].reshape((3, 3)))

#This function creates a rotation matrix about the 2-axis (or the Y-axis)

def RY(angle):
    
    radang=deg2rad(angle)
    p11=np.cos(radang)
    p13=-(np.sin(radang))
    p31=np.sin(radang)
    p33=np.cos(radang)
    text = [[p11, 0, p13, 0, 1, 0, p31, 0, p33]]
    text = np.array(text,dtype=object)
    return(text[0].reshape((3, 3)))

#This function creates a rotation matrix about the 3-axis (or the Z-axis)

def RZ(angle):

    radang=deg2rad(angle)
    p11=np.cos(radang)
    p12=np.sin(radang)
    p21=-(np.sin(radang))
    p22=np.cos(radang)

    text = [[p11, p12, 0, p21, p22, 0, 0, 0, 1]]
    text = np.array(text,dtype=object)
    return(text[0].reshape((3, 3)))



print("ADR_Clean... STARTING")

def read_clean_ADR():
    # Iteration on the ADR Files Directory
    # Where the files are
        # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir3):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.TAB'):
                #if file.find(file_md) != -1.00:
                adr_file = file
                
                sun = "0"+adr_file[16:20]
                w_file = "first_ADR_"+sun+".dat"
                with open(in_dir3 + adr_file, 'r+') as textfile1, open(out_dir3 + w_file, 'w+') as output_file:
                    output_file.truncate()
                    for y in (textfile1):
                        y = y.split(",")
                        #print(y)
                        if len(y)<9:
                            continue
                        else:
                            output_file.write(y[0].strip('\"').replace('UNK','-1.00') + ' ' + y[1].strip('\"').replace(sun+'M','')+ ' ' + y[2].strip('\"').replace('UNK','-1.00') + ' ' + y[3].strip('\"').replace('UNK','-1.00') + ' ' + y[4].strip('\"').replace('UNK','-1.00') +
                                                ' ' + y[5].strip('\"').replace('UNK','-1.00') + ' ' + y[6].strip('\"').replace('UNK','-1.00') + ' ' + y[7].strip('\"').replace('UNK','-1.00') + ' ' + y[8].strip('\"').replace('UNK','-1.00') + ' ' + y[9].strip('\"').replace('UNK','-1.00') +
                                                ' ' + y[10].strip('\"').replace('UNK','-1.00') + ' ' + y[11].strip('\"').replace('UNK','-1.00')+ '\n')
                    
                with open(out_dir3 + 'first_ADR_' + sun+ '.dat','r') as input_file, open(out_dir3 + 'ADR_' + sun+ '.dat','w') as output_file:

                    file = input_file    
                    
                    
                    for i in input_file:
                        
                        col=(i.split())
                        #print(col)
                        
                        if len(col) < 12:
                            continue
                        else:
                            sla_curiosityFIX=float(col[4])
                            sza_curiosityFIX=float(col[5])
                            
                            if ((sla_curiosityFIX == -1) or (sza_curiosityFIX == -1)):
                                sla_MSL_SurfLev_FIX=-1.0
                                sza_MSL_SurfLev_FIX=-1.0
                            else:
                                sckl=col[0]
                                # print("Soy SCLK"+ str(sckl))
                                LMST=col[1]
                                # print("Soy LOCALTIME"+ str(LMST))
                                LTST=col[2]
                                sza_MSL_SurfLev_FIX=0
                                sla_MSL_SurfLev_FIX=0
                                sla_curiosityFIX=float(col[4])
                                #print("Soy sla_curiosityFIX"+ str(sla_curiosityFIX))
                                sza_curiosityFIX=float(col[5])
                                #print("Soy sza_curiosityFIX"+ str(sza_curiosityFIX))
                                ROVER_PITCH=float(col[10])
                                #print("Soy ROVER_PITCH"+ str(ROVER_PITCH))
                                ROVER_YAW=float(col[11])
                                #print("Soy ROVER_YAW"+ str(ROVER_YAW))
                                ROVER_ROLL=float(col[12])
                                #print("Soy ROVER_ROLL"+ str(ROVER_ROLL))
                                
                                radio=1.0
                                sunp=[[],[],[]]
                                #X_sun
                                sunp[0]=((np.cos(deg2rad(sla_curiosityFIX)))*(np.sin(deg2rad(sza_curiosityFIX))))
                                #Y_sun
                                sunp[1]=((np.sin(deg2rad(sla_curiosityFIX)))*(np.sin(deg2rad(sza_curiosityFIX))))
                                #Z_sun
                                sunp[2]=((np.cos(deg2rad(sza_curiosityFIX))))
                                #print(sunp)
                                
                                a1 = -(ROVER_ROLL)
                                a2 = -(ROVER_PITCH)
                                a3 = -(ROVER_YAW)
                                M1 = np.dot((RY(a2)),(RZ(a3)))
                            
                                M2 = np.dot((M1),(RX(a1)))
                                
                                SUN=[[],[],[]]
                                SUN = np.dot(M2,sunp)
                                
                                sla_MSL_SurfLev_FIX = rad2deg(np.arctan2(SUN[1], SUN[0]))
                                
                                sza_MSL_SurfLev_FIX = rad2deg(np.arccos(SUN[2]))

                                sza_MSL_SurfLev_FIX = round(float(sza_MSL_SurfLev_FIX), 3)

                                sla_MSL_SurfLev_FIX = round(float(sla_MSL_SurfLev_FIX), 3)
                                

                                output_file.write(str(sckl)+' '+str(LMST)+' '+str(sza_MSL_SurfLev_FIX)+' '+str(sla_MSL_SurfLev_FIX)+'\n')

    #return df3_final



# #We decide which colums we want to have in our new clean file 
#read_clean_ADR(['col0', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11'])

read_clean_ADR()

print("ADR_Clean... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)



# Path from where I am reading
in_dir = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"
in_dir2 = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/NV_CLEAN/"
in_dirMD = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"
in_dirNV = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/NV_CLEAN/"

# path where I will put the results

out_dir1 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/Out_Temp_B1_B2/"
out_dir2 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/Out_Lowest_Temp/"
out_dir3 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/Out_Means_GTS/"
out_dir4 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/Out_Mean_Pressure/"
out_dir5 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/Out_Mean_UV/"
out_dir6 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/Out_Means/"

# path where I will put the results
out_dirMD = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/MD_CLEAN/"
out_dirNV = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/NV_CLEAN/"

block_secs = 300
pause = 120
tempMin = 218.0
pos_globaL_UV = 1
pos_shadow_UVS = 6
status_globalIrr_UVS = '1'
status_shadow_UVS = '1'
minT = -1
minT1 = -1
minT2 = -1
n_GTS = 0
n_UV_A = 0
n_UV_B = 0
n_UV_C = 0
n_UV_ABC = 0
n_UV_D = 0
n_UV_E = 0
add_GTS = 0.0
add_UV_A = 0.0
add_UV_B = 0.0
add_UV_C = 0.0
add_UV_ABC = 0.0
add_UV_D = 0.0
add_UV_E = 0.0
sec_per_hour = 3600
sec_per_minute = 60

def get_meanTime(time1,time2):
    
    a = getSeconds(time1)
    b = getSeconds(time2)

    return int((a+b)/2)

def getSeconds(LocalTime):
    
    hour = str(LocalTime)[0:2]
    hour = int(hour)
    minutes = str(LocalTime)[3:5]
    minutes = int(minutes)
    seconds = str(LocalTime)[6:8]
    seconds = int(seconds)
    totalSec = hour*sec_per_hour + minutes*sec_per_minute + seconds

    return totalSec

def getLMST(timeSec):
    
    nsecs = (timeSec%86400)
    sec = "{:02}".format(int(nsecs%60))
    nsecs = nsecs / 60
    minute = "{:02}".format(int(nsecs%60))
    hh = "{:02}".format(int(nsecs / 60))

    timeLMST = str(hh) + ':' + str(minute) + ':' + str(sec)

    return timeLMST


def mean_Out_Temp_B1_B2_MD():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.dat'):
                #if file.find(file_md) != -1.00:
                md_file = file
                
                sun = "0" + md_file[3:8]
                w_file = "air_temp_sol_"+sun+".dat"
                with open(in_dir + md_file) as textfile1, open(out_dir1 + w_file, 'w+') as output_file:
                    output_file.truncate()
                    for y in (textfile1):
                        y = y.split()
                        if len(y)<9:
                            continue
                        else:
                            output_file.write(y[0].strip('\"').replace('UNK','-1.00') + ' ' + y[1].strip('\"').replace(sun+'M','') + ' ' + y[8].strip('\"').replace('UNK','-1.00') + ' ' + y[10].strip('\"').replace('UNK','-1.00') +'\n')




def lowest_temp_MD():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(out_dirMD):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                
                sun = filename[9:14]
                #print(sun)
            
                with open(out_dirMD + 'MD_CLEAN_' + sun+ '.dat','r') as input_fileMD, open(out_dir6 + 'means_GTS_lowestTemp_Press_UV_sol_' + sun+ '.dat','w') as output_file_GTS_UV_PR_Min , open(out_dirNV + 'NV_CLEAN_' + sun+ '.dat','r') as input_fileNV, open(out_dir2 + 'lowest_temp_sol_' + sun+ '.dat','w') as output_fileTemp , open(out_dir3 + 'mean_GTS_sol_' + sun+ '.dat','w') as output_fileGTS, open(out_dir4 + 'mean_Pressure_sol_' + sun+ '.dat','w') as output_filePr , open(out_dir5 + 'mean_UV_sol_' + sun+ '.dat','w') as output_fileUV:
                    
                    
                    #file = input_file    
                    currentsclk = int(input_fileMD.readline().split()[0])
                    priorsclk = int(input_fileMD.readline().split()[0])
                    endsclk = currentsclk+block_secs
                    time1=(input_fileMD.readline().split()[1])

                    n_TB1 = 0
                    n_TB2 = 0
                    TB1_array=[1000]
                    TB2_array=[1000]

                    n_GTS = 0
                    add_GTS = 0.0
                    mean_GTS=-1.0
                    array_GTS=[]

                    n_pressure = 0
                    add_pressure = 0.0
                    mean_pressure=-1.0

                    n_UV_A = 0
                    n_UV_B = 0
                    n_UV_C = 0
                    n_UV_ABC = 0
                    n_UV_D = 0
                    n_UV_E = 0
                    add_UV_A = 0.0
                    add_UV_B = 0.0
                    add_UV_C = 0.0
                    add_UV_ABC = 0.0
                    add_UV_D = 0.0
                    add_UV_E = 0.0

                    mean_UV_A=-1
                    mean_UV_B=-1
                    mean_UV_C=-1
                    mean_UV_ABC=-1
                    mean_UV_D=-1
                    mean_UV_E=-1

                    for MD, NV in zip(input_fileMD, input_fileNV):
                        
                        col=(MD.split())
                        colNV=(NV.split())

                        if len(col) < 10 or len(colNV)<6:
                            #print(Hola)
                            continue
                        else:
                            totalSec = getSeconds(col[1])
                            currentsclk = int(col[0])
                            TB1 = float(col[8])
                            TB2 = float(col[10])
                            GTS = float(col[6])
                            pressure = float(col[5])

                            UV_A = float(colNV[2])
                            UV_B = float(colNV[3])
                            UV_C = float(colNV[4])
                            UV_ABC = float(colNV[5])
                            UV_D = float(colNV[6])
                            UV_E = float(colNV[7])
                            UV_conf = str(colNV[9])
                            #1 q=mean_GTS

                            if(((currentsclk-priorsclk)>=pause) or (currentsclk >= endsclk)):
                                
                                if n_TB1 != 0:
                                    minT1 = min(TB1_array)
                                if n_TB2 != 0:
                                    minT2 = min(TB2_array)
                                if minT1 < minT2:
                                    minT = minT1
                                elif minT2 < tempMin:
                                    minT = minT1
                                else:
                                    minT = minT2

                                if (n_GTS != 0):
                                    
                                    mean_GTS = (add_GTS/n_GTS)

                                if (n_pressure != 0):
                                    mean_pressure = add_pressure/n_pressure

                                if (n_UV_A != 0):
                                    mean_UV_A = add_UV_A/n_UV_A
                                if (n_UV_B != 0):
                                    mean_UV_B = add_UV_B/n_UV_B
                                if (n_UV_C != 0):
                                    mean_UV_C = add_UV_C/n_UV_C
                                if (n_UV_ABC != 0):
                                    mean_UV_ABC = add_UV_ABC/n_UV_ABC
                                if (n_UV_D != 0):
                                    mean_UV_D = add_UV_D/n_UV_D
                                if (n_UV_E != 0):
                                    mean_UV_E = add_UV_E/n_UV_E
                                
                                    #1 if q == mean_GTS:
                                    #     mean_GTS=-1.0

                                
                                meanTimeSec = get_meanTime(time1,time2)
                                
                                endsclk = currentsclk+block_secs
                                mean_timeLMST = getLMST(meanTimeSec)
                                time1 = (col[1])

                                TB1_array=[1000]
                                TB2_array=[1000]

                                if minT==1000:
                                    minT=-1.00

                                mean_GTS = round(mean_GTS, 2)
                                mean_pressure = round(mean_pressure, 2)
                                mean_UV_A = round(mean_UV_A, 2)
                                mean_UV_B = round(mean_UV_B, 2)
                                mean_UV_C = round(mean_UV_C, 2)
                                mean_UV_ABC = round(mean_UV_ABC, 2)
                                mean_UV_D = round(mean_UV_D, 2)
                                mean_UV_E = round(mean_UV_E, 2)
                                
                            
                                output_fileTemp.write(str(meanTimeSec)+' '+str(mean_timeLMST)+' '+str(minT)+'\n')
                                output_fileGTS.write(str(meanTimeSec)+' '+str(mean_timeLMST)+' '+str(mean_GTS)+'\n')
                                output_filePr.write(str(meanTimeSec)+' '+str(mean_timeLMST)+' '+str(mean_pressure)+'\n')
                                output_fileUV.write(str(meanTimeSec)+' '+str(mean_timeLMST)+' '+str(mean_UV_A)+' '+str(mean_UV_B)+' '+str(mean_UV_C)+' '+str(mean_UV_ABC)+' '+str(mean_UV_D)+' '+str(mean_UV_E)+'\n')
                                output_file_GTS_UV_PR_Min.write(str(int(meanTimeSec))+' '+str(mean_timeLMST)+' '+str(mean_GTS)+' '+str(minT)+' '+str(mean_pressure)+' '+str(mean_UV_A)+' '+str(mean_UV_B)+' '+str(mean_UV_C)+' '+str(mean_UV_ABC)+' '+str(mean_UV_D)+' '+str(mean_UV_E)+'\n')

                                minT = -1.0
                                minT1 = -1.0
                                minT2 = -1.0
                                mean_GTS=-1.0
                                mean_pressure=-1.0
                                mean_UV_A = -1.00
                                mean_UV_B = -1.00
                                mean_UV_C = -1.00
                                mean_UV_ABC = -1.00
                                mean_UV_D = -1.00
                                mean_UV_E = -1.00

                                n_GTS=0
                                add_GTS = 0.0

                                n_pressure=0
                                add_pressure=0.0

                                n_UV_A = 0
                                n_UV_B = 0
                                n_UV_C = 0
                                n_UV_ABC = 0
                                n_UV_D = 0
                                n_UV_E = 0
                                add_UV_A = 0.0
                                add_UV_B = 0.0
                                add_UV_C = 0.0
                                add_UV_ABC = 0.0
                                add_UV_D = 0.0
                                add_UV_E = 0.0

                            if (TB1 != -1):
                                n_TB1 = n_TB1 + 1
                                TB1_array.append(TB1)            
                    
                            if (TB2 != -1):
                                n_TB2 = n_TB2 + 1
                                TB2_array.append(TB2)

                            if (GTS != -1):
                                n_GTS = n_GTS + 1
                                add_GTS = add_GTS + GTS
                                array_GTS.append(GTS)

                            if (pressure != -1):
                                
                                n_pressure = n_pressure + 1
                                add_pressure = add_pressure + pressure

                            if len(UV_conf) == 8 :
                                
                                if ((UV_conf[pos_globaL_UV] == status_globalIrr_UVS) and (UV_conf[pos_shadow_UVS] == status_shadow_UVS)):
                                    if (UV_A > 0.0):
                                        n_UV_A = n_UV_A + 1
                                        add_UV_A = add_UV_A + UV_A
                
                                    if (UV_B > 0.0):
                                        n_UV_B = n_UV_B + 1
                                        add_UV_B = add_UV_B + UV_B
            
                                    if (UV_C > 0.0):
                                        n_UV_C = n_UV_C + 1
                                        add_UV_C = add_UV_C + UV_C
                
                                    if (UV_ABC > 0.0):
                                        n_UV_ABC = n_UV_ABC + 1
                                        add_UV_ABC = add_UV_ABC + UV_ABC
                    
                                    if (UV_D > 0.0):
                                        n_UV_D = n_UV_D + 1
                                        add_UV_D = add_UV_D + UV_D
                                    if (UV_E > 0.0):
                                        n_UV_E = n_UV_E + 1
                                        add_UV_E = add_UV_E + UV_E

                            priorsclk = currentsclk
                            time2 = (col[1])






def readMD():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dirMD):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.dat'):
                #if file.find(file_md) != -1.00:
                md_file = file
                
                sun =  md_file[3:8]
                w_file = "MD_CLEAN_"+sun+".dat"
                with open(in_dirMD + md_file) as textfile1, open(out_dirMD+w_file, 'w+') as output_file:
                    output_file.truncate()
                    for y in (textfile1):
                        y = y.split()
                        if len(y)<9:
                            continue
                        else:
                            output_file.write(y[0].strip('\"').replace('UNK','-1.00') + ' ' + y[1].strip('\"').replace(sun+'M','') + ' ' + y[2].strip('\"').replace('UNK','-1.00') + ' ' + y[3].strip('\"').replace('UNK','-1.00') + ' ' + y[4].strip('\"').replace('UNK','-1.00') +
                                                ' ' + y[5].strip('\"').replace('UNK','-1.00') + ' ' + y[6].strip('\"').replace('UNK','-1.00') + ' ' + y[7].strip('\"').replace('UNK','-1.00') + ' ' + y[8].strip('\"').replace('UNK','-1.00') + ' ' + y[9].strip('\"').replace('UNK','-1.00') +
                                                ' ' + y[10].strip('\"').replace('UNK','-1.00') + ' ' + y[11].strip('\"').replace('UNK','-1.00') +'\n')



def readNV():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dirNV):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.dat'):
                #if file.find(file_md) != -1.00:
                nv_file = file
                
                sun = nv_file[3:8]
                w_file = "NV_CLEAN_"+sun+".dat"
                with open(in_dirNV + nv_file) as textfile1, open(out_dirNV + w_file, 'w+') as output_file:
                    output_file.truncate()
                    for y in (textfile1):
                        y = y.split()
                        
                        if len(y)<9:
                            continue
                        else:
                            output_file.write(y[0].strip('\"').replace('UNK','-1.00') + ' ' + y[1].strip('\"').replace(sun+'M','') + ' ' + y[2].strip('\"').replace('UNK','-1.00') + ' ' + y[3].strip('\"').replace('UNK','-1.00') + ' ' + y[4].strip('\"').replace('UNK','-1.00') +
                                                ' ' + y[5].strip('\"').replace('UNK','-1.00') + ' ' + y[6].strip('\"').replace('UNK','-1.00') + ' ' + y[7].strip('\"').replace('UNK','-1.00') + ' ' + y[8].strip('\"').replace('UNK','-1.00') + ' ' + y[9].strip('\"').replace('UNK','-1.00') +'\n')



print("MEAN_1 ... STARTING")


readMD()
readNV()

lowest_temp_MD()
mean_Out_Temp_B1_B2_MD()

print("MEAN_1 ... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


# Path from where I am reading

in_dirNV = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/NV_CLEAN/"
in_dirMD = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"


# path where I will put the results
out_dirMD = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/MD_CLEAN/"
out_dirNV = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/NV_CLEAN/"
# out_dirMD = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/MD_CLEAN/"
# out_dirNV = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/NV_CLEAN/"

out_dir1 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_Temp_B1_B2/"
out_dir2 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_lowest_Temp/"
out_dir3 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_Mean_GTS/"
out_dir4 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_mean_Pressure/"
out_dir5 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_mean_UV/"
out_dir6 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_mean_RH/"
out_dir7 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_mean_Tg_P/"
out_dir8 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_mean_P_Tg_Ta_rho/"
out_dir9 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_Means/"

block_secs = 300 # Cada 5 minutos = 300 segundos realizamos una media
block_secs_RH = 5 # Cada 5 seg segundos realizamos una media para RH
pause = 120 # Si las no adquisiciones son mayores de 120 seg, pasamos a una nueva media
tempMin = 218 # (-55C). Cuando la temperatura en el boom 2 sea menor que esta, se descarta y se toma la del boom1

pos_globaL_UV = 1 # Posición 2 empezando por la izq
pos_shadow_UVS = 6 # Posición 7 empezando por la izq
status_globalIrr_UVS = "1" # 1 = global irradiance (SZA 0-30) / 0 = No global irradiance    
status_shadow_UVS = "1" # 1 = no shadow or night /  0 = Sensor UV en sombra

#GTS_conf = 'XXXX'
B1_conf = 'XXXXXXXX'
B2_conf = 'XXXXXXXX'
UV_conf = 'XXXXXXXX'

sec_per_hour = 3600
sec_per_minute = 60

# def get_meanTime(time1,time2):
    
#     a = getSeconds(time1)
#     b = getSeconds(time2)

#     return int((a+b)/2)

# def getSeconds(LocalTime):
    
#     hour = str(LocalTime)[0:2]
#     hour = int(hour)
#     minutes = str(LocalTime)[3:5]
#     minutes = int(minutes)
#     seconds = str(LocalTime)[6:8]
#     seconds = int(seconds)
#     totalSec = hour*sec_per_hour + minutes*sec_per_minute + seconds
#     #print(totalSec)

#     return totalSec
# def getLMST(timeSec):
    
#     nsecs = (timeSec%86400)
#     sec = "{:02}".format(int(nsecs%60))
#     nsecs = nsecs / 60
#     minute = "{:02}".format(int(nsecs%60))
#     hh = "{:02}".format(int(nsecs / 60))

#     timeLMST = str(hh) + ':' + str(minute) + ':' + str(sec)

#     return timeLMST

def Temp5_b1_b2():
    for base, dirs, files in os.walk(out_dirMD):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and  not file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[9:14]
                    
                with open(out_dirMD + 'MD_CLEAN_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'air_temp_sol_' + sun+ '.dat','w') as output_file:
                    for i in input_file:
                        col=(i.split())
                        if len(col) < 11:
                            continue
                        else:
                            sclk=col[0]
                            LMST=col[1][0:8]
                            TB1=col[8]
                            TB2=col[10]
                            output_file.write(str(sclk)+' '+str(LMST)+' '+str(TB1)+' '+str(TB2)+'\n')
                                


def mean_Out5():
    for base, dirs, files in os.walk(out_dirMD):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and  not file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[9:14]
    
                with open(out_dirMD + 'MD_CLEAN_' + sun+ '.dat','r') as input_fileMD, open(out_dirNV + 'NV_CLEAN_' + sun+ '.dat','r') as input_fileNV, open(out_dir9 + 'means_RH_GTS_lowestTemp_Press_UV_sol_' + sun+ '.dat','w') as output_file, open(out_dir2 + 'lowest_temp_sol_' + sun+ '.dat','w') as output_fileMin, open(out_dir3 + 'mean_GTS_sol_' + sun+ '.dat','w') as output_fileGTS, open(out_dir4 + 'mean_Pressure_sol_' + sun+ '.dat','w') as output_filePr, open(out_dir5 + 'mean_UV_sol_' + sun+ '.dat','w') as output_fileUV, open(out_dir6 + 'mean_RH_sol_' + sun+ '.dat','w') as output_fileRH, open(out_dir7 + 'mean_Tg_P_sol_' + sun+ '.dat','w') as output_fileTG_P, open(out_dir8 + 'mean_P_Tg_Ta_tGrad_rho_sol_' + sun+ '.dat','w') as output_file_P_Tg_Ta:
                    
                    current_sclk = int(input_fileMD.readline().split()[0])
                    prior_sclk = int(input_fileMD.readline().split()[0])
                    end_sclk = current_sclk+block_secs

                    block_hours=[] #Array que lleva la cuenta de si ha hecho ya media para una hora in o no.
                    new_init = True# Indica si se comienza una nueva media (true) para poder inicializar las variables.
                    
                    TB1_array=[]
                    TB2_array=[]

                    R = 189 # [J/Kg/K] => rho: [Kg/m3] ya que 1J = 1 Pa*m3 y mis unidades de presión están en Pa. 
                    vel = 1 # Estimación velocidad del viento
                    
                    for MD, NV in zip(input_fileMD, input_fileNV):
                        col=(MD.split())
                        colNV=(NV.split())

                        if len(col) < 10 or len(colNV)<6:
                            continue
                        else:
                            current_hour=int(col[1][0:2])
                            current_sclk=int(col[0])
                            
                            
                            if (current_hour in block_hours):
                                continue

                            elif (new_init == True):
                                
                                n_local_H = 0
                                n_H_Temp = 0
                                
                                add_local_H = 0.0
                                add_H_Temp = 0.0

                                add_GTS = 0.0
                                n_GTS = 0
                                aux_deviation_GTS = 0.0

                                minT = -1
                                minT1 = -1
                                minT2 = -1
                                n_TB1 = 0
                                n_TB2 = 0

                                add_pressure = 0.0
                                n_pressure = 0

                                n_UV_A = 0
                                n_UV_B = 0
                                n_UV_C = 0
                                n_UV_ABC = 0
                                n_UV_D = 0
                                n_UV_E = 0

                                add_UV_A = 0.0
                                add_UV_B = 0.0
                                add_UV_C = 0.0
                                add_UV_ABC = 0.0
                                add_UV_D = 0.0
                                add_UV_E = 0.0

                                #Inicializo tiempos para empezar la nueva media
                                prior_sclk = current_sclk
                                prior_hour = current_hour
                                time_1=col[1][0:8]
                                end_sclk = current_sclk + block_secs
                                end_sclk_RH = current_sclk + block_secs_RH
                                array_GTS=[]
                                TB1_array=[]
                                TB2_array=[]


                                new_init = False #! Una vez inicializadas las variables de la nueva media, ya no debe inicializarse más.
                            
                            local_H=float(col[2 ])
                            H_Temp=float(col[3])
                            mean_H_Temp=-1.00
                            mean_local_H=-1.00

                            GTS=float(col[6])
                            mean_GTS=-1.00
                            stand_deviation_GTS=-1.00
                            #GTS_conf=float(col[7])

                            TB1=col[8]
                            TB2=col[10]
                            minT = -1

                            pressure=float(col[5])
                            mean_pressure = -1.00

                            UV_A=float(colNV[2])
                            UV_B=float(colNV[3])
                            UV_C=float(colNV[4])
                            UV_ABC=float(colNV[5])
                            UV_D=float(colNV[6])
                            UV_E=float(colNV[7])
                            UV_conf=(colNV[9])
                            mean_UV_A = -1.00
                            mean_UV_B = -1.00
                            mean_UV_C = -1.00
                            mean_UV_ABC = -1.00
                            mean_UV_D = -1.00
                            mean_UV_E = -1.00

                            if (((current_sclk - prior_sclk) >= pause) or (current_sclk >= end_sclk) or (prior_hour != current_hour)):

                                if (n_local_H != 0):
                                    mean_local_H =  add_local_H/n_local_H

                                if (n_H_Temp != 0):
                                    mean_H_Temp =  add_H_Temp/n_H_Temp

                                if (n_GTS != 0):
                                    
                                    mean_GTS = (add_GTS/n_GTS)

                                    for i in range(n_GTS):
                                        
                                        aux_deviation_GTS = aux_deviation_GTS + (array_GTS[i] - mean_GTS) ** 2

                                    stand_deviation_GTS = np.sqrt(aux_deviation_GTS/n_GTS)

                                if (n_TB1 != 0):
                                    minT1 = min(TB1_array)
                     
                                if (n_TB2 != 0):
                                    minT2 = min(TB2_array)

                                if (minT1 < minT2):
                                    minT = minT1

                                elif (float(minT2) < tempMin):
                                    minT = minT1

                                else:
                                    minT = minT2

                                if (n_pressure != 0):
                                    mean_pressure = add_pressure/n_pressure

                                if (n_UV_A != 0):
                                    mean_UV_A = add_UV_A/n_UV_A
                                if (n_UV_B != 0):
                                    mean_UV_B = add_UV_B/n_UV_B
                                if (n_UV_C != 0):
                                    mean_UV_C = add_UV_C/n_UV_C
                                if (n_UV_ABC != 0):
                                    mean_UV_ABC = add_UV_ABC/n_UV_ABC
                                if (n_UV_D != 0):
                                    mean_UV_D = add_UV_D/n_UV_D
                                if (n_UV_E != 0):
                                    mean_UV_E = add_UV_E/n_UV_E

                                
                                mean_sec = get_meanTime(time_1, time_2)# Media en segundos
                                mean_timeLMST = getLMST(mean_sec)# Media en formato LMST
                                
                                block_hours.append(current_hour) #Indica que se ha hecho la media para esta hora, si sigue habiendo valores para esta hora no se tienen en cuenta (continue en if arriba)
                                new_init = True

                                mean_local_H = round(mean_local_H, 2)
                                mean_H_Temp = round(mean_H_Temp, 2)
                                mean_GTS = round(mean_GTS, 2)
                                stand_deviation_GTS = round(stand_deviation_GTS, 2)
                                mean_pressure = round(mean_pressure, 2)
                                mean_UV_A = round(mean_UV_A, 2)
                                mean_UV_B = round(mean_UV_B, 2)
                                mean_UV_C = round(mean_UV_C, 2)
                                mean_UV_ABC = round(mean_UV_ABC, 2)
                                mean_UV_D = round(mean_UV_D, 2)
                                mean_UV_E = round(mean_UV_E, 2)
                                
                                
                                if mean_sec<300:
                                    mean_sec=mean_sec-2
                                    mean_timeLMST = getLMST(mean_sec)# Media en formato LMST

                                if ((mean_pressure != - 1.00) and (minT != - 1.00)):
                                    mean_rho = float(mean_pressure)/R/float(minT)

                                mean_GTS_minT = float(mean_GTS) - float(minT)
                                    
                                mean_vel_rho_GTS_rho_GTS_minT = vel * mean_rho * mean_GTS_minT

                                mean_GTS_minT = round(mean_GTS_minT, 2)
                                mean_rho = round(mean_rho, 5)
                                mean_vel_rho_GTS_rho_GTS_minT = round(mean_vel_rho_GTS_rho_GTS_minT, 5)
                                


                                    
                                output_file.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_local_H)+' '+str(mean_H_Temp)+' '+str(mean_GTS)+' '+str(stand_deviation_GTS)+' '+str(minT)+' '+str(mean_pressure)+' '+str(mean_UV_A)+' '+str(mean_UV_B)+' '+str(mean_UV_C)+' '+str(mean_UV_ABC)+' '+str(mean_UV_D)+' '+str(mean_UV_E)+'\n')
                                output_fileMin.write(str(mean_sec)+' '+str(mean_timeLMST)+' '+str(minT)+'\n')
                                output_fileGTS.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_GTS)+' '+str(stand_deviation_GTS)+'\n')
                                output_filePr.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_pressure)+'\n')
                                output_fileUV.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_UV_A)+' '+str(mean_UV_B)+' '+str(mean_UV_C)+' '+str(mean_UV_ABC)+' '+str(mean_UV_D)+' '+str(mean_UV_E)+'\n')
                                output_fileRH.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_local_H)+' '+str(mean_H_Temp)+'\n')
                                output_fileTG_P.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_GTS)+' '+str(mean_pressure)+'\n')
                                output_file_P_Tg_Ta.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_pressure)+' '+str(mean_GTS)+' '+str(minT)+' '+str(mean_GTS_minT)+' '+str(mean_rho)+' '+str(mean_vel_rho_GTS_rho_GTS_minT)+'\n')

                            # For RH average for block_secs_RH seconds
                            if ((local_H != -1.00) and (current_sclk < end_sclk_RH)):
                                n_local_H = n_local_H + 1
                                add_local_H = add_local_H + local_H
                            
                            # For RH_Temp average for block_secs_RH seconds
                            if ((H_Temp != -1.00) and (current_sclk < end_sclk_RH)):
                                n_H_Temp = n_H_Temp + 1
                                add_H_Temp = add_H_Temp + H_Temp

                            if (GTS != -1):
                                n_GTS = n_GTS + 1
                                add_GTS = add_GTS + GTS
                                array_GTS.append(GTS)

                            if (TB1 != -1):
                                n_TB1 = n_TB1 + 1
                                TB1_array.append(TB1)

                            if (TB2 != -1):
                                n_TB2 = n_TB2 + 1
                                TB2_array.append(TB2)

                            if (pressure != -1.00):
                                n_pressure = n_pressure + 1
                                add_pressure = add_pressure + pressure

                            if len(UV_conf) == 8 :

                                if ((UV_conf[pos_globaL_UV: pos_globaL_UV+1] == (status_globalIrr_UVS)) and (UV_conf[pos_shadow_UVS: pos_shadow_UVS+1] == (status_shadow_UVS))):            
                    
                                

                                    #! For UV_A average
                                    if (UV_A > 0.0):
                                        n_UV_A = n_UV_A + 1
                                        add_UV_A = add_UV_A + UV_A

                                # ! For UV_B average
                                    if (UV_B > 0.0):
                                        n_UV_B = n_UV_B + 1
                                        add_UV_B = add_UV_B + UV_B

                                # ! For UV_C average
                                    if (UV_C > 0.0):
                                        n_UV_C = n_UV_C + 1
                                        add_UV_C = add_UV_C + UV_C

                                # ! For UV_ABC average
                                    if (UV_ABC > 0.0):
                                        n_UV_ABC = n_UV_ABC + 1
                                        add_UV_ABC = add_UV_ABC + UV_ABC

                                # ! For UV_D average
                                    if (UV_D > 0.0):
                                        n_UV_D = n_UV_D + 1
                                        add_UV_D = add_UV_D + UV_D
                                # ! For UV_E average
                                    if (UV_E > 0.0):
                                        n_UV_E = n_UV_E + 1
                                        add_UV_E = add_UV_E + UV_E

                            time_2 = col[1][0:8]

                            prior_sclk = current_sclk
                            prior_hour = current_hour


print("MEAN_5 ... STARTING")

###### readMD([0,1,2,3,4,5,6,7,8,9,10,11])
###### readNV([0,1,2,3,4,5,6,7,9])
Temp5_b1_b2()
mean_Out5()

print("MEAN_5 ... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)




# Path from where I am reading

in_dirNV = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/NV_CLEAN/"
in_dirMD = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"
# path where I will put the results

# out_dirMD = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/MD_CLEAN/"
# out_dirNV = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/NV_CLEAN/"

out_dirMD = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/MD_CLEAN/"
out_dirNV = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/NV_CLEAN/"

out_dir1 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/Out_Temp_B1_B2/"
out_dir2 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/Out_lowest_Temp/"
out_dir3 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/Out_mean_GTS/"
out_dir4 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/Out_mean_Pressure/"
out_dir5 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/Out_mean_UV/"
out_dir6 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/Out_mean_RH/"

out_dir9 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/Out_means/"

block_secs = 300 # Cada 5 minutos = 300 segundos realizamos una media
block_secs_RH = 5 # Cada 5 seg segundos realizamos una media para RH
pause = 120 # Si las no adquisiciones son mayores de 120 seg, pasamos a una nueva media
tempMin = 218 # (-55C). Cuando la temperatura en el boom 2 sea menor que esta, se descarta y se toma la del boom1.

pos_globaL_UV = 1 # Posición 2 empezando por la izq.
pos_shadow_UVS = 6 # Posición 7 empezando por la izq.
status_globalIrr_UVS = "1" # 1 = global irradiance (SZA 0-30) / 0 = No global irradiance    
status_shadow_UVS = "1" # 1 = no shadow or night /  0 = Sensor UV en sombra

#GTS_conf = 'XXXX'
B1_conf = 'XXXXXXXX'
B2_conf = 'XXXXXXXX'
UV_conf = 'XXXXXXXX'

sec_per_hour = 3600
sec_per_minute = 60

# def get_meanTime(time1,time2):
    
#     a = getSeconds(time1)
#     b = getSeconds(time2)

#     return int((a+b)/2)

# def getSeconds(LocalTime):
    
#     hour = str(LocalTime)[0:2]
#     hour = int(hour)
#     minutes = str(LocalTime)[3:5]
#     minutes = int(minutes)
#     seconds = str(LocalTime)[6:8]
#     seconds = int(seconds)
#     totalSec = hour*sec_per_hour + minutes*sec_per_minute + seconds
#     #print(totalSec)

#     return totalSec
# def getLMST(timeSec):
    
#     nsecs = (timeSec%86400)
#     sec = "{:02}".format(int(nsecs%60))
#     nsecs = nsecs / 60
#     minute = "{:02}".format(int(nsecs%60))
#     hh = "{:02}".format(int(nsecs / 60))

#     timeLMST = str(hh) + ':' + str(minute) + ':' + str(sec)

#     return timeLMST

def Temp6_b1_b2():
    for base, dirs, files in os.walk(out_dirMD):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and  not file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[9:14]
                    
                with open(out_dirMD + 'MD_CLEAN_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'air_temp_sol_' + sun+ '.dat','w') as output_file:
                    for i in input_file:
                        col=(i.split())
                        if len(col) < 11:
                            continue
                        else:
                            sclk=col[0]
                            LMST=col[1][0:8]
                            TB1=col[8]
                            TB2=col[10]
                            output_file.write(str(sclk)+' '+str(LMST)+' '+str(TB1)+' '+str(TB2)+'\n')
                                


def mean_Out6():
    for base, dirs, files in os.walk(out_dirMD):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and  not file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[9:14]
    
                with open(out_dirMD + 'MD_CLEAN_' + sun+ '.dat','r') as input_fileMD, open(out_dirNV + 'NV_CLEAN_' + sun+ '.dat','r') as input_fileNV, open(out_dir9 + 'means_RH_GTS_lowestTemp_Press_UV_sol_' + sun+ '.dat','w') as output_file, open(out_dir2 + 'lowest_temp_sol_' + sun+ '.dat','w') as output_fileMin, open(out_dir3 + 'mean_GTS_sol_' + sun+ '.dat','w') as output_fileGTS, open(out_dir4 + 'mean_Pressure_sol_' + sun+ '.dat','w') as output_filePr, open(out_dir5 + 'mean_UV_sol_' + sun+ '.dat','w') as output_fileUV, open(out_dir6 + 'mean_RH_sol_' + sun+ '.dat','w') as output_fileRH:
                    
                    current_sclk = int(input_fileMD.readline().split()[0])
                    prior_sclk = int(input_fileMD.readline().split()[0])
                    end_sclk = current_sclk+block_secs

                    block_hours=[] #Array que lleva la cuenta de si ha hecho ya media para una hora in o no.
                    new_init = True# Indica si se comienza una nueva media (true) para poder inicializar las variables.
                    
                    TB1_array=[]
                    TB2_array=[]

                    R = 189 # [J/Kg/K] => rho: [Kg/m3] ya que 1J = 1 Pa*m3 y mis unidades de presión están en Pa. 
                    vel = 1 # Estimación velocidad del viento
                    
                    for MD, NV in zip(input_fileMD, input_fileNV):
                        col=(MD.split())
                        colNV=(NV.split())

                        if len(col) < 10 or len(colNV)<6:
                            continue
                        else:
                            current_hour=int(col[1][0:2])
                            current_sclk=int(col[0])
                            
                            
                            if (current_hour in block_hours):
                                continue

                            elif (new_init == True):
                                
                                n_local_H = 0
                                n_H_Temp = 0
                                
                                add_local_H = 0.0
                                add_H_Temp = 0.0

                                add_GTS = 0.0
                                n_GTS = 0
                                aux_deviation_GTS = 0.0

                                minT = -1
                                minT1 = -1
                                minT2 = -1
                                n_TB1 = 0
                                n_TB2 = 0

                                add_pressure = 0.0
                                n_pressure = 0

                                n_UV_A = 0
                                n_UV_B = 0
                                n_UV_C = 0
                                n_UV_ABC = 0
                                n_UV_D = 0
                                n_UV_E = 0

                                add_UV_A = 0.0
                                add_UV_B = 0.0
                                add_UV_C = 0.0
                                add_UV_ABC = 0.0
                                add_UV_D = 0.0
                                add_UV_E = 0.0

                                #Inicializo tiempos para empezar la nueva media
                                prior_sclk = current_sclk
                                prior_hour = current_hour
                                time_1=col[1][0:8]
                                end_sclk = current_sclk + block_secs
                                end_sclk_RH = current_sclk + block_secs_RH
                                array_GTS=[]
                                TB1_array=[]
                                TB2_array=[]


                                new_init = False #! Una vez inicializadas las variables de la nueva media, ya no debe inicializarse más.
                            
                            local_H=float(col[2 ])
                            H_Temp=float(col[3])
                            mean_H_Temp=-1.00
                            mean_local_H=-1.00

                            GTS=float(col[6])
                            mean_GTS=-1.00
                            stand_deviation_GTS=-1.00
                            #GTS_conf=float(col[7])

                            TB1=col[8]
                            TB2=col[10]
                            minT = -1

                            pressure=float(col[5])
                            mean_pressure = -1.00

                            UV_A=float(colNV[2])
                            UV_B=float(colNV[3])
                            UV_C=float(colNV[4])
                            UV_ABC=float(colNV[5])
                            UV_D=float(colNV[6])
                            UV_E=float(colNV[7])
                            UV_conf=(colNV[9])
                            mean_UV_A = -1.00
                            mean_UV_B = -1.00
                            mean_UV_C = -1.00
                            mean_UV_ABC = -1.00
                            mean_UV_D = -1.00
                            mean_UV_E = -1.00

                            if (((current_sclk - prior_sclk) >= pause) or (current_sclk >= end_sclk) or (prior_hour != current_hour)):

                                if (n_local_H != 0):
                                    mean_local_H =  add_local_H/n_local_H

                                if (n_H_Temp != 0):
                                    mean_H_Temp =  add_H_Temp/n_H_Temp

                                if (n_GTS != 0):
                                    
                                    mean_GTS = (add_GTS/n_GTS)

                                    for i in range(n_GTS):
                                        
                                        aux_deviation_GTS = aux_deviation_GTS + (array_GTS[i] - mean_GTS) ** 2

                                    stand_deviation_GTS = np.sqrt(aux_deviation_GTS/n_GTS)

                                if (n_TB1 != 0):
                                    minT1 = min(TB1_array)
                     
                                if (n_TB2 != 0):
                                    minT2 = min(TB2_array)

                                if (minT1 < minT2):
                                    minT = minT1

                                elif (float(minT2) < tempMin):
                                    minT = minT1

                                else:
                                    minT = minT2

                                if (n_pressure != 0):
                                    mean_pressure = add_pressure/n_pressure

                                if (n_UV_A != 0):
                                    mean_UV_A = add_UV_A/n_UV_A
                                if (n_UV_B != 0):
                                    mean_UV_B = add_UV_B/n_UV_B
                                if (n_UV_C != 0):
                                    mean_UV_C = add_UV_C/n_UV_C
                                if (n_UV_ABC != 0):
                                    mean_UV_ABC = add_UV_ABC/n_UV_ABC
                                if (n_UV_D != 0):
                                    mean_UV_D = add_UV_D/n_UV_D
                                if (n_UV_E != 0):
                                    mean_UV_E = add_UV_E/n_UV_E

                                
                                mean_sec = get_meanTime(time_1, time_2)# Media en segundos
                                mean_timeLMST = getLMST(mean_sec)# Media en formato LMST
                                
                                block_hours.append(current_hour) #Indica que se ha hecho la media para esta hora, si sigue habiendo valores para esta hora no se tienen en cuenta (continue en if arriba)
                                new_init = True

                                mean_local_H = round(mean_local_H, 2)
                                mean_H_Temp = round(mean_H_Temp, 2)
                                mean_GTS = round(mean_GTS, 2)
                                stand_deviation_GTS = round(stand_deviation_GTS, 2)
                                mean_pressure = round(mean_pressure, 2)
                                mean_UV_A = round(mean_UV_A, 2)
                                mean_UV_B = round(mean_UV_B, 2)
                                mean_UV_C = round(mean_UV_C, 2)
                                mean_UV_ABC = round(mean_UV_ABC, 2)
                                mean_UV_D = round(mean_UV_D, 2)
                                mean_UV_E = round(mean_UV_E, 2)
                                
                                
                                if mean_sec<300:
                                    mean_sec=mean_sec-2
                                    mean_timeLMST = getLMST(mean_sec)# Media en formato LMST

                                if ((mean_pressure != - 1.00) and (minT != - 1.00)):
                                    mean_rho = float(mean_pressure)/R/float(minT)

                                #mean_GTS_minT = float(mean_GTS) - float(minT)
                                    
                                #mean_vel_rho_GTS_rho_GTS_minT = vel * mean_rho * mean_GTS_minT

                                #mean_GTS_minT = round(mean_GTS_minT, 2)
                                #mean_rho = round(mean_rho, 2)
                                #mean_vel_rho_GTS_rho_GTS_minT = round(mean_vel_rho_GTS_rho_GTS_minT, 2)
                                


                                    
                                output_file.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_local_H)+' '+str(mean_H_Temp)+' '+str(mean_GTS)+' '+str(stand_deviation_GTS)+' '+str(minT)+' '+str(mean_pressure)+' '+str(mean_UV_A)+' '+str(mean_UV_B)+' '+str(mean_UV_C)+' '+str(mean_UV_ABC)+' '+str(mean_UV_D)+' '+str(mean_UV_E)+'\n')
                                output_fileMin.write(str(mean_sec)+' '+str(mean_timeLMST)+' '+str(minT)+'\n')
                                output_fileGTS.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_GTS)+' '+str(stand_deviation_GTS)+'\n')
                                output_filePr.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_pressure)+'\n')
                                output_fileUV.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_UV_A)+' '+str(mean_UV_B)+' '+str(mean_UV_C)+' '+str(mean_UV_ABC)+' '+str(mean_UV_D)+' '+str(mean_UV_E)+'\n')
                                output_fileRH.write(str(int(mean_sec))+' '+str(mean_timeLMST)+' '+str(mean_local_H)+' '+str(mean_H_Temp)+'\n')

                            # For RH average for block_secs_RH seconds
                            if ((local_H != -1.00) and (current_sclk < end_sclk_RH)):
                                n_local_H = n_local_H + 1
                                add_local_H = add_local_H + local_H
                            
                            # For RH_Temp average for block_secs_RH seconds
                            if ((H_Temp != -1.00) and (current_sclk < end_sclk_RH)):
                                n_H_Temp = n_H_Temp + 1
                                add_H_Temp = add_H_Temp + H_Temp

                            if (GTS != -1):
                                n_GTS = n_GTS + 1
                                add_GTS = add_GTS + GTS
                                array_GTS.append(GTS)

                            if (TB1 != -1):
                                n_TB1 = n_TB1 + 1
                                TB1_array.append(TB1)

                            if (TB2 != -1):
                                n_TB2 = n_TB2 + 1
                                TB2_array.append(TB2)

                            if (pressure != -1.00):
                                n_pressure = n_pressure + 1
                                add_pressure = add_pressure + pressure

                           

                                #! For UV_A average
                            if (UV_A > 0.0):
                                n_UV_A = n_UV_A + 1
                                add_UV_A = add_UV_A + UV_A

                            # ! For UV_B average
                            if (UV_B > 0.0):
                                n_UV_B = n_UV_B + 1
                                add_UV_B = add_UV_B + UV_B

                            # ! For UV_C average
                            if (UV_C > 0.0):
                                n_UV_C = n_UV_C + 1
                                add_UV_C = add_UV_C + UV_C

                            # ! For UV_ABC average
                            if (UV_ABC > 0.0):
                                n_UV_ABC = n_UV_ABC + 1
                                add_UV_ABC = add_UV_ABC + UV_ABC

                            # ! For UV_D average
                            if (UV_D > 0.0):
                                n_UV_D = n_UV_D + 1
                                add_UV_D = add_UV_D + UV_D
                            # ! For UV_E average
                            if (UV_E > 0.0):
                                n_UV_E = n_UV_E + 1
                                add_UV_E = add_UV_E + UV_E

                            time_2 = col[1][0:8]

                            prior_sclk = current_sclk
                            prior_hour = current_hour
            

print("MEAN_6 ... STARTING")

######readMD([0,1,2,3,4,5,6,7,8,9,10,11])
######readNV([0,1,2,3,4,5,6,7,9])
Temp6_b1_b2()
mean_Out6()

print("MEAN_6 ... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)



in_dir = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_Mean_GTS/"

out_dir1 = "/data/PDS_Python/PDS_out_release/3_Splines/Derivative/"

interval = 1000
yp1 = 1e+31
ypn = 1e+31
sig=1.0
u=[]
sec_per_hour=3600
sec_per_minute=60


# def getSeconds(LocalTime):
    
#     hour = str(LocalTime)[0:2]
#     hour = int(hour)
#     minutes = str(LocalTime)[3:5]
#     minutes = int(minutes)
#     seconds = str(LocalTime)[6:8]
#     seconds = int(seconds)
#     totalSec = hour * sec_per_hour + minutes * sec_per_minute + seconds

#     return totalSec


def getHHMMSS(timeSeconds):
    sec_per_hour = 3600
    sec_per_minute = 60
    # time ok. calculate the number of hours, and the number of
    # seconds left over after the hours are calculated.
    hour = "{:02}".format(int(timeSeconds/sec_per_hour))
    remain = timeSeconds - (float(hour)*sec_per_hour)
    # calculate the number of minutes left, and the number of
    # seconds left over after the hours are calculated
    minute = "{:02}".format(int(remain / sec_per_minute))
    remain = remain - float(minute) * sec_per_minute
    #Round it to the upper number
    sec = "{:02}".format(int(remain+0.5))
    timeLMST = str(hour) + ':' + str(minute) + ':' + str(sec)


    return timeLMST

def calculate_spline(x,y,n,yp1,ypn):
    
    y2=np.zeros(n+1)
    u=np.zeros(n+1)
    if (yp1 > 0.99e30):
            y2[0] = 0.0
            u[0] = 0.0
    else:
        y2[0] = -0.5
        u[0] = (3./(x[1] - x[1])*((y[1] - y[0])/(x[1] - x[0]) - yp1))
    
    for i in range(1,n - 1):
        if i >= 1:
            sig = (x[i] - x[i - 1])/(x[i + 1] - x[i - 1])
            p = sig * y2[i - 1] + 2.0
            y2[i] = (sig - 1.0)/p
            u[i] = (6.0 * ((y[i + 1] - y[i])/(x[i + 1] - x[i])-(y[i] - y[i - 1]) / (x[i] - x[i - 1]))/(x[i + 1] - x[i - 1]) - sig * u[i - 1])/p
        else:
            continue
    
    if (ypn > 0.99e30):
        qn = 0.0
        un = 0.0
    else:
        qn = 0.5
        un = (3./(x[n] - x[n - 1]))*(ypn - (y[n] - y[n - 1])/(x[n] - x[n - 1]))
    
    y2[n] = (un - qn * u[n - 1])/(qn * y2[n - 1] + 1.0)
    for k in range(n-1,0,-1):

        y2[k] = y2[k] * y2[k + 1] + u[k]
    return (y2, x)

def calculate_splint(xa,ya,n,y2a,x):
    
    klo = 1
    khi = n
    while (khi - klo > 1):
        k = int(float(khi + klo)/2.0)

        if (xa[k-1] > x):
            khi = k

        else:   
            klo = k
       
    h = xa[khi-1] - xa[klo-1]
    if (h == 0.0):
        return -1

    a = (xa[khi-1] - x)/h
    b = (x - xa[klo-1])/h
    splint = a * ya[klo-1] + b * ya[khi-1] + ((a**3 - a) * y2a[klo-1] +(b**3 - b) * y2a[khi-1])*(h**2)/6.0
    return splint
    

def spline_GTSDer():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(out_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and file.startswith('f'):
            
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[21:26]
                #print("SplineGTSDER1" + sun)
                
                if os.stat(out_dir1 + 'first_GTS_spline_sol_' + sun+ '.dat').st_size != 0:
                    with open(out_dir1 + 'first_GTS_spline_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'GTS_spline_sol_' + sun+ '.dat','w') as output_file:
                        x=[]
                        y=[]
                        m=[]
                        for c in input_file:
                            file=input_file.name
                            
                            col=(c.split())
                            
                            if len(col) < 2:
                                continue
                            else:
                                
                                a=float(col[0]) #time
                                x.append(a)
                                
                                b=float(col[1]) #value
                                v=str(col[1])
                                y.append(b)
                                m.append(v)

                        if "-1.00" in m:
                            q=m.index("-1.00")
                            y.remove(-1.00)
                            x.pop(q)
                            n = ((len(open(file).readlines())))-1
                        else:
                            
                            n = (len(open(file).readlines()))

                        D2y, x=(calculate_spline(x,y,n,yp1,ypn))
                        size_max = (int(x[n-1]))
                        
                        i=x[0]
                        for ii in range(size_max):
                            
                            splint= calculate_splint(x,y,n,D2y,i)
                            splint = str(round(splint, 2))
                            LMST=getHHMMSS(i)
                            output_file.write(str(int(i))+' '+str(LMST)+' '+(splint)+'\n')
                            i=i+interval
                            
                            if i >= size_max:
                                break

    #return df2_final


def spline_GTSDer1():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #sprint(file)
                # Checking the file extension
            if str(file).endswith('.dat') and not str(file).startswith('f'):
                #if file.find(file_md) != -1.00:
                md_file = file
                if os.stat(in_dir + md_file).st_size != 0:
    
                    sun = md_file[13:18]
                    w_file = "first_GTS_spline_sol_"+sun+".dat"
                    with open(in_dir+md_file) as textfile1, open(out_dir1 + w_file, 'w+') as output_file:
                        output_file.truncate()
                        for y in (textfile1):
                            y = y.split()
                            if len(y)<2:
                                continue
                            else:
                                output_file.write(y[0].strip('\"') + ' ' + y[2].strip('\"') +'\n')
            


print("Spline_Derivative ... STARTING")

spline_GTSDer1()

spline_GTSDer()

print("Spline_Derivative ... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


in_dir = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_Mean_GTS/"
out_dir1 = "/data/PDS_Python/PDS_out_release/3_Splines/Derivative/"

out_dir2 = "/data/PDS_Python/PDS_out_release/3_Splines/GTSspli/"

interval = 1
yp1 = 1e+31
ypn = 1e+31
sig=1.0
u=[]
sec_per_hour=3600
sec_per_minute=60


# def getSeconds(LocalTime):
    
#     hour = str(LocalTime)[0:2]
#     hour = int(hour)
#     minutes = str(LocalTime)[3:5]
#     minutes = int(minutes)
#     seconds = str(LocalTime)[6:8]
#     seconds = int(seconds)
#     totalSec = hour * sec_per_hour + minutes * sec_per_minute + seconds

#     return totalSec


# def getHHMMSS(timeSeconds):
#     sec_per_hour = 3600
#     sec_per_minute = 60
#     # time ok. calculate the number of hours, and the number of
#     # seconds left over after the hours are calculated.
#     hour = "{:02}".format(int(timeSeconds/sec_per_hour))
#     remain = timeSeconds - (float(hour)*sec_per_hour)
#     # calculate the number of minutes left, and the number of
#     # seconds left over after the hours are calculated
#     minute = "{:02}".format(int(remain / sec_per_minute))
#     remain = remain - float(minute) * sec_per_minute
#     #Round it to the upper number
#     sec = "{:02}".format(int(remain+0.5))
#     timeLMST = str(hour) + ':' + str(minute) + ':' + str(sec)


#     return timeLMST

def calculate_spline(x,y,n,yp1,ypn):
    
    y2=np.zeros(n+1)
    u=np.zeros(n+1)
    if (yp1 > 0.99e30):
            y2[0] = 0.0
            u[0] = 0.0
    else:
        y2[0] = -0.5
        u[0] = (3./(x[1] - x[1])*((y[1] - y[0])/(x[1] - x[0]) - yp1))
    
    for i in range(1,n - 1):
        if i >= 1:
            sig = (x[i] - x[i - 1])/(x[i + 1] - x[i - 1])
            p = sig * y2[i - 1] + 2.0
            y2[i] = (sig - 1.0)/p
            u[i] = (6.0 * ((y[i + 1] - y[i])/(x[i + 1] - x[i])-(y[i] - y[i - 1]) / (x[i] - x[i - 1]))/(x[i + 1] - x[i - 1]) - sig * u[i - 1])/p
        else:
            continue
    
    if (ypn > 0.99e30):
        qn = 0.0
        un = 0.0
    else:
        qn = 0.5
        un = (3./(x[n] - x[n - 1]))*(ypn - (y[n] - y[n - 1])/(x[n] - x[n - 1]))
    
    y2[n] = (un - qn * u[n - 1])/(qn * y2[n - 1] + 1.0)
    for k in range(n-1,0,-1):

        y2[k] = y2[k] * y2[k + 1] + u[k]
    return (y2, x)

def calculate_splint(xa,ya,n,y2a,x):
    
    klo = 1
    khi = n
    while (khi - klo > 1):
        k = int(float(khi + klo)/2.0)

        if (xa[k-1] > x):
            khi = k

        else:   
            klo = k
       
    h = xa[khi-1] - xa[klo-1]
    if (h == 0.0):
        return -1

    a = (xa[khi-1] - x)/h
    b = (x - xa[klo-1])/h
    splint = a * ya[klo-1] + b * ya[khi-1] + ((a**3 - a) * y2a[klo-1] +(b**3 - b) * y2a[khi-1])*(h**2)/6.0
    return splint

def spline_GTSspli():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(out_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and file.startswith('f'):
                
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[21:26]
                #
                # print("SplineGTSspli2" + sun)

                if os.stat(out_dir1 + 'first_GTS_spline_sol_' + sun+ '.dat').st_size != 0:

                    with open(out_dir1 + 'first_GTS_spline_sol_' + sun+ '.dat','r') as input_file, open(out_dir2 + 'GTS_spline_sol_' + sun+ '.dat','w') as output_file:
                        x=[]
                        y=[]
                        m=[]
                        for c in input_file:
                            file=input_file.name
                            
                            col=(c.split())
                            
                            
                                
                            a=float(col[0]) #time
                            x.append(a)
                            b=float(col[1]) #value
                            v=str(col[1])
                            y.append(b)
                            m.append(v)

                        if "-1.00" in m:
                            q=m.index("-1.00")
                            y.remove(-1.00)
                            x.pop(q)
                            n = ((len(open(file).readlines())))-1
                        else:
                            
                            n = (len(open(file).readlines()))
                        
                        D2y, x=(calculate_spline(x,y,n,yp1,ypn))
                        size_max = (int(x[n-1]))
                        
                        i=x[0]
                        for ii in range(size_max):
                            
                            splint= calculate_splint(x,y,n,D2y,i)
                            splint = str(round(splint, 2))
                            
                            LMST=getHHMMSS(i)
                        
                            output_file.write(str(int(i))+' '+str(LMST)+' '+(splint)+'\n')
                            if i >= size_max:
                                break
                            i=i+interval
                    
    #return df2_final


                
print("Spline_GTS ... STARTING")

########    spline_GTSspli1([0,2])

spline_GTSspli()

print("Spline_GTS ... COMPLETED")


ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)



in_dir = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_mean_Pressure/"  

out_dir1 = "/data/PDS_Python/PDS_out_release//3_Splines/Pspline/"

interval = 1
yp1 = 1e+31
ypn = 1e+31
sig=1.0
u=[]
sec_per_hour=3600
sec_per_minute=60


# def getSeconds(LocalTime):
    
#     hour = str(LocalTime)[0:2]
#     hour = int(hour)
#     minutes = str(LocalTime)[3:5]
#     minutes = int(minutes)
#     seconds = str(LocalTime)[6:8]
#     seconds = int(seconds)
#     totalSec = hour * sec_per_hour + minutes * sec_per_minute + seconds

#     return totalSec


# def getHHMMSS(timeSeconds):
#     sec_per_hour = 3600
#     sec_per_minute = 60
#     # time ok. calculate the number of hours, and the number of
#     # seconds left over after the hours are calculated.
#     hour = "{:02}".format(int(timeSeconds/sec_per_hour))
#     remain = timeSeconds - (float(hour)*sec_per_hour)
#     # calculate the number of minutes left, and the number of
#     # seconds left over after the hours are calculated
#     minute = "{:02}".format(int(remain / sec_per_minute))
#     remain = remain - float(minute) * sec_per_minute
#     #Round it to the upper number
#     sec = "{:02}".format(int(remain+0.5))
#     timeLMST = str(hour) + ':' + str(minute) + ':' + str(sec)


#     return timeLMST

def calculate_spline(x,y,n,yp1,ypn):
    
    y2=np.zeros(n+1)
    u=np.zeros(n+1)
    if (yp1 > 0.99e30):
            y2[0] = 0.0
            u[0] = 0.0
    else:
        y2[0] = -0.5
        u[0] = (3./(x[1] - x[1])*((y[1] - y[0])/(x[1] - x[0]) - yp1))
    
    for i in range(1,n - 1):
        if i >= 1:
            
            sig = (x[i] - x[i - 1])/(x[i + 1] - x[i - 1])
            p = sig * y2[i - 1] + 2.0
            y2[i] = (sig - 1.0)/p
            u[i] = (6.0 * ((y[i + 1] - y[i])/(x[i + 1] - x[i])-(y[i] - y[i - 1]) / (x[i] - x[i - 1]))/(x[i + 1] - x[i - 1]) - sig * u[i - 1])/p
        else:
            continue
    
    if (ypn > 0.99e30):
        qn = 0.0
        un = 0.0
    else:
        qn = 0.5
        un = (3./(x[n] - x[n - 1]))*(ypn - (y[n] - y[n - 1])/(x[n] - x[n - 1]))
    
    y2[n] = (un - qn * u[n - 1])/(qn * y2[n - 1] + 1.0)
    for k in range(n-1,0,-1):

        y2[k] = y2[k] * y2[k + 1] + u[k]
    return (y2, x)

def calculate_splint(xa,ya,n,y2a,x):
    
    klo = 1
    khi = n
    while (khi - klo > 1):
        k = int(float(khi + klo)/2.0)

        if (xa[k-1] > x):
            khi = k

        else:   
            klo = k
       
    h = xa[khi-1] - xa[klo-1]
    if (h == 0.0):
        return -1

    a = (xa[khi-1] - x)/h
    b = (x - xa[klo-1])/h
    splint = a * ya[klo-1] + b * ya[khi-1] + ((a**3 - a) * y2a[klo-1] +(b**3 - b) * y2a[khi-1])*(h**2)/6.0
    return splint
    

def spline_GTS():
    
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(out_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and file.startswith('f'):
                
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[26:31]
                #print("SplineGTS3" + sun)

                if os.stat(out_dir1 + 'first_pressure_spline_sol_' + sun+ '.dat').st_size != 0:
    
                    with open(out_dir1 + 'first_pressure_spline_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'pressure_spline_sol_' + sun+ '.dat','w') as output_file:
                        x=[]
                        y=[]
                        m=[]
                        for c in input_file:
                            file=input_file.name
                            
                            
                            col=(c.split())
                            
                            if len(col) < 2:
                                continue
                            else:
                                
                                a=float(col[0]) #time
                                x.append(a)
                                b=float(col[1]) #value
                                v=str(col[1])
                                y.append(b)
                                m.append(v)

                        if "-1.00" in m:
                            q=y.index("-1.00")
                            #y.remove(-1.00)
                            y.pop(q)
                            x.pop(q)
                            n = ((len(open(file).readlines())))-1
                        else:
                            
                            n = (len(open(file).readlines()))
                        
                        D2y, x=(calculate_spline(x,y,n,yp1,ypn))
                        size_max = (int(x[n-1]))
                        i=x[0]

                        
                        for ii in range(size_max):
                            
                            splint= calculate_splint(x,y,n,D2y,i)
                            splint = str(round(splint, 2))

                            LMST=getHHMMSS(i)

                            output_file.write(str(int(i))+' '+str(LMST)+' '+(splint)+'\n')
                            
                            if i >= size_max:
                                break
                            i=i+interval
                  

def spline_GTS1():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
                # Checking the file extension
            if str(file).endswith('.dat') and not str(file).startswith('f'):
                #if file.find(file_md) != -1.00:
                md_file = file
                if os.stat(in_dir + md_file).st_size != 0:
                
                    sun = md_file[18:23]
                    w_file = "first_pressure_spline_sol_"+sun+".dat"
                    with open(in_dir+md_file) as textfile1, open(out_dir1 + w_file, 'w+') as output_file:
                        output_file.truncate()
                        for y in (textfile1):
                            y = y.split()
                            if len(y)<2:
                                continue
                            else:
                                output_file.write(y[0].strip('\"') + ' ' + y[2].strip('\"') +'\n')
                    #print (w_file + ' Completed!')


                    
print("Spline_PS ... STARTING")

spline_GTS1()

spline_GTS()

print("Spline_PS ... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)

in_dir = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"

out_dir1 = "/data/PDS_Python/PDS_out_release/4_RH/RHumidity/"


sec_per_hour = 3600
sec_per_minute = 60
block_secs = 5
#We are looking in the primary folders, maybe too many suns for us and is not a good 
#choice because of the last checking suns change in_dir for a folder with the suns that are not empty

# def get_meanTime(time1,time2):
    
#     a = getSeconds(time1)
#     b = getSeconds(time2)

#     return (a+b)/2

# def getSeconds(LocalTime):
    
#     hour = str(LocalTime)[0:2]
#     hour = int(hour)
#     minutes = str(LocalTime)[3:5]
#     minutes = int(minutes)
#     seconds = str(LocalTime)[6:8]
#     seconds = int(seconds)
#     totalSec = hour * sec_per_hour + minutes * sec_per_minute + seconds
#     #print(totalSec)

#     return totalSec

# def getMMSS(time):
#     minute = str(time)[3:5]
#     sec = (str(time)[6:8])
    
#     getMMSS= str(minute)+ ':' + str(sec)
#     return getMMSS



# def getLMST(timeSec):
    
#     nsecs = (timeSec%86400)
#     sec = "{:02}".format(int(nsecs%60))
#     nsecs = nsecs / 60
#     minute = "{:02}".format(int(nsecs%60))
#     hh = "{:02}".format(int(nsecs / 60))

#     timeLMST = str(hh) + ':' + str(minute) + ':' + str(sec)

#     return timeLMST


def RHumidity():
    
    # Iteration on the MD Files Directory
    # Where the files are        
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #sprint(file)
                # Checking the file extension
            if str(file).endswith('.dat'):
                #if file.find(file_md) != -1.00:
                md_file = file
                if os.stat(in_dir + md_file).st_size != 0:
    
                    sun = md_file[3:8]
                    w_file = "first_RH_first_Instants_sol_"+sun+".dat"
                    with open(in_dir+md_file) as textfile1, open(out_dir1 + w_file, 'w+') as output_file:
                        output_file.truncate()
                        for y in (textfile1):
                            y = y.split()
                            if len(y)<2:
                                continue
                            else:
                                output_file.write(y[0].strip('\"') + ' ' + y[1].strip('\"') + ' ' + y[2].strip('\"') + ' ' + y[3].strip('\"') +'\n')
            


                    with open(out_dir1 + 'first_RH_first_Instants_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'RH_first_Instants_sol_' + sun+ '.dat','w') as output_file:
                        
                        j = 0
                        block_hours = False #Vector que lleva la cuenta de si ha hecho ya media para una hora (true) o no (false).
                        new_init = True 
                        file=input_file.name

                        size = (len(open(file).readlines()))
                        control=-1
                        block_hours=[]
                        
                        for i in input_file:
                            control=control+1
                            
                            col=(i.split())
                            #print(col)
                    
                            if len(col) < 4:
                                continue
                            else:
                                current_sclk = int(col[0])

                                seg=(getSeconds(col[1]))
                                current_hour=(str(col[1]))[0:2]
                                

                                current_hour = int(current_hour) +1
                                LMST = str(getLMST(seg))

                                RH=col[2]
                                RHTemp=col[3]  

                                if current_hour in block_hours:
                                    continue
                                elif new_init==True:
                                    #Inicializo tiempos para empezar las nuevas medidas de la nueva hora
                                    prior_sclk = current_sclk
                                    prior_hour = current_hour
                                    end_sclk = current_sclk + block_secs
                                    new_init = False #Una vez inicializadas las variables de la nueva hora, ya no debe inicializarse más.

                                if ((current_sclk >= end_sclk) or (prior_hour != current_hour) or ((control == size) and (prior_hour not in block_hours))):
                                                    
                                    block_hours.append(prior_hour) # Indica que ya han pasado los segundos que queremos almacenar (block_secs). Si sigue habiendo valores para esta hora no se tienen en cuenta (cycle en if1)
                                    new_init = True # Indica que se va a empezar una nueva toma de medidas, por lo tanto, hay que inicializar variables (else de if1).
                                output_file.write(str(seg)+' '+str(LMST)+' '+str(RH)+' '+str(RHTemp)+'\n')

                                #j = j + 1

                                # RH_array[j] = dta % RH(i)
                                # dta_RH % RH_Temp_array(j) = dta % RH_Temp(i)
                                
                                prior_sclk = current_sclk
                                prior_hour = current_hour


                                
                                

print("RHumidity ... STARTING")

RHumidity()  

print("RHumidity ... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)

in_dir1 = "/data/PDS_Python/PDS_out_release/4_RH/RHumidity/"
in_dir2 = "/data/PDS_Python/PDS_out_release/3_Splines/Pspline/"
in_dir3 = "/data/PDS_Python/PDS_out_release/3_Splines/GTSspli/"

out_dir1 = "/data/PDS_Python/PDS_out_release/4_RH/RHSurface5/"


def absoluteMax(y):
    
    abs_max=max(y)
    return float(abs_max)


def absoluteMin(y):
    a=[]
    
    for i in y:
        if i==-1:
            aux=1000
            a.append(aux)
        else:
            a.append(i)

    abs_min=min(a)
    if abs_min==1000:
        abs_min=-1


    return float(abs_min)

def RHSurface5():
    found_PS = False
    found_GTS = False
    
    
    index_PS = 1
    index_GTS = 1
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files1 in os.walk(in_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for fileRH in sorted(files1):
            #make sure that we are only working with the correct files ending with the termination ".dat" and avoiding the one that start with 'f'
            if fileRH.endswith('.dat') and not fileRH.startswith('f'):
            
                sunRH = fileRH[22:27]
                #print("1 " + sunRH)
     
                for base, dirs, files2 in os.walk(in_dir2):
                    for filePS in sorted(files2):
                        if filePS.endswith('.dat') and not filePS.startswith('f'):
                                                        
                            sunPS = filePS[20:25]
                            #print("2 " + sunPS)
                            if sunPS == sunRH:


                                for base, dirs, files3 in os.walk(in_dir3):
                                    for fileGTS in sorted(files3):
                                        if fileGTS.endswith('.dat') and not fileGTS.startswith('f'):
                                            
                                            sunGTS = fileGTS[15:20]
                                            #print("3 " + sunGTS)

                                            
                                            if sunRH==sunPS==sunGTS:
                                            
                                                
                                                with open(in_dir1 + fileRH) as input_fileRH1, open(in_dir3 + fileGTS) as input_fileGTS1:
                                                    segs_RH=[]
                                                    GTS=[]
                                                    LTimes_local_RH1=[]
                                                    locals_RH=[]
                                                    locals_RH_Temp=[]
                                                    fileRH1=input_fileRH1.name
                                                        
                                                    nRH = (len(open(fileRH1).readlines()))

                                                    for RH1 in (input_fileRH1):   
                                                        
                                                        colRH1 = RH1.split()
                                                        seg_RH1=int(colRH1[0])
                                                        segs_RH.append(seg_RH1)  

                                                        
                                                        LTime_local_RH1=(colRH1[1])
                                                        LTimes_local_RH1.append(LTime_local_RH1)
                                                        local_RH=float(colRH1[2])
                                                        locals_RH.append(local_RH)
                                                        local_RH_Temp=float(colRH1[3])
                                                        locals_RH_Temp.append(local_RH_Temp)

                                                    for GTS1 in (input_fileGTS1):
                                                        colGTS1 = GTS1.split()

                                                        x=(colGTS1[2])
                                                        GTS.append(x)

                                                    maximo = absoluteMax(GTS)

                                                    minimo = absoluteMin(GTS)

                                                    Sub_Temp = minimo + (maximo - minimo)/2.3


                                                with open(in_dir1 + fileRH) as input_fileRH, open(in_dir2 + filePS) as input_filePS , open(in_dir3 + fileGTS) as input_fileGTS, open(out_dir1 + 'RH_Surf_SubSurf_sol_'+ sunGTS + '.dat','w') as output_file:
                                                    #segs_RH=[]
                                                    size_RH_Surf=0
                                                    
                                                    for RH in input_fileRH:
                                                        colRH = RH.split()
                                                        seg_RH=int(colRH[0])

                                                    
                                                    for PS, GTS in zip(input_filePS, input_fileGTS):
                                                    
                                                        colPS = PS.split()
                                                        colGTS = GTS.split()

                                                    
                                                        
                                                        seg_PS=int(colPS[0])
                                                        pressure=(colPS[2])

                                                        seg_GTS=int(colGTS[0])
                                                        GTS=(colGTS[2])
                                                        

                                                        if (seg_PS in segs_RH) and (seg_GTS in segs_RH):# Comprueba que si el dato de RH se encuentran en pressure

                                                            found_PS = True
                                                            found_GTS = True
                                                            index_PS = index_PS + 1
                                                            i=segs_RH.index(seg_PS)
                                                        

                                                        if ((found_PS == True) and (found_GTS == True)): # Si hay medidas para ese segundo de RH, P y GTS, entonces calcula RH_Surf
                                                            LTime_local_RH=LTimes_local_RH1[i]
                                                            local_RH=locals_RH[i]
                                                            local_RH_Temp=locals_RH_Temp[i]
                                                            if (local_RH == -1):

                                                                surface_RH = -1
                                                                MR = -1
                                                                VMR = -1

                                                                Sub_surface_RH = -1
                                                                Sub_MR = -1
                                                                Sub_VMR = -1

                                                            else:

                                                                if (local_RH > 100.0):
                                                                    
                                                                    local_RH = 100
                                                                # Surface RH:
                                                                surface_RH, MR,VMR=calling_subroutines(local_RH, local_RH_Temp, pressure, GTS)
                                                                # Subsurface RH:                                      
                                                                Sub_surface_RH, Sub_MR, Sub_VMR=  calling_subroutines(local_RH, local_RH_Temp, pressure, Sub_Temp)
                                                            
                                                            Sub_surface_RH = round(Sub_surface_RH, 2)
                                                            VMR = round(VMR, 2)
                                                            surface_RH = round(surface_RH, 2)
                                                            MR = round(MR, 2)

                                                            output_file.write(str(segs_RH[i])+' '+str(LTimes_local_RH1[i])+' '+str(pressure)+' '+str(locals_RH_Temp[i])+' '+str(GTS)+' '+str(locals_RH[i])+' '+str(surface_RH)+' '+str(MR)+' '+str(VMR)+' '+str(Sub_surface_RH)+'\n')

                                                            
                                                            seg_surface_RH = seg_RH
                                                            LTime_surface_RH = LTime_local_RH

                                                            local_RH = local_RH
                                                            local_RH_Temp = local_RH_Temp
                                                            pressure = pressure
                                                            GTS = GTS


                                                            size_RH_Surf= size_RH_Surf+1

                                                        found_PS = False
                                                        found_GTS = False
                                                break
                                break

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

    return RH_out, W, VMR

def rh2mr(RH, P, esat):
    
    
        # ! PURPOSE:
        # !	Convert relative humidity (%) into mixing ratio (g H2O per kg of dry air) given
        # !       temperature and pressure.
        # !   
        # !  Derivation:
        # !                                     Mw*e              e
        # !  W (mixing ratio) = m_h2o/m_dry = -------- = Mw/Md * ---- *1000
        # !                                    Md*(p-e)           p-e
        # !
        # !  RH (rel. hum.)    = e/esat(T)*100
        # !
        # !  Thus: W = Mw/Md*U*esat(T)/(p-U*esat(T))*1000, 
        # !        where U=RH/100
        # !
        # !
        # ! INPUTS:
        # !	RH: Relative humidity in percent
        # !       p : pressure in hPa
        # !       T : Temperature in C or K
        # !       es: Saturation vapor pressure in C or K -- computed with subroutine es.f90 
        # !
        # ! OUTPUTS:
        # !	Returns the mixing ratio as g H2O per kg of dry air
        # !

    Mw = 18.0160 # molecular weight of water
    Md = 43.3400 # molecular weight of dry air on Mars 
    
    #        ! This is the mixing ratio

    W = Mw/Md * RH/100. * esat/(P - RH/100. * esat) * 1000.

    VMR = Md/Mw * W * 1e3
    
    return W, VMR


def mr2rh(P, W, esat):
    
        # ! PURPOSE:
        # !	Convert mixing ratio (g H2O per kg of dry air) at given
        # !	temperature and pressure into relative humidity (%)
        # !   
        # ! INPUTS:
        # !	W : H2O mixing ratios in g H2O per kg dry air
        # !       p : pressure in hPa
        # !       T : Temperature in C or K -- implicitely in the calculation of es
        # !
        # !
        # ! OUTPUTS:
        # !	returns the relative humidity 
        # !
        # !  Derivation:
        # !                                      Mw*e              e
        # !  W (mixing ratio) = m_h2o/m_dry = --------- = Mw/Md * ----
        # !                                    Md*(p-e)           p-e
        # !
        # !  RH (rel. hum.) = e/es(T)*100.
        # !  e = water vapor pressure
        # !  es = saturation vapor pressure
        # !
        # !

        Mw = 18.0160 # molecular weight of water
        Md = 43.3400 # molecular weight of dry air on Mars 
        
        fact = W/1000. * Md/Mw

        # This is the Relative Humidity (%)
        RH_out = P/esat * fact/(1 + fact) * 100.0

        if (RH_out > 100.0):
            RH_out = 100


        return RH_out



def es(T):
    # !
    #     ! PURPOSE:
    #     !	Compute saturation vapor pressure given temperature in K or C
    #     !
    #     !  ******************************************************************
    #     !  **** NOTE: es formulae are Earth-based                       *****
    #     !  **** We should think about changes for Mars conditions        ****
    #     ! *******************************************************************
    #     ! INPUTS:
    #     !	T	SCALAR OR VECTOR OF TEMPERATURES IN K
    #     !
    #     !
    #     ! OUTPUTS:
    #     !	returns the saturation vapor pressure in hPa
    #     !
    #     !
    #     !       A good reference is Gibbins, C.J., Ann. Geophys., 8, 859-886, 1990

    #     ! Used by Richardson. This formulation agrees well with standard high- and low-temperature approximations [Goff and Gratch, 1946; Bar-Nun et al., 1985]
    #     ! http://www.gfdl.noaa.gov/bibliography/related_files/richardson0202.pdf page 5:
    #     !        ew = 6.11 * EXP(22.5 * (1. - TK/ T)), ew in hPascals, T in kelvin

    #     !    
    #     ! Formula with T = temperature in K
    #     !    es = exp( -6763.6/(T+T0) - 4.9283*alog((T+T0)) + 54.2190 )

    #     ! Formula close to that of Magnus, 1844 with temperature TC in Celsius
    #     !    es = 6.1078 * EXP( 17.2693882 * TC / (TC + 237.3) ) ; TC in Celsius

    #     ! or Emanuel's formula (also approximation in form of Magnus' formula,
    #     ! 1844), which was taken from Bolton, Mon. Wea. Rev. 108, 1046-1053, 1980.
    #     ! This formula is very close to Goff and Gratch with differences of
    #     ! less than 0.25% between -50 and 0 deg C (and only 0.4% at -60degC)    
    #     !    es =  6.112*EXP(17.67*TC/(243.5+TC))

    #     ! WMO reference formula is that of Goff and Gratch (1946), slightly
    #     ! modified by Goff in 1965:

    
    e1 = 1013.250
    TK = 273.14159

    # ! T0 = 273.14159

    #         ! TC = T - TK
    #         ! ESTA ES LA QUE UTILIZABA ANTES:
    #         !        es = e1 * 10**(10.79586 * (1 - TK/(T)) - 5.02808 * alog10((T)/TK)+ &
    #         !        1.50474 * 1e-4 * (1 - 10**(-8.29692 * ((T)/TK - 1)))+ &
    #         !        0.42873 * 1e-3 * (10**(4.76955 * (1 - TK/(T))) - 1) - 2.2195983)

    #         !        es = e1 * 10**(10.79586 * (1 - TK/(T + T0)) - 5.02808 * alog10((T + T0)/TK)+ &
    #         !        1.50474 * 1e-4 * (1 - 10**(-8.29692 * ((T + T0)/TK - 1)))+ &
    #         !        0.42873 * 1e-3 * (10**(4.76955 * (1 - TK/(T + T0))) - 1) - 2.2195983)


    #         ! This formulation agrees well with standard high- and low-temperature approximations [Goff and Gratch, 1946; Bar-Nun et al., 1985]
    #         ! http://www.gfdl.noaa.gov/bibliography/related_files/richardson0202.pdf page 5:
    es = 6.11 * np.exp(22.5 * (1. - TK/ T)) # saturation vapor pressure in Pa ??????.
    return es
    #         !        es = ew/10**2 ! saturation vapor pressure in hPa.


    #         !        ! Emanuel's formula
    #         !        es = 6.112 * EXP(17.67 * TC/(243.5 + TC))

    #         ! WMO based its recommendation on a paper by Goff (1957)
    #         !        Log10 ew =  10.79574 (1-273.16/T)- 5.02800 Log10(T/273.16)
    #         !                    + 1.50475 10-4 (1 - 10(-8.2969*(T/273.16-1)))
    #         !                    + 0.42873 10-3 (10(+4.76955*(1-273.16/T)) - 1) + 0.78614 

    #         !         es = e1 * 10**(10.79586 * (1 - TK/(T)) - 5.02808 * alog10((T)/TK)+ &
    #         !                1.50474 * 1e-4 * (1 - 10**(-8.29692 * ((T)/TK - 1)))+ &
    #         !                0.42873 * 1e-3 * (10**(4.76955 * (1 - TK/(T))) - 1) + 0.78614)



print("RHSurface5 ... STARTING")
                  
RHSurface5()

print("RHSurface5 ... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)

in_dir1 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean6/Out_means/"
out_dir1 = "/data/PDS_Python/PDS_out_release/4_RH/RHSurface6/"


def absoluteMax(y):
    
    abs_max=max(y)
    return float(abs_max)


def absoluteMin(y):
    a=[]
    
    for i in y:
        if i==-1:
            aux=1000
            a.append(aux)
        else:
            a.append(i)

    abs_min=min(a)
    if abs_min==1000:
        abs_min=-1


    return float(abs_min)



def RH_Surface6():
    for base, dirs, files in os.walk(in_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and  not file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[37:42]
                #print(sun)
                with open(in_dir1 + 'means_RH_GTS_lowestTemp_Press_UV_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'means_RH_RHSurf_Temps_UV_sigmas_sol_' + sun+ '.dat','w') as output_file:
                    #file = input_file    
                    file=input_file.name
                    n = (len(open(file).readlines()))
                    GTS=[]

                    for i in input_file:
                        
                        col1=(i.split())

                        if len(col1) < 4:
                            continue
                        else:
                            gtsss = col1[4]
                            GTS.append(gtsss)

                            maximo = absoluteMax(GTS)
                            minimo = absoluteMin(GTS)
                            sub_Temp = minimo + (maximo - minimo)/2.3


                with open(in_dir1 + 'means_RH_GTS_lowestTemp_Press_UV_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'means_RH_RHSurf_Temps_UV_sigmas_sol_' + sun+ '.dat','w') as output_file:
                    #file = input_file    
                    file=input_file.name
                    n = (len(open(file).readlines()))

                    for i in input_file:
                        
                        col=(i.split())

                        if len(col) < 4:
                            continue
                        else:
                            
                            seg = col[0] 
                            LMST = col[1] 
                            local_RH = col[2]
                            local_RH_Temp = col[3]
                            gtss = col[4]
                            sigma_GTS = col[5]
                            lowest_Air_Temp = col[6]
                            pressure = col[7]
                            UV_A = col[8]
                            UV_B = col[9]
                            UV_C = col[10]
                            UV_ABC = col[11]
                            UV_D = col[12]
                            UV_E = col[13]

                           
                            if (local_RH) == -1:
                                
                                surface_RH = -1
                                sigma_RHSurf = -1
                                MR = -1
                                VMR = -1
                            
                            else:
                                
                                surface_RH, sigma_RHSurf, MR,VMR=calling_subroutines(local_RH, local_RH_Temp, pressure, gtss, sigma_GTS)
                                                        
                            sigma_RHSurf = round(sigma_RHSurf, 2)
                            surface_RH = round(surface_RH, 2)
                            

                            output_file.write(str(seg)+' '+str(LMST)+' '+str(local_RH_Temp)+' '+str(local_RH)+' '+str(gtss)+' '+str(sigma_GTS)+' '+str(surface_RH)+' '+str(sigma_RHSurf)+' '+str(lowest_Air_Temp)+' '+str(pressure)+' '+str(UV_A)+' '+str(UV_B)+' '+str(UV_C)+' '+str(UV_ABC)+' '+str(UV_D)+' '+str(UV_E)+'\n')

                                

def calling_subroutines(RH, T_RH, P, T, sigma_GTS):
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
    RH_out, sigma_RHSurf = mr2rh(hP, W, T, sigma_GTS, esat2)

    return RH_out, sigma_RHSurf, W, VMR

def rh2mr(RH, P, esat):
    
    
        # ! PURPOSE:
        # !	Convert relative humidity (%) into mixing ratio (g H2O per kg of dry air) given
        # !       temperature and pressure.
        # !   
        # !  Derivation:
        # !                                     Mw*e              e
        # !  W (mixing ratio) = m_h2o/m_dry = -------- = Mw/Md * ---- *1000
        # !                                    Md*(p-e)           p-e
        # !
        # !  RH (rel. hum.)    = e/esat(T)*100
        # !
        # !  Thus: W = Mw/Md*U*esat(T)/(p-U*esat(T))*1000, 
        # !        where U=RH/100
        # !
        # !
        # ! INPUTS:
        # !	RH: Relative humidity in percent
        # !       p : pressure in hPa
        # !       T : Temperature in C or K
        # !       es: Saturation vapor pressure in C or K -- computed with subroutine es.f90 
        # !
        # ! OUTPUTS:
        # !	Returns the mixing ratio as g H2O per kg of dry air
        # !

    Mw = 18.0160 # molecular weight of water
    Md = 43.3400 # molecular weight of dry air on Mars 
    
    #        ! This is the mixing ratio

    W = Mw/Md * RH/100. * esat/(P - RH/100. * esat) * 1000.

    VMR = Md/Mw * W * 1e3
    
    return W, VMR


def mr2rh(hp, W, T, sigma_GTS, esat):
    
        # ! PURPOSE:
        # !	Convert mixing ratio (g H2O per kg of dry air) at given
        # !	temperature and pressure into relative humidity (%)
        # !   
        # ! INPUTS:
        # !	W : H2O mixing ratios in g H2O per kg dry air
        # !       p : pressure in hPa
        # !       T : Temperature in C or K -- implicitely in the calculation of es
        # !
        # !
        # ! OUTPUTS:
        # !	returns the relative humidity 
        # !
        # !  Derivation:
        # !                                      Mw*e              e
        # !  W (mixing ratio) = m_h2o/m_dry = --------- = Mw/Md * ----
        # !                                    Md*(p-e)           p-e
        # !
        # !  RH (rel. hum.) = e/es(T)*100.
        # !  e = water vapor pressure
        # !  es = saturation vapor pressure
        # !
        # !
        derv_RH_Surf = 0.0

        Mw = 18.0160 # molecular weight of water
        Md = 43.3400 # molecular weight of dry air on Mars 
        
        TK = 273.14159

        fact = W/1000. * Md/Mw

        # This is the Relative Humidity (%)
        RH_out = hp/esat * fact/(1 + fact) * 100.0
    
        if (RH_out > 100.0):
            RH_out = 100.0
        
        derv_RH_Surf = (-RH_out * 22.5 * TK/T**2)

        if math.isnan(derv_RH_Surf) or hp < 0.2:
            
            sigma_RHSurf=0.00
           
        else:

            sigma_RHSurf = float((abs(derv_RH_Surf)) * float(sigma_GTS))
            
        return RH_out, sigma_RHSurf



def es(T):
    # !
    #     ! PURPOSE:
    #     !	Compute saturation vapor pressure given temperature in K or C
    #     !
    #     !  ******************************************************************
    #     !  **** NOTE: es formulae are Earth-based                       *****
    #     !  **** We should think about changes for Mars conditions        ****
    #     ! *******************************************************************
    #     ! INPUTS:
    #     !	T	SCALAR OR VECTOR OF TEMPERATURES IN K
    #     !
    #     !
    #     ! OUTPUTS:
    #     !	returns the saturation vapor pressure in hPa
    #     !
    #     !
    #     !       A good reference is Gibbins, C.J., Ann. Geophys., 8, 859-886, 1990

    #     ! Used by Richardson. This formulation agrees well with standard high- and low-temperature approximations [Goff and Gratch, 1946; Bar-Nun et al., 1985]
    #     ! http://www.gfdl.noaa.gov/bibliography/related_files/richardson0202.pdf page 5:
    #     !        ew = 6.11 * EXP(22.5 * (1. - TK/ T)), ew in hPascals, T in kelvin

    #     !    
    #     ! Formula with T = temperature in K
    #     !    es = exp( -6763.6/(T+T0) - 4.9283*alog((T+T0)) + 54.2190 )

    #     ! Formula close to that of Magnus, 1844 with temperature TC in Celsius
    #     !    es = 6.1078 * EXP( 17.2693882 * TC / (TC + 237.3) ) ; TC in Celsius

    #     ! or Emanuel's formula (also approximation in form of Magnus' formula,
    #     ! 1844), which was taken from Bolton, Mon. Wea. Rev. 108, 1046-1053, 1980.
    #     ! This formula is very close to Goff and Gratch with differences of
    #     ! less than 0.25% between -50 and 0 deg C (and only 0.4% at -60degC)    
    #     !    es =  6.112*EXP(17.67*TC/(243.5+TC))

    #     ! WMO reference formula is that of Goff and Gratch (1946), slightly
    #     ! modified by Goff in 1965:

    
    e1 = 1013.250
    TK = 273.14159

    # ! T0 = 273.14159

    #         ! TC = T - TK
    #         ! ESTA ES LA QUE UTILIZABA ANTES:
    #         !        es = e1 * 10**(10.79586 * (1 - TK/(T)) - 5.02808 * alog10((T)/TK)+ &
    #         !        1.50474 * 1e-4 * (1 - 10**(-8.29692 * ((T)/TK - 1)))+ &
    #         !        0.42873 * 1e-3 * (10**(4.76955 * (1 - TK/(T))) - 1) - 2.2195983)

    #         !        es = e1 * 10**(10.79586 * (1 - TK/(T + T0)) - 5.02808 * alog10((T + T0)/TK)+ &
    #         !        1.50474 * 1e-4 * (1 - 10**(-8.29692 * ((T + T0)/TK - 1)))+ &
    #         !        0.42873 * 1e-3 * (10**(4.76955 * (1 - TK/(T + T0))) - 1) - 2.2195983)


    #         ! This formulation agrees well with standard high- and low-temperature approximations [Goff and Gratch, 1946; Bar-Nun et al., 1985]
    #         ! http://www.gfdl.noaa.gov/bibliography/related_files/richardson0202.pdf page 5:
    es = 6.11 * np.exp(22.5 * (1. - TK/ T)) # saturation vapor pressure in Pa ??????.
    return es
    #         !        es = ew/10**2 ! saturation vapor pressure in hPa.


    #         !        ! Emanuel's formula
    #         !        es = 6.112 * EXP(17.67 * TC/(243.5 + TC))

    #         ! WMO based its recommendation on a paper by Goff (1957)
    #         !        Log10 ew =  10.79574 (1-273.16/T)- 5.02800 Log10(T/273.16)
    #         !                    + 1.50475 10-4 (1 - 10(-8.2969*(T/273.16-1)))
    #         !                    + 0.42873 10-3 (10(+4.76955*(1-273.16/T)) - 1) + 0.78614 

    #         !         es = e1 * 10**(10.79586 * (1 - TK/(T)) - 5.02808 * alog10((T)/TK)+ &
    #         !                1.50474 * 1e-4 * (1 - 10**(-8.29692 * ((T)/TK - 1)))+ &
    #         !                0.42873 * 1e-3 * (10**(4.76955 * (1 - TK/(T))) - 1) + 0.78614)


                                        
print("RHSurface6 ... STARTING")

    
RH_Surface6()

print("RHSurface6 ... COMPLETED")


ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


in_dir = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/NV_CLEAN/"

out_dir1 = "/data/PDS_Python/PDS_out_release/5_UV/"



sec_per_hour=3600
sec_per_minute=60

sclk = 0
seg = 0
LocalTime = '00:00:00.000'
UV_A = -1
UV_B = -1
UV_C = -1
UV_ABC = -1
UV_D = -1
UV_E = -1
UV_conf = 'XXXXXXXX'
size_dta = 0

global_UV_A = -1
global_UV_B = -1
global_UV_C = -1
global_UV_ABC = -1
global_UV_D = -1
global_UV_E = -1

direct_UV_A = -1
direct_UV_B = -1
direct_UV_C = -1
direct_UV_ABC = -1
direct_UV_D = -1
direct_UV_E = -1

diffuse_UV_A = -1
diffuse_UV_B = -1
diffuse_UV_C = -1
diffuse_UV_ABC = -1
diffuse_UV_D = -1
diffuse_UV_E = -1

max_diff_UV_A = -1
max_diff_UV_B = -1
max_diff_UV_C = -1
max_diff_UV_ABC = -1
max_diff_UV_D = -1
max_diff_UV_E = -1    

pos_SZA_UVS = 0 # Posición 1 empezando por la izq.
pos_globaL_UV = 1 # Posición 2 empezando por la izq.
pos_diffuseIrr_UVS = 2 # Posición 3 empezando por la izq.
pos_motion_UVS = 3 # Posición 4 empezando por la izq.
pos_shadow_UVS = 6 # Posición 7 empezando por la izq.

status_SZA_UVS = "1" # 1 = SZA in FoV (SZA 0-20) or pure diffuse (SZA [55-inf))/ 0 = out of FoV (20-55)
status_globalIrr_UVS = "1" # 1 = global irradiance (SZA 0-30) / 0 = No global irradiance  
status_diffuseIrr_UVS = "1" # 1 = diffuse irradiance (SZA 0-inf)
status_motion_UVS = "1" # 1 = rover still / 0 = rover motion
status_shadow_UVS = "1" # 1 = no shadow or night /  0 = Sensor UV en sombra




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

def getLMST(timeSec):
    
    nsecs = (timeSec%86400)
    sec = "{:02}".format(int(nsecs%60))
    nsecs = nsecs / 60
    minute = "{:02}".format(int(nsecs%60))
    hh = "{:02}".format(int(nsecs / 60))

    timeLMST = str(hh) + ':' + str(minute) + ':' + str(sec)

    return timeLMST



def UV_Direct_Irradiance():
    #changes to out_dir1 to check the same folder where we are reading.
    
    for base, dirs, files in os.walk(out_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[24:29]
                #print(sun)
                #print(sun)
                    
                with open(out_dir1 + 'first_irradiance_UV_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'irradiance_UV_sol_' + sun+ '.dat','w') as output_file:
                    #file = input_file    
                    file=input_file.name
                    n = (len(open(file).readlines()))

                    UV_A_Comlete=[]
                    UV_B_Comlete=[]
                    UV_C_Comlete=[]
                    UV_ABC_Comlete=[]
                    UV_D_Comlete=[]
                    UV_E_Comlete=[]

                    global_UV_A_Comlete=[]
                    global_UV_B_Comlete=[]
                    global_UV_C_Comlete=[]
                    global_UV_ABC_Comlete=[]
                    global_UV_D_Comlete=[]
                    global_UV_E_Comlete=[]

                    diffuseUV_A_Comlete=[]
                    diffuseUV_B_Comlete=[]
                    diffuseUV_C_Comlete=[]
                    diffuseUV_ABC_Comlete=[]
                    diffuseUV_D_Comlete=[]
                    diffuseUV_E_Comlete=[]

                    seg=[]
                    LocalTime=[]

                    max_diff_UV_A=-1.00
                    max_diff_UV_B=-1.00
                    max_diff_UV_C=-1.00
                    max_diff_UV_ABC=-1.00
                    max_diff_UV_D=-1.00
                    max_diff_UV_E=-1.00
                    
                    for i in input_file:
                        
                        col=(i.split())
                       # print(col)

                        if len(col) < 4:
                            continue
                        else:
                            #sclk=col[0]
                            LTime=col[1][0:8]
                            LocalTime.append(LTime)
                            s=getSeconds(LTime)
                            seg.append(s)

                            UV_A=float(col[2])
                            UV_A_Comlete.append(UV_A)

                            UV_B=float(col[3])
                            UV_B_Comlete.append(UV_B)
                            
                            UV_C=float(col[4])
                            UV_C_Comlete.append(UV_C)
                            
                            UV_ABC=float(col[5])
                            UV_ABC_Comlete.append(UV_ABC)

                            UV_D=float(col[6])
                            UV_D_Comlete.append(UV_D)
                            
                            UV_E=float(col[7])
                            UV_E_Comlete.append(UV_E)

                            UV_conf=col[8]
                            # ====================================== Obtaining global irradiance:
                            # global irradiance + rover still
                            if len(UV_conf) == 8 :
                               # print("Hols")
                                if ((UV_conf[pos_globaL_UV: pos_globaL_UV+1] == (status_globalIrr_UVS)) and ((UV_conf[pos_motion_UVS: pos_motion_UVS+ 1] == (status_motion_UVS)))):

                                    global_UV_A = UV_A
                                    global_UV_B = UV_B
                                    global_UV_C = UV_C
                                    global_UV_ABC = UV_ABC
                                    global_UV_D = UV_D
                                    global_UV_E = UV_E
                                    global_UV_A_Comlete.append(global_UV_A)
                                    global_UV_B_Comlete.append(global_UV_B)
                                    global_UV_C_Comlete.append(global_UV_C)
                                    global_UV_ABC_Comlete.append(global_UV_ABC)
                                    global_UV_D_Comlete.append(global_UV_D)
                                    global_UV_E_Comlete.append(global_UV_E)
                                else:
                                    global_UV_A_Comlete.append(-1.00)
                                    global_UV_B_Comlete.append(-1.00)
                                    global_UV_C_Comlete.append(-1.00)
                                    global_UV_ABC_Comlete.append(-1.00)
                                    global_UV_D_Comlete.append(-1.00)
                                    global_UV_E_Comlete.append(-1.00)
                                # ====================================== Obtaining diffuse irradiance
                                # [SZA = 1 + rover still] + [(global irradiance + shadow) or (diffuse irradiance)] 
                                
                                if (((UV_conf [pos_SZA_UVS: pos_SZA_UVS+1] == (status_SZA_UVS)) and (UV_conf [pos_motion_UVS: pos_motion_UVS+1] == (status_motion_UVS)) ) and 
                                    (((UV_conf[pos_globaL_UV: pos_globaL_UV+1] == (status_globalIrr_UVS)) and (UV_conf[pos_shadow_UVS: pos_shadow_UVS+1] != (status_shadow_UVS))) or 
                                    (UV_conf [pos_diffuseIrr_UVS: pos_diffuseIrr_UVS+1] == (status_diffuseIrr_UVS)))):

                                    diffuse_UV_A = UV_A
                                    diffuse_UV_B = UV_B
                                    diffuse_UV_C = UV_C
                                    diffuse_UV_ABC = UV_ABC
                                    diffuse_UV_D = UV_D
                                    diffuse_UV_E = UV_E
                                    diffuseUV_A_Comlete.append(diffuse_UV_A)
                                    diffuseUV_B_Comlete.append(diffuse_UV_B)
                                    diffuseUV_C_Comlete.append(diffuse_UV_C)
                                    diffuseUV_ABC_Comlete.append(diffuse_UV_ABC)
                                    diffuseUV_D_Comlete.append(diffuse_UV_D)
                                    diffuseUV_E_Comlete.append(diffuse_UV_E)
                                    
                                
                                    
        # ====================================== Obtaining greatest diffuse irradiance

                                    if (diffuse_UV_A > max_diff_UV_A):
                                        max_diff_UV_A = diffuse_UV_A


                                    if (diffuse_UV_B > max_diff_UV_B):
                                        max_diff_UV_B = diffuse_UV_B

                                    if (diffuse_UV_C > max_diff_UV_C):
                                        max_diff_UV_C = diffuse_UV_C

                                    if (diffuse_UV_ABC > max_diff_UV_ABC):
                                        max_diff_UV_ABC = diffuse_UV_ABC
                                    
                                    if (diffuse_UV_D > max_diff_UV_D):
                                        max_diff_UV_D = diffuse_UV_D

                                    if (diffuse_UV_E > max_diff_UV_E):
                                        max_diff_UV_E = diffuse_UV_E
                                else:
                                    diffuseUV_A_Comlete.append(-1.00)
                                    diffuseUV_B_Comlete.append(-1.00)
                                    diffuseUV_C_Comlete.append(-1.00)
                                    diffuseUV_ABC_Comlete.append(-1.00)
                                    diffuseUV_D_Comlete.append(-1.00)
                                    diffuseUV_E_Comlete.append(-1.00)



                    for i in range(len(global_UV_A_Comlete)-1):
                        
                        if (global_UV_A_Comlete[i] == -1 or not global_UV_A_Comlete):
                            direct_UV_A =-1.00
                        elif global_UV_A_Comlete[i] != -1   :
                            direct_UV_A = global_UV_A_Comlete[i] - max_diff_UV_A
                            
                        if (global_UV_B_Comlete[i] == -1 or not global_UV_B_Comlete):
                            direct_UV_B =-1.00
                        elif (global_UV_B_Comlete[i] != -1):
                            direct_UV_B = global_UV_B_Comlete[i] - max_diff_UV_B
                        
                        if (global_UV_C_Comlete[i] == -1 or not global_UV_C_Comlete):
                            direct_UV_C =-1.00
                        elif (global_UV_C_Comlete[i] != -1):
                            direct_UV_C = global_UV_C_Comlete[i] - max_diff_UV_C

                        if (global_UV_ABC_Comlete[i] == -1 or not global_UV_ABC_Comlete):
                            direct_UV_ABC =-1.00
                        elif (global_UV_ABC_Comlete[i] != -1):
                            direct_UV_ABC = global_UV_ABC_Comlete[i] - max_diff_UV_ABC
                        
                        if (global_UV_D_Comlete[i] == -1 or not global_UV_D_Comlete):
                            direct_UV_D =-1.00
                        elif (global_UV_D_Comlete[i] != -1):
                            direct_UV_D = global_UV_D_Comlete[i] - max_diff_UV_D
                        
                        if (global_UV_E_Comlete[i] == -1 or not global_UV_E_Comlete):
                            direct_UV_E =-1.00
                        elif (global_UV_E_Comlete[i] != -1):
                            direct_UV_E = global_UV_E_Comlete[i] - max_diff_UV_E
                        

                        output_file.write(str(seg[i])+' '+str(LocalTime[i])+' '+str(global_UV_A_Comlete[i])+' '+str(diffuseUV_A_Comlete[i])+' '+str(direct_UV_A)+' '+str(global_UV_B_Comlete[i])+' '+str(diffuseUV_B_Comlete[i])+' '+str(direct_UV_B)+' '+str(global_UV_C_Comlete[i])+' '+str(diffuseUV_C_Comlete[i])+' '+str(direct_UV_C)+' '+str(global_UV_ABC_Comlete[i])+' '+str(diffuseUV_ABC_Comlete[i])+' '+str(direct_UV_ABC)+' '+str(global_UV_D_Comlete[i])+' '+str(diffuseUV_D_Comlete[i])+' '+str(direct_UV_D)+' '+str(global_UV_E_Comlete[i])+' '+str(diffuseUV_E_Comlete[i])+' '+str(direct_UV_E)+'\n')

                                

# def UV_Direct_Irradiance1(columns):
#     # Iteration on the MD Files Directory
#     # Where the files are
#     for base, dirs, files in os.walk(in_dir):
#         ##Read each file name
#         #variable file is the name of the file with the extension and we put it as the file name 
#         for file in files:
#             #make sure that we are only working with the correct files ending with the termination ".dat"
#             if file.endswith('.dat') and  not file.startswith('f'):
#                 #Now we have the name of every file in order to insert it to pandas 
#                 filename = file
#                 # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
#                 sun = filename[3:8]
#                 # We tell pandas some informatio the file, the separator, the type of object (normally object) and there is no header the PDS files has no header.
#                 df = pd.read_csv(in_dir + filename, sep=' ',error_bad_lines=False, dtype=object, header=None,encoding='latin1') #encoding = "ISO-8859-1"
#                 #seconds LMST mean_GTS lowest_Air_Temp mean_P mean_UV_A mean_UV_B mean_UV_C mean_UV_ABC mean_UV_D mean_UV_E      
#                 df2_final = df.to_csv(out_dir1 + 'first_irradiance_UV_sol_' + sun+ '.dat', sep='\t', index=False, columns=columns, header=None)


def UV_Direct_Irradiance1():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #sprint(file)
                # Checking the file extension
            if str(file).endswith('.dat') and not str(file).startswith('f'):
                #if file.find(file_md) != -1.00:
                md_file = file
                if os.stat(in_dir + md_file).st_size != 0:
    
                    sun = md_file[3:8]
                    w_file = "first_irradiance_UV_sol_"+sun+".dat"
                    with open(in_dir+md_file) as textfile1, open(out_dir1 + w_file, 'w+') as output_file:
                        output_file.truncate()
                        for y in (textfile1):
                            y = y.split()
                            if len(y)<2:
                                continue
                            else:
                                output_file.write(y[0].strip('\"') + ' ' + y[1].strip('\"')+ ' ' + y[2].strip('\"')+ ' ' + y[3].strip('\"')+ ' ' + y[4].strip('\"')+ ' ' + y[5].strip('\"')+ ' ' + y[6].strip('\"')+ ' ' + y[7].strip('\"')+ ' ' + y[9].strip('\"')+'\n')
                    #print (w_file + ' Completed!')

                #read_clean_MD([0,1,30,31,33,37,7,10,11,12,13,14,15,16])



print("UV_Direct_Irradiance ... STARTING")

    
UV_Direct_Irradiance1()
UV_Direct_Irradiance()

print("UV_Direct_Irradiance ... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


in_dir = "/data/PDS_Python/PDS_out_release/3_Splines/Derivative/"

out_dir1 = "/data/PDS_Python/PDS_out_release/6_HEA_COO/Derivative_GTS/"


interval_1 = 1000.0
interval_2 = 1000.0
interval_3 = 1000.0
interval_4 = 1000.0

def getHHMMSS(timeSeconds):
    sec_per_hour = 3600
    sec_per_minute = 60
    # time ok. calculate the number of hours, and the number of
    # seconds left over after the hours are calculated.
    hour = "{:02}".format(int(timeSeconds/sec_per_hour))
    remain = timeSeconds - (float(hour)*sec_per_hour)
    # calculate the number of minutes left, and the number of
    # seconds left over after the hours are calculated
    minute = "{:02}".format(int(remain / sec_per_minute))
    remain = remain - float(minute) * sec_per_minute
    #Round it to the upper number
    sec = "{:02}".format(int(remain+0.5))
    timeLMST = str(hour) + ':' + str(minute) + ':' + str(sec)


    return timeLMST


def spldiff(x, y, h, n):
    #print(n)

    
    a=np.zeros(n)
    b=np.zeros(n)
    c=np.zeros(n)
    r=np.zeros(n)
    u=np.zeros(n)

    

    a[n-1] = 1.0
    b[0] = 2.0
    b[n-1] = 2.0
    c[n - 2] = 1.0
    r[0] = 3.0 * (y[1] - y[0])/h
    r[n-1] = 3.0 * (y[n-1] - y[n - 2])/h

    
    for i in range(n-1):
        if i<1:
            continue
        else:    
    
            a[i] = 1.0
            b[i] = 4.0
            c[i - 1] = 1.0
            r[i] = 3.0 * (y[i + 1] - y[i - 1])/h



    Dy= tridag(a, b, c, r, u, n)

    return Dy


def tridag(a, b, c, r, u, n):
    gam=np.zeros(n)
    
    
    if (b[0] == 0.):
        # If this happens then you should rewrite your equations as a set of order N − 1, with u2 trivially eliminated.

        raise ValueError("tridag: rewrite equations")
    else:
            
        bet = b[0]
        u[0] = r[0]/bet

        #Decomposition and forward substitution.
    for j in range(n):
        if j<1:
            continue
        else:   
            gam[j] = c[j - 1]/bet
            bet = b[j] - a[j] * gam[j]

            if (bet == 0.):
                raise ValueError("tridag failed")# Algorithm fails; see below.
                break
        

            u[j] = (r[j] - a[j] * u[j - 1])/bet

    j=n-2
    # Backsubstitution.
    while j>1:
        u[j] = u[j] - gam[j + 1] * u[j + 1]

        j=j-1
    #print(u)
    return u




def heat_cool_DER():
    #changes to out_dir1 to check the same folder where we are reading.
    for base, dirs, files in os.walk(out_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                
                sun = filename[25:30]
                #print("heat_cool_DER " + sun)
                    
                with open(out_dir1 + 'first_derivativesGTS_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'derivativesGTS_sol_' + sun+ '.dat','w') as output_file:
                    #file = input_file    
                    x=[]
                    y=[]
                    colD1y=[]
                    file=input_file.name
                    n = (len(open(file).readlines()))
                    
                    LMST=[]
                #  m=[]
                    for i in input_file:
                        
                        col=(i.split())

                        if len(col) < 3 or col[2] == -1.00:
                            continue
                        else:
                            
                            time=int(col[0]) #time
                            x.append(time)
                            q = str(col[1])
                            LMST.append(q)
                            
                            b=float(col[2]) #value
                            #v=str(col[2])
                            y.append(b)
                        #  m.append(v)

                    # if "-1.00" in m:
                    #     q=m.index("-1.00")
                    #     y.remove(-1.00)
                    #     x.pop(q)
                    #     n = ((len(open(file).readlines())))-1
                    # else:

                    
                    if len(x) > 2 and len(y) >2:           
                        
                        D1y =(spldiff(x,y,interval_1,n))
                        # colD1y.append(D1y)
                        # print(colD1y)
                        D2y =(spldiff(x,(D1y),interval_1,n))
                        D3y =(spldiff(x,(D2y),interval_1,n))
                        D4y =(spldiff(x,(D3y),interval_1,n))
                            # D2y=0
                            # D3y=0
                            # D4y=0

                                
                        for i in range(n):
                            #LMST=getHHMMSS(x[i])
                        # print(colD1y[i])
                            #print(y)
                                

                                    
                            output_file.write(str(x[i])+' '+str(LMST[i])+' '+str(y[i])+' '+str(D1y[i])+' '+str(D2y[i])+' '+str(D3y[i])+' '+str(D4y[i])+'\n')
                                            
                                        


def heat_cool_DER1(columns):
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(in_dir):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and  not file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                
                sun = filename[15:20]
                #print(sun)
                #Insert to pandas the file and in every iteration it will do this with evey file
                
                # We tell pandas some informatio the file, the separator, the type of object (normally object) and there is no header the PDS files has no header.
                df = pd.read_csv(in_dir + filename, sep=' ',error_bad_lines=False, dtype=object, header=None,encoding='latin1') #encoding = "ISO-8859-1"
                

                #seconds LMST mean_GTS lowest_Air_Temp mean_P mean_UV_A mean_UV_B mean_UV_C mean_UV_ABC mean_UV_D mean_UV_E      
                df2_final = df.to_csv(out_dir1 + 'first_derivativesGTS_sol_' + sun+ '.dat', sep='\t', index=False, columns=columns, header=None)

print("heat_cool_DER ... STARTING")
  
heat_cool_DER1([0,1,2])
heat_cool_DER()

print("heat_cool_DER ... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)



in_dir = "/data/PDS_Python/PDS_out_release/6_HEA_COO/Derivative_GTS/"

out_dir1 = "/data/PDS_Python/PDS_out_release/6_HEA_COO/splineGTS/"


yp1 = 1e+31
ypn = 1e+31
interval = 60
sec_day = 86400

def getHHMMSS(timeSeconds):
    sec_per_hour = 3600
    sec_per_minute = 60
    # time ok. calculate the number of hours, and the number of
    # seconds left over after the hours are calculated.
    hour = "{:02}".format(int(timeSeconds/sec_per_hour))
    remain = timeSeconds - (float(hour)*sec_per_hour)
    # calculate the number of minutes left, and the number of
    # seconds left over after the hours are calculated
    minute = "{:02}".format(int(remain / sec_per_minute))
    remain = remain - float(minute) * sec_per_minute
    #Round it to the upper number
    sec = "{:02}".format(int(remain+0.5))
    timeLMST = str(hour) + ':' + str(minute) + ':' + str(sec)


    return timeLMST



def calculate_spline(x,y,n,yp1,ypn):
    
    y2=np.zeros(n+1)
    u=np.zeros(n+1)
    if (yp1 > 0.99e30):
            y2[0] = 0.0
            u[0] = 0.0
    else:
        y2[0] = -0.5
        u[0] = (3./(x[1] - x[1])*((y[1] - y[0])/(x[1] - x[0]) - yp1))
    
    for i in range(1,n - 1):
        if i >= 1:
            sig = (x[i] - x[i - 1])/(x[i + 1] - x[i - 1])
            p = sig * y2[i - 1] + 2.0
            y2[i] = (sig - 1.0)/p
            u[i] = (6.0 * ((y[i + 1] - y[i])/(x[i + 1] - x[i])-(y[i] - y[i - 1]) / (x[i] - x[i - 1]))/(x[i + 1] - x[i - 1]) - sig * u[i - 1])/p
        else:
            continue
    
    if (ypn > 0.99e30):
        qn = 0.0
        un = 0.0
    else:
        qn = 0.5
        un = (3./(x[n] - x[n - 1]))*(ypn - (y[n] - y[n - 1])/(x[n] - x[n - 1]))
    
    y2[n] = (un - qn * u[n - 1])/(qn * y2[n - 1] + 1.0)
    for k in range(n-1,0,-1):

        y2[k] = y2[k] * y2[k + 1] + u[k]
    return (y2, x)

def calculate_splint(xa,ya,n,y2a,x):
    
    klo = 1
    khi = n
    while (khi - klo > 1):
        k = int(float(khi + klo)/2.0)

        if (xa[k-1] > x):
            khi = k

        else:   
            klo = k
       
    h = xa[khi-1] - xa[klo-1]
    if (h == 0.0):
        return -1

    a = (xa[khi-1] - x)/h
    b = (x - xa[klo-1])/h
    splint = a * ya[klo-1] + b * ya[khi-1] + ((a**3 - a) * y2a[klo-1] +(b**3 - b) * y2a[khi-1])*(h**2)/6.0
    return splint
    

def heat_cool_DER_GTS():
    #changes to out_dir1 to check the same folder where we are reading.

    for base, dirs, files in os.walk(out_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                
                sun = filename[39:44]
                #print(sun)
                    
                with open(out_dir1 + 'first_1_2_3_4_derivativeGTS_spline_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + '1_2_3_4_derivativeGTS_spline_sol_' + sun+ '.dat','w') as output_file:
                    #file = input_file    
                    file=input_file.name
                    n = (len(open(file).readlines()))
                    x=[]
                    y=[]
                    y1=[]
                    y2=[]
                    y3=[]
                    y4=[]
                    
                    for i in input_file:
                        
                        col=(i.split())

                        if len(col) < 6:
                            continue
                        else:
                            v=float(col[3])
                            if v != -1.00:
                            
                            
                                a=int(col[0]) #time
                                x.append(a)

                                LMST=getHHMMSS(a)
                                b = float(col[1])#value
                                y.append(b)

                                c=float(col[2]) #value1
                                y1.append(c)
                                
                                d=float(col[3]) #value1
                                y2.append(d)
                                
                                e=float(col[4]) #value1
                                y3.append(e)
                                
                                f=float(col[5]) #value1
                                y4.append(f)
                                
                    if len(x) > 2 and len(y) >2 and len(y1) >2 and len(y2) >2 and len(y3) >2 and len(y4) >2:           

                        D2y, x=(calculate_spline(x,y,n,yp1,ypn))
                        #print(D2y)
                        D2y1, seg=(calculate_spline(x,y1,n,yp1,ypn))
                        D2y2, k=(calculate_spline(x,y2,n,yp1,ypn))
                        #print(D2y2)
                        D2y3, k=(calculate_spline(x,y3,n,yp1,ypn))
                        D2y4, k=(calculate_spline(x,y4,n,yp1,ypn))
                        
                    size_max = (int(x[n-1]))

                    ii=seg[0] 
                    for i in range(99990): #99990 random number, just to unlimit the loop until the if from the bottom stops the loop
                        
                        splint1= calculate_splint(x,y,n,D2y,ii)
                        splint2= calculate_splint(x,y1,n,D2y1,ii)
                        splint3= calculate_splint(x,y2,n,D2y2,ii)
                        splint4= calculate_splint(x,y3,n,D2y3,ii)
                        splint5= calculate_splint(x,y4,n,D2y4,ii)

                        LMST=getHHMMSS(ii)
                        #We decide to round the splints in order to have better results in localExtrema

                        # splint1 = str(round(splint1, 2))
                        # # #print(splint1)
                        # splint2 = str(round(splint2, 6))
                        # splint3 = str(round(splint3, 11))
                        # splint4 = str(round(splint4, 16))
                        # splint5 = str(round(splint5, 20))

                        output_file.write(str(int(ii))+' '+str(LMST)+' '+str(splint1)+' '+str(splint2)+' '+str(splint3)+' '+str(splint4)+' '+str(splint5)+'\n')
                        ii=ii+interval
                        if ii > size_max:
                            break
      
                                    


def heat_cool_DER_GTS1(columns):
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(in_dir):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
               #not empty file 
                
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and  not file.startswith('f'):
                if os.stat(in_dir+file).st_size != 0:
                    
                    #Now we have the name of every file in order to insert it to pandas 
                    filename = file
                    # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                    
                    sun = filename[19:24]
                    #print(sun)
                    #print(sun)
                    #Insert to pandas the file and in every iteration it will do this with evey file
                    
                    # We tell pandas some informatio the file, the separator, the type of object (normally object) and there is no header the PDS files has no header.
                    df = pd.read_csv(in_dir + filename, sep=' ',error_bad_lines=False, dtype=object, header=None,encoding='latin1') #encoding = "ISO-8859-1"
                    

                    #seconds LMST mean_GTS lowest_Air_Temp mean_P mean_UV_A mean_UV_B mean_UV_C mean_UV_ABC mean_UV_D mean_UV_E      
                    df2_final = df.to_csv(out_dir1 + 'first_1_2_3_4_derivativeGTS_spline_sol_' + sun+ '.dat', sep='\t', index=False, columns=columns, header=None)

print("heat_cool_DER_GTS ... STARTING")
  
heat_cool_DER_GTS1([0,2,3,4,5,6])
heat_cool_DER_GTS()

print("heat_cool_DER_GTS ... COMPLETED")
    

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


in_dir = "/data/PDS_Python/PDS_out_release/6_HEA_COO/splineGTS/"

out_dir1 = "/data/PDS_Python/PDS_out_release/6_HEA_COO/localExtrema/"



interval = 60

def localExtrema(localExtrem, max_min, deriv1_GTS, deriv2_GTS, size):
    
    #Take comments out if you want to get the same result than Patricia, Taking less decimals so 0,0000007 would be 
        #interpreted as 0,0 and it would enter in the if (deriv1_GTS[i] * deriv1_GTS[i+1] <= 0.0):
    # for i in range(size):
    #     deriv1_GTS[i] = float(round(deriv1_GTS[i], 6))
    #     deriv2_GTS[i] = float(round(deriv2_GTS[i], 12))
    for i in range(size-1):
        
        max_min[i] = "-" #-1
        if (deriv1_GTS[i] * deriv1_GTS[i+1] <= 0.0):

            if (deriv2_GTS[i] > 0.0):
                localExtrem[i] = 1
                max_min[i] = "min" #-1000
                #return max_min, localExtrem
            
            if (deriv2_GTS[i] < 0.0):
                localExtrem[i] = 2
                max_min[i] = "max" # 1000
    return max_min, localExtrem

def inflexionPoints(inflexionPoint, deriv2_GTS, size):
    
    for i in range(size-1):
        inflexionPoint[i]=0
         
        if (deriv2_GTS[i] * deriv2_GTS[i+1] <= 0.0):

            inflexionPoint[i] = 1
    
    return inflexionPoint

def heat_cool_EXTREMA_GTS():
    #changes to out_dir1 to check the same folder where we are reading.

    for base, dirs, files in os.walk(out_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                
                sun = filename[43:48]
                #print(sun)
                    
                with open(out_dir1 + 'first_GTS_localExtrema_inflexionPoints_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'GTS_localExtrema_inflexionPoints_sol_' + sun+ '.dat','w') as output_file:
                    #file = input_file    
                    file=input_file.name
                    n = (len(open(file).readlines()))
                    seg=[]
                    LMST=[]
                    deriv1_GTS=[]
                    deriv2_GTS=[]
                    
                    for i in input_file:
                        
                        col=(i.split())

                        if len(col) < 4:
                            continue
                        else:
                            v=float(col[3])
                            if v != -1.00:
                            
                                a=int(col[0]) #time
                                seg.append(a)

                                b = str(col[1])#value
                                LMST.append(b)

                                c=float(col[2]) #value1
                                deriv1_GTS.append(c)
                                
                                
                                d=float(col[3]) #value1
                                deriv2_GTS.append(d)
                                
                    max_min = ["-"] * n #np.zeros(n)
                    inflexionPoint = np.zeros(n)
                    localExtrem = np.zeros(n)

                    max_min, localExtrem=localExtrema(localExtrem, max_min, deriv1_GTS,deriv2_GTS,n)
                    inflexionPoint=inflexionPoints(inflexionPoint, deriv2_GTS, n)
                    
                    
                    for i in range(n):
                        #Take coments out if you want to show it like Patricia but have the correct Maths done

                        # deriv1_GTS[i] = float(round(deriv1_GTS[i], 6))
                        # deriv2_GTS[i] = float(round(deriv2_GTS[i], 12))
                        
                        output_file.write(str(sun)+' '+str(seg[i])+' '+str(LMST[i])+' '+str((deriv1_GTS[i]))+' '+str((deriv2_GTS[i]))+' '+str(int(localExtrem[i]))+' '+str(max_min[i])+' '+str(int(inflexionPoint[i]))+'\n')
                                
    return 0

def heat_cool_EXTREMA_GTS1(columns):
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(in_dir):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and  not file.startswith('f'):
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[33:38]
                # We tell pandas some informatio the file, the separator, the type of object (normally object) and there is no header the PDS files has no header.
                df = pd.read_csv(in_dir + filename, sep=' ',error_bad_lines=False, dtype=object, header=None,encoding='latin1') #encoding = "ISO-8859-1"
                #seconds LMST mean_GTS lowest_Air_Temp mean_P mean_UV_A mean_UV_B mean_UV_C mean_UV_ABC mean_UV_D mean_UV_E      
                df2_final = df.to_csv(out_dir1 + 'first_GTS_localExtrema_inflexionPoints_sol_' + sun+ '.dat', sep='\t', index=False, columns=columns, header=None)

print("heat_cool_EXTREMA_GTS ... STARTING")

heat_cool_EXTREMA_GTS1([0,1,3,4])
heat_cool_EXTREMA_GTS()

    
print("heat_cool_EXTREMA_GTS ... COMPLETED")


ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)





in_dir = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_Means/"

out_dir1 = "/data/PDS_Python/PDS_out_release/7_AirGround_Tdiff/"

initreal = -1
initinteger = 0

def Ta_Tg_Difference():
        #changes to out_dir1 to check the same folder where we are reading.

    for base, dirs, files in os.walk(out_dir1):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and file.startswith('f'):
                
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                
                sun = filename[33:38]
                #print( "Ta_Tg_Difference " + sun)
                    
                with open(out_dir1 + 'first_difference_AirTemp_GTS_sol_' + sun+ '.dat','r') as input_file, open(out_dir1 + 'difference_AirTemp_GTS_sol_' + sun+ '.dat','w') as output_file:
                    #file = input_file    
                    file=input_file.name
                    n = (len(open(file).readlines()))
                    seg=[]
                    LMST=[]
                    GTS=[]
                    Ta=[]
                    difference=[]
                    
                    for i in input_file:
                        
                        col=(i.split())

                        if len(col) < 4:
                            continue
                        else:
                            
                            GTSS=float(col[2])
                            Taa=float(col[3]) #value1
                            

                            if (GTSS != -1 and Taa != -1):
                                
                                a=(col[0]) #time
                                
                                seg.append(a)

                                LMSTT = (col[1])#value
                                LMST.append(LMSTT)

                                GTSS=float(col[2]) #value1
                                GTS.append(GTSS)
                                
                                Taa=float(col[3]) #value1
                                Ta.append(Taa)
                                
                                diff = Taa - GTSS
                                difference.append(diff)
                            else:
                                a=(col[0]) #time
                                
                                seg.append(a)

                                LMSTT = (col[1])#value
                                LMST.append(LMSTT)

                                GTSS=-1.00 #value1
                                GTS.append(GTSS)
                                
                                Taa=-1.00 #value1
                                Ta.append(Taa)
                                
                                diff = -1.00
                                difference.append(diff)
                                
                            
                    for i in range(len(difference)):
                        
                        output_file.write(str(seg[i])+' '+str(LMST[i])+' '+str(Ta[i])+' '+str((GTS[i]))+' '+str((difference[i]))+'\n')
                                

def Ta_Tg_Difference1(columns):
    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(in_dir):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
                
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat') and  not file.startswith('f'):
                
                #Now we have the name of every file in order to insert it to pandas 
                filename = file
                # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                sun = filename[37:42]
                if os.stat(in_dir + 'means_RH_GTS_lowestTemp_Press_UV_sol_' + sun+ '.dat').st_size != 0:
                    
                    # We tell pandas some informatio the file, the separator, the type of object (normally object) and there is no header the PDS files has no header.
                    df = pd.read_csv(in_dir + filename, sep=' ',error_bad_lines=False, dtype=object, header=None,encoding='latin1') #encoding = "ISO-8859-1"
                    #seconds LMST mean_GTS lowest_Air_Temp mean_P mean_UV_A mean_UV_B mean_UV_C mean_UV_ABC mean_UV_D mean_UV_E      
                    df2_final = df.to_csv(out_dir1 + 'first_difference_AirTemp_GTS_sol_' + sun+ '.dat', sep='\t', index=False, columns=columns, header=None)

    
print("Ta_Tg_Difference ... STARTING")

Ta_Tg_Difference1([0,1,4,6])
Ta_Tg_Difference()

    
print("Ta_Tg_Difference ... COMPLETED")
    

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


in_dir = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"
out_dir = "/data/PDS_Python/PDS_out_release/9_VMR_GTS/VMR/"

def timestamp_fixed(timestamp):
    length = len(str(timestamp))
    if length == 1:
        time = str(timestamp)
        time_vmr = '00:00:0' + time
        return time_vmr
    elif length == 2:
        time = str(timestamp)
        time_vmr = '00:00:' + time
        return time_vmr
    elif length == 3:
        time = str(timestamp)
        time_vmr = '00:0' + time[0:1] + ':' + time[1:3]
        return time_vmr
    elif length == 4:
        time = str(timestamp)
        time_vmr = '00:' + time[0:2] + ':' + time[2:4]
        return time_vmr
    elif length == 5:
        time = str(timestamp)
        time_vmr = '0' + time[0:1] + ':' + time[1:3] + ':' + time[3:5]
        return time_vmr
    elif length == 6:
        time = str(timestamp)
        time_vmr = time[0:2] + ':' + time[2:4] + ':' + time[4:6]
        return time_vmr


def VMR_Max():
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat'):
                if os.stat(in_dir+file).st_size != 0:
                    #Now we have the name of every file in order to insert it to pandas 
                    filename = file
                    # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                    sun = filename[3:8]

                    with open(in_dir + 'MD_'+ sun + '.dat', 'r+') as input_file, open(out_dir + 'VMR_' + sun + '.dat', 'w+') as output_file:


                        #file = input_file    
                        file=input_file.name
                        vmr_max = 0.0
                        vmr_aux = 0.0
                        vmr_max_2 = 0.0
                        vmr_aux_2 = 0.0
                        vmr_max_3 = 0.0
                        vmr_aux_3 = 0.0
                        vmr_max_4 = 0.0
                        vmr_aux_4 = 0.0
                        vmr_max_5 = 0.0
                        vmr_aux_5 = 0.0
                        vmr_max_6 = 0.0
                        vmr_aux_6 = 0.0
                        vmr_max_7 = 0.0
                        vmr_aux_7 = 0.0
                        vmr_max_8 = 0.0
                        vmr_aux_8 = 0.0
                        vmr_max_9 = 0.0
                        vmr_aux_9 = 0.0
                        vmr_max_10 = 0.0
                        vmr_aux_10 = 0.0
                        vmr_max_11 = 0.0
                        vmr_aux_11 = 0.0
                        vmr_max_12 = 0.0
                        vmr_aux_12 = 0.0
                        timestamp_vmr_1 = str("0")
                        timestamp_vmr_2 = str("0")
                        timestamp_vmr_3 = str("0")
                        timestamp_vmr_4 = str("0")
                        timestamp_vmr_5 = str("0")
                        timestamp_vmr_6 = str("0")
                        timestamp_vmr_7 = str("0")
                        timestamp_vmr_8 = str("0")
                        timestamp_vmr_9 = str("0")
                        timestamp_vmr_10 = str("0")
                        timestamp_vmr_11= str("0")
                        timestamp_vmr_12= str("0")
                        timestamp_vmr= str("0")
                        #vmr_max = '-1'

                        for line in input_file:
                            col = line.split()
                            timestamp_hour = str(col[1][0:2])
                            timestamp_min = str(col[1][3:5])
                            timestamp_seg = str(col[1][6:8])
                            timestamp = timestamp_hour + timestamp_min + timestamp_seg
                            timestamp = int(timestamp)
                            if (col[4]) == 'NULL' or (col[4]) == 'UNK':
                                vmr_aux = 0.0
                            else:
                            
                                vmr_aux = float(col[4])
                                vmr_aux_2 = float(col[4])
                                vmr_aux_3 = float(col[4])
                                vmr_aux_4 = float(col[4])
                                vmr_aux_5 = float(col[4])
                                vmr_aux_6 = float(col[4])
                                vmr_aux_7 = float(col[4])
                                vmr_aux_8 = float(col[4])
                                vmr_aux_9 = float(col[4])
                                vmr_aux_10 = float(col[4])
                                vmr_aux_11 = float(col[4])
                                vmr_aux_12 = float(col[4])

                            if timestamp > 210000 and timestamp < 220000:
                                if vmr_aux_2 > vmr_max_2:
                                    vmr_max_2 = vmr_aux_2
                                    timestamp_vmr_2 = timestamp

                            if timestamp > 220000 and timestamp < 230000:
                                if vmr_aux > vmr_max:
                                    vmr_max = vmr_aux
                                    timestamp_vmr = timestamp

                        
                            if timestamp > 230000 and timestamp <= 235959:
                                if vmr_aux_3 > vmr_max_3:
                                    vmr_max_3 = vmr_aux_3
                                    timestamp_vmr_3 = timestamp

                            if timestamp > 0000 and timestamp < 10000:
                                if vmr_aux_4 > vmr_max_4:
                                    vmr_max_4 = vmr_aux_4
                                    timestamp_vmr_4 = timestamp


                            if timestamp > 10000 and timestamp < 20000:
                                if vmr_aux_5 > vmr_max_5:
                                    vmr_max_5 = vmr_aux_5
                                    timestamp_vmr_5 = timestamp

                            
                            if timestamp > 20000 and timestamp < 30000:
                                if vmr_aux_6 > vmr_max_6:
                                    vmr_max_6 = vmr_aux_6
                                    timestamp_vmr_6 = timestamp
                                    

                            if timestamp > 30000 and timestamp < 40000:
                                if vmr_aux_7 > vmr_max_7:
                                    vmr_max_7 = vmr_aux_7
                                    timestamp_vmr_7 = timestamp


                            if timestamp > 40000 and timestamp < 50000:
                                if vmr_aux_8 > vmr_max_8:
                                    vmr_max_8 = vmr_aux_8
                                    timestamp_vmr_8 = timestamp
                            
                            
                            if timestamp > 50000 and timestamp < 60000:
                                if vmr_aux_9 > vmr_max_9:
                                    vmr_max_9 = vmr_aux_9
                                    timestamp_vmr_9 = timestamp


                            if timestamp > 60000 and timestamp < 70000:
                                if vmr_aux_10 > vmr_max_10:
                                    vmr_max_10 = vmr_aux_10
                                    timestamp_vmr_10 = timestamp


                            if timestamp > 70000 and timestamp < 80000:
                                if vmr_aux_11 > vmr_max_11:
                                    vmr_max_11 = vmr_aux_11
                                    timestamp_vmr_11 = timestamp


                            if timestamp > 80000 and timestamp < 90000:
                                if vmr_aux_12 > vmr_max_12:
                                    vmr_max_12 = vmr_aux_12
                                    timestamp_vmr_12 = timestamp


                        time_vmr = str("-")
                        time_vmr = timestamp_fixed(timestamp_vmr)
                        time_vmr_2 = timestamp_fixed(timestamp_vmr_2)
                        time_vmr_3 = timestamp_fixed(timestamp_vmr_3)
                        time_vmr_4 = timestamp_fixed(timestamp_vmr_4)
                        time_vmr_5 = timestamp_fixed(timestamp_vmr_5)
                        time_vmr_6 = timestamp_fixed(timestamp_vmr_6)
                        time_vmr_7 = timestamp_fixed(timestamp_vmr_7)
                        time_vmr_8 = timestamp_fixed(timestamp_vmr_8)
                        time_vmr_9 = timestamp_fixed(timestamp_vmr_9)
                        time_vmr_10 = timestamp_fixed(timestamp_vmr_10)
                        time_vmr_11 = timestamp_fixed(timestamp_vmr_11)
                        time_vmr_12 = timestamp_fixed(timestamp_vmr_12)

                        if vmr_max == 0.0:
                                output_file.write('-1' +  ' ' + '0.0' +  ' ' + '-1' + ' ' + '0.0' +  ' ' + '-1' + ' ' + '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' +  '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' +  ' ' +  '0.0' +  ' ' + '-1' + '\n')
                        else:
                            output_file.write(str(vmr_max_2) + ' ' + str(time_vmr_2) + ' ' + str(vmr_max) + ' ' + str(time_vmr) +  ' ' + str(vmr_max_3) + ' ' + str(time_vmr_3) + ' ' + str(vmr_max_4) + ' ' + str(time_vmr_4) + 
                            ' ' + str(vmr_max_5) + ' ' + str(time_vmr_5) + ' ' + str(vmr_max_6) + ' ' + str(time_vmr_6) +  ' ' + str(vmr_max_7) + ' ' + str(time_vmr_7) +  ' ' + str(vmr_max_8) + ' ' + str(time_vmr_8) +  ' ' + str(vmr_max_9) + ' ' + str(time_vmr_9) +
                            ' ' + str(vmr_max_10) + ' ' + str(time_vmr_10) + ' ' + str(vmr_max_11) + ' ' + str(time_vmr_11) + ' ' + str(vmr_max_12) + ' ' + str(time_vmr_12) + '\n')

print("VMR_Max ... STARTING")

VMR_Max()

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)

print("VMR_Max ... COMPLETED")


in_dir = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"
in_dir2 = "/data/PDS_Python/PDS_out_release/9_VMR_GTS/VMR/"

out_dir = "/data/PDS_Python/PDS_out_release/9_VMR_GTS/VMR_GTS_P_MAX/"

def HourFromTimestamp(timestamp):
    if timestamp == '-1':
        return '-1'
    else:
        hour = str(timestamp[0:2])
        return hour

def VMR_GTS_P_MAX():
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #make sure that we are only working with the correct files ending with the termination ".dat"
            if file.endswith('.dat'):
                if os.stat(in_dir+file).st_size != 0:
                    #Now we have the name of every file in order to insert it to pandas 
                    filename = file
                    # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                    sun = filename[3:8]
                    #print(sun)

                    with open(in_dir + 'MD_'+ sun + '.dat', 'r+') as input_file, open(out_dir + 'VMR_GTS_P_MAX_' + sun + '.dat', 'w') as output_file:
                        vmr_original = pd.read_csv(in_dir2 + 'VMR_' + sun+'.dat', sep=' ', dtype=object, header=None)
                        vmr_max_21 = str(vmr_original[0].tolist()[0])
                        vmr_max_22 = str(vmr_original[2].tolist()[0])
                        vmr_max_23 = str(vmr_original[4].tolist()[0])
                        vmr_max_24 = str(vmr_original[6].tolist()[0])
                        vmr_max_01 = str(vmr_original[8].tolist()[0])
                        vmr_max_02 = str(vmr_original[10].tolist()[0])
                        vmr_max_03 = str(vmr_original[12].tolist()[0])
                        vmr_max_04 = str(vmr_original[14].tolist()[0])
                        vmr_max_05 = str(vmr_original[16].tolist()[0])
                        vmr_max_06 = str(vmr_original[18].tolist()[0])
                        vmr_max_07 = str(vmr_original[20].tolist()[0])
                        vmr_max_08 = str(vmr_original[22].tolist()[0])

                        timestamp_21 = str(vmr_original[1].tolist()[0])
                        timestamp_22 = str(vmr_original[3].tolist()[0])
                        timestamp_23 = str(vmr_original[5].tolist()[0])
                        timestamp_24 = str(vmr_original[7].tolist()[0])
                        timestamp_01 = str(vmr_original[9].tolist()[0])
                        timestamp_02 = str(vmr_original[11].tolist()[0])
                        timestamp_03 = str(vmr_original[13].tolist()[0])
                        timestamp_04 = str(vmr_original[15].tolist()[0])
                        timestamp_05 = str(vmr_original[17].tolist()[0])
                        timestamp_06 = str(vmr_original[19].tolist()[0])
                        timestamp_07 = str(vmr_original[21].tolist()[0])
                        timestamp_08 = str(vmr_original[23].tolist()[0])

                        hour_21 = HourFromTimestamp(timestamp_21)
                        hour_22 = HourFromTimestamp(timestamp_22)
                        hour_23 = HourFromTimestamp(timestamp_23)
                        hour_24 = HourFromTimestamp(timestamp_24)
                        hour_01 = HourFromTimestamp(timestamp_01)
                        hour_02 = HourFromTimestamp(timestamp_02)
                        hour_03 = HourFromTimestamp(timestamp_03)
                        hour_04 = HourFromTimestamp(timestamp_04)
                        hour_05 = HourFromTimestamp(timestamp_05)
                        hour_06 = HourFromTimestamp(timestamp_06)
                        hour_07 = HourFromTimestamp(timestamp_07)
                        hour_08 = HourFromTimestamp(timestamp_08)
                        #print(timestamp_08)
                            

                        #col_vmr_row = vmr_original.split()
                        #print(vmr_max_01)

                        #n = (len(open(file).readlines()))
                        avg_n_21 = 0
                        avg_n_22 = 0
                        avg_n_23 = 0
                        avg_n_24 = 0
                        avg_n_01 = 0
                        avg_n_02 = 0
                        avg_n_03 = 0
                        avg_n_04 = 0
                        avg_n_05 = 0
                        avg_n_06 = 0
                        avg_n_07 = 0
                        avg_n_08 = 0

                        avg_n_p_21 = 0
                        avg_n_p_22 = 0
                        avg_n_p_23 = 0
                        avg_n_p_24 = 0
                        avg_n_p_01 = 0
                        avg_n_p_02 = 0
                        avg_n_p_03 = 0
                        avg_n_p_04 = 0
                        avg_n_p_05 = 0
                        avg_n_p_06 = 0
                        avg_n_p_07 = 0
                        avg_n_p_08 = 0

                        avg_gts_21 = 0
                        avg_gts_22 = 0
                        avg_gts_23 = 0
                        avg_gts_24 = 0
                        avg_gts_01 = 0
                        avg_gts_02 = 0
                        avg_gts_03 = 0
                        avg_gts_04 = 0
                        avg_gts_05 = 0
                        avg_gts_06 = 0
                        avg_gts_07 = 0
                        avg_gts_08 = 0

                        avg_p_21 = 0
                        avg_p_22 = 0
                        avg_p_23 = 0
                        avg_p_24 = 0
                        avg_p_01 = 0
                        avg_p_02 = 0
                        avg_p_03 = 0
                        avg_p_04 = 0
                        avg_p_05 = 0
                        avg_p_06 = 0
                        avg_p_07 = 0
                        avg_p_08 = 0

                        avg_p_final_21 = 0
                        avg_p_final_22 = 0
                        avg_p_final_23 = 0
                        avg_p_final_24 = 0
                        avg_p_final_01 = 0
                        avg_p_final_02 = 0
                        avg_p_final_03 = 0
                        avg_p_final_04 = 0
                        avg_p_final_05 = 0
                        avg_p_final_06 = 0
                        avg_p_final_07 = 0
                        avg_p_final_08 = 0

                        avg_gts_final_21 = 0
                        avg_gts_final_22 = 0
                        avg_gts_final_23 = 0
                        avg_gts_final_24 = 0
                        avg_gts_final_01 = 0
                        avg_gts_final_02 = 0
                        avg_gts_final_03 = 0
                        avg_gts_final_04 = 0
                        avg_gts_final_05 = 0
                        avg_gts_final_06 = 0
                        avg_gts_final_07 = 0
                        avg_gts_final_08 = 0
                        file=input_file.name
                        for line in input_file:
                            col = line.split()
                            #print(col)
                            gts = str(col[6])
                            pressure = str(col[5])
                            hour = str(col[1])[0:2]

                            if gts != '-1.00' and hour == hour_21:
                                avg_gts_21 = avg_gts_21 + float(gts)
                                avg_n_21 = avg_n_21 + 1

                            if pressure != '-1.00' and hour == hour_21:
                                avg_p_21 = avg_p_21 + float(pressure)
                                avg_n_p_21 = avg_n_p_21 + 1

                            if gts != '-1.00' and hour == hour_22:
                                avg_gts_22 = avg_gts_22 + float(gts)
                                avg_n_22 = avg_n_22 + 1

                            if pressure != '-1.00' and hour == hour_22:
                                avg_p_22 = avg_p_22 + float(pressure)
                                avg_n_p_22 = avg_n_p_22 + 1

                            if gts != '-1.00' and hour == hour_23:
                                avg_gts_23 = avg_gts_23 + float(gts)
                                avg_n_23 = avg_n_23 + 1

                            if pressure != '-1.00' and hour == hour_23:
                                avg_p_23 = avg_p_23 + float(pressure)
                                avg_n_p_23 = avg_n_p_23 + 1

                            if gts != '-1.00' and hour == hour_24:
                                avg_gts_24 = avg_gts_24 + float(gts)
                                avg_n_24 = avg_n_24 + 1

                            if pressure != '-1.00' and hour == hour_24:
                                avg_p_24 = avg_p_24 + float(pressure)
                                avg_n_p_24 = avg_n_p_24 + 1

                            if gts != '-1.00' and hour == hour_01:
                                avg_gts_01 = avg_gts_01 + float(gts)
                                avg_n_01 = avg_n_01 + 1

                            if pressure != '-1.00' and hour == hour_01:
                                avg_p_01 = avg_p_01 + float(pressure)
                                avg_n_p_01 = avg_n_p_01 + 1

                            if gts != '-1.00' and hour == hour_02:
                                avg_gts_02 = avg_gts_02 + float(gts)
                                avg_n_02 = avg_n_02 + 1

                            if pressure != '-1.00' and hour == hour_02:
                                avg_p_02 = avg_p_02 + float(pressure)
                                avg_n_p_02 = avg_n_p_02 + 1

                            if gts != '-1.00' and hour == hour_03:
                                avg_gts_03 = avg_gts_03 + float(gts)
                                avg_n_03 = avg_n_03 + 1

                            if pressure != '-1.00' and hour == hour_03:
                                avg_p_03 = avg_p_03 + float(pressure)
                                avg_n_p_03 = avg_n_p_03 + 1

                            if gts != '-1.00' and hour == hour_04:
                                avg_gts_04 = avg_gts_04 + float(gts)
                                avg_n_04 = avg_n_04 + 1

                            if pressure != '-1.00' and hour == hour_04:
                                avg_p_04 = avg_p_04 + float(pressure)
                                avg_n_p_04 = avg_n_p_04 + 1

                            if gts != '-1.00' and hour == hour_05:
                                avg_gts_05 = avg_gts_05 + float(gts)
                                avg_n_05 = avg_n_05 + 1

                            if pressure != '-1.00' and hour == hour_05:
                                avg_p_05 = avg_p_05 + float(pressure)
                                avg_n_p_05 = avg_n_p_05 + 1

                            if gts != '-1.00' and hour == hour_06:
                                avg_gts_06 = avg_gts_06 + float(gts)
                                avg_n_06 = avg_n_06 + 1

                            if pressure != '-1.00' and hour == hour_06:
                                avg_p_06 = avg_p_06 + float(pressure)
                                avg_n_p_06 = avg_n_p_06 + 1

                            if gts != '-1.00' and hour == hour_07:
                                avg_gts_07 = avg_gts_07 + float(gts)
                                avg_n_07 = avg_n_07 + 1

                            if pressure != '-1.00' and hour == hour_07:
                                avg_p_07 = avg_p_07 + float(pressure)
                                avg_n_p_07 = avg_n_p_07 + 1

                            if gts != '-1.00' and hour == hour_08:
                                avg_gts_08 = avg_gts_08 + float(gts)
                                avg_n_08 = avg_n_08 + 1

                            if pressure != '-1.00' and hour == hour_08:
                                avg_p_08 = avg_p_08 + float(pressure)
                                avg_n_p_08 = avg_n_p_08 + 1

                        if avg_n_21 != 0:
                            avg_gts_final_21 = avg_gts_21 / avg_n_21
                        else:
                            avg_gts_final_21 = 0.0
                        
                        if avg_n_p_21 != 0:
                            avg_p_final_21 = avg_p_21 / avg_n_p_21
                        else:
                            avg_p_final_21 = 0.0

                        if avg_n_22 != 0:
                            avg_gts_final_22 = avg_gts_22 / avg_n_22
                        else:
                            avg_gts_final_22 = 0.0
                        
                        if avg_n_p_22 != 0:
                            avg_p_final_22 = avg_p_22 / avg_n_p_22
                        else:
                            avg_p_final_22 = 0.0

                        if avg_n_23 != 0:
                            avg_gts_final_23 = avg_gts_23 / avg_n_23
                        else:
                            avg_gts_final_23 = 0.0
                        
                        if avg_n_p_23 != 0:
                            avg_p_final_23 = avg_p_23 / avg_n_p_23
                        else:
                            avg_p_final_23 = 0.0

                        if avg_n_24 != 0:
                            avg_gts_final_24 = avg_gts_24 / avg_n_24
                        else:
                            avg_gts_final_24 = 0.0
                        
                        if avg_n_p_24 != 0:
                            avg_p_final_24 = avg_p_24 / avg_n_p_24
                        else:
                            avg_p_final_24 = 0.0

                        if avg_n_01 != 0:
                            avg_gts_final_01 = avg_gts_01 / avg_n_01
                        else:
                            avg_gts_final_01 = 0.0
                        
                        if avg_n_p_01 != 0:
                            avg_p_final_01 = avg_p_01 / avg_n_p_01
                        else:
                            avg_p_final_01 = 0.0

                        if avg_n_02 != 0:
                            avg_gts_final_02 = avg_gts_02 / avg_n_02
                        else:
                            avg_gts_final_02 = 0.0
                        
                        if avg_n_p_02 != 0:
                            avg_p_final_02 = avg_p_02 / avg_n_p_02
                        else:
                            avg_p_final_02 = 0.0

                        if avg_n_03 != 0:
                            avg_gts_final_03 = avg_gts_03 / avg_n_03
                        else:
                            avg_gts_final_03 = 0.0
                        
                        if avg_n_p_03 != 0:
                            avg_p_final_03 = avg_p_03 / avg_n_p_03
                        else:
                            avg_p_final_03 = 0.0

                        if avg_n_04 != 0:
                            avg_gts_final_04 = avg_gts_04 / avg_n_04
                        else:
                            avg_gts_final_04 = 0.0
                        
                        if avg_n_p_04 != 0:
                            avg_p_final_04 = avg_p_04 / avg_n_p_04
                        else:
                            avg_p_final_04 = 0.0

                        if avg_n_05 != 0:
                            avg_gts_final_05 = avg_gts_05 / avg_n_05
                        else:
                            avg_gts_final_05 = 0.0
                        
                        if avg_n_p_05 != 0:
                            avg_p_final_05 = avg_p_05 / avg_n_p_05
                        else:
                            avg_p_final_05 = 0.0

                        if avg_n_06 != 0:
                            avg_gts_final_06 = avg_gts_06 / avg_n_06
                        else:
                            avg_gts_final_06 = 0.0
                        
                        if avg_n_p_06 != 0:
                            avg_p_final_06 = avg_p_06 / avg_n_p_06
                        else:
                            avg_p_final_06 = 0.0

                        if avg_n_07 != 0:
                            avg_gts_final_07 = avg_gts_07 / avg_n_07
                        else:
                            avg_gts_final_07 = 0.0
                        
                        if avg_n_p_07 != 0:
                            avg_p_final_07 = avg_p_07 / avg_n_p_07
                        else:
                            avg_p_final_07 = 0.0

                        if avg_n_08 != 0:
                            avg_gts_final_08 = avg_gts_08 / avg_n_08
                        else:
                            avg_gts_final_08 = 0.0
                        
                        if avg_n_p_08 != 0:
                            avg_p_final_08 = avg_p_08 / avg_n_p_08
                        else:
                            avg_p_final_08 = 0.0

                        avg_gts_final_21 = round(float(avg_gts_final_21), 3)
                        avg_p_final_21 = round(float(avg_p_final_21), 3)
                        


                        output_file.write(vmr_max_21 + '   ' + timestamp_21 + '   ' + str(avg_gts_final_21) + '   ' + str(avg_p_final_21) + '   ' + vmr_max_22 + '   ' + timestamp_22 + '   ' + str(avg_gts_final_22) + '   ' + str(avg_p_final_22) + '   ' + vmr_max_23 +
                        '   ' + timestamp_23 + '   ' + str(avg_gts_final_23) + '   ' + str(avg_p_final_23) +  '   ' + vmr_max_24 + '   ' + timestamp_24 + '   ' + str(avg_gts_final_24) + '   ' + str(avg_p_final_24) + '   ' + vmr_max_01 + '   ' + timestamp_01 + '   ' + str(avg_gts_final_01) + '   ' + str(avg_p_final_01) + 
                        '   ' + vmr_max_02 + '   ' + timestamp_02 + '   ' + str(avg_gts_final_02) + '   ' + str(avg_p_final_02) +  '   ' + vmr_max_03 + '   ' + timestamp_03 + '   ' + str(avg_gts_final_03) + '   ' + str(avg_p_final_03) +  '   ' + vmr_max_04 + '   ' + timestamp_04 + '   ' + str(avg_gts_final_04) + '   ' + str(avg_p_final_04) + 
                        '   ' + vmr_max_05 + '   ' + timestamp_05 + '   ' + str(avg_gts_final_05) + '   ' + str(avg_p_final_05) + '   ' + vmr_max_06 + '   ' + timestamp_06 + '   ' + str(avg_gts_final_06) + '   ' + str(avg_p_final_06) + '   ' + vmr_max_07 + '   ' + timestamp_07 + '   ' + str(avg_gts_final_07) + '   ' + str(avg_p_final_07) + 
                        '   ' + vmr_max_08 + '   ' + timestamp_08 + '   ' + str(avg_gts_final_08) + '   ' + str(avg_p_final_08))

print("VMR_GTS_P_MAX ... STARTING")

VMR_GTS_P_MAX()


ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)

print("VMR_GTS_P_MAX ... COMPLETED")


# path where I will put the results
in_dir = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"
out_dir = "/data/PDS_Python/PDS_out_release/10_ATS/Read_Global/"

#NV path
# path where I will put the results
in_dir2 = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/NV_CLEAN/"

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print("read_clean_MD_NV... STARTING")

print(st)


def read_clean_MD_NV():
    
    # Iteration on the MD Files Directory
    for base, dirs, filesMD in os.walk(in_dir):
        for fileMD in filesMD:
            #print file
                # Checking the file extension
            if str(fileMD).endswith('.dat'):
                if os.stat(in_dir+fileMD).st_size != 0:
                    
                    #if file.find(file_md) != -1.00:
                    md_file = fileMD
                    
                    sunMD = md_file[3:8]
                    for base, dirs, filesNV in os.walk(in_dir2):
                        for fileNV in filesNV:
                            if str(fileNV).endswith('.dat'):
                                                
                                if os.stat(in_dir2+fileNV).st_size != 0:
        
                            
                                    nv_file = fileNV
                                    
                                    sunNV = nv_file[3:8]

                                    if sunMD == sunNV:
                                        w_file = "GBL_"+sunMD+".dat"
                                        #print(sunMD)

                                    
                            
                                        with open(in_dir + md_file,'r') as textfile1, open(in_dir2 + nv_file,'r') as textfile2, open(out_dir + w_file, 'w') as output_file:
                                            output_file.truncate()
                                            for x,y in zip(textfile1,textfile2):
                                                x = x.split()
                                                y = y.split()
                                                
                                                if len(y)<9 or len(x)<9:
                                                    continue
                                                else:
                                                    output_file.write(y[0].strip('\"').replace('UNK','-1') + ' ' + y[1].strip('\"').replace('UNK','-1') + ' ' + y[10].strip('\"').replace('UNK','-1') + ' ' + y[14].strip('\"').replace('UNK','-1') + ' ' + y[15].strip('\"').replace('UNK','-1') +
                                                                ' ' + y[16].strip('\"').replace('UNK','-1') + ' ' + y[17].strip('\"').replace('UNK','-1') + ' ' + x[14].strip('\"').replace('UNK','-1') + ' ' + y[12].strip('\"').replace('UNK','-1') + ' ' + y[18].strip('\"').replace('UNK','-1') +
                                                                ' ' + y[19].strip('\"').replace('UNK','-1') + ' ' + x[15].strip('\"').replace('UNK','-1') +'\n')

    #[1]sckl [2]LMST [3]ATS_Boom1_Temp_Base [4]ATS_Boom1_Temp_Intermediate [5]ATS_Boom1_Temp_Tip [6]Pressure_1 [7]Pressure_2 [8]Horizontal_Wind_Speed [9]ATS_Boom2_Temp_Base [10]ATS_Boom2_Temp_Intermediate [11]ATS_Boom2_Temp_Tip [12]Wind_Direction\n')

read_clean_MD_NV()

print("read_clean_MD_NV... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


in_dir = "/data/PDS_Python/PDS_out_release/10_ATS/Read_Global/"
out_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom1_Calculations/"
#NV path
# path where I will put the results

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print("ATS_Boom1... STARTING")

print(st)


def ATS_Boom1():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.dat'):
                #if file.find(file_md) != -1.00:
                filename = file
                
                sun = filename[4:9]
                                
                w_file = "ATS_Boom1_m_tf_" + sun + ".dat"
                with open(in_dir + filename,'r') as input_file, open(out_dir + w_file, 'w') as output_file:
                    output_file.truncate()
                    for lines in input_file:
                        column = lines.split()
                        
                        if len(column)<3:
                            continue
                        else:
                            
                            Tb = float(column[2])
                            TLn = float(column[3])
                            TLa = float(column[4])
                            a = Tb - TLn
                            b = TLa - Tb
                            c = TLn - TLa
                            n = 4
                            delta = 0.01

                            if (a * c) > 0:
                                x = c / (a+c)
                                m = delta
                                while x * (np.cosh(m) - 1.0) < (np.cosh (m * (1 - 1 / (n + 0.0))) - 1.0):
                                    m = m + delta

                                m = m - delta
                                    
                            else:
                                m = 1.8
                                Am = (np.cosh(m) - 1.0) / (np.cosh (m * (1-1 / (n + 0.0))) - 1.0)
                                Tb = (1 - Am) * TLa + TLn * Am

                            if m > 0:
                                Tf = (TLa - Tb * np.cosh(0.0) / np.cosh(m)) / (1 - np.cosh(0.0) / np.cosh(m))
                            else:
                                Tf = "0.0"
                            output_file.write(column[0].strip('\"').replace('UNK','-1') + '  ' + column[1].strip('\"').replace('UNK','-1') + '  ' + column[2].strip(' \"').replace('UNK','-1') + '  ' + column[3].strip(' \"').replace('UNK','-1') + '  ' + column[4].strip(' \"').replace('UNK','-1') +
                                        '  ' + column[5].strip(' \"').replace('UNK','-1') + '  ' + column[6].strip(' \"').replace('UNK','-1') + '  ' + column[7].strip(' \"').replace('UNK','-1') + '  ' + str(m) + '  ' + str(Tf) + '\n')

#[1]sckl [2]LMST [3]ATS_Boom1_Temp_Base [4]ATS_Boom1_Temp_Intermediate [5]ATS_Boom1_Temp_Tip [6]Pressure_1 [7]Pressure_2 [8]Horizontal_Wind_Speed [9]ATS_Boom2_Temp_Base [10]ATS_Boom2_Temp_Intermediate [11]ATS_Boom2_Temp_Tip [12]Wind_Direction\n')

ATS_Boom1()

print("ATS_Boom1... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


in_dir = "/data/PDS_Python/PDS_out_release/10_ATS/Read_Global/"
out_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom2_Calculations/"
#NV path
# path where I will put the results

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print("ATS_Boom2... STARTING")

print(st)


def ATS_Boom2():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.dat'):
                #if file.find(file_md) != -1.00:
                filename = file
                
                sun = filename[4:9]
                #print(sun)
                                
                w_file = "ATS_Boom2_m_tf_" + sun + ".dat"
                with open(in_dir + filename,'r') as input_file, open(out_dir + w_file, 'w') as output_file:
                    output_file.truncate()
                    for lines in input_file:
                        column = lines.split()
                        
                        if len(column)<9:
                            continue
                        else:
                            
                            Tb = float(column[8])
                            TLn = float(column[9])
                            TLa = float(column[10])
                            a = Tb - TLn
                            b = TLa - Tb
                            c = TLn - TLa
                            n = 4
                            delta = 0.01

                            if (a * c) > 0:
                                x = c / (a+c)
                                m = delta
                                while x * (np.cosh(m) - 1.0) < (np.cosh (m * (1 - 1 / (n + 0.0))) - 1.0):
                                    m = m + delta

                                m = m - delta
                                    
                            else:
                                m = 1.8
                                Am = (np.cosh(m) - 1.0) / (np.cosh (m * (1-1 / (n + 0.0))) - 1.0)
                                Tb = (1 - Am) * TLa + TLn * Am

                            if m > 0:
                                Tf = (TLa - Tb * np.cosh(0.0) / np.cosh(m)) / (1 - np.cosh(0.0) / np.cosh(m))
                            else:
                                Tf = "0.0"
                            # Write the output file
                            m = round(float(m), 3)
                            Tf = round(float(Tf), 3)
                            

                            output_file.write(column[0].strip('\"').replace('UNK','-1') + '  ' + column[1].strip('\"').replace('UNK','-1') + '  ' + column[8].strip(' \"').replace('UNK','-1') + '  ' + column[9].strip(' \"').replace('UNK','-1') + '  ' + column[10].strip(' \"').replace('UNK','-1') +
                                            '  ' + column[5].strip(' \"').replace('UNK','-1') + '  ' + column[6].strip(' \"').replace('UNK','-1') + '  ' + column[7].strip(' \"').replace('UNK','-1') + '  ' + str(m) + '  ' + str(Tf) + '  ' + column[11].strip(' \"').replace('UNK','-1') + '\n')

#[1]sckl [2]lmst [3]Tb [4]TLn [5]TLa [6]Pressure_1 [7]Presssure_2 [8]Horizontal_Wind_Speed [9]m [10]Tf [11]Wind_Direction

ATS_Boom2()

print("ATS_Boom2... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


in_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom1_Calculations/"
out_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom1_means/"

#NV path
# path where I will put the results

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print("Means_Boom1... STARTING")

print(st)


def Means_Boom1():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.dat'):
                #if file.find(file_md) != -1.00:
                filename = file
                
                sol_num = filename[15:20]
                w_file = "ATS_Boom1_m_tf_means_" + sol_num + ".dat"

                with open(in_dir + filename,'r') as input_file, open(out_dir + w_file, 'w') as output_file:
                    output_file.truncate()
                    n = 1
                    tmax = 61
                    time = 5
                    for lines in input_file:
                        column = lines.split()
                        if n == 1:
                            aux = column[0]
                            lmst = column[1]
                            lmst_hour = int(lmst[0:2])*3600
                            lmst_minute = int(lmst[3:5])*60
                            lmst_second = int(lmst[6:8])
                            lmst_total = lmst_hour + lmst_minute + lmst_second
                            #print lmst[6:8]
                            #print lmst[9:11]
                            #print lmst[12:14]
                            Tb_avg = float(column[2])
                            TLn_avg = float(column[3])
                            TLa_avg = float(column[4])
                            P_avg = float(column[6])
                            n = n + 1
                            continue
                        else:
                            if ((float(column[0]) - float(aux)) and n < tmax):
                                lmst_hour = int(lmst[0:2])*3660
                                lmst_minute = int(lmst[3:5])*60
                                lmst_second = int(lmst[6:8])
                                lmst_full = lmst_hour + lmst_minute + lmst_second
                                lmst_total = lmst_total + lmst_full
                                Tb_avg += float(column[2])
                                TLn_avg = TLn_avg + float(column[3])
                                TLa_avg = TLa_avg + float(column[4])
                                P_avg = P_avg + float(column[6])
                                n = n + 1
                                continue
                            else:
                                lmst_avg = lmst_total / n
                                P_final = P_avg / n
                                Tb_final = Tb_avg / n
                                TLn_final = TLn_avg / n
                                TLa_final = TLa_avg / n
                                a = Tb_final - TLn_final
                                b = TLa_final - Tb_final
                                c = TLn_final - TLa_final
                                z = 4
                                delta = 0.01

                                if (a * c) > 0:
                                    x = c / (a+c)
                                    m = delta
                                    while x * (np.cosh(m) - 1.0) < (np.cosh (m * (1 - 1 / (z + 0.0))) - 1.0):
                                        m = m + delta

                                    m = m - delta
                                else:
                                    m = 1.8
                                    Am = (np.cosh(m) - 1.0) / (np.cosh (m * (1-1 / (z + 0.0))) - 1.0)
                                    Tb_final = (1 - Am) * TLa_final + TLn_final * Am

                                if m > 0:
                                    Tf = (TLa_final - Tb_final * np.cosh(0.0) / np.cosh(m)) / (1 - np.cosh(0.0) / np.cosh(m))
                                else:
                                    Tf = "0.0"
                                n = 1
                                m = round(float(m), 3)
                                Tf = round(float(Tf), 3)
                                P_final = round(float(P_final), 3)
                                
                                output_file.write(str(datetime.timedelta(seconds=lmst_avg))[0:10] + ' ' + str(m) + '  ' + str(Tf) + '  ' + str(P_final) + '\n')

Means_Boom1()

print("Means_Boom1... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)


in_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom2_Calculations/"
out_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom2_means/"

#NV path
# path where I will put the results

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print("Means_Boom2... STARTING")

print(st)


def Means_Boom2():
    
    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('.dat'):
                #if file.find(file_md) != -1.00:
                filename = file
                
                sol_num = filename[15:20]
                w_file = "ATS_Boom1_m_tf_means_" + sol_num + ".dat"

                with open(in_dir + filename,'r') as input_file, open(out_dir + w_file, 'w') as output_file:
                    output_file.truncate()
                    n = 1
                    tmax = 61
                    time = 5
                    for lines in input_file:
                        column = lines.split()
                        if n == 1:
                            aux = column[0]
                            lmst = column[1]
                            lmst_hour = int(lmst[0:2])*3600
                            lmst_minute = int(lmst[3:5])*60
                            lmst_second = int(lmst[6:8])
                            lmst_total = lmst_hour + lmst_minute + lmst_second
                            #print lmst[6:8]
                            #print lmst[9:11]
                            #print lmst[12:14]
                            Tb_avg = float(column[2])
                            TLn_avg = float(column[3])
                            TLa_avg = float(column[4])
                            P_avg = float(column[6])
                            n = n + 1
                            continue
                        else:
                            if ((float(column[0]) - float(aux)) and n < tmax):
                                lmst_hour = int(lmst[0:2])*3600
                                lmst_minute = int(lmst[3:5])*60
                                lmst_second = int(lmst[6:8])
                                lmst_full = lmst_hour + lmst_minute + lmst_second
                                lmst_total = lmst_total + lmst_full
                                Tb_avg += float(column[2])
                                TLn_avg = TLn_avg + float(column[3])
                                TLa_avg = TLa_avg + float(column[4])
                                P_avg = P_avg + float(column[6])
                                n = n + 1
                                continue
                            else:
                                lmst_avg = lmst_total / n
                                P_final = P_avg / n
                                Tb_final = Tb_avg / n
                                TLn_final = TLn_avg / n
                                TLa_final = TLa_avg / n
                                a = Tb_final - TLn_final
                                b = TLa_final - Tb_final
                                c = TLn_final - TLa_final
                                z = 4
                                delta = 0.01

                                if (a * c) > 0:
                                    x = c / (a+c)
                                    m = delta
                                    while x * (np.cosh(m) - 1.0) < (np.cosh (m * (1 - 1 / (z + 0.0))) - 1.0):
                                        m = m + delta

                                    m = m - delta
                                else:
                                    m = 1.8
                                    Am = (np.cosh(m) - 1.0) / (np.cosh (m * (1-1 / (z + 0.0))) - 1.0)
                                    Tb_final = (1 - Am) * TLa_final + TLn_final * Am

                                if m > 0:
                                    Tf = (TLa_final - Tb_final * np.cosh(0.0) / np.cosh(m)) / (1 - np.cosh(0.0) / np.cosh(m))
                                else:
                                    Tf = "0.0"
                                n = 1
                                m = round(float(m), 3)
                                Tf = round(float(Tf), 3)
                                P_final = round(float(P_final), 3)
                                
                                output_file.write(str(datetime.timedelta(seconds=lmst_avg))[0:10] + ' ' + str(m) + '  ' + str(Tf) + '  ' + str(P_final) + '\n')

Means_Boom2()

print("Means_Boom2... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)

in_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom1_means/"
in_dir2 = "/data/PDS_Python/PDS_out_release/10_ATS/Read_Global/"

out_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom1_Global/"

#NV path
# path where I will put the results

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print("Boom1_global... STARTING")

print(st)


def Boom1_global():
    
    for base, dirs, files1 in os.walk(in_dir2):
        for file1 in files1:
            if (str(file1).endswith('.dat')):
                wind_file = file1
                sun1 = wind_file[4:9]
                for base, dirs, files2 in os.walk(in_dir):
                    for file2 in files2:
                        # Checking the file extension
                        if str(file2).endswith('.dat'):
                            means_file = file2
                            sun2 = means_file[21:26]
                            if sun1 == sun2:
                                #Open for read the file who fulfil the file extension and type.
                                with open(in_dir + means_file, 'r+') as input_file, open(in_dir2 +wind_file, 'r+') as input_file2, open(out_dir + 'ATS_Boom1_m_max_m_min_global_' + sun2 +'.dat', 'w') as output_file:
                                    output_file.truncate()
                                    

                                    # for line in csvfile:
                                    #     column_csv = line.split()
                                    #     #print(column_csv)
                                    #     print((column_csv[2]))
                                    #     if (int(wind_file[4:9]) == int(column_csv[0])) and int(column_csv[0]) <= 1260:
                                    #         ls = column_csv[2]
                                    #         #ls_column = num_ls.split()
                                    #         #ls = ls_column[0]+"."+ls_column[1]
                                    #     if (int(wind_file[4:9]) == int(column_csv[0])) and int(column_csv[0]) > 1260:
                                    #         ls = "-"
                                    n=1
                                    n_avg = 1

                                    v_max_orientation = -1
                                    wind_orientation_v_max = -1
                                    v_max_orien = 0

                                    for line in input_file2:
                                        column_input_wind = line.split()
                                        v_max_aux = float(column_input_wind[7])
                                        wind_direction_aux = float(column_input_wind[11])

                                        #if wind_direction_aux != -1:
                                            #  print wind_direction_aux

                                        if n_avg == 1:
                                            wind_direction = 0.0
                                            if (wind_direction_aux != -1):
                                                wind_direction = wind_direction + wind_direction_aux
                                                n_avg = n_avg + 1
                                        else:
                                            if wind_direction_aux != -1:
                                                wind_direction = wind_direction + wind_direction_aux
                                                #print wind_direction_aux , n_avg
                                                n_avg = n_avg + 1

                                        if n==1:
                                            v_max = 0.0
                                            n += n
                                        else:
                                            if (v_max_aux > v_max) and v_max_aux != -1:
                                                time_v_max = column_input_wind[1]
                                                v_max = v_max_aux
                                                n += n

                                        if wind_direction_aux != -1 and v_max_aux != -1:
                                            v_max_2 = v_max_aux
                                            if (v_max_2 > v_max_orien):
                                                v_max_orientation = v_max_2
                                                wind_orientation_v_max = float(column_input_wind[11])
                                    x=1
                                    for line in input_file:
                                        column_input_mean = line.split()
                                        m_max_aux = float(column_input_mean[1])
                                        m_min_aux = float(column_input_mean[1])
                                        if x==1:
                                            m_max = 0.0
                                            m_min = 100000.0
                                            x += x
                                        else:
                                            if (m_max_aux > m_max):
                                                m_max = m_max_aux
                                                time_m_max = column_input_mean[0]
                                                p_m_max = column_input_mean[3]
                                                tf_m_max = column_input_mean[2]
                                                x += x
                                            if (m_min_aux < m_min) and m_min_aux != 0:
                                                time_m_min = column_input_mean[0]
                                                p_m_min = column_input_mean[3]
                                                tf_m_min = column_input_mean[2]
                                                m_min = m_min_aux
                                                x += x
                                    #print wind_direction
                                    m_max_top = m_max
                                    time_m_max_top = time_m_max
                                    m_min_top = m_min
                                    pressure_m_max = p_m_max
                                    tf_m_max_top = tf_m_max
                                    time_m_min_top = time_m_min
                                    pressure_m_min = p_m_min
                                    tf_m_min_top = tf_m_min
                                    v_max_top = v_max
                                    #ls_final = ls
                                    wind_direction_final = wind_direction / n_avg #Average of all the wind directions in a SOL.
                                    v_max_orientation_final = v_max_orientation #Max speed when there is orientation
                                    wind_orientation = wind_orientation_v_max   #Wind orientation for the maximum speed when there is orientation
                                    #print n_avg
                                    #print wind_direction
                                    output_file.write(str(time_m_max_top) + ' ' + str(m_max_top) + ' ' + str(pressure_m_max) + ' ' + str(tf_m_max_top) + ' ' + str(time_m_min_top) + ' ' + str(m_min_top) + ' ' + str(pressure_m_min) +
                                                        ' ' + str(tf_m_min_top) + ' ' + str(v_max_top) + ' ' + str(wind_direction_final) + ' ' + str(v_max_orientation_final) + ' ' + str(wind_orientation))
                                
        
    
Boom1_global()

print("Boom1_global... COMPLETED")

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)

in_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom2_means/"
in_dir2 = "/data/PDS_Python/PDS_out_release/10_ATS/Read_Global/"

out_dir = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom2_Global/"

#NV path
# path where I will put the results

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print("Boom2_global... STARTING")

print(st)


def Boom2_global():
    
    for base, dirs, files1 in os.walk(in_dir2):
        for file1 in files1:
            if (str(file1).endswith('.dat')):
                wind_file = file1
                sun1 = wind_file[4:9]
                for base, dirs, files2 in os.walk(in_dir):
                    for file2 in files2:
                        # Checking the file extension
                        if str(file2).endswith('.dat'):
                            means_file = file2
                            sun2 = means_file[21:26]
                            if sun1 == sun2:
                                #Open for read the file who fulfil the file extension and type.
                                with open(in_dir + means_file, 'r+') as input_file, open(in_dir2 +wind_file, 'r+') as input_file2, open(out_dir + 'ATS_Boom2_m_max_m_min_global_' + sun2 +'.dat', 'w') as output_file:
                                    output_file.truncate()
                                    

                                    # for line in csvfile:
                                    #     column_csv = line.split()
                                    #     #print(column_csv)
                                    #     print((column_csv[2]))
                                    #     if (int(wind_file[4:9]) == int(column_csv[0])) and int(column_csv[0]) <= 1260:
                                    #         ls = column_csv[2]
                                    #         #ls_column = num_ls.split()
                                    #         #ls = ls_column[0]+"."+ls_column[1]
                                    #     if (int(wind_file[4:9]) == int(column_csv[0])) and int(column_csv[0]) > 1260:
                                    #         ls = "-"
                                    n=1
                                    n_avg = 1

                                    v_max_orientation = -1
                                    wind_orientation_v_max = -1
                                    v_max_orien = 0

                                    for line in input_file2:
                                        column_input_wind = line.split()
                                        v_max_aux = float(column_input_wind[7])
                                        wind_direction_aux = float(column_input_wind[11])

                                        #if wind_direction_aux != -1:
                                            #  print wind_direction_aux

                                        if n_avg == 1:
                                            wind_direction = 0.0
                                            if (wind_direction_aux != -1):
                                                wind_direction = wind_direction + wind_direction_aux
                                                n_avg = n_avg + 1
                                        else:
                                            if wind_direction_aux != -1:
                                                wind_direction = wind_direction + wind_direction_aux
                                                #print wind_direction_aux , n_avg
                                                n_avg = n_avg + 1

                                        if n==1:
                                            v_max = 0.0
                                            n += n
                                        else:
                                            if (v_max_aux > v_max) and v_max_aux != -1:
                                                time_v_max = column_input_wind[1]
                                                v_max = v_max_aux
                                                n += n

                                        if wind_direction_aux != -1 and v_max_aux != -1:
                                            v_max_2 = v_max_aux
                                            if (v_max_2 > v_max_orien):
                                                v_max_orientation = v_max_2
                                                wind_orientation_v_max = float(column_input_wind[11])
                                    x=1
                                    for line in input_file:
                                        column_input_mean = line.split()
                                        m_max_aux = float(column_input_mean[1])
                                        m_min_aux = float(column_input_mean[1])
                                        if x==1:
                                            m_max = 0.0
                                            m_min = 100000.0
                                            x += x
                                        else:
                                            if (m_max_aux > m_max):
                                                m_max = m_max_aux
                                                time_m_max = column_input_mean[0]
                                                p_m_max = column_input_mean[3]
                                                tf_m_max = column_input_mean[2]
                                                x += x
                                            if (m_min_aux < m_min) and m_min_aux != 0:
                                                time_m_min = column_input_mean[0]
                                                p_m_min = column_input_mean[3]
                                                tf_m_min = column_input_mean[2]
                                                m_min = m_min_aux
                                                x += x
                                    #print wind_direction
                                    m_max_top = m_max
                                    time_m_max_top = time_m_max
                                    m_min_top = m_min
                                    pressure_m_max = p_m_max
                                    tf_m_max_top = tf_m_max
                                    time_m_min_top = time_m_min
                                    pressure_m_min = p_m_min
                                    tf_m_min_top = tf_m_min
                                    v_max_top = v_max
                                    #ls_final = ls
                                    wind_direction_final = wind_direction / n_avg #Average of all the wind directions in a SOL.
                                    v_max_orientation_final = v_max_orientation #Max speed when there is orientation
                                    wind_orientation = wind_orientation_v_max   #Wind orientation for the maximum speed when there is orientation
                                    #print n_avg
                                    #print wind_direction
                                    output_file.write(str(time_m_max_top) + ' ' + str(m_max_top) + ' ' + str(pressure_m_max) + ' ' + str(tf_m_max_top) + ' ' + str(time_m_min_top) + ' ' + str(m_min_top) + ' ' + str(pressure_m_min) +
                                                        ' ' + str(tf_m_min_top) + ' ' + str(v_max_top) + ' ' + str(wind_direction_final) + ' ' + str(v_max_orientation_final) + ' ' + str(wind_orientation))
                                
        
    
Boom2_global()

print("Boom2_global... COMPLETED")


ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)



    #***************************************************************** Pressure Spline:
in_file_path1 = "/data/PDS_Python/PDS_out_release/3_Splines/Pspline/"


 # ***************************************************************** lowest Air Temperature:
    ####################### nominal acquisitions:
in_file_path8 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_lowest_Temp/"

    ####################### nominal and extended acquisitions:
in_file_path2 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean1/Out_Lowest_Temp/"

############### means GTS, sigma GTS, sigma RHSurf:
in_file_path3 = "/data/PDS_Python/PDS_out_release/4_RH/RHSurface6/"

# ***************************************************************** RH air at 1.5m:
in_file_path4 = "/data/PDS_Python/PDS_out_release/4_RH/RHSurface5/"

# ***************************************************************** Global, diffuse and direct irradiance:
in_file_path5 = "/data/PDS_Python/PDS_out_release/5_UV/"

# ***************************************************************** Derivative Spline GTS
in_file_path6 = "/data/PDS_Python/PDS_out_release/6_HEA_COO/splineGTS/"

# ***************************************************************** Difference AirTemp, GTS
in_file_path7 = "/data/PDS_Python/PDS_out_release/7_AirGround_Tdiff/"

# ***************************************************************** u*rho*(Tg-Ta)
in_file_path9 = "/data/PDS_Python/PDS_out_release/2_MEAN/Mean5/Out_mean_P_Tg_Ta_rho/"


# ***************************************************************** ENV & MOD from FMT V.6 (RDR_03.07.2015) para temperatura booms y UV temp
in_file_path10 = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/MD_CLEAN/"
in_file_path11 = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/NV_CLEAN/"
    
    
# ***************************************************************** ADR from FMT V.7 (RDR_18.02.2016) topography files
sun_topo_file_path = "/data/PDS_Python/PDS_out_release/1_AWK/CLEAN_ALL/ADR_CLEAN/"


#in_file_path12 = "/data/PDS_Python/PDS_out_release/Other_files/"
#in_file_path12 = "/data/PDS_Python/PDS_out_release/Other_files/"
in_file_path12 = "/data/PDS_Python/Code_Python/Other_files/"
#in_file_path12 = "/data/PDS_Python/PDS_out_release/Other_files/"

in_file_path13 = "/data/PDS_Python/PDS_out_release/TOA/"

in_file_path14 = "/data/PDS_Python/PDS_out_release/9_VMR_GTS/VMR_GTS_P_MAX/"

in_file_path15 = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom1_Global/"

in_file_path16 = "/data/PDS_Python/PDS_out_release/10_ATS/ATS_Boom2_Global/"

in_file_path17 = "/data/RAD/PDS_out/2_MEAN_MAX_MIN/"






out_dir1 = "/data/PDS_Python/PDS_out_release/8_Extrema/"




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