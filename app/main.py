from typing import Any


class Node:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.hash = hash(key)


class Dictionary:
    def __init__(self, load_factor: float = 2/3) -> None:
        self.hash_table = [None] * 8
        self.empty_cells = [cell for cell in range(8)]
        self.load_factor = load_factor

    def __setitem__(self, key, value) -> None:
        self._resize()
        new_node = Node(
            key=key,
            value=value
        )
        cell = self.get_slot(new_node.key)

        if self.hash_table[cell] is None or self.hash_table[cell].key == new_node.key:
            self.hash_table[cell] = new_node
        else:
            for cell in range(len(self.hash_table)):
                if self.hash_table[cell] is None:
                    self.hash_table[cell] = new_node

    def __getitem__(self, key) -> Any:
        if self.hash_table[self.get_slot(key)] is None:
            raise KeyError
        if self.hash_table[self.get_slot(key)].key == key:
            return self.hash_table[self.get_slot(key)].value
        else:
            for cell in self.hash_table:
                if not isinstance(cell, Node) or cell.key != key:
                    continue
                elif cell.key == key:
                    return cell.value
            # raise KeyError

    def _resize(self) -> None:
        if self.__len__() > len(self.hash_table) * self.load_factor:
            old_hash_table = self.hash_table.copy()
            self.hash_table = [None] * (len(self.hash_table) * 2)
            for item in old_hash_table:
                if item:
                    self.__setitem__(item.key, item.value)

    def get_slot(self, key) -> int:
        slot_number = hash(key) % len(self.hash_table)
        return slot_number

    def __len__(self) -> int:
        nods_count = 0
        for slot in self.hash_table:
            if slot is not None:
                nods_count += 1
        return nods_count
