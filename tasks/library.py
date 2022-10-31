class Item:
    def __init__(self, title, isbn, is_downloadable):
        self.title = title,
        self.isbn = isbn,
        self.is_downloadable = is_downloadable


class Library:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    @property
    def items(self):
        return self._items


class Book(Item):
    def __init__(self, title, isbn, author, number_pages, is_downloadable):
        super().__init__(title, isbn, is_downloadable)
        self.author = author,
        self.number_pages = number_pages


class PaperBook(Book):
    def __init__(self):
        super().__init__(title, isbn, False)


class Ebook(Book):
    def __init__(self):
        super().__init__(title, isbn, True)


class Disc(Item):
    def __init__(self, title, isbn, is_downloadable, type):
        super().__init__(title, isbn, is_downloadable)
        self._tracks = [],
        self.type = type

    def add_track(self, track):
        self._tracks.append(track)

    @property
    def tracks(self):
        return self._tracks


class Track:
    def __init__(self, title, duration, artist):
        self.title = title,
        self.artist = artist,
        self.duration = duration,
