from typing import List

def parse(filepath) -> List[str]:
    with open(filepath, "r") as f:
        return [[x.strip()] for x in f.read().split('\n')]

def parse_list_of_list(filepath) -> List[str]:
    with open(filepath, "r") as f:
        return [[y.strip() for y in x.split(" ")] for x in f.read().split('\n')]
