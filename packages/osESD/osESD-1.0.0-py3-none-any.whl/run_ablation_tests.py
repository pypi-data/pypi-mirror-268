
### Code for replicating ablation test results.
### Results will appear in 'test_results//ablation_test'.
### Scores are exactly the same as those made in R.

############################################################
############################################################
############################################################
############################################################

import os
import numpy as np
import pandas as pd
import time as t
import random
import torch

from models import osESD_Detector
from models import sosESD_Detector
from models import oGESD_Detector
from models import norep_osESD_Detector

from utils import scores_module
from utils import plotting_modules
from utils import data_aug

random.seed(42)
np.random.seed(42)
torch.manual_seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(42)


### Set parameters for ablation tests. In case of shorter datasets (Yahoo!) then smaller values of
### window size, dwin, rwin, and maxr is recommended. ARIMA and seasonal state-space datasets are longer
### thus larger values are used.
class options_class_big:
    size = 100
    dwin = 10
    rwin = 10
    maxr = 10
    alpha = 0.01
    condition = False
    visualize_pred = False
    visualize_real = False

class options_class_small:
    size = 100
    dwin = 2
    rwin = 4
    maxr = 10
    alpha = 0.01
    condition = False
    visualize_pred = False
    visualize_real = False


def main():

    main_dir = os.getcwd()
    Models = {0:'osESD', 1:'oGESD', 2: 'sosESD', 3:'norep_osESD'}
    Test_Dirs=['real','synthetic']

    ### Set models that will be used in testing. If set to 0, then model will not run.
    ### In order, 'osESD', 'oGESD', 'sosESD', 'norep_osESD'.
    Model_Switch = [1,1,1,1]

    ### Create column names accordingly to models being used.
    Cols = ['Data Name']
    for idx, switch in enumerate(Model_Switch):
        if switch == 1:
            Cols.append(Models[idx] + str('__recall'))
            Cols.append(Models[idx] + str('__precision'))
            Cols.append(Models[idx] + str('__f1score'))
            Cols.append(Models[idx] + str('__time (sec)'))

    ### Start running tests.
    ### Final_Values is where all values are saved and will be exported as csv file.
    IDX=1
    Final_Values = []
    os.chdir('Datasets')
    for name in Test_Dirs:
        ### Don't run tests if Model_Switch is all 0.
        if sum(Model_Switch)==0:
            break

        os.chdir(name)
        for data in os.listdir():
            Row = [data]
            file_path = data
            print("\n\n\nCurrent Test : ", IDX)
            print(data)

            ### Change parameters accordingly to 'Yahoo!' dataset or not.
            if 'Benchmark' in data:
                options_class = options_class_small
            else:
                options_class = options_class_big

            ### Run all models with 'data' dataset in function 'Run_ablation_tests' written below.
            Results = Run_ablation_tests(file_path,main_dir+"//test_results//ablation_test//",options_class,Model_Switch)
            for val in Results:
                Row.append(val)
            Final_Values.append(Row)
            IDX+=1
        os.chdir('..')
    os.chdir('..')

    ### Write csv.
    if sum(Model_Switch)!=0:
        os.chdir('..')
        Ablation_tests = pd.DataFrame(Final_Values)
        Ablation_tests.columns = Cols
        Ablation_tests.to_csv(main_dir+"//test_results//ablation_test//Ablation_Tests_Python_all_scores.csv",sep='\t',index=False)

        cols = Ablation_tests.columns[1:]
        datasets = ['A1','A2','A3','A4','ARIMA','seasonal']
        def group_value(value):
            for data_group_name in datasets:
                if data_group_name in value:
                    return data_group_name
        
        Ablation_tests['Group'] = Ablation_tests['Data Name'].apply(group_value)
        grouped = Ablation_tests.groupby('Group')
        Averaged_Values = []
        for group_name, group_data in grouped:
            group_values = [group_name]
            for col in cols:
                group_values.append(round(group_data[col].mean(),3))
            Averaged_Values.append(group_values)

        Averaged_Values = pd.DataFrame(Averaged_Values)
        Averaged_Values.columns = Ablation_tests.columns[:-1]
        Averaged_Values.to_csv(main_dir + "//test_results//ablation_test//Ablation_Tests_Python_averaged_scores.csv", sep='\t',
                index=False)
                




def Run_ablation_tests(data_path, save_path, options, switch=[1,1,1,1] ):

    ### Read dataset to use in tests.
    file_path = data_path
    df = pd.read_csv(file_path)

    ### Options for plotting.
    Plot_Pred = True

    ### Basic processing for running models.
    df = data_aug.add_timestamp(df)
    df = df[['timestamps','value','anomaly']]
    df['value'] = df['value'].astype('float64')
    real_index = df['anomaly'][options.size:]

    ### 'Return_Values' is where all values will be saved and later exported to csv files.
    Return_Values=[]
    if switch[0] == 1:

        ### Run osESD.
        T1 = t.time()
        predictions = osESD_Detector.osESD(data=list(df['value']),
                                           time=list(df['timestamps']),
                                           train_size=options.size,
                                           dwins=options.dwin,
                                           rwins=options.rwin,
                                           alpha=options.alpha,
                                           condition = options.condition,
                                           maxr=options.maxr)
        T2 = t.time()

        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[options.size:]
        results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        if Plot_Pred:
            df['predictions'] = data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_path,'predictions',df,save_path+"//plots//","osESD")

        for result_idx in range(2,6):
            Return_Values.append(results[result_idx])



    if switch[1] == 1:

        ### Run oGESD.
        T1 = t.time()
        predictions = oGESD_Detector.oGESD(data=list(df['value']),
                                           time=list(df['timestamps']),
                                           train_size=options.size,
                                           dwins=options.dwin,
                                           rwins=options.rwin,
                                           alpha=options.alpha,
                                           maxr=options.maxr)
        T2 = t.time()

        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[options.size:]
        results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        if Plot_Pred:
            df['predictions'] = data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_path,'predictions',df,save_path+"//plots//","oGESD")

        for result_idx in range(2,6):
            Return_Values.append(results[result_idx])

    if switch[2] == 1:

        ### Run sosESD.
        T1 = t.time()
        predictions = sosESD_Detector.sosESD(data=list(df['value']),
                                             wins=options.size,
                                             alpha=options.alpha,
                                             maxr=options.maxr)
        T2 = t.time()

        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[options.size:]
        results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        if Plot_Pred:
            df['predictions'] = data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_path,'predictions',df,save_path+"//plots//","sosESD")

        for result_idx in range(2,6):
            Return_Values.append(results[result_idx])

    if switch[3] == 1:

        ### Run norep_osESD
        T1 = t.time()
        predictions = norep_osESD_Detector.norep_osESD(data=list(df['value']),
                                                       time=list(df['timestamps']),
                                                       train_size=options.size,
                                                       dwins=options.dwin,
                                                       rwins=options.rwin,
                                                       alpha=options.alpha,
                                                       maxr=options.maxr)
        T2 = t.time()

        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[options.size:]
        results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        if Plot_Pred:
            df['predictions'] = data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_path,'predictions',df,save_path+"//plots//","norep_osESD")

        for result_idx in range(2,6):
            Return_Values.append(results[result_idx])

    return Return_Values

if __name__ == "__main__":
    result_directory = 'test_results//ablation_test//plots'
    if not os.path.exists(result_directory):
        print("Creating results directory for ablation tests.")
        os.makedirs(result_directory)
    main()


