def get_hand(x, y):
    if y == 0:
        return "L"
    if y == 2:
        return "R"

    left_dist = abs(x - left_x) + abs(y - left_y)
    right_dist = abs(x - right_x) + abs(y - right_y)

    if left_dist < right_dist:
        return "L"
    elif left_dist > right_dist:
        return "R"
    else:
        return hand_type


def push(x, y, hand_type):
    global left_x, left_y, right_x, right_y
    if hand_type == "L":
        left_x, left_y = x, y
    else:
        right_x, right_y = x, y
    return hand_type


def solution(numbers, hand):
    global left_x, left_y, right_x, right_y, hand_type
    ans = ""
    left_x, left_y = 3, 0
    right_x, right_y = 3, 2
    hand_type = "L" if hand == "left" else "R"

    for n in numbers:
        if n == 0:
            x, y = 3, 1
        else:
            x, y = (n - 1) // 3, (n - 1) % 3
        ans += push(x, y, get_hand(x, y))

    return ans
