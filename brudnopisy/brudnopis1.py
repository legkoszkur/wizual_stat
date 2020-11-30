import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew

data = sns.load_dataset('iris')
data.head()
variables = list(data.columns)
input_variables = ['sepal_width', 'petal_length', ]
input_statistics_list_one = ['sum', 'mean', 'min', 'max', 'std', 'median', 'skew', 'kurtosis', ]
input_statistics_list_two = ['0.25', 'other']


class Statistic_backend():
    def __init__(self, data, input_variables):
        self.data = data
        self.variables = variables
        self.input_variables = input_variables

        self.average_measures_l = []
        self.differentiation_measures_l = []
        self.skewness_l = []
        self.kurtosis_l = []

        self.average_measures_id = ['Sum', 'Mean', "Max", "Min", "Median", "Quantile_25", "Quantile_75", "Dominant"]
        self.differentiation_measures_id = ["Standard deviation", "Coefficient of variation", "Range",
                                            "Interquartile range", "Quarterly deviation", ]
        self.skewness_id = ["Skewness"]
        self.kurtosis_id = ["Kurtosis"]

        for i in self.input_variables:
            self.average_measures_l.append([sum(self.data[i]),
                                            np.mean(self.data[i]),
                                            max(self.data[i]),
                                            min(self.data[i]),
                                            np.quantile(self.data[i], q=0.5),
                                            np.quantile(self.data[i], q=0.25),
                                            np.quantile(self.data[i],
                                            q=0.75), self.data[i].mode(dropna=False)[0]])

        self.average_measures_df = pd.DataFrame(np.array(self.average_measures_l).reshape(-1,
                                                len(self.input_variables)),index=self.average_measures_id,
                                                columns=self.input_variables)

        for i in self.input_variables:
            self.differentiation_measures_l.append([
                np.std(self.data[i]),
                np.std(self.data[i]) / np.mean(self.data[i]) * 100,
                max(self.data[i]) - min(self.data[i]),
                np.quantile(self.data[i],q=0.75) - np.quantile(self.data[i], q=0.25),
                ((np.quantile(self.data[i], q=0.75) - np.quantile(self.data[i], q=0.25)) / 2),])

        self.differentiation_measures_df = pd.DataFrame(np.array(self.differentiation_measures_l).reshape(-1,
                                                        len(self.input_variables)),
                                                        index=self.differentiation_measures_id,
                                                        columns=self.input_variables)

        for i in self.input_variables:
            self.skewness_l.append([skew(self.data[i])])  # wpółczynnik Pearsona

        self.skewness_df = pd.DataFrame(np.array(self.skewness_l).reshape(-1, len(self.input_variables)),
                                                        index=self.skewness_id,columns=self.input_variables)

        for i in self.input_variables:
            self.kurtosis_l.append([kurtosis(self.data[i])])  # też chyba pearson

        self.kurtosis_df = pd.DataFrame(np.array(self.kurtosis_l).reshape(-1, len(self.input_variables)),
                                        index=self.kurtosis_id, columns=self.input_variables)



check = Statistic_backend(data, input_variables,)

