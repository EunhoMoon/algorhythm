"""
https://www.acmicpc.net/problem/2559
 - 슬라이딩 윈도우
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

old_val = sum(arr[0:K])
result = old_val

for i in range(1, len(arr) - K + 1):
    new_val = old_val - arr[i - 1] + arr[i + K - 1]
    if result < new_val:
        result = new_val
    old_val = new_val

print(result)