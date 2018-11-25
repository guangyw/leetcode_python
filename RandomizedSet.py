# Design a data structure that supports all following operations in average O(1) time.
# 
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = []
        self._index = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self._index.keys():
            return False
        self._index[val] = len(self._data)
        self._data.append(val)
        return True
            
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self._index:
            return False
        
        idx = self._index[val]
        replaceVal = self._data[-1]
        self._data[idx] = replaceVal
        self._index[replaceVal] = idx
        self._data.pop()     
        self._index.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self._data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()