import sys

sys.setrecursionlimit(10**6)


def find(room_id):
    if room_id not in next_rooms:
        next_rooms[room_id] = room_id + 1
        return room_id

    next_rooms[room_id] = find(next_rooms[room_id])
    return next_rooms[room_id]


def solution(k, room_number):
    global next_rooms
    next_rooms = {}
    ans = []
    for room_id in room_number:
        ans.append(find(room_id))
    return ans
