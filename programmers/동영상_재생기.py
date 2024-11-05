def solution(video_len, pos, op_start, op_end, commands):
    video_seconds = time_string_to_seconds_int(video_len)
    pos_seconds = time_string_to_seconds_int(pos)
    opening_start_seconds = time_string_to_seconds_int(op_start)
    opening_end_seconds = time_string_to_seconds_int(op_end)

    pos_seconds = opening_skip(pos_seconds, opening_start_seconds, opening_end_seconds)

    for command in commands:
        if command == "next":
            pos_seconds += 10
        elif command == "prev":
            pos_seconds -= 10
        if pos_seconds < 0:
            pos_seconds = 0
        pos_seconds = opening_skip(
            pos_seconds, opening_start_seconds, opening_end_seconds
        )
        if pos_seconds > video_seconds:
            pos_seconds = video_seconds

    return f"{string_time_fomater(pos_seconds // 60)}:{string_time_fomater(pos_seconds % 60)}"


def time_string_to_seconds_int(time_str):
    time_m, time_s = map(int, time_str.split(":"))
    return time_m * 60 + time_s


def string_time_fomater(num):
    return f"0{num}" if num < 10 else f"{num}"


def opening_skip(s, op_start, op_end):
    if op_start <= s < op_end:
        return op_end
    else:
        return s
