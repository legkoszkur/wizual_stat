import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew

# x = pd.DataFrame([[2.22,2.22,2.22,2.22,2.22,2.22,2.22,2.22,1,1,1,1,1],[1,1,1,1,11,1,2,21,3,3,2,32,32,43,34,32,42,4]])
# print(x.agg(['min','max','median','mean','std','mode']))
# print(x.mode()[0][0])

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

        self.average_measures_list = []
        self.differentiation_measures_list = []
        self.skewness_list = []
        self.kurtosis_list = []

        self.average_measures_index = ['Sum', 'Mean', "Max", "Min", "Median", "Quantile_25", "Quantile_75", "Dominant"]
        self.differentiation_measures_index = ["Standard deviation", "Coefficient of variation", "Range",
                                               "Interquartile range", "Quarterly deviation", ]
        self.skewness_index = ["Skewness"]
        self.kurtosis_index = ["Kurtosis"]

        for i in self.input_variables:
            self.average_measures_list.append([sum(self.data[i]),np.mean(self.data[i]),max(self.data[i]),min(self.data[i]),np.quantile(self.data[i], q=0.5),
                                               np.quantile(self.data[i], q=0.25),np.quantile(self.data[i], q=0.75),self.data[i].mode(dropna=False)[0]])


        self.average_measures_data_frame = pd.DataFrame(np.array(self.average_measures_list).reshape(-1, len(self.input_variables)), index=self.average_measures_index,columns=self.input_variables)
        print(self.average_measures_data_frame)

        for i in self.input_variables:
            self.differentiation_measures_list.append(np.std(self.data[i]))
            self.differentiation_measures_list.append((np.std(self.data[i]) / np.mean(self.data[i]) * 100))
            self.differentiation_measures_list.append(max(self.data[i]) - min(self.data[i]))  # rozstęp
            self.differentiation_measures_list.append(
                np.quantile(self.data[i], q=0.75) - np.quantile(self.data[i], q=0.25))  # rozstęp ćwiartkowy
            self.differentiation_measures_list.append(
                (np.quantile(self.data[i], q=0.75) - np.quantile(self.data[i], q=0.25)) / 2)  # odchylenie ćwiartkowe

        for i in self.input_variables:
            self.skewness_list.append(skew(self.data[i]))  # wpółczynnik Pearsona

        for i in self.input_variables:
            self.kurtosis_measures_list.append(kurtosis(self.data[i]))  # też chyba pearson


check = Statistic_backend(data, input_variables, )

