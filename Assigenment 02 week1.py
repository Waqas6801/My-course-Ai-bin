#  PART 1 — STRING MANIPULATION
# 1️ First, Middle, Last Character
s = input("Enter string: ")

if len(s) == 0:
    print("Empty string")
elif len(s) == 1:
    print(s)
else:
    middle = s[len(s)//2]
    print("New string:", s[0] + middle + s[-1])
# 2️ Count All Character Occurrences
s = input("Enter string: ")

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# 3️ Reverse String
s = input("Enter string: ")
print(s[::-1])
# 4️ Split on Hyphens
s = input("Enter hyphen string: ")
print(s.split("-"))
# 5️ Remove Special Symbols
import string

s = input("Enter string: ")
clean = ""

for ch in s:
    if ch.isalnum() or ch.isspace():
        clean += ch

print(clean)
#  LIST MANIPULATION
# 1️ Reverse List
lst = [1, 2, 3, 4]
lst.reverse()
print(lst)
# 2️ Square Every Item
lst = [1, 2, 3, 4]
squared = [x**2 for x in lst]
print(squared)
# 3️ Remove Empty Strings
lst = ["apple", "", "banana", "", "cherry"]
clean = [x for x in lst if x != ""]
print(clean)
# 4️ Add Item After Specific Item
lst = [10, 20, 30, 40]
value = 20
new_item = 25

if value in lst:
    index = lst.index(value)
    lst.insert(index+1, new_item)

print(lst)
# 5️ Replace Item If Found
lst = [1, 2, 3, 4]
old = 3
new = 99

if old in lst:
    lst[lst.index(old)] = new

print(lst)
#  DICTIONARY MANIPULATION
# 1️ Check If Value Exists
d = {"a": 10, "b": 20, "c": 30}

value = 20
print(value in d.values())
# 2️ Key of Minimum Value
d = {"a": 10, "b": 5, "c": 30}
min_key = min(d, key=d.get)
print(min_key)
# 3️ Delete List of Keys
d = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_to_remove = ["b", "d"]

for k in keys_to_remove:
    d.pop(k, None)

print(d)
#  TUPLE MANIPULATION
# 1️ Reverse Tuple
t = (1, 2, 3, 4)
print(t[::-1])
# 2️ Access Value 20
t = (10, 20, 30, 40)
print(t[1])
# 3️ Swap Two Tuples
t1 = (1, 2)
t2 = (3, 4)

t1, t2 = t2, t1
print(t1, t2)
#  LOOP MANIPULATION
# 1️ First 10 Natural Numbers
i = 1
while i <= 10:
    print(i)
    i += 1
# 2️ Print Even Numbers
n = int(input("Enter number: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
# 3️ Print Odd Numbers
n = int(input("Enter number: "))

for i in range(1, n+1):
    if i % 2 != 0:
        print(i)
# 4️ Print Prime Numbers
n = int(input("Enter number: "))

for num in range(2, n+1):
    prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
# 5️ Multiplication Table
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)


# Program to create a LIST of nouns from the story

nouns = [
    "year", "Humanity", "control", "functions", "intelligence",
    "Cities", "transportation", "Dr. Elias Voss",
    "Athena-9", "Neo-Tokyo"
]

print("List of Nouns:")
print(nouns)
# List of nouns and nested list of numbers from story

story = """
The year was 2147. Dr. Elias Voss created Athena-9.
"""

nouns = [
    "year", "Dr. Elias Voss", "Athena-9"
]

numbers = []

words = story.split()

for word in words:
    if word.strip(".-").isdigit():
        numbers.append(int(word.strip(".-")))

nouns.append(numbers)   # Nested list added as last element

print("List with nested numbers list:")
print(nouns)
# Program to create a TUPLE of nouns

nouns_tuple = (
    "year", "Humanity", "control", "functions",
    "intelligence", "Cities", "transportation",
    "Dr. Elias Voss", "Athena-9", "Neo-Tokyo"
)

print("Tuple of Nouns:")
print(nouns_tuple)
# Tuple of nouns with nested tuple of numbers

story = """
The year was 2147. Athena-9 was activated.
"""

nouns = (
    "year",
    "Athena-9"
)

numbers = []

words = story.split()

for word in words:
    if word.strip(".-").isdigit():
        numbers.append(int(word.strip(".-")))

final_tuple = nouns + (tuple(numbers),)

#  Create a Set of all nouns


story = """
The year was 2147. Humanity had long since ceded control.
Dr. Elias Voss created Athena-9 in Neo-Tokyo.
"""

# Manually selected nouns from story
nouns = {
    "year",
    "Humanity",
    "control",
    "Dr. Elias Voss",
    "Athena-9",
    "Neo-Tokyo"
}

# Extract numbers from story
numbers = set()

words = story.split()

for word in words:
    clean_word = word.strip(".-")
    if clean_word.isdigit():
        numbers.add(int(clean_word))



# Program to create dictionary of nouns from story

story = """
The year was 2147. Dr. Elias Voss activated Athena-9.
"""

# Manually selected nouns
nouns_dict = {
    1: "year",
    2: "Dr. Elias Voss",
    3: "Athena-9"
}

# Extract numbers from story
numbers_dict = {}

words = story.split()

count = 1
for word in words:
    clean_word = word.strip(".-")
    if clean_word.isdigit():
        numbers_dict[count] = int(clean_word)
        count += 1

# Add nested dictionary as last element
nouns_dict["Numbers"] = numbers_dict

print("Dictionary with nested dictionary of numbers:")
print(nouns_dict)