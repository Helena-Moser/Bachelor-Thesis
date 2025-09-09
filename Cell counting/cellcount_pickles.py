# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:18:35 2024

@author: helen
"""
#script for counting the number of cells using the last pickle file of a simulation, putting it all into a csv at the end

import pickle as cPickle
import sys
import csv

#eliminating the ModuleNotFound Error for CellModeller, it's confused bc there's multiple CellModeller Folders
sys.path.append('C://Users/helen/CellModeller')

filepaths = ['C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_100rep_5_BlockerPercent_95_24-08-17-16-59-02/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_10rep_1_BlockerPercent_45_24-08-15-20-27-27/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_11rep_1_BlockerPercent_50_24-08-15-20-41-12/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_12rep_1_BlockerPercent_55_24-08-15-20-54-53/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_13rep_1_BlockerPercent_60_24-08-15-21-08-28/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_14rep_1_BlockerPercent_65_24-08-15-21-22-03/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_15rep_1_BlockerPercent_70_24-08-15-21-35-36/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_16rep_1_BlockerPercent_75_24-08-15-21-48-56/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_17rep_1_BlockerPercent_80_24-08-15-22-02-15/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_18rep_1_BlockerPercent_85_24-08-15-22-15-28/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_19rep_1_BlockerPercent_90_24-08-15-22-28-38/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_1rep_1_BlockerPercent_0_24-08-15-18-20-58/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_20rep_1_BlockerPercent_95_24-08-15-22-41-48/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_21rep_2_BlockerPercent_0_24-08-15-22-54-53/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_22rep_2_BlockerPercent_5_24-08-15-23-09-12/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_23rep_2_BlockerPercent_10_24-08-15-23-23-26/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_24rep_2_BlockerPercent_15_24-08-15-23-37-33/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_25rep_2_BlockerPercent_20_24-08-15-23-51-37/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_26rep_2_BlockerPercent_25_24-08-16-00-05-41/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_27rep_2_BlockerPercent_30_24-08-16-00-19-41/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_28rep_2_BlockerPercent_35_24-08-16-00-33-37/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_29rep_2_BlockerPercent_40_24-08-16-00-47-25/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_2rep_1_BlockerPercent_5_24-08-15-18-35-18/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_30rep_2_BlockerPercent_45_24-08-16-01-01-18/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_31rep_2_BlockerPercent_50_24-08-16-01-15-04/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_32rep_2_BlockerPercent_55_24-08-16-01-28-36/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_33rep_2_BlockerPercent_60_24-08-16-01-42-12/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_34rep_2_BlockerPercent_65_24-08-16-01-55-42/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_35rep_2_BlockerPercent_70_24-08-16-02-09-01/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_36rep_2_BlockerPercent_75_24-08-16-02-22-29/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_37rep_2_BlockerPercent_80_24-08-16-02-35-56/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_38rep_2_BlockerPercent_85_24-08-16-02-49-16/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_39rep_2_BlockerPercent_90_24-08-16-03-02-29/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_3rep_1_BlockerPercent_10_24-08-15-18-49-28/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_40rep_2_BlockerPercent_95_24-08-16-03-15-41/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_41rep_3_BlockerPercent_0_24-08-16-23-52-30/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_42rep_3_BlockerPercent_5_24-08-17-00-07-46/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_43rep_3_BlockerPercent_10_24-08-17-00-22-14/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_44rep_3_BlockerPercent_15_24-08-17-00-36-38/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_45rep_3_BlockerPercent_20_24-08-17-00-51-12/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_46rep_3_BlockerPercent_25_24-08-17-01-05-36/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_47rep_3_BlockerPercent_30_24-08-17-01-19-56/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_48rep_3_BlockerPercent_35_24-08-17-01-34-11/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_49rep_3_BlockerPercent_40_24-08-17-01-48-15/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_4rep_1_BlockerPercent_15_24-08-15-19-03-41/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_50rep_3_BlockerPercent_45_24-08-17-02-02-34/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_51rep_3_BlockerPercent_50_24-08-17-02-16-45/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_52rep_3_BlockerPercent_55_24-08-17-02-30-44/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_53rep_3_BlockerPercent_60_24-08-17-02-44-41/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_54rep_3_BlockerPercent_65_24-08-17-02-58-27/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_55rep_3_BlockerPercent_70_24-08-17-03-12-15/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_56rep_3_BlockerPercent_75_24-08-17-03-25-56/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_57rep_3_BlockerPercent_80_24-08-17-03-39-34/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_58rep_3_BlockerPercent_85_24-08-17-03-53-03/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_59rep_3_BlockerPercent_90_24-08-17-04-06-28/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_5rep_1_BlockerPercent_20_24-08-15-19-17-41/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_60rep_3_BlockerPercent_95_24-08-17-04-19-53/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_61rep_4_BlockerPercent_0_24-08-17-04-33-15/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_62rep_4_BlockerPercent_5_24-08-17-04-47-55/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_63rep_4_BlockerPercent_10_24-08-17-05-02-25/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_64rep_4_BlockerPercent_15_24-08-17-05-16-56/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_65rep_4_BlockerPercent_20_24-08-17-05-31-18/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_66rep_4_BlockerPercent_25_24-08-17-05-45-39/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_67rep_4_BlockerPercent_30_24-08-17-06-00-01/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_68rep_4_BlockerPercent_35_24-08-17-06-14-08/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_69rep_4_BlockerPercent_40_24-08-17-06-28-16/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_6rep_1_BlockerPercent_25_24-08-15-19-31-41/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_70rep_4_BlockerPercent_45_24-08-17-06-42-21/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_71rep_4_BlockerPercent_50_24-08-17-06-56-31/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_72rep_4_BlockerPercent_55_24-08-17-07-10-24/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_73rep_4_BlockerPercent_60_24-08-17-07-24-11/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_74rep_4_BlockerPercent_65_24-08-17-07-38-01/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_75rep_4_BlockerPercent_70_24-08-17-07-51-40/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_76rep_4_BlockerPercent_75_24-08-17-08-05-24/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_77rep_4_BlockerPercent_80_24-08-17-08-18-58/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_78rep_4_BlockerPercent_85_24-08-17-11-28-12/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_79rep_4_BlockerPercent_90_24-08-17-11-42-52/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_7rep_1_BlockerPercent_30_24-08-15-19-45-54/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_80rep_4_BlockerPercent_95_24-08-17-11-58-23/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_81rep_5_BlockerPercent_0_24-08-17-12-13-40/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_82rep_5_BlockerPercent_5_24-08-17-12-29-41/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_83rep_5_BlockerPercent_10_24-08-17-12-45-17/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_84rep_5_BlockerPercent_15_24-08-17-13-01-15/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_85rep_5_BlockerPercent_20_24-08-17-13-16-37/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_86rep_5_BlockerPercent_25_24-08-17-13-32-14/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_87rep_5_BlockerPercent_30_24-08-17-13-47-39/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_88rep_5_BlockerPercent_35_24-08-17-14-03-39/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_89rep_5_BlockerPercent_40_24-08-17-14-19-19/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_8rep_1_BlockerPercent_35_24-08-15-19-59-50/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_90rep_5_BlockerPercent_45_24-08-17-14-35-27/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_91rep_5_BlockerPercent_50_24-08-17-14-51-09/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_92rep_5_BlockerPercent_55_24-08-17-15-05-48/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_93rep_5_BlockerPercent_60_24-08-17-15-19-55/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_94rep_5_BlockerPercent_65_24-08-17-15-33-43/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_95rep_5_BlockerPercent_70_24-08-17-15-47-23/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_96rep_5_BlockerPercent_75_24-08-17-16-01-01/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_97rep_5_BlockerPercent_80_24-08-17-16-14-33/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_98rep_5_BlockerPercent_85_24-08-17-16-28-12/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_99rep_5_BlockerPercent_90_24-08-17-16-43-41/step-00700.pickle',
'C:/Users/helen/CellModeller/Examples/Data_No_Blocker_Transfer_Sec_Recipient_Transfer_No_Growth_Dep/Sim_number_9rep_1_BlockerPercent_40_24-08-15-20-13-36/step-00700.pickle']


def read_file(filepath):
    #locate the folder where the pickle(s) are saved & insert the respective pickle name
    data = cPickle.load(open(filepath,'rb'))
    #data = cPickle.load(open(r"C:/\Users\helen\Documents\code_helena-24-04-10-15-52\step-00720.pickle",'rb'))
    cs = data['cellStates']
    
    number_donors = 0 # cell type 0
    number_recipients = 0 # cell type 1
    number_transconjugants = 0 # cell type 2
    number_blockers = 0 # cell type 3
    number_blocker_transconjugants = 0 # cell type 4
     
    for (id, cell) in cs.items():
        if cell.cellType==0:
            number_donors +=1
        if cell.cellType==1:
            number_recipients +=1 # Add rest of if statements for the other cell types
        if cell.cellType==2:
            number_transconjugants +=1
        if cell.cellType==3:
            number_blockers +=1
        if cell.cellType==4:
            number_blocker_transconjugants +=1
            
    return (filepath, str(data[ 'HGTevents']), number_donors, number_recipients, number_transconjugants, number_blockers)

output_csv = 'C://Users/helen/CellModeller/Examples/data/output.5_noBlockertransfer_SecTransfer_noGrowthdep.csv'

# Open the CSV file for writing
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header row (optional)
    csvwriter.writerow(['File Path', 'Recipient TransferEvents', 'final Donors', 'final Reciepients', 'final Transconjugants', 'final Blockers'])
    
    # Iterate through the list of file paths and write each file's info to the CSV
    for filepath in filepaths:
        file_info = read_file(filepath)
        csvwriter.writerow(file_info)

print(f"Data from files has been written to {output_csv}")

