
import pandas as pd
import numpy as np
import heapq
import rrcf

def run_rrcf(df,params):
    values = df['value']
    num_tree = params.num_tree
    shingle_size = params.shingle_size
    tree_size = params.tree_size
    forest = []
    for _ in range(num_tree):
        tree = rrcf.RCTree()
        forest.append(tree)
    points = rrcf.shingle(values, size=shingle_size)
    avg_codisp = {}
    for index, point in enumerate(points):
        for tree in forest:
            if len(tree.leaves) > tree_size:
                tree.forget_point(index - tree_size)
            tree.insert_point(point, index=index)
            new_codisp = tree.codisp(index)
            if not index in avg_codisp:
                avg_codisp[index] = 0
            avg_codisp[index] += new_codisp / num_tree
    n = int(0.01 * len(df))
    real_anom_index = np.where(df['anomaly'] == 1)
    pred_index = heapq.nlargest(n, avg_codisp, key=avg_codisp.get)
    anom_preds = pd.Series([0 for _ in range(len(df))])
    anom_preds[pred_index] = 1
    pred_index = list(np.where(anom_preds == 1)[0])
    return pred_index

class rrcf_parameters:
    num_tree = 40
    shingle_size = 4
    tree_size = 256
    plot = True

if __name__=='__main__':
    my_df = pd.read_csv('..//Datasets//synthetic//ARIMA1_ber_1.csv')
    pred = run_rrcf(my_df,rrcf_parameters)


