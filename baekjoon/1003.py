"""
https://www.acmicpc.net/problem/1003
"""
import sys 

input = sys.stdin.readline

T = int(input())

check = [[0, 0] for _ in range(41)]
check[0] = [1, 0]
check[1] = [0, 1]

def fibonacci(num):
    if num == 0 or num == 1:
        return check[num]
    else:
        if check[num] == [0, 0]:
            minus_one = fibonacci(num - 1)
            minus_two = fibonacci(num - 2)

            present_num = [minus_one[0] + minus_two[0], minus_one[1] + minus_two[1]]
            check[num] = present_num
            return check[num]
        else:
            return check[num]

for _ in range(T):
    N = int(input())

    count = fibonacci(N)
    print(f"{count[0]} {count[1]}")


