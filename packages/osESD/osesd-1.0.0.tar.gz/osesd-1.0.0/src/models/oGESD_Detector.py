
from . import oGESD_Test
from . import oGESD_Transform

def oGESD(data, dwins, rwins, train_size, alpha, maxr, time=None):
    offline_data = data[:train_size]
    online_data = data[train_size:len(data)]
    offline_time = time[:train_size]
    online_time = time[train_size:len(data)]
    r_ins = oGESD_Transform.TRES(data = offline_data, time = offline_time, wins = rwins)
    c_ins = oGESD_Transform.TCHA(data = offline_data, time = offline_time, wins = dwins)
    SESD_TRES = oGESD_Test.SESD_tres(data = r_ins.tres.copy(), alpha = alpha, maxr = maxr)
    SESD_TCHA = oGESD_Test.SESD_tcha(data = c_ins.tcha.copy(), alpha = alpha, maxr = maxr)
    anomaly_index = []
    for i in range(len(online_data)):
        up_val,t = r_ins.update(online_data[i], online_time[i])
        ranom = SESD_TRES.test(up_val,t)
        up_val = c_ins.update(online_data[i], online_time[i])
        canom = SESD_TCHA.test(up_val)
        if (canom or ranom):
            anomaly_index.append(i+train_size)
            D = r_ins.data.copy()
            T = r_ins.time.copy()
            del D[rwins-1]
            del T[rwins-1]
            x_bar = ((rwins*r_ins.x_bar) - r_ins.time[rwins-1]) / (rwins-1)
            y_bar = ((rwins*r_ins.y_bar) - r_ins.data[rwins-1]) / (rwins-1)
            beta_ = sum((T-x_bar)*(D-y_bar))/sum((T-x_bar)**2)
            alpha_ = y_bar - beta_*x_bar
            rep = alpha_ + beta_*T[rwins-2]
            c_ins.replace(rep)
            r_ins.replace(rep)

    return (anomaly_index)
