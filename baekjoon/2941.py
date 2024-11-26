"""
https://www.acmicpc.net/problem/2941
"""

alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

string = input().strip()

for alphabet in alphabets:
    count += string.count(alphabet)
    string = string.replace(alphabet, "0")

for char in string:
    if char != "0":
        count += 1


print(count)
