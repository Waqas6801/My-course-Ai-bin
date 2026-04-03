import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\dell\Desktop\RealEstate-USA.csv")

# Select columns from dataset
ids = df['brokered_by'].to_numpy()
price = df['price'].to_numpy()
zip_code = df['zip_code'].to_numpy()
house_size = df['house_size'].fillna(0).to_numpy()

print(ids)
print(price)
print(zip_code)
print(house_size)

# ===============================
# Statistics operations on price
# ===============================

print("Price mean:", np.mean(price))
print("Price average:", np.average(price))
print("Price std:", np.std(price))
print("Price median:", np.median(price))
print("Price percentile 25:", np.percentile(price,25))
print("Price percentile 75:", np.percentile(price,75))
print("Price percentile 3:", np.percentile(price,3))
print("Price min:", np.min(price))
print("Price max:", np.max(price))

# ===============================
# Math operations
# ===============================

print("Price square:", np.square(price))
print("Price sqrt:", np.sqrt(price))
print("Price abs:", np.abs(price))

# avoid overflow (remove power price^price)
print("Price power (price^2):", np.power(price,2))

# ===============================
# Arithmetic operations
# ===============================

addition = zip_code + house_size
subtraction = zip_code - house_size
multiplication = zip_code * house_size
division = zip_code / (house_size + 1)

print("Zip + House_size:", addition)
print("Zip - House_size:", subtraction)
print("Zip * House_size:", multiplication)
print("Zip / House_size:", division)

# ===============================
# Trigonometric Functions
# ===============================

pricePie = (price/np.pi) + 1

print("Sine values:", np.sin(pricePie))
print("Cosine values:", np.cos(pricePie))
print("Tangent values:", np.tan(pricePie))

print("Exponential:", np.exp(pricePie))

# Logarithms
print("Natural log:", np.log(pricePie))
print("Log10:", np.log10(pricePie))

# ===============================
# Hyperbolic Functions
# ===============================

print("Sinh:", np.sinh(pricePie))
print("Cosh:", np.cosh(pricePie))
print("Tanh:", np.tanh(pricePie))

print("Arcsinh:", np.arcsinh(pricePie))
print("Arccosh:", np.arccosh(pricePie + 1))

# ===============================
# 2D Array
# ===============================

D2Array = np.array([zip_code, house_size])

print("2D Array:", D2Array)

print("Dimension:", D2Array.ndim)
print("Total elements:", D2Array.size)
print("Shape:", D2Array.shape)
print("Datatype:", D2Array.dtype)

# ===============================
# Slicing
# ===============================

slice1 = D2Array[:1,:5]
print("Slice1:", slice1)

slice2 = D2Array[:1,4:15:4]
print("Slice2:", slice2)

# ===============================
# Indexing
# ===============================

print("Index item:", slice1[0,1])
print("Index item2:", slice2[0,0])

# ===============================
# Iteration
# ===============================

for elem in np.nditer(D2Array):
    print(elem)

for index, elem in np.ndenumerate(D2Array):
    print(index, elem)

# ===============================
# Reshape
# ===============================

reshape_array = np.reshape(D2Array,(1, D2Array.size))

print("Reshape:", reshape_array)
print("Size:", reshape_array.size)
print("ndim:", reshape_array.ndim)
print("Shape:", reshape_array.shape)