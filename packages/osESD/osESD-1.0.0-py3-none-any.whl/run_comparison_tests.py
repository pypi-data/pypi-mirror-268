

### Code for replicating comparison test results.
### Results will appear in 'test_results//comparison_test'.

############################################################
############################################################
############################################################
############################################################


import os
import pandas as pd
import numpy as np
import time
import random
import torch

from models import osESD_Detector
from models import ts_isolation_forest
from models import ts_random_robust_cut_classifier
from models import ts_AE
from models import ts_VAE
from models import ts_LSTMED
import parameters

from utils import plotting_modules
from utils import data_aug
from utils import scores_module

random.seed(42)
np.random.seed(42)
torch.manual_seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(42)

def main():

    main_dir = os.getcwd()
    print(main_dir)
    Models = {0: 'osESD', 1: 'isolation forest', 2: 'RRCF', 3: 'AE', 4:'VAE', 5:'LSTMED' }
    Test_Dirs = ['real','synthetic']

    ### Set models that will be used in testing. If set to 0, then model will not run.
    ### In order, 'osESD', 'isolation forest', 'random robust cut forest',
    ### 'auto-encoder', 'variational auto-encoder', 'lstm based encoder decoder'.
    Model_Switch = [1, 1, 1, 1, 1, 1]
    Cols = ['Data Name']
    for idx, switch in enumerate(Model_Switch):
        if switch == 1:
            Cols.append(Models[idx] + str('__recall'))
            Cols.append(Models[idx] + str('__precision'))
            Cols.append(Models[idx] + str('__f1score'))
            Cols.append(Models[idx] + str('__time (sec)'))

    ### Start running tests.
    ### All scores will be saved into 'Final_Values', and this will be exported to csv.
    IDX = 1
    Final_Values = []
    os.chdir('Datasets')
    for name in Test_Dirs:

        ### In case 'Model_Switch' are all zeros, then don't run.
        if sum(Model_Switch) == 0:
            break
        os.chdir(name)

        ### ALl models have been tuned to match each dataset, so set parameters accordingly.
        for data in os.listdir():
            if 'A1Benchmark' in data:
                major_class = parameters.A1
            elif 'A2Benchmark' in data:
                major_class = parameters.A2
            elif 'A3Benchmark' in data:
                major_class = parameters.A3
            elif 'A4Benchmark' in data:
                major_class = parameters.A4
            elif 'ARIMA' in data:
                major_class = parameters.ARIMA
            elif 'seasonal' in data:
                major_class = parameters.seasonal

            Row = [data]
            file_path = data
            print("\n\n\nCurrent Test : ", IDX)
            print(data)

            ### Run all models in function 'run_comparison_tests' written below.
            ### Results returned are scores of the models run in specific 'data' dataset.
            Results = run_comparison_tests(file_path, major_class, Model_Switch)

            ### If there are no labeled anomalies in the dataset, then f1-scores cannot be calculated
            ### and therefore excluded from the tests.
            if Results==False:
                continue

            for val in Results:
                Row.append(val)
            Final_Values.append(Row)
            IDX += 1
            
        os.chdir('..')
        
    ## Export 'Final_Values' as csv file, containing all scores of all datasets on all models.
    if sum(Model_Switch) != 0:
        Comparison_tests = pd.DataFrame(Final_Values)
        Comparison_tests.columns = Cols
        Comparison_tests.to_csv(main_dir + "//test_results//comparison_test//Comparison_Tests_Python_all_scores.csv", sep='\t',
                        index=False)
        
        cols = Comparison_tests.columns[1:]
        datasets = ['A1','A2','A3','A4','ARIMA','seasonal']
        def group_value(value):
            for data_group_name in datasets:
                if data_group_name in value:
                    return data_group_name
                
        Comparison_tests['Group'] = Comparison_tests['Data Name'].apply(group_value)
        grouped = Comparison_tests.groupby('Group')
        Averaged_Values = []
        for group_name, group_data in grouped:
            group_values = [group_name]
            for col in cols:
                group_values.append(round(group_data[col].mean(),3))
            Averaged_Values.append(group_values)

        Averaged_Values = pd.DataFrame(Averaged_Values)
        Averaged_Values.columns = Comparison_tests.columns[:-1]
        Averaged_Values.to_csv(main_dir + "//test_results//comparison_test//Comparison_Tests_Python_averaged_scores.csv", sep='\t',
                index=False)





def run_comparison_tests(data_path, classes, switch):

    ### Designate save_path for plots.
    save_path = '..//..//test_results//comparison_test//plots//'

    ### Read dataset and do basic preparations for running model.
    df = pd.read_csv(data_path)
    df = data_aug.add_timestamp(df)
    df = df[['timestamps','value','anomaly']]
    df['value'] = df['value'].astype('float64')

    ### Plot data with true anomalies pinpointed.
    plot_real = True
    if plot_real:
        plotting_modules.save_plot(data_path, 'anomaly', df, save_path, 'real_anomalies')

    ### Check if dataset has no true anomalies.
    ### If it doesn't, f1-score cannot be measured and will be excluded from tests.
    real_anomalies = df['anomaly']
    if sum(real_anomalies)==0: ### true anomalies are 0 and cannot be measured
        return False


    ### Start running tests.
    ### 'Return_Values' is where scores for specific 'data' dataset will be stored and returned
    ### to be saved in 'Final_Values' from main.
    Return_Values = []
    if switch[0]==1:
        ### Run osESD
        T1 = time.time()
        osESD_anom_index = osESD_Detector.osESD(data=list(df['value']), dwins=classes.osESD_parameters.dwin,
                                                rwins=classes.osESD_parameters.rwin, train_size=classes.osESD_parameters.size,
                                                alpha=classes.osESD_parameters.alpha, maxr=classes.osESD_parameters.maxr,
                                                condition=classes.osESD_parameters.condition, time=list(df['timestamps']))
        T2 = time.time()
        real_index = real_anomalies[classes.osESD_parameters.size:]
        pred_index = data_aug.change_to_index(osESD_anom_index,len(df))
        results = scores_module.return_PRF_values(real_index, pred_index[classes.osESD_parameters.size:], T1, T2)
        if classes.osESD_parameters.plot:
            df['predictions'] = pred_index
            plotting_modules.save_plot(data_path, 'predictions', df, save_path, 'osESD_predictions')
        for result_idx in range(2,6):
            Return_Values.append(results[result_idx])


    if switch[1] == 1:
        ### Run isolation forest.
        T1 = time.time()
        classes.isolation_forest_parameters.contamination = max(sum(df['anomaly'])/len(df),0.001)
        isof_anom = ts_isolation_forest.run_isolation_forest(df,classes.isolation_forest_parameters)
        T2 = time.time()
        isof_anom_index = data_aug.change_to_index(isof_anom,len(df))

        results = scores_module.return_PRF_values(real_anomalies, isof_anom_index,T1, T2)
        if classes.isolation_forest_parameters.plot:
            df['predictions'] = isof_anom_index
            plotting_modules.save_plot(data_path, 'predictions', df, save_path, 'IsoF_predictions')
        for result_idx in range(2, 6):
            Return_Values.append(results[result_idx])

    if switch[2] == 1:
        ### Run random robust cut forest.
        T1 = time.time()
        rrcf_anom =  ts_random_robust_cut_classifier.run_rrcf(df,classes.rrcf_parameters)
        T2 = time.time()
        rrcf_anom_index = data_aug.change_to_index(rrcf_anom, len(df))
        results = scores_module.return_PRF_values(real_anomalies, rrcf_anom_index, T1, T2)
        if classes.rrcf_parameters.plot:
            df['predictions'] = rrcf_anom_index
            plotting_modules.save_plot(data_path, 'predictions', df, save_path, 'RRCF_predictions')
        for result_idx in range(2,6):
            Return_Values.append(results[result_idx])


    if switch[3] == 1:
        ### Run auto-encoder.
        T1 = time.time()
        AE_anom =  ts_AE.run_AE(df,classes.ae_parameters)
        T2 = time.time()
        AE_anom_index = data_aug.change_to_index(AE_anom, len(df))
        results = scores_module.return_PRF_values(real_anomalies, AE_anom_index, T1, T2)
        if classes.ae_parameters.plot:
            df['predictions'] = AE_anom_index
            plotting_modules.save_plot(data_path, 'predictions', df, save_path, 'AE_predictions')

        for result_idx in range(2,6):
            Return_Values.append(results[result_idx])

    if switch[4] == 1:
        ### Run variational auto-encoder.
        T1 = time.time()
        VAE_anom =  ts_VAE.run_VAE(df,classes.vae_parameters)
        T2 = time.time()
        VAE_anom_index = data_aug.change_to_index(VAE_anom, len(df))
        results = scores_module.return_PRF_values(real_anomalies, VAE_anom_index, T1, T2)
        if classes.vae_parameters.plot:
            df['predictions'] = VAE_anom_index
            plotting_modules.save_plot(data_path, 'predictions', df, save_path, 'VAE_predictions')

        for result_idx in range(2,6):
            Return_Values.append(results[result_idx])

    if switch[5] == 1:
        ### Run LSTM encoder decoder.
        T1 = time.time()
        LSTMED_anom = ts_LSTMED.run_LSTMED(df,classes.lstmed_parameters)
        T2 = time.time()
        LSTMED_anom_index = data_aug.change_to_index(LSTMED_anom, len(df))
        results = scores_module.return_PRF_values(real_anomalies, LSTMED_anom_index, T1, T2)
        if classes.lstmed_parameters.plot:
            df['predictions'] = LSTMED_anom_index
            plotting_modules.save_plot(data_path, 'predictions', df, save_path, 'LSTMED_predictions')

        for result_idx in range(2, 6):
            Return_Values.append(results[result_idx])

    return Return_Values


if __name__=="__main__":
    result_directory = 'test_results//comparison_test//plots'
    if not os.path.exists(result_directory):
        print("Creating results directory for comparison tests.")
        os.makedirs(result_directory)
    main()



