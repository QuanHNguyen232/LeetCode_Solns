class RandomizedSet:

    def __init__(self):
        self.arr = set([])

    def insert(self, val: int) -> bool:
        if val in self.arr: return False
        self.arr.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.arr: return False
        self.arr.remove(val)
        return True

    def getRandom(self) -> int:
        # random.sample(self.arr, 1) return list of 1 element
        return random.sample(self.arr, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()