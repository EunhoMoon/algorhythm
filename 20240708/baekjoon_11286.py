"""
https://www.acmicpc.net/problem/11286
 - 우선순위 큐
 - 절대 값과 원 값을 tuple로 저장하여 값의 크기 확인
"""

import sys
import heapq as hq

input = sys.stdin.readline
pq = []

for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(pq, (abs(x), x))
    else:
        print(hq.heappop(pq)[1] if pq else 0)


# tuple을 사용하지 않는 방법
# min_heap = []  # 양수
# max_heap = []  # 음수(최대 heap)
# for _ in range(int(input())):
#     x = int(input())
#     if x:
#         if x > 0:
#             hq.heappush(min_heap, x)
#         else:
#             hq.heappush(max_heap, -x)
#     else:
#         if min_heap:
#             if max_heap:
#                 if min_heap[0] < max_heap[0]:
#                     print(hq.heappop(min_heap))
#                 else:
#                     print(-hq.heappop(max_heap))
#             else:
#                 print(hq.heappop(min_heap))
#         else:
#             if max_heap:
#                 print(-hq.heappop(max_heap))
#             else:
#                 print(0)
