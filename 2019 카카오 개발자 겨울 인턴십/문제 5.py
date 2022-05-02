# from bisect import bisect_left


def search(room_number, k, rooms):
    start, end = room_number, k
    while start + 1 < end:
        print(start, end, rooms)
        mid = (start + end) // 2
        if mid in rooms:
            end = mid
        else:
            start = mid
    return end


def solution(k, room_numbers):
    rooms = set(range(1, k + 1))
    ans = []

    for room_number in room_numbers:
        if room_number in rooms:
            rooms.remove(room_number)
            ans.append(room_number)
        else:
            target = search(room_number, k, rooms)
            rooms.remove(target)
            ans.append(target)

    return ans


print(solution(10, [1, 3, 4, 1, 3, 1]))
