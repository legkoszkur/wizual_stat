import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
       Sum     Mean    Max   Min  Median  Quantile_25  Quantile_75  Dominant
x1 -4632.0 -52.6364    1.0 -99.0   -56.0       -78.00       -28.50     -65.0
x2  4723.0  53.6705   99.0   1.0    52.5        33.50        79.25      24.0
x3  4938.0  56.1136  100.0   2.0    64.0        29.75        81.25      68.0
x4  4119.0  46.8068   99.0   1.0    42.5        22.00        73.25      81.0
"""
x = [[-4632.0, -52.6364, 1.0, -99.0, -56.0, -78.00, -28.50, -65.0,],
     [4723.0, 53.6705, 99.0, 1.0, 52.5, 33.50, 79.25, 24.0],
     [4938.0, 56.1136, 100.0, 2.0, 64.0, 29.75, 81.25, 68.0],
     [4119.0, 46.8068, 99.0, 1.0, 42.5, 22.00, 73.25, 81.0]]
inde = ["x1", "x2", "x3", "x4"]
kolumn = ["Sum", "Mean", "Max", "Min", "Median", "Quantile_25", "Quantile_75", "Dominant",]
df = pd.DataFrame(x, index=inde, columns=kolumn)

"""
df.plot(kind="bar")
plt.show()
"""

ax = df.plot(kind="bar")
print(type(x))
figure = plt.figure()
figure.add_subplot().df.plot(kind="bar")








