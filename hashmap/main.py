from typing import Hashable, Optional, Any


class HashMap:
    def __init__(self) -> None:
        self.load = 0
        self.items: list = [None] * 8  # Initial size of the hash table

    def __len__(self) -> int:
        return self.load

    def get(self, key: Hashable) -> Optional[Any]:
        for index in self.items:
            if index is not None and key == index[0]:  # try to find key
                return index[-1]  # return values
        raise KeyError

    def put(self, key: Hashable, value: Any) -> None:
        if not isinstance(key, Hashable):
            raise TypeError("Key must be hashable")

        if self.load > round(len(self.items) * (2 / 3)):  # check table size
            self.items += [None] * len(self.items)  # If 75% occupancy is reached, increase the size.
            self._resize()

        index = hash(key) % len(self.items)

        # find existing key and set value
        for ind, items in enumerate(self.items):
            if items is not None and items[0] == key:
                print(key)
                self.items[ind][-1] = value
                return

        # set new key and value if slot is empty
        for ind, item in enumerate(self.items[index:], start=index):
            if item is None:
                self.items[ind] = [key, hash(key), value]
                self.load += 1
                return

        # set new key and value in previous slots
        for ind, item in enumerate(self.items):
            if item is None:
                self.items[ind] = [key, hash(key), value]
                self.load += 1
                return

    # Here we rehash the entire hash table if the size has changed.
    def _resize(self) -> None:
        lengths = len(self.items)
        create_new = [None] * lengths

        for item in self.items:
            index = None
            if item is not None:
                index = item[1] % len(create_new)

            if index is not None and create_new[index] is None:
                create_new[index] = item
                return

        self.items = create_new
