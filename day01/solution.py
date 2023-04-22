from utils import parse

from typing import List

input = 'day01/input.txt'

measures = parse(input)

def nb_increase(input : List[int]) -> int:
    previous = input[0]
    count = 0
    for x in input[1:]:
        if x > previous:
            count += 1
        previous = x
    return count

print("solution 1 ", nb_increase(measures))
print("solution 2 ", nb_increase([sum([measures[i+k] for k in range(3)]) for i in range(len(measures)-2)]))
Hahahahh