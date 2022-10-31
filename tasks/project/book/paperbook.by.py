from tasks.project.book.book import Book


class PaperBook(Book):
    def __init__(self,title,isbn):
        super().__init__(title, isbn, is_downloadable=False)
