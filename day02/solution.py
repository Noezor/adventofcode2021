from typing import Tuple
from utils import parse_list_of_list

def final_position_d1(commands) -> Tuple:
    x, y = 0, 0
    for (command, k) in commands:
        k = int(k)
        if command == "down":
            y += k
        if command == "up":
            if y-k >= 0:
                y -= k
        if command == "forward":
            x += k
    return (x,y)


def final_position_d2(commands) -> Tuple:
    x, y = 0, 0
    aim = 0
    for (command, k) in commands:
        k = int(k)
        if command == "down":
            aim += k
        if command == "up":
            aim -= k
        if command == "forward":
            x += k
            y += aim*k
    return (x,y)

def multiply_coordinates(last_position):
    return last_position[0]*last_position[1]

final_position_d1 = final_position_d1(parse_list_of_list("day02/input.txt"))
print("solution 1: " + str(final_position_d1[0]*final_position_d1[1]))
print("solution 2:" + str(multiply_coordinates(final_position_d2(parse_list_of_list("day02/input.txt")))))