from tasks.project.disc.disc import Disc


class Blueray(Disc):
    def __init__(self, title, isbn, is_downloadable, ):
        super().__init__(title, isbn, is_downloadable=False)
        self._tracks = [],
