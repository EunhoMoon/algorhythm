"""
https://www.acmicpc.net/problem/1157
"""

string = input().strip()
char_dict = {}

for char in string:
    char = char.upper()

    if char in char_dict.keys():
        char_dict[char] += 1
    else:
        char_dict[char] = 1

max_keys = [key for key, value in char_dict.items() if value == max(char_dict.values())]

print(max_keys[0] if len(max_keys) == 1 else "?")
