"""
https://www.acmicpc.net/problem/1213
"""

from collections import Counter

engilish_name = input().strip()
alphabet_count = Counter(engilish_name)

mid = ""
odd_count = 0

for char, count in alphabet_count.items():
    if count % 2 == 1:
        odd_count += 1
        mid = char

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    start = ""
    for char in sorted(alphabet_count.keys()):
        start += char * (alphabet_count[char] // 2)

    end = start[::-1]
    print(start + mid + end)