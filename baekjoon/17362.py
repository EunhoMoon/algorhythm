"""
https://www.acmicpc.net/problem/17362
"""

n = int(input())
finger = n % 8 if n % 8 != 0 else 2
finger = finger if finger < 6 else 10 - finger

print(finger)