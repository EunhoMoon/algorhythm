"""
https://www.acmicpc.net/problem/10816
 - 시간 복잡도
 - Counter
"""

import sys
from collections import Counter

input = sys.stdin.readline

answer = []
num = int(input())
cards = list(map(int, input().split()))
q = int(input())
numbers = list(map(int, input().split()))

card_count = Counter(cards)

for number in numbers:
    answer.append(card_count.get(number, 0))

# 결과 출력
print(" ".join(map(str, answer)))
