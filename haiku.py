# Build a random haiku from 5 and 7 syllable phrases saved on file

from random import randint


class Haiku():

    def __init__(self):
        self.five_path = "data/5s.txt"
        self.seven_path = "data/7s.txt"

        self.five_limit = self.get_limit(self.five_path)
        self.seven_limit = self.get_limit(self.seven_path)

    # Get the upper limit of the amount of phrases
    # for random number generation
    def get_limit(self, filepath):
        with open(filepath) as f:
            for i, l in enumerate(f):
                pass
            return i



    # Get a random 5 or 7 syllable phrase from file
    def get_phrase(self, choice, random_int):
        if choice == "five":
            f = open(self.five_path)
            five = f.readlines()[random_int]
            f.close
            return five
        else:
            f = open(self.seven_path)
            seven = f.readlines()[random_int]
            f.close
            return seven


    def build_haiku(self):

        # Get random phrase numbers between 0 and file length
        rand_five_one = randint(0, self.five_limit)
        rand_seven = randint(0, self.seven_limit)
        rand_five_two = randint(0, self.five_limit)


        # Prevent clashes in random numbers
        if rand_five_one == rand_five_two:
            while rand_five_one == rand_five_two:
                rand_five_two = randint(0, self.five_limit)

        five_one = self.get_phrase("five", rand_five_one)
        seven = self.get_phrase("seven", rand_seven)
        five_two = self.get_phrase("five", rand_five_two)

        # Return formatted haiku
        return five_one + seven + five_two
