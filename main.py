import csv
from math import log2
from typing import Dict, List, Tuple
from models.decision_table import DecisionTable
from models.node import Node
from utils import unique

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
        uniques = unique([val[i] for val in data])
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
        data_subset = [row for row in data if row[attribute_index] == attribute_key]
        info_value += (
            len(data_subset)
            / len(data)
            * compute_entropy(compute_probabilities(data_subset))
        )
    return info_value


def compute_gain(attribute_index: int, data: List[any]):
    return compute_entropy(compute_probabilities(data)) - compute_info(
        attribute_index, data
    )


def compute_split_info(attribute_index: int, data: List[any]):
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
    probabilities = []
    for attribute_key in class_occurances[attribute_index].keys():
        data_subset = [row for row in data if row[attribute_index] == attribute_key]
        probabilities.append(len(data_subset) / len(data))
    return compute_entropy(probabilities)


def compute_gain_ratio(attribute_index: int, data: List[any]):
    gain = compute_gain(attribute_index, data)
    split_info = compute_split_info(attribute_index, data)
    if split_info == 0:
        return 0
    return gain / split_info


def choose_attribute_to_divide_by(table: DecisionTable) -> Tuple[int, int]:
    max_gr = 0
    max_gr_index = None
    for i in range(len(table.table[0]) - 1):
        gr = compute_gain_ratio(i, table.table)
        if max_gr < gr:
            max_gr = gr
            max_gr_index = i
    return max_gr, max_gr_index


def divide_table_by_attribute(
    table: DecisionTable, attribute_index: int
) -> List[DecisionTable]:
    classes = list(count_class_occurances(table.table)[attribute_index].keys())
    subtables = {k: [] for k in classes}
    for row in table.table:
        subtables[row[attribute_index]].append(row)
    return [DecisionTable(subtable) for subtable in subtables.values()]


def divide_node(node: Node) -> None:
    table = node.decision_table
    max_gr, max_gr_index = choose_attribute_to_divide_by(table)
    if max_gr == 0:
        return None

    subtables = divide_table_by_attribute(table, max_gr_index)
    node.children.extend(
        [
            Node(max_gr_index, table.table[0][max_gr_index], [], table)
            for table in subtables
        ]
    )

    for c in node.children:
        divide_node(c)


def get_max_from_decision_table(table):
    temp = count_class_occurances(table)[-1]
    max_k = table[0][-1]
    max_v = temp[max_k]
    for k, v in temp.items():
        if v > max_v:
            max_v = v
            max_k = k
    return max_k

def print_tree(node: Node, indent: int) -> None:
    if node.label is None and node.branch_label is None:
        print(f'Atrybut: {node.children[0].label}')
    elif len(node.children) == 0:
        print(" "*indent + " " + str(node.branch_label) + "->" + get_max_from_decision_table(node.decision_table.table))
    else:
        print(" "*indent + " " + str(node.branch_label) + "->" + f'Atrybut: {str(node.children[0].label)}')
    for c in node.children:
        print_tree(c, indent+4)



def run():
    # data = read_from_file("data/gielda.txt")
    # data = read_from_file("data/car.data")
    data = read_from_file("data/breast-cancer.data")  

    root = Node(None, None, [], DecisionTable(data))
    divide_node(root)
    print_tree(root, 0)

run()
