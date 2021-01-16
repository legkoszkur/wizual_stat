import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew


class StatisticBackend:
    average_measures_df = None
    differentiation_measures_df = None
    skew_kurt_df = None

    # gives statistics into class
    @staticmethod
    def data_for_average_measures(data, input_var, input_stat):
        average_m_l = []
        average_m_id = [
            'Sum', 'Mean', "Max",
            "Min", "Median", "Q_25%",
            "Q_75%", "Dominant"
        ]
        for i in input_var:
            average_m_l.append([
                sum(data[i]), np.mean(data[i]), max(data[i]), min(data[i]),
                np.quantile(data[i], q=0.5), np.quantile(data[i], q=0.25),
                np.quantile(data[i], q=0.75), data[i].mode(dropna=False)[0]
            ])
        average_measures_df = pd.DataFrame(np.transpose(average_m_l), index=average_m_id, columns=input_var)
        average_measures_df = average_measures_df.loc[input_stat]
        average_measures_df = average_measures_df.round(decimals=4)
        return average_measures_df

    # gives statistics into class
    @staticmethod
    def data_for_differentiation_measures(data, input_var, input_stat):
        differentiation_m_l = []
        differentiation_m_id = [
            "Sd", "CV", "Range",
            "IQR", "QD",
        ]

        for i in input_var:
            differentiation_m_l.append([
                np.std(data[i]), np.std(data[i]) / np.mean(data[i]) * 100, max(data[i]) - min(data[i]),
                np.quantile(data[i], q=0.75) - np.quantile(data[i], q=0.25),
                (np.quantile(data[i], q=0.75) - np.quantile(data[i], q=0.25)) / 2,
            ])
        differentiation_measures_df = pd.DataFrame(np.transpose(differentiation_m_l),
                                                   index=differentiation_m_id, columns=input_var)
        differentiation_measures_df = differentiation_measures_df.loc[input_stat]
        differentiation_measures_df = differentiation_measures_df.round(decimals=4)
        return differentiation_measures_df

    # gives statistics into class
    @staticmethod
    def data_for_skewness_and_kurtosis(data, input_var, input_stat):
        skew_kurt_l = []
        skew_kurt_id = [
            "Skewness", "Kurtosis", 'Mean',
            "Median", "Dominant"
        ]
        for i in input_var:

            skew_kurt_l.append([skew(data[i]), kurtosis(data[i]), np.mean(data[i]),
                                np.quantile(data[i], q=0.5), data[i].mode(dropna=False)[0], ])
        skew_kurt_df = pd.DataFrame(np.transpose(skew_kurt_l), index=skew_kurt_id, columns=input_var)
        skew_kurt_df = skew_kurt_df.loc[input_stat]
        return skew_kurt_df
