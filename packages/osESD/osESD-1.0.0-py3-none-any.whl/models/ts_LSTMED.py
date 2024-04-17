import numpy as np
import pandas as pd
import random
np.random.seed(42)
random.seed(42)

from merlion.utils import TimeSeries
from merlion.models.anomaly.lstm_ed import LSTMEDConfig, LSTMED

def run_LSTMED(data, parameters):
    train_data = data['value']
    train_labels =  data['anomaly']
    train_data = TimeSeries.from_pd(train_data)
    train_labels = TimeSeries.from_pd(train_labels)
    config = LSTMEDConfig(lr=parameters.lr,batch_size=parameters.batch_size)
    model = LSTMED(config)
    model.train(train_data=train_data, anomaly_labels=train_labels)
    train_scores = model.get_anomaly_label(train_data)
    pred_index = list(np.where(train_scores.to_pd()>0)[0])
    return pred_index

class LSTMED_parameters:
    lr = 0.0003
    batch_size = 64
    plot = True

if __name__=='__main__':
    my_df = pd.read_csv('..//Datasets//synthetic//ARIMA1_ber_1.csv')
    pred = run_LSTMED(my_df,LSTMED_parameters)


