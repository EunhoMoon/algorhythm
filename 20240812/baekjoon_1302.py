"""
https://www.acmicpc.net/problem/1302
 - dictionary & sorting
"""

d = dict()
for _ in range(int(input())):
    book = input()
    d[book] = d.get(book, 0) + 1

max_val = max(d.values())

for k, v in sorted(d.items()):
    if v == max_val:
        print(k)
        break
