#!/usr/bin/env python3

### Code for running 'auto_osESD'.
### Results will appear in 'auto_osESD_test_results' if not provided otherwise.

############################################################
############################################################
############################################################
############################################################

import os
import argparse
import numpy as np
import pandas as pd
import time as t

from models import auto_osESD_Detector
from utils import data_aug
from utils import scores_module
from utils import plotting_modules

'''
python auto_osESD.py --dataset Datasets//synthetic//seasonal_ber_6.csv

python auto_oseSD.py --dataset Datasets//synthetic//seasonal_ber_6.csv --labeled True --result_directory auto_osESD_results --sizes "50,100,150,200" --conditions "0,1" --maxrs "3,5,7,10,20" --dwins "2,5,10,20,30" --rwins "4,5,10,20,30" --alphas "0.0001,0.005,0.01,0.05" --weights "0,0,1,0.1" --learning_length 0.15 --min_max_switch False

python auto_osESD.py --dataset Datasets//auto_osESD_tests//unlabeled//AAPL.csv --result_directory auto_osESD_results --labeled false
'''

def main(dataset, plot, labeled, result_directory, value_name,
         timestamp_name, anomaly_name, sizes, conditions, dwins,
         rwins, maxrs, alphas, weights, learning_length,
         min_max_switch):

    ### Read dataset.
    df = pd.read_csv(dataset)
    data_name = dataset.split("//")[-1]
    # print(data_name)
    # adsaasd
    ### Add timestamps to dataset if not labeled.
    if timestamp_name in df.columns:
        df['timestamps'] = df[timestamp_name]
    else:
        df['timestamps'] = [i for i in range(1, len(df) + 1)]

    ### Deal with whether dataset is labeled or not. If labeled, then f1-scores will be returned as well.
    ### If not, then only index and a plot of predicted anomalies will be returned.
    if labeled:
        df[['value', 'anomaly']] = df[[value_name, anomaly_name]]
    else:
        df['value'] = df[value_name]

    ### If condition is not explicitly provided, use parameters set within 'auto_osESD' implementation.
    if args.sizes == [] and args.conditions == [] and args.dwins == [] and args.rwins == [] and args.maxrs == [] and args.alphas == [] :
        parameters = []
    else:
        parameters = [
            ["--WindowSizes", sizes],
            ["--AndOr", conditions],
            ["--MaxRs", maxrs],
            ["--Dwins", dwins],
            ["--Rwins", rwins],
            ["--Alphas", alphas]
        ]

    ### Run function 'osESD_Detector_auto' which will return [anomaly_list, anomaly_indices, best_parameters].
    ### Then use best_parameters (tuning_results[2]) to find final anomalies in full dataset.
    T1 = t.time()
    tuning_results = auto_osESD_Detector.osESD_Detector_auto(database=df, data_label=labeled,
                                                             weights=weights,
                                                             par_len=learning_length,
                                                             parameters=parameters, min_max_switch=min_max_switch)
    tuning_params = tuning_results[2]
    predictions = auto_osESD_Detector.run_osESD_modified(data=list(df['value']), time=list(df['timestamps']),
                                                        full_size=len(df), init_size=tuning_params[1],
                                                        params=tuning_params)
    T2 = t.time()

    pred_index = np.where(np.array(predictions)==1)

    Results = ""
    if labeled:
        real_index = df['anomaly'][tuning_params[1]:]
        results = scores_module.return_PRF_values(real_index, predictions[tuning_params[1]:], T1, T2)
        Results = '\nPrecision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Time {:.4f} (sec)'.format(results[2],results[3],results[4],results[5])
        Results += "\n\nReal : [ "
        reals = np.where(df['anomaly'] == 1)
        Results += ', '.join([str(i) for i in reals[0]]) + " ]"

    Results += "\n\nAnomalies : [ "
    Results += ', '.join([str(i) for i in list(pred_index[0])]) + " ]"

    file_path = result_directory+"//"+data_name[:-4]+"_auto_osESD_result.txt"
    with open(file_path, "w") as file:
        file.write(Results)

    if plot:
        df['predictions'] = predictions
        plotting_modules.save_plot(data_path=data_name,column_name='predictions',
                                   df=df,save_path=result_directory+'//', model_name='auto_osESD')

    print("Test successfully done.")
    print("Results can be seen in "+result_directory+" .")


### Function for accepting string type booleans in cmd.
def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == '__main__':
    ### Read in arguments.
    parser = argparse.ArgumentParser(description="Running online sequential ESD test code.")

    parser.add_argument("--dataset", type=str, required=True, help="Specify the dataset directory.")
    parser.add_argument("--plot", type=str2bool, default=True, help="Specify whether to draw a plot or not(default True).")
    parser.add_argument("--labeled", type=str2bool, default=True, help="Specify whether the dataset is labeled(default True).")
    parser.add_argument("--result_directory", type=str, default='auto_osESD_results', help="Specify the result directory(default 'results').")
    parser.add_argument("--value_name", type=str, default='value',  help="Specify the value column name(default 'value').")

    parser.add_argument("--timestamp_name", type=str, default='timestamps', help="Specify the timestamp column name(default 'timestamps').")
    parser.add_argument("--anomaly_name", type=str, default='anomaly', help="Specify the plot directory(default 'anomaly').")
    parser.add_argument("--sizes", type=str, default="", help="Specify window sizes.")
    parser.add_argument("--conditions", type=str, default="", help="Specify the choice functions.")
    parser.add_argument("--dwins", type=str, default="", help="Specify leap sizes for change-rate trend vector.")

    parser.add_argument("--rwins", type=str, default="", help="Specify within-k2 trend sizes.")
    parser.add_argument("--maxrs", type=str, default="", help="Specify max numbers of anomalies in window.")
    parser.add_argument("--alphas", type=str, default="", help="Specify hypothesis testing alpha values.")
    parser.add_argument("--weights", type=str, default="0,0,1,0.01", help="Specify weights used when grid searching(Precision, Recall, F1-score, runtime) (default [0,0,1,0].")
    parser.add_argument("--learning_length", type=float, default=0.2, help="Specify length used in grid searching(default 0.2).")

    parser.add_argument("--min_max_switch", type=str2bool, default=False, help="Specify whether parameters given are end points(default False).")
    args = parser.parse_args()

    ### Set arguments
    if args.sizes != "": args.sizes = [int(i) for i in args.sizes.split(',')]
    else: args.sizes = []
    if args.conditions != "": args.conditions = [int(i) for i in args.conditions.split(',')]
    else: args.conditions = []
    if args.dwins != "": args.dwins = [int(i) for i in args.dwins.split(',')]
    else: args.dwins = []
    if args.rwins != "": args.rwins = [int(i) for i in args.rwins.split(',')]
    else: args.rwins = []
    if args.maxrs != "": args.maxrs = [int(i) for i in args.maxrs.split(',')]
    else: args.maxrs = []
    if args.alphas != "": args.alphas = [float(i) for i in args.alphas.split(',')]
    else: args.alphas = []
    args.weights = [float(i) for i in args.weights.split(',')]

    ### If weights is not 4 numbers, then raise exception.
    if len(args.weights)!=4:
        raise "Weights must be 4 float numbers, [precision recall f1-time runtime] order."

    ### Make result directory if not existing.
    if not os.path.exists(args.result_directory):
        os.makedirs(args.result_directory)

    ### Run main
    main(args.dataset, args.plot, args.labeled, args.result_directory, args.value_name,
         args.timestamp_name, args.anomaly_name, args.sizes, args.conditions, args.dwins,
         args.rwins, args.maxrs, args.alphas, args.weights, args.learning_length,
         args.min_max_switch)


