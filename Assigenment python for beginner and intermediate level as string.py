# Beginner Level — String Fundamentals
# 1️ Length of a String
s = input("Enter a string: ")
print(len(s))
# 2️ Uppercase & Lowercase
s = input("Enter a string: ")
print(s.upper())
print(s.lower())
# 3️ Count a Character
s = input("Enter a string: ")
ch = input("Enter a character to count: ")
print(s.count(ch))
# 4️ First & Last Character
s = input("Enter a string: ")

if not s:
    print("Empty string")
else:
    print("First:", s[0])
    print("Last:", s[-1])
# 5️ Check Substring Presence
s = input("Enter main string: ")
sub = input("Enter substring: ")
print(sub in s)
# 6️ Slice a String
s = input("Enter string: ")
start = int(input("Start index: "))
end = int(input("End index: "))
print(s[start:end])
# 7️ Reverse a String
s = input("Enter string: ")
print(s[::-1])
# 8️ Replace Substring (Case-Sensitive)
s = input("Enter sentence: ")
old = input("Word to replace: ")
new = input("Replace with: ")

print(s.replace(old, new))
# 9️ Split and Join
s = input("Enter sentence: ")
words = s.split()
result = "-".join(words)
print(result)
# 10 Strip Whitespace
s = input("Enter text with spaces: ")
print(s.strip())
# Intermediate Level — More Involved String Tasks
# 1️ Count Vowels & Consonants
s = input("Enter string: ")

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
# 2️ Palindrome Check (Ignore Case & Non-Alphanumeric)
s = input("Enter string: ")

normalized = ''.join(ch.lower() for ch in s if ch.isalnum())

print(normalized == normalized[::-1])
# 3️ Manual Title Case
s = input("Enter sentence: ")

words = s.split()
title_words = []

for word in words:
    if word:
        title_words.append(word[0].upper() + word[1:].lower())

print(" ".join(title_words))
# 4️ Find All Indices of a Substring (Allow Overlaps)
s = input("Enter string: ")
sub = input("Enter substring: ")

indices = []

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        indices.append(i)

print(indices)
# 5️ Character Frequency Dictionary
s = input("Enter string: ")

freq = {}

for ch in s.lower():
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

print(freq)
# 6️ Anagram Checker
s1 = input("First string: ")
s2 = input("Second string: ")

clean1 = ''.join(ch.lower() for ch in s1 if ch.isalpha())
clean2 = ''.join(ch.lower() for ch in s2 if ch.isalpha())

print(sorted(clean1) == sorted(clean2))
# 7️ Compress Repeated Characters (RLE-lite)
s = input("Enter string: ")

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1

if s:
    result += s[-1] + str(count)

print(result)
# 8️ Longest Word in Sentence
s = input("Enter sentence: ")

words = s.split()
longest = ""

for word in words:
    clean = ''.join(ch for ch in word if ch.isalpha())
    if len(clean) > len(longest):
        longest = clean

print(longest)
# 9️ Remove Duplicate Characters (Keep Order)
s = input("Enter string: ")

seen = set()
result = ""

for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)
# 10 Mask Email Username
email = input("Enter email: ")

username, domain = email.split("@")

if len(username) >= 2:
    masked = username[0] + "*" * (len(username) - 2) + username[-1]
else:
    masked = username

print(masked + "@" + domain)