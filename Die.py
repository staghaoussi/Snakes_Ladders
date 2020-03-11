import random


class Die:
    def __init__(self):
        self.__faceUp = 1

    def throw(self):
        if random.randint(1, 6) == 1:
            self.__faceUp = 1
        elif random.randint(1, 6) == 2:
            self.__faceUp = 2
        elif random.randint(1, 6) == 3:
            self.__faceUp = 3
        elif random.randint(1, 6) == 4:
            self.__faceUp = 4
        elif random.randint(1, 6) == 5:
            self.__faceUp = 5
        else:
            self.__faceUp = 6

    def get_faceUp(self):
        return self.__faceUp


if __name__ == "__main__":
    main()
