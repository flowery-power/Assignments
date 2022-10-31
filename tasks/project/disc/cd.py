from tasks.project.disc.disc import Disc


class CD(Disc):
    def __init__(self, title, isbn ):
        super().__init__(title, isbn, is_downloadable=True)
        self._tracks = [],
