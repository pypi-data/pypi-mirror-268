
### Code for running all models explained in paper.
### Results will appear in 'test_results//single_test' with results and plots.

############################################################
############################################################
############################################################
############################################################

import os
import random
import pandas as pd
import time as t
import numpy as np
import torch

from models import osESD_Detector
from models import ts_isolation_forest
from models import ts_random_robust_cut_classifier
from models import ts_AE
from models import ts_VAE
from models import ts_LSTMED
from models import sosESD_Detector
from models import oGESD_Detector
from models import norep_osESD_Detector

from utils import scores_module
from utils import data_aug
from utils import plotting_modules

random.seed(42)
np.random.seed(42)
torch.manual_seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(42)

def main():

    ### Set paths for data and saving points.
    ### 'dataset_path' is directory where dataset currently is,
    ### 'data_name' is name of dataset in 'dataset_path'.
    ### 'save_path' is where results will be saved.
    dataset_path = "Datasets//synthetic//"
    data_name = 'A3Benchmark_TS10.csv'
    save_path = 'test_results//single_test//'
    print(data_name)

    ### Read in the dataset and do basic preprocessing for running models.
    df = pd.read_csv(os.path.join(dataset_path, data_name))
    df = data_aug.add_timestamp(df)
    df = df[['timestamps','value','anomaly']]

    ### Check if dataset has no true anomalies.
    ### If it doesn't, f1-score cannot be measured and tests will not run.
    if sum(df['anomaly'])==0:
        raise Exception("No true anomalies in dataset, cannot measure f1-score.")

    ### Print true anomalies.
    print("Real anomalies : ",np.where(df['anomaly'] == 1)[0])

    ### Plot function. if True, will plot real or predictions in save_point.
    Plot_Real, Plot_Pred = True, True
    if Plot_Real:
        plotting_modules.save_plot(data_name, 'anomaly', df, save_path+'plots//', 'real_anomalies')

    ### Model switch. If set to 0, then will not run. If 1, will run.
    ### In order, osESD, IF, RRCF, AE,  VAE,  LSTMED, oGESD, sosESD, norep_osESD .
    #      osESD, IF, RRCF, AE,  VAE,  LSTMED, oGESD, sosESD, norep_osESD
    test = [1,    1,   1,   1,    1,    1,      1,      1,       1]

    ### Must be only 0 or 1.
    if all(x == 0 or x == 1 for x in test) == False:
        raise "Models switch must be either 0 or 1."

    if test[0] == 1:
        ### Run osESD.
        class osESD_parameters:
            size = 100
            dwin = 2
            rwin = 4
            maxr = 10
            alpha = 0.01
            condition = False

        T1 = t.time()
        predictions = osESD_Detector.osESD(data=list(df['value']),
                                           time=list(df['timestamps']),
                                           train_size=osESD_parameters.size,
                                           dwins=osESD_parameters.dwin,
                                           rwins=osESD_parameters.rwin,
                                           alpha=osESD_parameters.alpha,
                                           condition=osESD_parameters.condition,
                                           maxr=osESD_parameters.maxr)


        T2 = t.time()
        real_index = df['anomaly'][osESD_parameters.size:]
        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[osESD_parameters.size:]
        osESD_results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        Results = "\nPredicted anomalies : ["
        Results += ', '.join([str(i) for i in predictions]) + "]\n"
        Results += "osESD results, Number of real anomalies : {} , Number of predicted anomalies : {} \n".format(osESD_results[0],osESD_results[1])
        Results += "Precision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Run time : {:.4f} (sec)".format(osESD_results[2],osESD_results[3],osESD_results[4],osESD_results[5])
        print(Results)

        with open(save_path+data_name[:-4]+"_osESD_results.txt", "w") as file:
            file.write(Results)

        if Plot_Pred:
            df['predictions']=data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_name, 'predictions', df, save_path+'plots//', 'single_test_osESD_predictions' )

        print('\n\n')


    if test[1] == 1:
        ### Run isolation forest.
        class isolation_forest_parameters:
            n_estimators = 100
            max_samples = 100
            contamination = 0.01
            plot = True

        T1 = t.time()
        isolation_forest_parameters.contamination = max(sum(df['anomaly'])/len(df),0.001)
        predictions = ts_isolation_forest.run_isolation_forest(df,isolation_forest_parameters)
        T2 = t.time()

        real_index = df['anomaly'][osESD_parameters.size:]
        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[osESD_parameters.size:]
        isolation_forest_results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        Results = "\nPredicted anomalies : ["
        Results += ', '.join([str(i) for i in predictions]) + "]\n"
        Results += "isolation_forest results, Number of real anomalies : {} , Number of predicted anomalies : {} \n".format(isolation_forest_results[0],isolation_forest_results[1])
        Results += "Precision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Run time : {:.4f} (sec)".format(isolation_forest_results[2],isolation_forest_results[3],isolation_forest_results[4],isolation_forest_results[5])
        print(Results)

        with open(save_path+data_name[:-4]+"_isolation_forest_results.txt", "w") as file:
            file.write(Results)

        if Plot_Pred:
            df['predictions']=data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_name, 'predictions', df, save_path+'plots//', 'single_test_isolation_forest_predictions' )

    if test[2] == 1:
        ### Run random robust cut forest.
        class rrcf_parameters:
            num_tree = 40
            shingle_size = 4
            tree_size = 256
            plot = True

        T1 = t.time()
        predictions =  ts_random_robust_cut_classifier.run_rrcf(df,rrcf_parameters)
        T2 = t.time()

        real_index = df['anomaly'][osESD_parameters.size:]
        pred_index = data_aug.change_to_index(predictions, len(df))
        pred_index = pred_index[osESD_parameters.size:]
        rrcf_results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        Results = "\nPredicted anomalies : ["
        Results += ', '.join([str(i) for i in predictions]) + "]\n"
        Results += "rrcf results, Number of real anomalies : {} , Number of predicted anomalies : {} \n".format(rrcf_results[0],rrcf_results[1])
        Results += "Precision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Run time : {:.4f} (sec)".format(rrcf_results[2],rrcf_results[3],rrcf_results[4],rrcf_results[5])
        print(Results)

        with open(save_path+data_name[:-4]+"_rrcf_results.txt", "w") as file:
            file.write(Results)

        if Plot_Pred:
            df['predictions']=data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_name, 'predictions', df, save_path+'plots//', 'single_test_rrcf_predictions' )



    if test[3] == 1:
        ### Run auto-encoder.
        class AE_parameters:
            lr = 0.0003
            batch_size = 64
            plot = True

        T1 = t.time()
        predictions = ts_AE.run_AE(df,AE_parameters)
        T2 = t.time()
        real_index = df['anomaly'][osESD_parameters.size:]
        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[osESD_parameters.size:]
        AE_results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        Results = "\nPredicted anomalies : ["
        Results += ', '.join([str(i) for i in predictions]) + "]\n"
        Results += "AE results, Number of real anomalies : {} , Number of predicted anomalies : {} \n".format(AE_results[0],AE_results[1])
        Results += "Precision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Run time : {:.4f} (sec)".format(AE_results[2],AE_results[3],AE_results[4],AE_results[5])
        print(Results)

        with open(save_path+data_name[:-4]+"_AE_results.txt", "w") as file:
            file.write(Results)

        if Plot_Pred:
            df['predictions']=data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_name, 'predictions', df, save_path+'plots//', 'single_test_AE_predictions' )


    if test[4] == 1:
        ### Run variational auto-encoder.
        class VAE_parameters:
            lr = 0.0003
            batch_size = 64
            plot = True

        T1 = t.time()
        predictions = ts_VAE.run_VAE(df,VAE_parameters)
        print(predictions)
        T2 = t.time()
        real_index = df['anomaly'][osESD_parameters.size:]
        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[osESD_parameters.size:]
        VAE_results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        Results = "\nPredicted anomalies : ["
        Results += ', '.join([str(i) for i in predictions]) + "]\n"
        Results += "VAE results, Number of real anomalies : {} , Number of predicted anomalies : {} \n".format(VAE_results[0],VAE_results[1])
        Results += "Precision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Run time : {:.4f} (sec)".format(VAE_results[2],VAE_results[3],VAE_results[4],VAE_results[5])
        print(Results)

        with open(save_path+data_name[:-4]+"_VAE_results.txt", "w") as file:
            file.write(Results)

        if Plot_Pred:
            df['predictions']=data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_name, 'predictions', df, save_path+'plots//', 'single_test_VAE_predictions' )


    if test[5] == 1:
        ### Run LSTM based encoder decoder.
        class LSTMED_parameters:
            lr = 0.0003
            batch_size = 64
            plot = True

        T1 = t.time()
        predictions = ts_LSTMED.run_LSTMED(df,LSTMED_parameters)
        print(predictions)
        T2 = t.time()
        real_index = df['anomaly'][osESD_parameters.size:]
        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[osESD_parameters.size:]
        LSTMED_results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        Results = "\nPredicted anomalies : ["
        Results += ', '.join([str(i) for i in predictions]) + "]\n"
        Results += "LSTMED results, Number of real anomalies : {} , Number of predicted anomalies : {} \n".format(LSTMED_results[0],LSTMED_results[1])
        Results += "Precision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Run time : {:.4f} (sec)".format(LSTMED_results[2],LSTMED_results[3],LSTMED_results[4],LSTMED_results[5])
        print(Results)

        with open(save_path+data_name[:-4]+"_LSTMED_results.txt", "w") as file:
            file.write(Results)

        if Plot_Pred:
            df['predictions']=data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_name, 'predictions', df, save_path+'plots//', 'single_test_LSTMED_predictions' )

    if test[6] == 1:
        ### Run oGESD.
        class options:
            size = 100
            dwin = 2
            rwin = 4
            maxr = 10
            alpha = 0.01

        T1 = t.time()
        predictions = oGESD_Detector.oGESD(data=list(df['value']),
                                           time=list(df['timestamps']),
                                           train_size=options.size,
                                           dwins=options.dwin,
                                           rwins=options.rwin,
                                           alpha=options.alpha,
                                           maxr=options.maxr)
        T2 = t.time()
        real_index = df['anomaly'][options.size:]
        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[options.size:]
        oGESD_results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        Results = "\nPredicted anomalies : ["
        Results += ', '.join([str(i) for i in predictions]) + "]\n"
        Results += "oGESD results, Number of real anomalies : {} , Number of predicted anomalies : {} \n".format(oGESD_results[0],oGESD_results[1])
        Results += "Precision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Run time : {:.4f} (sec)".format(oGESD_results[2],oGESD_results[3],oGESD_results[4],oGESD_results[5])
        print(Results)

        with open(save_path+data_name[:-4]+"_oGESD_results.txt", "w") as file:
            file.write(Results)

        if Plot_Pred:
            df['predictions']=data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_name, 'predictions', df, save_path+'plots//', 'single_test_oGESD_predictions' )

    if test[7] == 1:
        ### Run sosESD.
        class options:
            size = 100
            dwin = 2
            rwin = 4
            maxr = 10
            alpha = 0.01

        T1 = t.time()
        predictions = sosESD_Detector.sosESD(data=list(df['value']),
                                             wins=options.size,
                                             alpha=options.alpha,
                                             maxr=options.maxr)
        print(predictions)
        T2 = t.time()
        real_index = df['anomaly'][options.size:]
        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[options.size:]
        sosESD_results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        Results = "\nPredicted anomalies : ["
        Results += ', '.join([str(i) for i in predictions]) + "]\n"
        Results += "sosESD results, Number of real anomalies : {} , Number of predicted anomalies : {} \n".format(sosESD_results[0],sosESD_results[1])
        Results += "Precision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Run time : {:.4f} (sec)".format(sosESD_results[2],sosESD_results[3],sosESD_results[4],sosESD_results[5])
        print(Results)

        with open(save_path+data_name[:-4]+"_sosESD_results.txt", "w") as file:
            file.write(Results)

        if Plot_Pred:
            df['predictions']=data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_name, 'predictions', df, save_path+'plots//', 'single_test_sosESD_predictions' )

    if test[8] == 1:
        ### Run norep_osESD.
        class options:
            size = 100
            dwin = 10
            rwin = 10
            maxr = 10
            alpha = 0.01
            visualize_pred = False
            visualize_real = False

        T1 = t.time()
        predictions = norep_osESD_Detector.norep_osESD(data=list(df['value']),
                                                       time=list(df['timestamps']),
                                                       train_size=options.size,
                                                       dwins=options.dwin,
                                                       rwins=options.rwin,
                                                       alpha=options.alpha,
                                                       maxr=options.maxr)
        T2 = t.time()
        real_index = df['anomaly'][options.size:]
        pred_index = data_aug.change_to_index(predictions,len(df))
        pred_index = pred_index[options.size:]
        norep_osESD_results = scores_module.return_PRF_values(real_index, pred_index, T1, T2)

        Results = "\nPredicted anomalies : ["
        Results += ', '.join([str(i) for i in predictions]) + "]\n"
        Results += "norep_osESD results, Number of real anomalies : {} , Number of predicted anomalies : {} \n".format(norep_osESD_results[0],norep_osESD_results[1])
        Results += "Precision : {:.4f}, Recall : {:.4f}, F1-score : {:.4f}, Run time : {:.4f} (sec)".format(norep_osESD_results[2],norep_osESD_results[3],norep_osESD_results[4],norep_osESD_results[5])
        print(Results)

        with open(save_path+data_name[:-4]+"_norep_osESD_results.txt", "w") as file:
            file.write(Results)

        if Plot_Pred:
            df['predictions']=data_aug.change_to_index(predictions,len(df))
            plotting_modules.save_plot(data_name, 'predictions', df, save_path+'plots//', 'single_test_norep_osESD_predictions' )


if __name__=="__main__":
    result_directory = 'test_results//single_test//plots'
    if not os.path.exists(result_directory):
        print("Creating results directory for single run tests.")
        os.makedirs(result_directory)
    main()




