from collections import UserDict
from collections.abc import KeysView

class SKVIterator:
    def __init__(self, dict_: dict, out_type: str, reversed=False):
        self.dict = dict_
        self.index = 0
        self.out_type = out_type
        self.reversed = reversed
        self.keyview = dict_.keys()

    def __next__(self):
        if self.index >= len(self.keyview):
            raise StopIteration
        keys = list(self.keyview)
        keys.sort()
        if self.reversed:
            idx = -self.index - 1
        else:
            idx = self.index
        key = keys[idx]
        self.index += 1

        if self.out_type == 'keys':
            return key
        if self.out_type == 'values':
            return self.dict[key]
        if self.out_type == 'items':
            return key, self.dict[key]
        raise Exception(f"Unknown iterator type {self.out_type}")


class SortedView:
    def __init__(self, dict_: dict, out_type: str):
        self.dict = dict_
        self.out_type = out_type

    def __iter__(self):
        return SKVIterator(self.dict, self.out_type)

    def __len__(self):
        return len(self.dict)

    def __reversed__(self):
        return SKVIterator(self.dict, self.out_type, reversed=True)


class SortedKeyView(SortedView):
    def __init__(self, dict_: dict):
        super().__init__(dict_, 'keys')

    def __contains__(self, item):
        return item in self.dict.keys()


class SortedDict(UserDict):
    def keys(self) -> SortedKeyView:
        return SortedKeyView(self.data)

    def items(self) -> SortedView:
        return SortedView(self.data, 'items')

    def values(self) -> SortedView:
        return SortedView(self.data, 'values')

    def __iter__(self):
        return self.keys().__iter__()


if __name__ == "__main__":

    y = {
        'xyz': 1,
        'abc': 2,
        'def': 3,
    }
    x = SortedDict(
        y
    )

    print(y.keys())
    print(list(x.keys()))
    print()
    print(y.items())
    print(list(x.items()))
    print()
    print(y.values())
    print(list(x.values()))
    print()