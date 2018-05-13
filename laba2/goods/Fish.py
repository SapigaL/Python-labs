from goods.Good import *
from enums.FishType import *


class Fish(Good):

    def __init__(self, fish_name, weight, price, fishType):
        super().__init__(fish_name, weight, price,fishType)

    def __str__(self):
        return ", Name:" + str(self.fish_name) + " Fish type: " + str(self.fishType) + ", Price:" + str(
            self.price) + ", Weight:" + str(self.weight)