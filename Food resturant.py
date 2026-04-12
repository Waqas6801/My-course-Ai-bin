import pandas as pd

# Read CSV file
df = pd.read_csv(r'C:\Users\dell\Downloads\FastFoodRestaurants.csv',delimiter=",",index_col='keys')
print(df)
print("df - data types" , df.dtypes)
print("df.info():   " , df.info() )
# display the last four rows
print('Last four Rows:')
print(df.tail(4))
# display the first four rows
print('First fou Rows:')
print(df.head(4))
print()
#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()
# access the Name column
myname = df['name']
print("access the Name column: df : ")
print(myname)
print()
# access multiple columns
myname_myprovince = df[['name','province']]
print("access multiple columns: df : ")
print(myname_myprovince)
print()
#Selecting a single row using .loc
First_row = df.loc['us/ny/massena/324mainst/-1161002137', 'address']
print("#Selecting a single row using .loc")
print(First_row)
print()
#Selecting multiple rows using .loc
first_row2 = df.loc['us/ny/massena/324mainst/-1161002137', 'city']
print("#Selecting multiple rows using .loc")
print(first_row2)
print()
#Selecting a slice of rows using .loc
first_row3 = df.loc['us/ny/massena/324mainst/-1161002137','country']
print("#Selecting a slice of rows using .loc")
print(first_row3)
print()
#Conditional selection of rows using .loc
first_row4 = df.loc[df['address'] == '408 Market']
print("#Conditional selection of rows using .loc")
print(first_row4)
print()
#Selecting a single column using .loc

single_column = df.loc[:, 'name']

print("#Selecting a single column using .loc")
print(single_column)
print()
#Selecting multiple columns using .loc
second_row6 = df.loc[:'us/ny/massena/6098statehighway37/-1161002137',['province','websites']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()
#Selecting a slice of rows using .loc
second_row3 = df.loc["us/sc/saluda/401njenningsst/-1161002137":"us/ky/lexington/125townecenterdr/-1055723171"]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()
#Conditional selection of rows using .loc
second_row4 = df.loc[df['province'] == 'KY']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()
#Selecting a single column using .loc
second_row5 = df.loc[:,'latitude']
print("#Selecting a single column using .loc")
print(second_row5)
print()
#Selecting multiple columns using .loc
second_row6 = df.loc[:,['postalCode','province']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()
#Selecting a slice of columns using .loc
second_row7 = df.loc[:,'name':'websites']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()
#Combined row and column selection using .loc
second_row8 = df.loc[df['city'] == 'Tell City','province':'websites']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
#iloc starts from here

#Selecting a single row using .iloc
second_row = df.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()
#Selecting multiple rows using .iloc
second_row2 = df.iloc[[4, 5,6]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()
#Selecting a slice of rows using .iloc
second_row3 = df.iloc[1:7]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()
#Selecting a single column using .iloc
second_row5 = df.iloc[:,5]
print("#Selecting a single column using .iloc")
print(second_row5)
print()
#Selecting multiple columns using .iloc
second_row6 = df.iloc[:,[3,6]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()
#Selecting a slice of columns using .iloc
second_row7 = df.iloc[:,1:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()
#Combined row and column selection using .iloc
second_row8 = df.iloc[[1, 4,6],3:5]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

