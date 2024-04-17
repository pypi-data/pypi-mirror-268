
from . import sosESD_Test

def sosESD(data, wins, alpha, maxr):
    current_data = data[:wins]
    anomaly_index = []
    SESD_TRES = sosESD_Test.SESD(data=current_data, alpha=alpha, maxr=maxr)
    for i in range(wins,len(data)):
        anom = SESD_TRES.test(data[i])
        if (anom):
            anomaly_index.append(i)
    return (anomaly_index)
