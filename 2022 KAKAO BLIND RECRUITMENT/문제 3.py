from math import ceil


def time_to_min(time):
    hour, min_ = time.split(":")
    hour, min_ = int(hour), int(min_)
    return 60 * hour + min_


def solution(fees, records):
    basic_time, basic_fare, unit_time, unit_fare = fees
    history = {}
    ans = []

    for record in records:
        time, carnum, detail = record.split()
        if carnum not in history:
            history[carnum] = [time]
        else:
            history[carnum].append(time)

    for carnum in history:
        if len(history[carnum]) % 2 == 1:
            history[carnum].append("23:59")
        elapsed_time = 0
        for i in range(0, len(history[carnum]), 2):
            elapsed_time += time_to_min(history[carnum][i + 1]) - time_to_min(
                history[carnum][i]
            )

        total = (
            basic_fare + ceil(max(elapsed_time - basic_time, 0) / unit_time) * unit_fare
        )
        ans.append((total, carnum))

    ans.sort(key=lambda x: x[1])
    return [x[0] for x in ans]
