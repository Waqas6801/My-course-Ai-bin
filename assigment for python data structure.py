# Part A — Python Lists (10 Answers)
#1
nums = [3, 1, 4, 1, 5]
print(nums[0])
print(nums[-1])
#2
colors = ['red', 'blue', 'green']
print(len(colors))
#3
colors = ['red', 'blue']
colors.append('yellow')
print(colors)
#4
fruits = ['apple', 'banana']
fruits.insert(1, 'orange')
print(fruits)
#5
fruits = ['apple', 'banana', 'grapes']
fruits.remove('banana')
print(fruits)
#6
items = [10, 20, 30]
popped_value = items.pop()
print(popped_value)
#7
nums = [1, 2, 3, 4]
print(3 in nums)
#8
a = [0, 1, 2, 3, 4]
print(a[2:4])
#9
a = [5, 10, 15]
a[1] = 12
print(a)
#10
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))
# Part B — Python Tuples (10 Answers)
#1
t = (10, 20, 30)
print(t[1])
#2
t = ('a', 'b', 'c')
print(len(t))
#3
x, y = (4, 5)
print(x)
print(y)
#4
t = ('a', 'b', 'c')
print('b' in t)
#5
t = ()
print(type(t))
#6
t1 = (1, 2)
t2 = (3, 4)
new_tuple = t1 + t2
print(new_tuple)
#7
t = (7,)
print(t * 3)
#8
t = (1, 2, 3, 2)
print(t.index(2))
#9
t = (1, 2, 3, 2)
print(t.count(2))
#10
t = (5,)
print(t)
# Part C — Python Sets (10 Answers)
#1
s = set([1, 2, 2, 3])
print(s)
#2
s = {1, 2, 3}
s.add(4)
print(s)
#3
s = {1, 2, 3}
s.remove(2)
print(s)
#4
s = {1, 3, 5}
print(5 in s)
#5
s = {10, 20, 30}
print(len(s))
#6
s = {1, 2, 3}
s.clear()
print(s)
#7
s = {'a', 'b'}
if 'c' not in s:
    s.add('c')
print(s)
#8
lst = ['a', 'a', 'b']
s = set(lst)
print(s)
#9
set1 = {1, 2}
set2 = {2, 3}
print(set1 | set2)
#10
set1 = {1, 2}
set2 = {2, 3}
print(set1 & set2)
# Part D — Python Dictionaries (10 Answers)
#1
d = {'name': 'Ali', 'age': 25}
print(d['name'])
#2
d = {'name': 'Ali', 'age': 25}
d['city'] = 'Lahore'
print(d)
#3
d = {'name': 'Ali', 'age': 25}
d['age'] = 30
print(d)
#4
d = {'name': 'Ali', 'age': 25}
del d['age']
print(d)
#5
d = {'name': 'Ali', 'age': 25}
print('salary' in d)
#6
d = {'a': 1, 'b': 2}
print(d.keys())
#7
d = {'a': 1, 'b': 2}
print(d.values())
#8
d = {'x': 10, 'y': 20}
for k, v in d.items():
    print(k, v)
#9
d = {}
print(d.get('score', 0))
#10
keys = ['a', 'b']
values = [1, 2]
d = dict(zip(keys, values))
print(d)