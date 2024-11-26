"""
https://www.acmicpc.net/problem/25206
"""

import sys

input = sys.stdin.readline

sum_score = 0
total_score = 0

class_avg_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

while True:
    try:
        classes, score, rank = input().split()
        if rank != "P":
            sum_score += float(score) * class_avg_score[rank]
            total_score += float(score)
    except:
        break

print(sum_score / total_score)
