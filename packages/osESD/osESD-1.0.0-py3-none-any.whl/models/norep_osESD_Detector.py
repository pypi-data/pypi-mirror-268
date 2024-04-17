
from . import osESD_Test
from . import osESD_Transform

def norep_osESD(data, dwins, rwins, train_size, alpha, maxr, time=None):
    offline_data = data[:train_size]
    online_data = data[train_size:len(data)]
    offline_time = time[:train_size]
    online_time = time[train_size:len(data)]
    r_ins = osESD_Transform.TRES(data = offline_data, time = offline_time, wins = rwins)
    c_ins = osESD_Transform.TCHA(data = offline_data, time = offline_time, wins = dwins)
    SESD_TRES = osESD_Test.SESD_tres(data = r_ins.tres.copy(), alpha = alpha, maxr = maxr)
    SESD_TCHA = osESD_Test.SESD_tcha(data = c_ins.tcha.copy(), alpha = alpha, maxr = maxr)
    anomaly_index = []
    for i in range(len(online_data)):
        ranom = SESD_TRES.test(r_ins.update(online_data[i], online_time[i]))
        canom = SESD_TCHA.test(c_ins.update(online_data[i], online_time[i]))
        if (canom or ranom):
            anomaly_index.append(i+train_size)

    return (anomaly_index)
