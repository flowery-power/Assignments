from tasks.project.disc.disc import Disc


class Dvd(Disc):
    def __init__(self, title, isbn):
        super().__init__(title, isbn, is_downloadable=False)
        self._tracks = [],
