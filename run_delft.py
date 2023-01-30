##################################################################
#
#     Developed by: Débora Rodrigues and Ana Oliveira
#     LAPMAR (UFPA) and MARETEC (IST)
#     OBSERVATÓRIO DA COSTA AMAZÔNICA
#     Date: 27/01/2023
#
##################################################################


#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports
import os
import sys
import datetime
import dateutil.relativedelta
from calendar import monthrange

# Define the begin and end of the simulation. 
start_date = '20000101'
end_date = '20000102'

# Define the simulation folder, where the MDU file is located. 
simulation_folder = 'C:/Your/Simulation/Folder/Project1.dsproj_data/FlowFM/'
results_folder = 'C:/Your/Results/Folder/Project1.dsproj_data/FlowFM/DFM_OUTPUT_FlowFM/'

# Define the model run interval. Do you want to run the simulation each day or month?
interval= 'D' #D for daily, M for monthly. Y for yearly is not defined yet

# Transform the dates to python dates, thus it can be read it.
start_date_py = datetime.datetime.strptime(start_date, '%Y%m%d')
actual_date_py = datetime.datetime.strptime(start_date, '%Y%m%d')
end_date_py = datetime.datetime.strptime(end_date, '%Y%m%d')

def edit_mdu_file ():

# Here we edit the MDU file. 
# For now, four changes are being made, the RefDate (day of simulation)
# the TStop, the definition of when the model needs to stop running and closing the output files
# Output names, His and Map files. 

    fin_template = open(simulation_folder + 'FlowFM_temp.mdu', 'r')
    fin_model = open(simulation_folder + 'FlowFM.mdu', 'w')
    
    template = fin_template.readlines()
    
    for lin in template:
        if "RefDate_replace" in lin:
            lin = lin.replace("RefDate_replace", actual_date)
            fin_model.writelines(lin)
            
        elif "TStop_replace" in lin:
            lin = lin.replace("TStop_replace", str(interval_seconds))
            fin_model.writelines(lin)
            
        elif "MapFile_replace" in lin:
            lin = lin.replace("MapFile_replace", str(map_name))
            fin_model.writelines(lin)
            
        elif "His_File_replace" in lin:
            lin = lin.replace("His_File_replace", str(his_name))
            fin_model.writelines(lin)

        elif "RestartFile_replace" in lin:
            if actual_date_py > start_date_py:
                lin = lin.replace("RestartFile_replace", str(restart_name))
                fin_model.writelines(lin)
            
            else:
                print ('continuos does not work or not started')
                
        else:
            fin_model.writelines(lin)

    fin_template.close()
    fin_model.close()
    
while actual_date_py<=end_date_py:

    actual_date = datetime.date.strftime(actual_date_py, '%Y%m%d') #date written in string dates

# Definition of montlhy number of days
    year = actual_date_py.year
    month = actual_date_py.month
    num_days = monthrange(year, month)[1]
    
# Interval Loop
    if interval == 'D':
        interval_seconds= 86400
        addtime= dateutil.relativedelta.relativedelta(days=+1)
        
    elif interval == 'M':
        interval_seconds = 86400*num_days
        addtime= dateutil.relativedelta.relativedelta(months=+1)

# Year definition is not implemented yet
#    elif interval== 'Y':
#        interval_seconds= 86400*365 #leap years?
#        addtime= dateutil.relativedelta.relativedelta(years=+1)
    else:
        print ('Define time interval')

    # Define the output names according to the time running
    map_name = actual_date + '_map.nc'
    his_name = actual_date + '_his.nc'
    restart_name = results_folder + 'FlowFM_' + actual + '_000000_rst.nc'
    # Here we call the function that edits the mdu file
    edit_mdu_file()
    
    actual_date_py = actual_date_py + addtime #date written in python dates

    # Call the model.exe
    os.system('run.bat')
