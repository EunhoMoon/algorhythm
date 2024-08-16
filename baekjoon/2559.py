"""
https://www.acmicpc.net/problem/2559
 - 슬라이딩 윈도우
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = sum(arr[:K])
max_sum = current_sum

for i in range(K, N):
    current_sum = current_sum - arr[i - K] + arr[i]
    max_sum = max(current_sum, max_sum)

print(max_sum)