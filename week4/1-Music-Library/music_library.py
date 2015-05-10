import json
from tabulate import tabulate
from random import randint
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3
import os

class Song(object):

    def __init__(self, title="None", artist="None", album="None", length="None"):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __eq__(self, other):
        same_title = self.title == other.title
        same_artist = self.artist == other.artist
        same_album = self.album == other.album
        same_length = self.length == other.length
        return same_title and same_artist and same_album and same_length

    def __hash__(self):
        return hash(self.artist)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def song_to_dict(self):
        return {"artist": self.artist, "title": self.title,
                "album": self.album, "length": self.length}

    def get_length(self, seconds=False, minutes=False, hours=False):
        result = 0
        tmp = []
        tmp1 = self.length.split(":")
        for each in tmp1:
            tmp.append(int(each))

        if seconds is True:
            if len(tmp) == 2:
                result += tmp[0] * 60 + tmp[1]
            else:
                result += (tmp[0] * 60 + tmp[1]) * 60 + tmp[2]
        elif minutes is True:
            if len(tmp) == 2:
                result += tmp[0]
            else:
                result += tmp[1] + tmp[0] * 60
        elif hours is True:
            if len(tmp) == 3:
                result += tmp[0]
            else:
                raise ValueError

        if seconds is False and minutes is False and hours is False:
            return str(self.length)

        return result


class Playlist(object):

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle

        self.songs = []
        self.counter = 0

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def add_songs(self, songs):
        for each in songs:
            self.songs.append(each)

    def total_length(self):
        totalSongLen = 0
        for song in self.songs:
            current_song_len = song.get_length(seconds=True)
            totalSongLen += current_song_len
        hours = totalSongLen // 360
        minutes = (totalSongLen % 360) // 60
        seconds = (totalSongLen // 360) % 60
        tmp_length = [str(hours), str(minutes), str(seconds)]
        return ":".join(tmp_length)

    def artists(self):
        dict_of_artist = {}
        for song in self.songs:
            if song.artist in dict_of_artist:
                dict_of_artist[song.artist] += 1
            else:
                dict_of_artist[song.artist] = 1
        return dict_of_artist

    def mapping_to_lists(self):
        helper_list = []
        for element in self.songs:
            helper_list.append(
                [element.artist, element.title, element.album, element.length])
        return helper_list

    def pprint_playlist(self):
        tmp = self.mapping_to_lists()
        print(tabulate(
            tmp, headers=["Artist", "Title", "Album", "Length"], tablefmt="fancy_grid"))

    def next_song(self):
        if self.counter == len(self.songs):
            if self.repeat is True:
                self.counter = 0
                song_to_play = self.counter
        else:
            song_to_play = self.counter
        self.counter += 1

        if self.shuffle is True:
            song_to_play = randint(0, len(self.songs))

        return self.songs[song_to_play]

    def save(self):
        temp = {"songs": [element.song_to_dict() for element in self.songs]}
        json_text = json.dumps(temp, indent=4)
        filename = "-".join(self.name.split(" "))  # + ".json"
        music_player_file = open(filename, "w")
        music_player_file.write(json_text)
        music_player_file.close()

    @staticmethod
    def load(path):
        filename = " ".join(path.split("-"))
        current_playlist = open(filename, 'r')
        contents = current_playlist.read()
        da_text = json.loads(contents)
        da_playlist = Playlist(filename)
        for dict_song in da_text["songs"]:
            song = Song(artist=dict_song["artist"], title=dict_song[
                        "title"], album=dict_song["album"], length=dict_song["length"])
            da_playlist.add_song(song)

        current_playlist.close()
        return da_playlist


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        file_list = []
        rootdir = self.path
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                file_list.append(os.path.join(subdir, file))
        print(file_list)
    """
        current_playlist = Playlist("MyPlaylist")

        for song in file_list:
            audio = MP3(song)
            audio_a = EasyID3(song)
            tmp_song = Song(length=["audio.info.length"], artist=audio_a['artist'][0], album=audio_a['album'][0], title=audio_a['title'][0])
            current_playlist.add_song(tmp_song)

        return current_playlist
    """

def main():
    """
    s = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
    other = Song("Dva", "Manowar", "The Sons of Odin", "3:44")
    other2 = Song("Tri", "Manowar", "The Sons of Odin", "3:4:40")
    tmp = [s, other, other2]
    spisuk = Playlist("toqplaylist")

    spisuk.add_songs(tmp)
    spisuk.save()

    opii = spisuk.load("toqplaylist")
    opii.pprint_playlist()

    spisuk.pprint_playlist()

    print(spisuk.next_song())
    print(spisuk.next_song())
    print(spisuk.next_song())
    print(spisuk.next_song())

     print(spisuk.artists())

    """
    """
crawler = MusicCrawler("/home/hrizantema/Music")
playlist = crawler.generate_playlist()
playlist.pprint_playlist()
"""

if __name__ == '__main__':
    main()
