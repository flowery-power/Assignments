class Library:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    @property
    def items(self):
        return self._items
