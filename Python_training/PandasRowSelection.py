#Import pandas
import pandas as pd
#File path variable
fileLink = '/Users/atoomic/Documents/VSCode/Excel/Employee.csv'
#Add csv file
df = pd.read_csv(fileLink,index_col='Employee ID')
#insert a new column
df.insert(3,'Age',[24,25,27,22,23,34,33,36,40],True)
#converting row 0 to 2 into a df and then converting to a list for manipulation
row1 = df.iloc[0:2]
k = row1.values.tolist()
print(k)
cl_name = list(df)
print(cl_name)