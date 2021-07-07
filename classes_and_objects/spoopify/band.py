from project.album import Album
from project.song import Song

class Band:
    albums = []
    def __init__(self, name):
        self.name = name

    def add_album(self, album):
        if not album in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        for i in self.albums:
            if i.name == album_name:
                if i.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(i)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        nl = "\n"
        return f"Band {self.name}\n" \
               f"{nl.join(x.details() for x in self.albums)}"

