from tasks.project.track.track import Item


class Disc(Item):
    def __init__(self, title, isbn, is_downloadable, ):
        super().__init__(title, isbn, is_downloadable)
        self._tracks = [],

