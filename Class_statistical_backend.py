import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew


class StatisticBackend:
    def __init__(self, data, input_var,input_stat, wish,):
        self.data = data
        self.input_var = input_var
        self.input_stat = input_stat
        self.wish = wish

        self.average_m_l = []
        self.differentiation_m_l = []
        self.skewness_l = []
        self.kurtosis_l = []

        self.average_m_id = ['Sum', 'Mean', "Max", "Min", "Median", "Quantile_25", "Quantile_75", "Dominant"]
        self.differentiation_m_id = ["Standard deviation", "Coefficient of variation", "Range",
                                            "Interquartile range", "Quarterly deviation", ]
        self.skewness_id = ["Skewness"]
        self.kurtosis_id = ["Kurtosis"]

        if self.wish == 0:
            for i in self.input_var:
                self.average_m_l.append([
                    sum(self.data[i]), np.mean(self.data[i]), max(self.data[i]), min(self.data[i]),
                    np.quantile(self.data[i], q=0.5), np.quantile(self.data[i], q=0.25),
                    np.quantile(self.data[i], q=0.75), self.data[i].mode(dropna=False)[0]])
            self.average_measures_df = pd.DataFrame(
                np.array(self.average_m_l).reshape(-1, len(self.input_var)),
                index=self.average_m_id, columns=self.input_var)
            self.average_measures_df = self.average_measures_df.loc[[self.input_stat]]

        elif self.wish == 1:
            for i in self.input_var:
                self.differentiation_m_l.append([
                    np.std(self.data[i]), np.std(self.data[i]) / np.mean(self.data[i]) * 100,
                    max(self.data[i]) - min(self.data[i]),
                    np.quantile(self.data[i], q=0.75) - np.quantile(self.data[i], q=0.25),
                    (np.quantile(self.data[i], q=0.75) - np.quantile(self.data[i], q=0.25)) / 2, ])
            self.differentiation_measures_df = pd.DataFrame(
                np.array(self.differentiation_m_l).reshape(-1, len(self.input_var)),
                index=self.differentiation_m_id, columns=self.input_var)
            self.differentiation_measures_df = self.differentiation_measures_df.loc[[self.input_stat]]

        elif self.wish == 2:
            for i in self.input_var:
                self.skewness_l.append([skew(self.data[i])])  # Pearson
            self.skewness_df = pd.DataFrame(
                np.array(self.skewness_l).reshape(-1, len(self.input_var)),
                index=self.skewness_id, columns=self.input_var)
            self.skewness_df = self.skewness_df.loc[[self.input_stat]]

        elif self.wish == 3:
            for i in self.input_var:
                self.kurtosis_l.append([kurtosis(self.data[i])])  # Pearson?~
            self.kurtosis_df = pd.DataFrame(
                np.array(self.kurtosis_l).reshape(-1, len(self.input_var)),
                index=self.kurtosis_id, columns=self.input_var)
            self.kurtosis_df = self.kurtosis_df.loc[[self.input_stat]]
