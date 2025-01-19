def solution(s):
    s_num = list(map(int, s.split()))
    answer = f"{min(s_num)} {max(s_num)}"

    return answer
