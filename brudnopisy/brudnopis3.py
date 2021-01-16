from pandas import DataFrame
d = [["M",10,2.5,12],["F",6,1.6,7],["M",9,2.2,9],["M",11,2.4,10],["F",7,1.9,9]]
df = DataFrame(d, columns=['Gender','Lenght','Height','Weight'])
print(df)