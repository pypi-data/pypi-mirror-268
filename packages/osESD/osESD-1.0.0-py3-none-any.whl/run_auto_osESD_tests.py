
### Code for replicating auto_osESD results.
### Results will appear in 'test_results//auto_osESD'.

############################################################
############################################################
############################################################
############################################################


import os
import pandas as pd
import time as t
import random
import torch
import numpy as np

from models import auto_osESD_Detector
from utils import scores_module
from utils import plotting_modules
from utils import data_aug

random.seed(42)
np.random.seed(42)
torch.manual_seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(42)


def main():

    ### Set main_dir before tests due to numerous directory changes later.
    main_dir = os.getcwd()
    Model_Name = 'osESD_auto'

    ### Prepare column names.
    Cols = ['Data Name']
    Cols.append(Model_Name + str('__recall'))
    Cols.append(Model_Name + str('__precision'))
    Cols.append(Model_Name + str('__f1score'))
    Cols.append(Model_Name + str('__time (sec)'))

    ### Weights for auto_osESD. In order, precision, recall, f1-score and run-time.
    ### Currently, it is set to find parameters that bring best f1-scores.
    testing_weights = [0, 0, 1, 0]
    parameter_learning_length = 0.2

    ### Parameters that will be used for grid searching.
    parameters = [
        ["--WindowSizes", [50,100,150,200]],
        ["--AndOr", [1, 0]],
        ["--MaxRs", [3,5,7,10,20]],
        ["--Dwins", [2,5,10,20,30]],
        ["--Rwins", [4,5,10,20,30]],
        ["--Alphas", [0.001,0.005,0.01,0.05]]
    ]

    ### Start of tests.
    ### 'RESULTS' will store all results of auto_osESD according to each dataset.
    ### 'PARAMS' will store all parameters of auto_osESD according to each dataset.
    IDX = 1
    RESULTS = []
    PARAMS = []
    os.chdir('Datasets//auto_osESD_tests')

    Use_labeled = False
    for data_type in os.listdir():
        ### If dataset is labeled, then simply use prior 'paramater_learning_length' amount for grid searching.
        ### If not, then pseudo y anomaly values will be added to 'parameter_learning_length' amount for grid searching.
        ### After finding the best parameters, these will be used for finding anomalies in the whole dataset.
        if data_type == 'labeled':
            labeled = True
            # continue
            Use_labeled = True
        else:
            labeled = False

        os.chdir(data_type)
        for data_name in os.listdir():
            ### Run code in all datasets.

            data = pd.read_csv(data_name)
            data['value'] = data['value'].astype('float64')

            ### If labeled, change columns appropriately.
            ### If not, continue without 'anomaly'.

            data = data_aug.add_timestamp(data)
            if labeled:
                data = data[['timestamps', 'value', 'anomaly']]
            else:
                data = data[['timestamps','value']]

            print("\n\n\nCurrent Test : ", IDX)
            print(data_name)
            Start_time = t.time()

            ### Run function 'osESD_Detector_auto' which will return [anomaly_list, anomaly_indices, best_parameters].
            ### Then use best_parameters (tuning_results[2]) to find final anomalies in full dataset.
            tuning_results = auto_osESD_Detector.osESD_Detector_auto(database=data, data_label=labeled,
                                                                     weights=testing_weights,
                                                                     par_len=parameter_learning_length,
                                                                     parameters=parameters, min_max_switch=False)

            tuning_params = tuning_results[2]

            data = pd.read_csv(data_name)
            data['value'] = data['value'].astype('float64')
            data = data_aug.add_timestamp(data)
            if labeled:
                data = data[['timestamps', 'value', 'anomaly']]
            else:
                data = data[['timestamps','value']]

            pred_anoms = auto_osESD_Detector.run_osESD_modified(data=list(data['value']), time=list(data['timestamps']),
                                                                full_size=len(data), init_size=tuning_params[1],
                                                                params=tuning_params)  # print(pred_anoms)
            End_time = t.time()

            ### Prepare list to save all scores and parameters. [:-4] for deleting '.csv' at the end of 'data_name'.
            final_parameters = [data_name[:-4]]
            data_results = [data_name[:-4]]

            ### Add values to RESULTS and PARAMS.
            if labeled:
                true_outlier = data['anomaly'][tuning_params[1] + 1:]
                osESD_auto_values = scores_module.Precision_Recall_f1score(true_outlier, pred_anoms[tuning_params[1] + 1:])
                osESD_auto_values.append(End_time - Start_time)
                for val in osESD_auto_values:
                    data_results.append(val)
                RESULTS.append(data_results)

            for par in tuning_params:
                final_parameters.append(par)
            PARAMS.append(final_parameters)

            data['predictions'] = pred_anoms
            plotting_modules.save_plot(data_path=data_name, column_name='predictions', df=data,
                                       save_path=main_dir + "//test_results//auto_osESD_test//plots//",
                                       model_name="auto_osESD")
            IDX += 1

        os.chdir('..')
    os.chdir('..')

    ### Prepare columns
    result_cols = ["Data Name", "auto_osESD__recall", "auto_osESD__precision", "auto_osESD__f1score",
                   "auto_osESD__time"]
    param_cols = ["Data Name", "Function", "Window Size", "Max R", "D window", "R window", "Alpha"]

    ### Export RESULTS and PARAMS as csv file.

    if True:
        if Use_labeled :
            result_csv = pd.DataFrame(RESULTS)
            result_csv.columns = result_cols
            result_csv.to_csv(main_dir + "//test_results//auto_osESD_test//auto_osESD_Results.csv" ,sep='\t', index=False)
        params_csv = pd.DataFrame(PARAMS)
        params_csv.columns = param_cols
        params_csv.to_csv(main_dir + "//test_results//auto_osESD_test//auto_osESD_Params.csv", sep='\t', index=False)

if __name__=="__main__":

    result_directory = 'test_results//auto_osESD_test//plots'
    if not os.path.exists(result_directory):
        print("Creating results directory for auto_osESD tests.")
        os.makedirs(result_directory)

    main()
