#!/usr/bin/python
# -*- coding: latin-1 -*-
import pandas as pd
import numpy as np
import os
import sys
import time
import datetime
import math


in_dir = "/Users/robertomantas/Documents/PDS_out2/"
out_dir = "/Users/robertomantas/Documents/PDS_out2/"

def extrema_RAD():

    # Iteration on the MD Files Directory
    for base, dirs, files in os.walk(in_dir):
        for file in files:
            #print file
                # Checking the file extension
            if str(file).endswith('02027.dat'):
                #if file.find(file_md) != -1.00:
                md_file = file
                
                w_file = "Extrema_RAD.dat"
                with open(in_dir+md_file) as textfile1, open(out_dir+w_file, 'w+') as output_file:
                    output_file.truncate()
                    for y in (textfile1):
                        col = y.split()
                        if len(y)<9:
                            continue
                        else:
                            print(col)

extrema_RAD()
                            