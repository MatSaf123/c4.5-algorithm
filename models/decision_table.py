from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class DecisionTable:
    table: List[List[any]]
