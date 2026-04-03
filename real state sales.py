# Real Estate Sales Dataset Analysis
import numpy as np

# Load only required numeric columns (ID and Sale Amount)
ids, price = np.genfromtxt(
    r"C:\Users\dell\Desktop\Real_Estate_Sales_2001-2022_GL-Short.csv",
    delimiter=",",
    skip_header=1,
    usecols=(0,6),     # Column 0 = ID, Column 6 = Sale Amount
    unpack=True,
    invalid_raise=False
)

print("IDs:\n", ids[:10])
print("Prices:\n", price[:10])

# -----------------------------
# Statistics Operations
# -----------------------------

print("Price mean:", np.mean(price))
print("Price average:", np.average(price))
print("Price std:", np.std(price))
print("Price median:", np.median(price))
print("Price percentile 25:", np.percentile(price,25))
print("Price percentile 75:", np.percentile(price,75))
print("Price percentile 3:", np.percentile(price,3))
print("Price min:", np.min(price))
print("Price max:", np.max(price))

# -----------------------------
# Math Operations
# -----------------------------

print("Price square:", np.square(price))
print("Price sqrt:", np.sqrt(price))
print("Price power:", np.power(price,2))
print("Price abs:", np.abs(price))

# -----------------------------
# Arithmetic Operations
# -----------------------------

price2 = price / 1000

addition = price + price2
subtraction = price - price2
multiplication = price * price2
division = price / (price2 + 1)

print("Addition:", addition[:10])
print("Subtraction:", subtraction[:10])
print("Multiplication:", multiplication[:10])
print("Division:", division[:10])

# -----------------------------
# Trigonometric Functions
# -----------------------------

pricePie = (price/np.pi) + 1

print("Sine:", np.sin(pricePie[:10]))
print("Cosine:", np.cos(pricePie[:10]))
print("Tangent:", np.tan(pricePie[:10]))
print("Exponential:", np.exp(pricePie[:10]))

# -----------------------------
# Logarithmic Functions
# -----------------------------

print("Natural log:", np.log(pricePie[:10]))
print("Log10:", np.log10(pricePie[:10]))

# -----------------------------
# Hyperbolic Functions
# -----------------------------

print("Sinh:", np.sinh(pricePie[:10]))
print("Cosh:", np.cosh(pricePie[:10]))
print("Tanh:", np.tanh(pricePie[:10]))

print("Arcsinh:", np.arcsinh(pricePie[:10]))
print("Arccosh:", np.arccosh(pricePie[:10] + 1))

# -----------------------------
# 2D Array
# -----------------------------

D2Price = np.array([price, price2])

print("Dimension:", D2Price.ndim)
print("Total elements:", D2Price.size)
print("Shape:", D2Price.shape)
print("Datatype:", D2Price.dtype)

# -----------------------------
# Slicing
# -----------------------------

slice1 = D2Price[:1,:5]
print("Slice1:", slice1)

slice2 = D2Price[:1,4:15:4]
print("Slice2:", slice2)

# -----------------------------
# Indexing
# -----------------------------

print("Index item:", slice1[0,1])

if slice2.size > 0:
    print("Index item2:", slice2[0,0])

# -----------------------------
# Iteration
# -----------------------------

for elem in np.nditer(D2Price[:, :5]):
    print(elem)

for index, elem in np.ndenumerate(D2Price[:, :5]):
    print(index, elem)

# -----------------------------
# Reshape
# -----------------------------

reshape_array = np.reshape(D2Price,(1,D2Price.size))

print("Reshaped array shape:", reshape_array.shape)

print("Program Completed Successfully")