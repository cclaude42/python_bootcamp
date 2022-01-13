""" GotCharacter class

"""
class GotCharacter:
    """A generic class to inherit from to represent a GoT character"""

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Baelish(GotCharacter):
    """A class to represent the Baelish House - or how one man can stand by himself"""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Baelish"
        self.house_words = "Knowledge is Power"

    def print_house_words(self):
        """A function that prints the motto of the character's house"""
        print(self.house_words)

    def die(self):
        """A function that kills the instance of the character"""
        self.is_alive = False
