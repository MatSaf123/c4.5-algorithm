import csv
from typing import Dict, List

# TODO: move this away from main.py


def read_from_file(path: str, delimiter=",") -> List[any]:
    with open(path, newline="") as file:
        return [row for row in csv.reader(file, delimiter=delimiter)]


def count_classes(data: List[List[any]]) -> List[int]:
    if data is None:
        return 0
    size = len(data[0])
    counts = []
    for i in range(size):
        uniques = set([val[i] for val in data])
        counts.append(len(uniques))
    return counts


def count_class_occurances(data: List[List[any]]) -> List[Dict[str, int]]:
    if data is None:
        return 0
    size = len(data[0])
    class_sets = []
    for i in range(size):
        uniques = set([val[i] for val in data])
        class_sets.append(list(uniques))
    occurances = [dict.fromkeys(class_set, 0) for class_set in class_sets]
    for ele in data:
        for i, row in enumerate(ele):
            occurances[i][str(row)] += 1
    return occurances
