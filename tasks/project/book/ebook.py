from tasks.project.book.book import Book


class Ebook(Book):
    def __init__(self, title, isbn):
        super().__init__(title, isbn, is_downloadable=True)
