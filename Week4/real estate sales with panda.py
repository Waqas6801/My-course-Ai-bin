import pandas as pd

# Read CSV file
df = pd.read_csv(r'C:\Users\dell\Documents\GitHub\My-course-Ai-bin\Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=",",index_col='Serial Number')
print(df)
print("df - data types" , df.dtypes)

print("\nDataset Info:")
print(df.info())

# Last four rows
print("\nLast four rows:")
print(df.tail(4))

# First four rows
print("\nFirst four rows:")
print(df.head(4))

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Shape
print("\nRows and Columns:", df.shape)

# Access single column
town = df['Town']
print("\nTown column:")
print(town)

# Access multiple columns
town_address = df[['Town','Address']]
print("\nTown and Address columns:")
print(town_address)

# Selecting a single row using .loc (using primary key)
row1 = df.loc[df.index[0]]
print("\nSingle row using loc:")
print(row1)

# Selecting multiple rows using .loc
row2 = df.loc[df.index[1:4]]
print("\nMultiple rows using loc:")
print(row2)

# Slice rows using .loc
row3 = df.loc[df.index[2]:df.index[6], 'Town']
print("\nSlice rows using loc:")
print(row3)

# Conditional selection
row4 = df.loc[df['Town'] == 'Bridgeport']
print("\nConditional rows (Town = Bridgeport):")
print(row4)

# Selecting a single column using .loc
column1 = df.loc[:, 'Sale Amount']
print("\nSingle column using loc:")
print(column1)

# Selecting multiple columns using .loc
column2 = df.loc[:, ['Town','Sale Amount']]
print("\nMultiple columns using loc:")
print(column2)

# Slice columns
column3 = df.loc[:, 'Town':'Sale Amount']
print("\nSlice columns using loc:")
print(column3)

# Combined row and column selection
rowcol = df.loc[df['Town'] == 'Bridgeport', 'Address':'Sale Amount']
print("\nCombined row and column selection:")
print(rowcol)

# ------------------ ILOC ------------------

# Single row
iloc1 = df.iloc[0]
print("\nSingle row using iloc:")
print(iloc1)

# Multiple rows
iloc2 = df.iloc[[2,4,6]]
print("\nMultiple rows using iloc:")
print(iloc2)

# Slice rows
iloc3 = df.iloc[1:6]
print("\nSlice rows using iloc:")
print(iloc3)

# Single column
iloc4 = df.iloc[:,4]
print("\nSingle column using iloc:")
print(iloc4)

# Multiple columns
iloc5 = df.iloc[:,[2,5]]
print("\nMultiple columns using iloc:")
print(iloc5)

# Slice columns
iloc6 = df.iloc[:,1:4]
print("\nSlice columns using iloc:")
print(iloc6)

# Combined row and column
iloc7 = df.iloc[[1,3,5],2:5]
print("\nCombined selection using iloc:")
print(iloc7)
