"""
https://www.acmicpc.net/problem/2475
"""

numbers = map(int, input().split())

pow_numbers = []

for number in numbers:
    pow_numbers.append(number * number)

print(sum(pow_numbers) % 10)
