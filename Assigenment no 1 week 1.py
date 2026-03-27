
# Question 1:
# Write a program that converts a temperature from Celsius to Fahrenheit.
# Formula: Fahrenheit = (Celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
# Question 2:
# Calculate Area of a Rectangle

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print("Area of Rectangle:", area)
# Question 3:
# Calculate Compound Interest
# CI = P * (1 + R/100)**T - P

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest: "))
T = float(input("Enter Time in years: "))

CI = P * (1 + R/100)**T - P
print("Compound Interest:", CI)
# Question 4:
# Calculate Perimeter of a Rectangle

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = 2 * (length + width)
print("Perimeter:", perimeter)
# Question 5:
# Average of Three Numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3
print("Average:", average)
# Question 6:
# Square and Cube of a Number

num = float(input("Enter a number: "))

print("Square:", num ** 2)
print("Cube:", num ** 3)
# Question 7:
# Distribute Items Equally

n = int(input("Enter number of candies: "))
k = int(input("Enter number of students: "))

each = n // k
left = n % k

print("Each student gets:", each)
print("Candies left:", left)
# Question 8:
# Calculate Profit or Loss

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    print("Profit:", sp - cp)
elif cp > sp:
    print("Loss:", cp - sp)
else:
    print("No Profit No Loss")
# Question 9:
# Total Marks and Percentage of 5 subjects

total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total += marks

percentage = total / 5
average = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)
print("Average:", average)
# Question 10:
# Salary Calculator

basic = float(input("Enter Basic Salary: "))

HRA = 0.20 * basic
DA = 0.15 * basic
total_salary = basic + HRA + DA

print("HRA:", HRA)
print("DA:", DA)
print("Total Salary:", total_salary)
# Question 11:
# Age in Months and Days

years = int(input("Enter your age in years: "))

months = years * 12
days = years * 365  # approximate

print("Age in months:", months)
print("Age in days:", days)
# Question 12:
# Currency Converter (USD to PKR)

usd = float(input("Enter amount in USD: "))
rate = 280  # Fixed exchange rate (example)

pkr = usd * rate

print("Amount in PKR:", pkr)
# Question 13:
# Sum of First N Natural Numbers
# Formula: n * (n + 1) / 2

n = int(input("Enter a number: "))

sum_n = n * (n + 1) // 2
print("Sum of first", n, "natural numbers:", sum_n)
# Question 14:
# Percentage of Correct Answers

total = int(input("Enter total questions: "))
correct = int(input("Enter correct answers: "))

percentage = (correct / total) * 100

print("Percentage Score:", percentage, "%")
# Question 15:
# Speed = Distance / Time

distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

speed = distance / time

print("Speed:", speed)
# Question 16:
# Body Mass Index (BMI)
# BMI = weight / (height ** 2)

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

BMI = weight / (height ** 2)

print("Your BMI:", BMI)
# Question 17:
# Convert Minutes to Hours and Minutes

minutes = int(input("Enter minutes: "))

hours = minutes // 60
remaining = minutes % 60

print(hours, "hours and", remaining, "minutes")