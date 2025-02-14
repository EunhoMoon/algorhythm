"""
https://www.acmicpc.net/problem/10988
"""

string = input().strip()
left = 0
right = len(string) - 1
is_true = True

while left <= right:
    if string[left] != string[right]:
        is_true = False
        break
    left += 1
    right -= 1

print(1 if is_true else 0)
