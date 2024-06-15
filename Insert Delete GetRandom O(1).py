# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

import random


class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.num_map = {}

    def insert(self, val: int) -> bool:
        if val not in self.num_map:
            self.num_map[val] = len(self.lst)
            self.lst.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.num_map:
            self.num_map.pop(val, None)
            self.lst.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        i = random.randrange(len(self.lst))
        return self.lst[i]


# Optimized remove
# by replacing the target with the last element and popping the last
# element to prevent duplications and updating its index in the num_map
def remove(self, val: int) -> bool:
    if val in self.num_map:
        place = self.num_map[val]
        self.lst[place] = self.lst[-1]
        self.num_map[self.lst[-1]] = place
        self.lst.pop()
        return True
    return False
