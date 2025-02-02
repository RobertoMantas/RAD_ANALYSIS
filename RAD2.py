
import pandas as pd
import numpy as np
import os
import sys
import time
import datetime


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

# Path from where I am reading

in_dir = "/Users/robertomantas/Documents/GitHub/RAD_ANALYSIS/PDS_out/1_AWK/RAW_ALL/"
out_dir = "/Users/robertomantas/Documents/GitHub/RAD_ANALYSIS/PDS_out/1_AWK/CLEAN_ALL/"

in_dir = "/Users/robertomantas/Documents/GitHub/RAD_ANALYSIS/PDS_out/1_AWK/RAW_ALL/"
out_dir = "/Users/robertomantas/Documents/GitHub/RAD_ANALYSIS/PDS_out/1_AWK/CLEAN_ALL/"

in_dir = "/data/RAD/PDS_out/1_AWK/RAW_ALL/"
out_dir = "/data/RAD/PDS_out/1_AWK/CLEAN_ALL/"

def read_clean_MD ():

    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(in_dir):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            filename = file
            
            if file.endswith('.TXT'):  
                # with open(in_dir+file, 'r') as f:
                #         lines = f.readlines()
                #         num_lines = len([l for l in lines if l.strip(' \n') != ''])
                # n = (len(open(in_dir+file).readlines()))
                sun = '0' + filename[23:27]
                print(sun)
                
                with open(in_dir+file,'r') as input_file1, open(out_dir + 'RAD_' +sun+'.dat', 'w') as output_file:
                    output_file.write("[1]START_OBS [2]DOSIMETRY_B_OBS [3]DOSIMETRY_B_DATA [4]DOSIMETRY_E_OBS [5]DOSIMETRY_E_DATA \n")
                    f = 0
                    q = 0

                    for k in input_file1:
                        
                        col = k.split()
                        if len(col) !=0:
                            if "START_OBS_UTC" in col[0]:
                               #print(col)
                                hora = col[1][0:8]
                                
                            if col[0] == "[DOSIMETRY_TOTAL_DOSE_B:" or f == 1:
                                #print(col)
                                
                                if f ==1:
                                    output_file.write(col[0] + ' ')
                                    f = 0

                                if f == 0:
                                   
                                    if len(col)>1:
                                        if len(col[1]) == 3:
                                            obs = col[1][0:2]
                                
                                        if len(col[1]) == 4:
                                            obs = col[1][0:3]
                                        
                                        output_file.write(str(hora) + ' ' + str(obs)+ ' ')
                                        f = 1

                            if  col[0] == "[DOSIMETRY_TOTAL_DOSE_E:" or q == 1:
                                
                                if q ==1:
                                    output_file.write(col[0] + '\n')
                                    q = 0

                                if q == 0:
                                   
                                    if len(col)>1:
                                        if len(col[1]) == 3:
                                            obs = col[1][0:2]
                                
                                        if len(col[1]) == 4:
                                            obs = col[1][0:3]
                                        
                                        output_file.write(str(obs)+ ' ')
                                        q = 1

                            #print(col[0][0])
                            #if "START_OBS_UTC" in col[0]:
                               #print(col)

                            # if is_number(col[0]):

                            #     if float(col[0])> 158306493.000:
                                    
                            #         output_file.write(str(col[0])+' '+str(col[1]).strip('\"').replace('"','')+' '+str(col[2]).strip('\"').replace('"','')+' '+str(col[3])+' '+str(col[4])+' '+str(col[5]).strip('\"').replace('"','')+' '+str(col[6]).strip('\"').replace('"','')+' '+str(col[7])+' '+str(col[8])
                            #         +' '+str(col[9])+' '+str(col[10])+' '+str(col[11])+' '+str(col[12])+' '+str(col[13])+' '+str(col[14])+' '+str(col[15])+' '+str(col[16])+' '+str(col[17])+' '+str(col[18])+' '+str(col[19])+' '+str(col[20])+' '+str(col[21])+' '+str(col[22])+' '+str(col[23])+' '+str(col[24]) 
                            #         +' '+str(col[25])+' '+str(col[26])+' '+str(col[27])+' '+str(col[28])+' '+str(col[29])+' '+str(col[30])+' '+str(col[31])+' '+str(col[32])+' '+str(col[33])+' '+str(col[34])+' '+str(col[35])+' '+str(col[36])+' '+str(col[37])+' '+str(col[38])+' '+str(col[39])+' '+str(col[40])+' '+str(col[41])+' '+str(col[42])
                            #         +' '+str(col[43])+' '+str(col[45])+' '+str(col[46])+' '+str(col[47])+' '+str(col[48])+' '+str(col[49])+' '+str(col[50])+' '+str(col[51])+' '+str(col[52])+' '+str(col[53])+' '+str(col[54])+' '+str(col[55])+' '+str(col[56])+' '+str(col[57])+' '+str(col[58])+' '+str(col[59])+' '+str(col[60])+' '+str(col[61])
                            #         +' '+str(col[62])+' '+str(col[63])+' '+str(col[64])+' '+str(col[65])+' '+str(col[66])+' '+str(col[67])+' '+str(col[68])+' '+str(col[69]) +' '+str(col[70])+' '+str(col[71])+' '+str(col[72])+' '+str(col[73])+' '+str(col[74])+' '+str(col[75])+' '+str(col[76])+' '+str(col[77])+' '+str(col[78])+'\n')

                        
#read_clean_MD()


in_dir = "/Users/robertomantas/Documents/GitHub/RAD_ANALYSIS/PDS_out/1_AWK/CLEAN_ALL/"
out_dir = "/Users/robertomantas/Documents/GitHub/RAD_ANALYSIS/PDS_out/2_MEAN_MAX_MIN/"

in_dir = "/Users/robertomantas/Documents/GitHub/RAD_ANALYSIS/PDS_out/1_AWK/CLEAN_ALL/"
out_dir = "/Users/robertomantas/Documents/GitHub/RAD_ANALYSIS/PDS_out/2_MEAN_MAX_MIN/"

in_dir = "/data/RAD/PDS_out/1_AWK/CLEAN_ALL/"
out_dir = "/data/RAD/PDS_out/2_MEAN_MAX_MIN/"

def avg_max_min():

    for base, dirs, files in os.walk(in_dir):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            filename = file
            
            if file.endswith('.dat'):  
                # with open(in_dir+file, 'r') as f:
                #         lines = f.readlines()
                #         num_lines = len([l for l in lines if l.strip(' \n') != ''])
                # n = (len(open(in_dir+file).readlines()))
                sun = filename[4:9]
                #print(sun)
                
                with open(in_dir+file,'r') as input_file1, open(out_dir + 'AVERAGE_MAX_MIN_' +sun+'.dat', 'w') as output_file:
                    lmst_Array = []
                    data_B_Array = []
                    data_E_Array = []
                    n = (len(open(in_dir+file).readlines()))
                    #output_file.write("[1]AVG_B [2]LMST_MAX_B [3]MAX_B [4]LMST_MIN_B [5]MIN_B [6]AVG_E [7]LMST_MAX_E [8]MAX_E [9]LMST_MIN_E [10]MIN_E \n")
                    cont = 0
                    q = 0

                    for k in input_file1:
                        
                        col = k.split()
                        if len(col)<4:
                            continue
                        else:
                            if q == 0:
                                q = 1
                                continue
                            else:
                                
                                lmst = col[0]
                                lmst_Array.append(lmst)
                                data_B = float(col[2])
                                data_B_Array.append(data_B)
                                data_E = float(col[4])
                                data_E_Array.append(data_E)
                                cont = cont + 1

                                if cont == n-1:
                                    
                                    avg_b = sum(data_B_Array)/len(data_B_Array)
                                    avg_e = sum(data_E_Array)/len(data_E_Array)

                                    max_b = max(data_B_Array)
                                    pos_max_b = data_B_Array.index(max_b)

                                    max_e = max(data_E_Array)
                                    pos_max_e = data_E_Array.index(max_e)
                                    
                                    min_b = min(data_B_Array)
                                    pos_min_b = data_B_Array.index(min_b)
                                    
                                    min_e = min(data_E_Array)
                                    pos_min_e = data_E_Array.index(min_e)

                                    lmst_max_b = lmst_Array[pos_max_b]
                                    lmst_max_e = lmst_Array[pos_max_e]
                                    lmst_min_b = lmst_Array[pos_min_b]
                                    lmst_min_e = lmst_Array[pos_min_e]

                                    avg_b = round(float(avg_b), 4)
                                    avg_e = round(float(avg_e), 4)

                                    
                                    output_file.write(str(avg_b) + ' ' + str(lmst_max_b)+ ' ' + str(max_b)+ ' ' + str(lmst_min_b)+ ' ' + str(min_b)+ ' ' + str(avg_e)+ ' ' + str(lmst_max_e)+ ' ' + str(max_e)+ ' ' + str(lmst_min_e)+ ' ' + str(min_e)+ '\n')
                                

avg_max_min()

