"""
https://www.acmicpc.net/problem/5622
"""

dial = "0000ABC0DEF0GHI0JKL0MNO0PQRSTUV0WXYZ"
string = input().strip()
result = 0

for char in string:
    result += dial.find(char) // 4 + 2


print(result)
