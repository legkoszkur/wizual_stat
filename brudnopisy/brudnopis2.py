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
    def __init__(self, data, variables, input_variables, input_statistics_list_one):
        self.data = data
        self.variables = variables
        self.input_variables = input_variables
        self.input_statistics_list_one = input_statistics_list_one

        self.dictionary = {}

        for i in self.input_variables:
            self.dictionary[i] = self.input_statistics_list_one

        print(self.data.agg(self.dictionary))

        self.all_other_amount_list = []

        for i in self.input_variables:
            self.all_other_amount_list.append(i)
            self.all_other_amount_list.append(sum(self.data[i]))
            self.all_other_amount_list.append(np.mean(self.data[i]))
            self.all_other_amount_list.append(max(self.data[i]))
            self.all_other_amount_list.append(min(self.data[i]))
            self.all_other_amount_list.append(np.quantile(self.data[i], q=0.5))
            self.all_other_amount_list.append(np.quantile(self.data[i], q=0.25))
            self.all_other_amount_list.append(np.quantile(self.data[i], q=0.75))
            self.all_other_amount_list.append(self.data[i].mode(dropna=False)[0])

            self.all_other_amount_list.append(np.std(self.data[i]))  # odchylenie standardowe
            self.all_other_amount_list.append((np.std(self.data[i]) / np.mean(self.data[i]) * 100))
            self.all_other_amount_list.append(max(self.data[i]) - min(self.data[i]))  # rozstęp
            self.all_other_amount_list.append(
                np.quantile(self.data[i], q=0.75) - np.quantile(self.data[i], q=0.25))  # rozstęp ćwiartkowy
            self.all_other_amount_list.append(
                (np.quantile(self.data[i], q=0.75) - np.quantile(self.data[i], q=0.25)) / 2)  # odchylenie ćwiartkowe

            self.all_other_amount_list.append(skew(self.data[i]))  # wpółczynnik Pearsona
            self.all_other_amount_list.append(kurtosis(self.data[i]))  # też chyba pearson

        print(self.all_other_amount_list)


check = Statistic_backend(data, variables, input_variables, input_statistics_list_one, )

