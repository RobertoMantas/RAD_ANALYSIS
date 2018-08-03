
import pandas as pd
import numpy as np
import os
import sys
import time
import datetime
import math
import matplotlib.pyplot as plt
import pylab


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
in_dir = "/Users/robertomantas/Documents/LTU/RAD/RAW_ALL/"
out_dir = "/Users/robertomantas/Documents/LTU/RAD/CLEAN_ALL/"


def read_clean_MD ():

    # Iteration on the MD Files Directory
    # Where the files are
    for base, dirs, files in os.walk(in_dir):
        ##Read each file name
        #variable file is the name of the file with the extension and we put it as the file name 
        for file in files:
            if file.endswith('.TXT'):  
                with open(in_dir+file, 'r') as f:
                        lines = f.readlines()
                        num_lines = len([l for l in lines if l.strip(' \n') != ''])
                n = (len(open(in_dir+file).readlines()))
                cont=0
                with open(out_dir + 'PRUEBA.dat', 'w') as output_file:
                    #Now we have the name of every file in order to insert it to pandas 
                    filename = file
                    # Get the sun number and put a zero extra and concatenate the 4 digit of the sun number. 
                    sun = '0' + filename[23:27]
                    #Insert to pandas the file and in every iteration it will do this with evey file
                    # We tell pandas some informatio the file, the separator, the type of object (normally object) and there is no header the PDS files has no header.
                    
                    for i in range(num_lines):
                            
                        df = pd.read_csv(in_dir + filename, dtype=object,sep = "\t", usecols = [0], header=None,encoding='latin1')

                        
                        df2 = df.replace('"', '', regex=True)

                        #df2 = df[df[0][0:10] < '1234120']

                        df2 = df2.loc[i].to_string()
                        df3 = df2.split()

                        #print(int(df3[2]))
                        # cont +=1
                        # print(cont)
                        print(df3)

                        if is_number(df3[1]) == True:
                            
                            if float(df3[1]) > 558306430.000:
                                

                                
                                print(i)
                                
                                output_file.write(str(df3[1])+' '+str(df3[2])+' '+str(df3[3])+' '+str(df3[4])+' '+str(df3[5]) +'\n')
                                #df3.to_csv(out_dir + 'PRUEBA_' + sun+ '.dat', sep='\t', index=False, header=None)
                                    
                                #print(float(first_words[0]))
                                # regex=True is very important because this makes the file to replace it and regenarete in order to show it.
                                #Because if we dont do this the file would not show that it has changed
                                # df2 = df.replace('UNK', '-1.00', regex=True)
                                # # We do the same thing as before but this time replacing NULL for -1
                                # df3 = df2.replace('NULL', '-1.00', regex=True)
                                # #We want to clean a pattern of a column which repeats in every single file. 
                                # df4=df3.replace(sun+'M','',regex=True)
                                # Once we have the file (df3) free of UNK and NULL and separeted by comas we are good to go. 
                                # Now we save the file in out_dir that goes to the PATH given before. With the name MD, and the sun number, the extension .dat to follow the standar, the separator that is with tabulations, no index because pandas always creates a index
                                # in the first column and when we want to read we take off the index and the header and we say the columns that we are working on (each time can be different )
                                #columns taken by patricia: 0 TIMESTAMP,1(without the first 6 letters)LMST,30 LOCAL_RELATIVE_HUMIDITY,31 HS_TEMP,33 VOLUME_MIXING_RATIO,37 PRESSURE, 7 GTS, 10 GTS CONFIDENCE, 11 Air_TempB1, 12 TempB1_Confidence,13 Air_TempB2,14 TempB2_Confidence
                                #15 AMB_TEMP
                                
                                #df4_final= df.to_csv(out_dir + 'RAD_' + sun+ '.dat', sep='\t', index=False, header=None )

                            # except:
                        #     pass
                        
        #return df4_final
    
#We decide which colums we want to have in our new clean file 
# columns taken by patricia: 0 TIMESTAMP,1(without the first 6 letters)LMST,30 LOCAL_RELATIVE_HUMIDITY,31 HS_TEMP,33 VOLUME_MIXING_RATIO,37 PRESSURE, 7 GTS, 10 GTS CONFIDENCE, 11 Air_TempB1, 12 TempB1_Confidence,13 Air_TempB2,14 TempB2_Confidence
# 15 AMB_TEMP, 16AMBIENT_TEMP_CONFIDENCE_LEVEL
read_clean_MD()
