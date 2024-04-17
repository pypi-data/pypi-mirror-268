
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def run_isolation_forest(df,params):
    values = df['value'].values.reshape(-1, 1)
    isolation_forest = IsolationForest(n_estimators = params.n_estimators,
                                       contamination = params.contamination,
                                       max_samples = params.max_samples,
                                       random_state=42)
    isolation_forest.fit(values)
    anom_preds = isolation_forest.predict(values)
    anom_preds[anom_preds == 1] = 0
    anom_preds[anom_preds == -1] = 1
    pred_index = list(np.where(anom_preds == 1)[0])
    return pred_index


class isolation_forest_parameters:
    n_estimators = 100
    max_samples = 100
    contamination = 0.01
    plot = False

if __name__=='__main__':
    my_df = pd.read_csv('..//Datasets//synthetic//ARIMA1_ber_1.csv')
    pred = run_isolation_forest(my_df,isolation_forest_parameters)


