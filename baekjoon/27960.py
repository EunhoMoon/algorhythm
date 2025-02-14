"""
https://www.acmicpc.net/problem/27960
"""
import sys

input = sys.stdin.readline

A, B = map(int, input().split())
score_board = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
score_A = [0]
score_B = [0]

for i in range(len(score_board)):
    if sum(score_A) < A and sum(score_A) + score_board[i] <= A:
        score_A.append(score_board[i])
    if sum(score_B) < B and sum(score_B) + score_board[i] <= B:
        score_B.append(score_board[i])

score_C = list(filter(lambda x: x not in score_B, score_A)) + list(
    filter(lambda x: x not in score_A, score_B)
)
print(sum(score_C))
