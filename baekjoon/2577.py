"""
https://www.acmicpc.net/problem/2577
"""

numbers = list(str(int(input()) * int(input()) * int(input())))

for i in range(10):
    print(numbers.count(str(i)))
