class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


from queue import Queue
import json

class Panda:

    def __init__(self, name, email, gender):
        if not self.__validation_email(email):
            raise ValueError
        self.name = name
        self.email = email
        self.gender = gender

    def __validation_email(self, email):
        tmp = email.split("@")
        if len(tmp) == 2:
            if tmp[1] == "pandamail.com":
                return True
        return False

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.name, self.email, self.gender)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.gender)

    def __eq__(self, other):
        equal_names = self.name == other.name
        equal_emails = self.email == other.email
        equal_genders = self.gender == other.gender
        return equal_names and equal_emails and equal_genders

    def __hash__(self):
        return hash(self.__str__())

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def isMale(self):
        return self.gender == "male"

    def isFemale(self):
        return self.gender == "female"


class PandaSocialNetwork:

    def __init__(self):
        self._pandas = {}

    def add_panda(self, panda):
        if panda in self._pandas:
            raise PandaAlreadyThere
        else:
            self._pandas[panda] = []

    def has_panda(self, panda):
        return panda in self._pandas

    def make_friends(self, panda1, panda2):
        if panda1 not in self._pandas:
            self.add_panda(panda1)
        if panda2 not in self._pandas:
            self.add_panda(panda2)

        if panda1 in self._pandas[panda2]:
            raise PandasAlreadyFriends

        if panda2 in self._pandas[panda1]:
            raise PandasAlreadyFriends

        self._pandas[panda1].append(panda2)
        self._pandas[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda1 not in self._pandas or panda2 not in self._pandas:
            return False
        if panda1 in self._pandas[panda2] and panda2 in self._pandas[panda1]:
            return True
        return False

    def friends_of(self, panda):
        if panda not in self._pandas:
            return False
        return self._pandas[panda]

    def connection_level(self, panda1, panda2):
        if panda1 not in self._pandas or panda2 not in self._pandas:
            return False

        c_level = 1
        if panda1 in self._pandas[panda2]:
            return c_level

        tmp = Queue()
        tmp.put(panda1)
        helper = []
        while not tmp.empty():
            current_panda = tmp.get()
            helper.append(current_panda)
            current_panda_frs = self.friends_of(current_panda)
            if panda2 in current_panda_frs:
                return c_level
            for each in current_panda_frs:
                if each not in helper:
                    tmp.put(each)
            c_level += 1

        return -1

    def are_connected(self, panda1, panda2):
        if(self.connection_level(panda1, panda2) >= 1):
            return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        counter = 0

        for current_panda in self._pandas:
            if self.connection_level(panda, current_panda) == level and \
                    current_panda.get_gender() == gender:
                counter += 1

        if level == 2:
            helper = self.how_many_gender_in_network(3, panda, gender)
            counter += helper

        return counter


    def save(self, file_name):
        temp = {str(panda): [str(friend) for friend in friends] for panda, friends in self._pandas.items()}
        a_text = json.dumps(temp)
        panda_file = open(file_name, "w")
        panda_file.write(a_text)
        panda_file.close()

    def load(self, file_name):
        panda_network = open(file_name, 'r')
        contents = panda_network.read()
        return json.load(contents)

        panda_network.close()


if __name__ == '__main__':

    pandio = Panda("Ivo", "ivo@pandamail.com", "male")
    pandio2 = Panda("Rado", "rado@pandamail.com", "male")
    pandio3 = Panda("Azi", "rado@pandamail.com", "female")
    pandiofriendless = Panda("tozi", "rado@pandamail.com", "female")
    pp = Panda("Azidazi", "rado@pandamail.com", "female")
    pandichki = PandaSocialNetwork()
    pandichki.make_friends(pandio, pandio2)
    pandichki.make_friends(pandio, pandio3)
    pandichki.make_friends(pandio, pandiofriendless)
    pandichki.make_friends(pp, pandio2)

    pandichki.save("testing_function.json")



