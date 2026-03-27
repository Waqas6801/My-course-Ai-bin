# Part A — Python Lists (Intermediate)
# 1. Squares of even numbers (0–20)
squares = [x**2 for x in range(21) if x % 2 == 0]
print(squares)
# 2. Sort without modifying original
nums = [3, 1, 4, 1, 5, 9]
sorted_nums = sorted(nums)
print(sorted_nums)
print(nums)  # original unchanged
# 3. Remove duplicates (preserve order)
nums = [1, 2, 2, 3, 1, 4]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)

print(unique)
# 4. Flatten nested list
nested = [[1, 2], [3, 4], [5]]
flat = [item for sublist in nested for item in sublist]
print(flat)
# 5. Sort names ignoring case
names = ['alice', 'Bob', 'charlie', 'DAVID']
sorted_names = sorted(names, key=str.lower)
print(sorted_names)
# 6. Replace index 2–4 using slice
a = [10, 20, 30, 40, 50, 60]
a[2:5] = [100, 200]
print(a)
# 7. Find all indices of a value
nums = [7, 1, 7, 3, 7]
indices = [i for i, v in enumerate(nums) if v == 7]
print(indices)
# 8. Elements appearing exactly once
nums = [1, 2, 2, 3, 4, 4, 5]
unique_once = [x for x in nums if nums.count(x) == 1]
print(unique_once)
# 9. Rotate list right by one
lst = [1, 2, 3, 4]
rotated = lst[-1:] + lst[:-1]
print(rotated)
# 10. Split into even and odd
nums = [1, 2, 3, 4, 5, 6]
even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if x % 2 != 0]
print("Even:", even)
print("Odd:", odd)
# Part B — Python Tuples (Intermediate)
# 1. Convert list → tuple and unpack
lst = [1, 2, 3, 4]
t = tuple(lst)
a, b, c, d = t
print(a, b, c, d)
# 2. List of second elements
t = (('a', 1), ('b', 2), ('c', 3))
seconds = [x[1] for x in t]
print(seconds)
# 3. Function returning multiple values
def stats(numbers):
    return sum(numbers), min(numbers), max(numbers)

result = stats([1, 2, 3, 4])
total, minimum, maximum = result
print(total, minimum, maximum)
# 4. Combine tuples and convert to list
t1 = (1, 2, 3)
t2 = (4, 5)
combined = list(t1 + t2)
print(combined)
# 5. Element with highest frequency
t = (1, 2, 2, 3, 3, 3, 4)
most_freq = max(set(t), key=t.count)
print(most_freq)
# 6. Check same elements (ignore order)
t1 = (1, 2, 3)
t2 = (3, 2, 1)
print(sorted(t1) == sorted(t2))
# 7. Last three items
t = (1, 2, 3, 4, 5, 6)
print(t[-3:])
# 8. Repeat tuple three times
t = (1, 2)
print(t * 3)
# 9. Flatten nested tuple
nested = ((1, 2), (3, 4))
flat = tuple(x for pair in nested for x in pair)
print(flat)
# 10. Manhattan distance
p1 = (2, 3)
p2 = (5, 7)

distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
print(distance)
# Part C — Python Sets (Intermediate)
# 1. Elements in first but not second
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
print(s1 - s2)
# 2. Common items between three sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 2, 5}
print(s1 & s2 & s3)
# 3. Unique words in lowercase
sentence = "Hello world hello Python"
words = set(sentence.lower().split())
print(words)
# 4. Remove duplicates → sorted list
lst = [4, 2, 1, 2, 4, 3]
result = sorted(set(lst))
print(result)
# 5. Strict subset check
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1 < s2)
# 6. Set comprehension (squares divisible by 3)
squares = {x*x for x in range(1, 16) if x % 3 == 0}
print(squares)
# 7. Count duplicates in list
lst = [1, 2, 2, 3, 3, 3]
duplicates = len(lst) - len(set(lst))
print(duplicates)
# 8. Remove vowels from string
text = "Hello World"
vowels = {'a', 'e', 'i', 'o', 'u'}
result = ''.join([c for c in text if c.lower() not in vowels])
print(result)
# 9. Symmetric difference
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 ^ s2)
# 10. Check anagram (unique characters only)
str1 = "listen"
str2 = "silent"

print(set(str1) == set(str2))
# Part D — Python Dictionaries (Intermediate)
# 1. Word frequency counter
sentence = "apple banana apple orange banana apple"
words = sentence.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
# 2. Invert dictionary
d = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in d.items()}
print(inverted)
# 3. Merge dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

merged = {**d1, **d2}
print(merged)
# 4. Group words by first letter
words = ['apple', 'ant', 'banana', 'ball']
grouped = {}

for word in words:
    grouped.setdefault(word[0], []).append(word)

print(grouped)
# 5. Filter values > 50
d = {'a': 40, 'b': 60, 'c': 80}
filtered = {k: v for k, v in d.items() if v > 50}
print(filtered)
# 6. Safely access nested dictionary
data = {'user': {'profile': {'name': 'Ali'}}}

name = data.get('user', {}).get('profile', {}).get('name', 'Not Found')
print(name)
# 7. Dictionary comprehension (cubes)
cubes = {x: x**3 for x in range(1, 11)}
print(cubes)
# 8. Key with highest value
d = {'a': 10, 'b': 50, 'c': 30}
highest = max(d, key=d.get)
print(highest)
# 9. Combine two lists into dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]

d = dict(zip(keys, values))
print(d)
# 10. Remove keys with None values
d = {'a': 1, 'b': None, 'c': 3}

cleaned = {k: v for k, v in d.items() if v is not None}
print(cleaned)
