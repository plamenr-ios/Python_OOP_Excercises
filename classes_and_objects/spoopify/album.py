from project.song import Song

class Album:
    def __init__(self, name, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = [x for x in args]

    def add_song(self, song):
        if self.published == True:
            return "Cannot add songs. Album is published."
        if not song in self.songs:
            if song.single == True:
                return f"Cannot add {song.name}. It's a single"
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        return "Song is already in the album."

    def remove_song(self, song_name):
        if self.published == True:
            return "Cannot remove songs. Album is published."
        for i in self.songs:
            if i.name == song_name:
                self.songs.remove(i)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        nl = "\n"
        return f"Album {self.name}\n" \
               f"{nl.join(f'== {x.get_info()}' for x in self.songs)}"



