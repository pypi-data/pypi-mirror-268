
### Code for running 'auto_osESD'.
### Results will appear in 'osESD_test_results' if not provided otherwise.

############################################################
############################################################
############################################################
############################################################


import os
import argparse
import numpy as np
import pandas as pd

import time as t
from models import osESD_Detector
from utils import data_aug
from utils import scores_module
from utils import plotting_modules


'''
python main.py --dataset Datasets//synthetic//A2Benchmark_synthetic_19.csv --result_directory osESD_results

python main.py --dataset Datasets//auto_osESD_tests//unlabeled//AAPL.csv --result_directory osESD_results --labeled false

python main.py --dataset Datasets//synthetic//A2Benchmark_synthetic_19.csv --result_directory osESD_results --labeled true
'''


def osESD(dataset, plot, labeled, result_directory, value_name,
         timestamp_name, anomaly_name, size, condition, dwin,
         rwin, maxr, alpha):

    ### Read dataset.
    df = pd.read_csv(dataset)
    data_name = dataset.split("//")[-1][:-4]


    ### Add timestamps to dataset if not labeled.
    if timestamp_name in df.columns:
        df['timestamps']=df[timestamp_name]
    else:
        df['timestamps']=[i for i in range(1,len(df)+1)]

    ### Deal with whether dataset is labeled or not. If labeled, then f1-scores will be returned as well.
    ### If not, then only index and a plot of predicted anomalies will be returned.
    if labeled:
        df[['value','anomaly']]=df[[value_name,anomaly_name]]
    else:
        df['value']=df[value_name]

    ### Run osESD with designated parameters. The indices of anomalies will be returned to 'predictions'.
    T1 = t.time()
    predictions = osESD_Detector.osESD(data=list(df['value']),
                                    time=list(df['timestamps']),
                                    train_size=size, condition=condition,
                                    dwins=dwin, rwins=rwin,
                                    alpha=alpha, maxr=maxr)
    T2 = t.time()

    ### Change the indices to a list of 0's and 1's of anomalies.
    pred_index = data_aug.change_to_index(predictions, len(df))
    pred_index = pred_index[size:]

    ### Export txt file.
    Results = ""
    if labeled:
        real_index = df['anomaly'][size:]
        results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)
        Results = '\nPrecision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Time {:.4f} (sec)'.format(results[2],results[3],results[4],results[5])
        Results += "\n\nReal : [ "
        reals = np.where(df['anomaly'] == 1)
        Results += ', '.join([str(i) for i in reals[0]]) + " ]"
    Results += "\n\nAnomalies : [ "
    Results += ', '.join([str(i) for i in predictions]) + " ]"

    file_path = result_directory+"//"+data_name+"_osESD_result.txt"
    with open(file_path, "w") as file:
        file.write(Results)

    ### Export plot
    if plot:
        df['predictions'] = data_aug.change_to_index(predictions, len(df))
        plotting_modules.save_plot(data_path=data_name,column_name='predictions',
                                   df=df,save_path=result_directory+'//', model_name='osESD')

    print("Test successfully done.")
    print("Results can be seen in "+result_directory+" .")

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

    parser = argparse.ArgumentParser(description="Running online sequential ESD test code.")

    parser.add_argument("--dataset", type=str, required=True, help="Specify the dataset directory.")
    parser.add_argument("--plot", type=str2bool, default=True, help="Specify whether to draw a plot or not(default True).")
    parser.add_argument("--labeled", type=str2bool, default=True, help="Specify whether the dataset is labeled(default True).")
    parser.add_argument("--result_directory", type=str, default='osESD_results', help="Specify the result directory(default 'results').")
    parser.add_argument("--value_name", type=str, default='value',  help="Specify the value column name(default 'value').")

    parser.add_argument("--timestamp_name", type=str, default='timestamps', help="Specify the timestamp column name(default 'timestamps').")
    parser.add_argument("--anomaly_name", type=str, default='anomaly', help="Specify the plot directory(default 'anomaly').")
    parser.add_argument("--size", type=int, default=100, help="Specify window size(default 100).")
    parser.add_argument("--condition", type=str2bool, default=False, help="Specify the choice function(default True, And).")
    parser.add_argument("--dwin", type=int, default=5, help="Specify leap size for change-rate trend vector(default 5).")

    parser.add_argument("--rwin", type=int, default=5, help="Specify within-k2 trend size(default 5).")
    parser.add_argument("--maxr", type=int, default=10, help="Specify max number of anomalies in window(default 10).")
    parser.add_argument("--alpha", type=float, default=0.01, help="Specify hypothesis testing alpha value(default 0.01).")

    args = parser.parse_args()

    if not os.path.exists(args.result_directory):
        os.makedirs(args.result_directory)

    main(args.dataset, args.plot, args.labeled, args.result_directory, args.value_name,
         args.timestamp_name, args.anomaly_name, args.size, args.condition, args.dwin,
         args.rwin,args.maxr, args.alpha)


