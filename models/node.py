from __future__ import annotations
from dataclasses import dataclass
from typing import List
from .decision_table import DecisionTable


@dataclass
class Node:
    label: int
    branch_label: str
    children: List[Node]
    decision_table: DecisionTable
