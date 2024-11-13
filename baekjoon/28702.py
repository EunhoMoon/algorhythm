"""
https://www.acmicpc.net/problem/28702
"""

for i in range(3):
    try:
        num = int(input()) + (3 - i)
        if num % 3 == 0 and num % 5 == 0:
            result = "FizzBuzz"
        elif num % 3 == 0:
            result = "Fizz"
        elif num % 5 == 0:
            result = "Buzz"
        else:
            result = num
        continue
    except:
        continue

print(result)
