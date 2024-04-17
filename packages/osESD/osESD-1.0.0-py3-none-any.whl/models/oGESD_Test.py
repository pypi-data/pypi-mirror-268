

import numpy as np
import scipy.stats as stats

class SESD_tres:
    def __init__(self, data=None, alpha=0.01, maxr=10):
        self.mean = 0
        self.sqsum = 0
        self.alpha = alpha
        self.maxr = maxr
        self.data = data
        self.size = len(data)
        self.mean = np.mean(data)
        self.sqsum = np.sum(np.square(data))

    def test(self, f, on):
        self.data = np.append(self.data[1:], on)
        GESD_ = GESD(data=self.data, alpha=self.alpha, max_outliers=self.maxr)
        anoms = GESD_.test()
        if anoms and (anoms[-1] == len(self.data) - 1):
            return True
        return False


class SESD_tcha:
    def __init__(self, data=None, alpha=0.01, maxr=10):
        self.mean = 0
        self.sqsum = 0
        self.alpha = alpha
        self.maxr = maxr
        self.data = data
        self.size = len(data)
        self.mean = np.mean(data)
        self.sqsum = np.sum(np.square(data))

    def test(self, on):
        self.data = np.append(self.data[1:], on)
        GESD_ = GESD(data=self.data, alpha=self.alpha, max_outliers=self.maxr)
        anoms = GESD_.test()
        if anoms and (anoms[-1] == len(self.data) - 1):
            return True
        return False



class GESD:
    def __init__(self, data=None, alpha=0.01, max_outliers=None):
        self.data = data
        self.alpha = alpha
        if max_outliers is None:
            self.max_outliers = int(len(self.data)*0.08)
        else:
            self.max_outliers = max_outliers

    def test(self):
        ANOMALIES = []
        for iterations in range(1, self.max_outliers + 1):
            stat, max_index = self.Ri_stat(self.data)
            critical = self.Critical_value(len(self.data))
            if stat > critical:
                ANOMALIES.append(max_index)
            else:
                break
            self.data = np.delete(self.data, max_index)
        return ANOMALIES

    def Ri_stat(self, y):
        std_dev = np.std(y,ddof=1)
        avg_y = np.mean(y)
        abs_val_minus_avg = abs(y - avg_y)
        max_of_deviations = max(abs_val_minus_avg)
        max_ind = np.argmax(abs_val_minus_avg)
        cal = max_of_deviations / std_dev
        return cal, max_ind

    def Critical_value(self, S):
        t_dist = stats.t.ppf(1 - self.alpha / (2 * S), S - 2)
        num = (S - 1) * np.sqrt(np.square(t_dist))
        den = np.sqrt(S) * np.sqrt(S - 2 + np.square(t_dist))
        critical_value = num / den
        return critical_value
