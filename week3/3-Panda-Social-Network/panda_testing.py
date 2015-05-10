import unittest
from panda import Panda
from panda import PandaSocialNetwork
from panda import PandaAlreadyThere
from panda import PandasAlreadyFriends

class TestPandaClass(unittest.TestCase):

    def setUp(self):
        self.test_obj = Panda("Ivo", "ivo@pandamail.com", "male")
        self.test_obj2 = Panda("Rado", "rado@pandamail.com", "male")
        self.test_obj3 = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_init(self):
        self.assertTrue(isinstance(self.test_obj, Panda))

    def test_wrong_init(self):
        with self.assertRaises(ValueError):
            wrong_answ = Panda("mitio", "mitko.com", "male")

    def test_str_method(self):
        self.assertEqual(str(self.test_obj), "Ivo")

    def test_eq_method(self):
        self.assertFalse(self.test_obj == self.test_obj2)
        self.assertEqual(self.test_obj, self.test_obj3)

    def test_get_name(self):
        self.assertEqual(self.test_obj.get_name(), "Ivo")

    def test_get_email(self):
        self.assertEqual(self.test_obj.get_email(), "ivo@pandamail.com")

    def test_is_Female(self):
        self.assertFalse(self.test_obj.isFemale())

    def test_is_Male(self):
        self.assertTrue(self.test_obj.isMale())

    def test_gender(self):
        self.assertEqual(self.test_obj.get_gender(), "male")


class TestingPandaSocialNetword(unittest.TestCase):

    def setUp(self):
        self.pandio = Panda("Ivo", "ivo@pandamail.com", "male")
        self.pandio2 = Panda("Rado", "rado@pandamail.com", "male")
        self.pandio3 = Panda("Azi", "rado@pandamail.com", "female")
        self.pandiofriendless = Panda("tozi", "rado@pandamail.com", "female")
        self.pp = Panda("Azidazi", "rado@pandamail.com", "female")
        self.pandichki = PandaSocialNetwork()

    def test_add_panda_function(self):
        self.pandichki.add_panda(self.pandio)
        self.assertTrue(self.pandio in self.pandichki._pandas)
        with self.assertRaises(PandaAlreadyThere):
            self.pandichki.add_panda(self.pandio)

    def test_has_panda_func(self):
        self.pandichki.add_panda(self.pandio)
        self.assertTrue(self.pandichki.has_panda(self.pandio))
        self.assertFalse(self.pandichki.has_panda(self.pandio2))

    def test_make_friends(self):
        self.pandichki.make_friends(self.pandio, self.pandio2)
        self.assertTrue(self.pandio in self.pandichki._pandas[self.pandio2])
        with self.assertRaises(PandasAlreadyFriends):
            self.pandichki.make_friends(self.pandio2, self.pandio)

    def test_are_friends(self):
        self.pandichki.make_friends(self.pandio, self.pandio2)
        self.assertTrue(self.pandichki.are_friends(self.pandio, self.pandio2))
        self.assertFalse(self.pandichki.are_friends(self.pandio, self.pandio3))

    def test_of_friendship(self):
        self.pandichki.make_friends(self.pandio, self.pandio2)
        self.assertEqual([self.pandio], self.pandichki.friends_of(self.pandio2))
        self.pandichki.make_friends(self.pandio2, self.pandio3)
        self.assertEqual([self.pandio, self.pandio3], self.pandichki.friends_of(self.pandio2))
        self.assertFalse(self.pandichki.friends_of(self.pandiofriendless))

    def test_connection_level(self):
        self.pandichki.make_friends(self.pandio, self.pandio2)
        self.pandichki.add_panda(self.pp)
        self.assertEqual(1, self.pandichki.connection_level(self.pandio, self.pandio2))
        self.pandichki.make_friends(self.pandio2, self.pandio3)
        self.assertEqual(2, self.pandichki.connection_level(self.pandio, self.pandio3))
        self.assertFalse(self.pandichki.connection_level(self.pandio, self.pandiofriendless))
        self.assertEqual(-1, self.pandichki.connection_level(self.pandio, self.pp))

    def test_are_connecter(self):
        self.pandichki.make_friends(self.pandio, self.pandio2)
        self.assertTrue(self.pandichki.are_connected(self.pandio, self.pandio2))
        self.pandichki.add_panda(self.pp)
        self.assertFalse(self.pandichki.are_connected(self.pandio, self.pp))

    def test_connection_with_cycle(self):
        pandas = [Panda("Ivo{}".format(i), "ivo@pandamail.com", "male") for i in range(5)]
        network = PandaSocialNetwork()

        network.make_friends(pandas[0], pandas[1])
        network.make_friends(pandas[0], pandas[2])
        network.make_friends(pandas[1], pandas[3])
        network.make_friends(pandas[3], pandas[4])
        network.make_friends(pandas[4], pandas[2])

        self.assertTrue(network.connection_level(pandas[0], pandas[4]), 2)

    def test_how_many_gender_in_network(self):
        network = PandaSocialNetwork()
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        tony = Panda("Tony", "tony@pandamail.com", "female")

        for panda in [ivo, rado, tony]:
            network.add_panda(panda)

        network.make_friends(ivo, rado)
        network.make_friends(rado, tony)

        self.assertTrue(network.how_many_gender_in_network(1, rado, "female") == 1)
        self.assertTrue(network.connection_level(ivo, rado) == 1)
        self.assertTrue(network.connection_level(ivo, tony) == 2)

    def test_how_many_gender_in_network_again(self):
        pass


if __name__ == '__main__':
    unittest.main()
