from typing import List, Union
from models.node import Node


def unique(sequence):
    """Preserves order of the sequence"""
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]
