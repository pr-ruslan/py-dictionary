from typing import Any
from dataclasses import dataclass


@dataclass
class Node:
    key: Any
    hash: int
    value: Any


class Dictionary:
    def __init__(self, load_factor: float = 0.66) -> None:
        self.hash_table = [None] * 8
        self.nods_count = 0
        self.empty_cells = [cell for cell in range(8)]
        self.load_factor = load_factor

    def __setitem__(self, key, value) -> None:
        new_node = Node(
            key=key,
            hash=hash(key),
            value=value
        )
        if self.need_resize():
            self.resize()
        if self.hash_table[self.get_cell_number(key)] is None:
            self.hash_table[self.get_cell_number(key)] = new_node
            self.empty_cells.remove(self.get_cell_number(key))
        else:
            self.hash_table[self.empty_cells[0]] = new_node
            self.empty_cells = self.empty_cells[1:]

    def __getitem__(self, key) -> Any:
        if self.hash_table[self.get_cell_number(key)].key == key:
            return self.hash_table[self.get_cell_number(key)].value
        else:
            for cell in self.hash_table:
                if not isinstance(cell, Node):
                    continue
                if key == cell.key:
                    return cell.value

    def need_resize(self) -> bool:
        return self.nods_count + 1 > len(self.hash_table) * self.load_factor

    def resize(self) -> None:
        new_hash_table = [None] * (len(self.hash_table) * 2)
        for item in self.hash_table:
            if item is not None:
                new_hash_table[self.get_cell_number(item.hash)] = item
        self.hash_table = new_hash_table

    def __len__(self) -> int:
        return self.nods_count

    def get_cell_number(self, key) -> int:
        return hash(key) % len(self.hash_table)

