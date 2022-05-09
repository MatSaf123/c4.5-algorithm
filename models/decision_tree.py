from dataclasses import dataclass
from models.node import Node


@dataclass
class Tree:
    root: Node
