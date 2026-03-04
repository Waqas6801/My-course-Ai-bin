s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) > len(s2):
    print("First string is longer")
elif len(s1) < len(s2):
    print("Second string is longer")
else:
    print("Both strings have equal length")