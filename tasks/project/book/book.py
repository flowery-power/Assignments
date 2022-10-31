from tasks.project.track.track import Item


class Book(Item):
    def __init__(self, title, isbn, author, number_pages, is_downloadable):
        super().__init__(title, isbn, is_downloadable)
        self.author = author,
        self.number_pages = number_pages
