import pandas as pd

data_set = pd.read_csv("D:/Data_QA/Test_Data/TestDataSet.csv")
view_dataframe = data_set.head()

t1 = data_set.tail()
h1 = data_set.head()

print(view_dataframe)