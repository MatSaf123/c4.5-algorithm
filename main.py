import csv
from math import log2
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


def compute_probabilities(data: List[Dict[str, int]]) -> List[float]:
    return [ele / len(data) for ele in count_class_occurances(data)[-1].values()]


def compute_entropy(probabilities: List[int]):
    for p in probabilities:
        if p < 0 or p > 1:
            raise ValueError(f"Expected value in <0,1> range, found: {p}")
    return -(sum([p * log2(p) for p in probabilities if p != 0]))


def compute_info(attribute_index: int, data: List[any]):
    n = len(data)
    len_entry = len(data[0])

    if attribute_index > len_entry - 1:
        raise ValueError(
            f"Attribute with index {attribute_index} not found in data dictionary keys"
        )
    elif attribute_index == len_entry - 1:
        raise ValueError(
            f"Last index ({attribute_index}) is reserved for decisional attribute"
        )

    class_occurances = count_class_occurances(data)
    info_value = 0
    for attribute_key in class_occurances[attribute_index].keys():
        data_subset = [row for row in data if row[0] == attribute_key]
        info_value += (
            len(data_subset) / n * compute_entropy(compute_probabilities(data_subset))
        )
    return info_value


def compute_gain(attribute_index: int, data: List[any]):
    return compute_entropy(compute_probabilities(data)) - compute_info(
        attribute_index, data
    )


def compute_gain_ratio():
    # TODO: implement
    pass
