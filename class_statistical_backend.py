import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew


class StatisticBackend:
    def __init__(self, data, input_var, input_stat, ):
        self.data = data
        self.input_var = input_var
        self.input_stat = input_stat
        self.average_measures_df = None
        self.differentiation_measures_df = None
        self.skew_kurt_df = None

        self.average_m_l = []
        self.differentiation_m_l = []
        self.skew_kurt_l = []

        self.average_m_id = [
            'Sum', 'Mean', "Max",
            "Min", "Median", "Q_25%",
            "Q_75%", "Dominant"
        ]

        self.differentiation_m_id = [
            "Sd", "CV", "Range",
            "IQR", "QD",
        ]

        self.skew_kurt_id = [
            "Skewness", "Kurtosis", 'Mean',
            "Median", "Dominant"
        ]


    def data_for_average_measures(self):
        for i in self.input_var:
            self.average_m_l.append([
                sum(self.data[i]), np.mean(self.data[i]), max(self.data[i]), min(self.data[i]),
                np.quantile(self.data[i], q=0.5), np.quantile(self.data[i], q=0.25),
                np.quantile(self.data[i], q=0.75), self.data[i].mode(dropna=False)[0]
            ])
        self.average_measures_df = pd.DataFrame(np.transpose(self.average_m_l),
                                                index=self.average_m_id, columns=self.input_var)

        self.average_measures_df = self.average_measures_df.loc[self.input_stat]
        self.average_measures_df = self.average_measures_df.round(decimals=4)
        return self.average_measures_df

    def data_for_differentiation_measures(self):
        for i in self.input_var:
            self.differentiation_m_l.append([
                np.std(self.data[i]), np.std(self.data[i]) / np.mean(self.data[i]) * 100,
                max(self.data[i]) - min(self.data[i]),
                np.quantile(self.data[i], q=0.75) - np.quantile(self.data[i], q=0.25),
                (np.quantile(self.data[i], q=0.75) - np.quantile(self.data[i], q=0.25)) / 2,
            ])
        self.differentiation_measures_df = pd.DataFrame(np.transpose(self.differentiation_m_l),
                                                        index=self.differentiation_m_id, columns=self.input_var)
        self.differentiation_measures_df = self.differentiation_measures_df.loc[self.input_stat]
        self.differentiation_measures_df = self.differentiation_measures_df.round(decimals=4)
        return self.differentiation_measures_df

    def data_for_skewness_and_kurtosis(self):
        for i in self.input_var:
            # Pearson
            self.skew_kurt_l.append([skew(self.data[i]), kurtosis(self.data[i]), np.mean(self.data[i]),
                                     np.quantile(self.data[i], q=0.5), self.data[i].mode(dropna=False)[0], ])
        self.skew_kurt_df = pd.DataFrame(np.transpose(self.skew_kurt_l),
                                         index=self.skew_kurt_id, columns=self.input_var)
        self.skew_kurt_df = self.skew_kurt_df.loc[self.input_stat]
        return self.skew_kurt_df
