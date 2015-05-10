import unittest
from music_library import Song
from music_library import Playlist

class TestingSongClass(unittest.TestCase):

    def setUp(self):
        self.s = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
        self.other = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
        self.other2 = Song("Odinkata", "Manowar", "The Sons of Odin", "3:4:40")

    def test_init(self):
        self.assertEqual(self.s.title, "Odin")
        self.assertEqual(self.s.artist, "Manowar")
        self.assertEqual(self.s.album, "The Sons of Odin")
        self.assertEqual(self.s.length, "3:44")

    def test_eq(self):

        self.assertEqual(self.s, self.other)
        self.assertFalse(self.s == self.other2)

    def test_hash(self):
        pass

    def test_str_dunder(self):
        self.assertEqual("Manowar - Odin from The Sons of Odin - 3:44", self.s.__str__())

    def test_lengths(self):
        self.assertEqual(self.s.get_length(seconds=True), 224)
        self.assertEqual(self.other2.get_length(minutes=True), 184)
        self.assertEqual(self.other2.get_length(hours=True), 3)
        self.assertEqual(self.other.get_length(), "3:44")


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.s = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
        self.other = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
        self.other2 = Song("Odinkata", "Manowar", "The Sons of Odin", "3:4:40")
        self.my_playlist = Playlist("MyPlaylist", repeat=True, shuffle=False)

    def test_init(self):
        self.assertTrue(isinstance(self.my_playlist, Playlist))

    def test_add_song(self):
        self.my_playlist.add_song(self.s)
        self.assertTrue(self.s in self.my_playlist.songs)

    def test_add_list_of_songs(self):
        tmp = [self.other, self.other2]
        self.my_playlist.add_songs(tmp)
        self.assertTrue(self.other in self.my_playlist.songs and self.other2 in self.my_playlist.songs)

    def test_remove_song(self):
        tmp = [self.other, self.other2]
        self.my_playlist.add_songs(tmp)
        self.my_playlist.remove_song(self.other)
        self.assertFalse(self.other in self.my_playlist.songs)

    def test_total_length(self):
        tmp = [self.other, self.s]
        self.my_playlist.add_songs(tmp)
#        self.assertEqual(self.my_playlist.total_length(), "3:8:20")

        self.assertEqual(self.my_playlist.total_length(), "7:28")

    def test_artists(self):
        pass

if __name__ == '__main__':
    unittest.main()
