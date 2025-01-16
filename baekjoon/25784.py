"""
https://www.acmicpc.net/problem/25784
"""

from queue import PriorityQueue

q = PriorityQueue(maxsize=3)
nums = map(int, input().split())

for num in nums:
    q.put(num)

min_num = q.get(0)
mid_num = q.get(1)
max_num = q.get(3)

if min_num + mid_num == max_num:
    print(1)
elif min_num * mid_num == max_num:
    print(2)
else:
    print(3)
