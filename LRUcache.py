# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

class LRUCache:
    def __init__(self,size):
        self.size = size
        self.cache = OrderedDict()
        
    def get(self,key):
        value = self.cache.pop(key, -1)
        if value != -1:
            self.cache[key] = value;
        return value
    
    def put(self,key,value):
        if self.get(key) == -1:
            if len(self.cache) >= self.size:
                self.cache.popitem(last = False)
            self.cache[key] = value


cache = LRUCache(2) # capacity of 2

cache.put(1, "foo")
cache.put(2, "bar")
print(cache.get(1))        # returns "foo"
cache.put(3, "baz") # evicts key 2
print(cache.get(2))        # returns -1 (not found)
cache.put(4, "a")   # evicts key 1
print(cache.get(1))        # returns -1 (not found)
print(cache.get(3))        # returns "baz"
print(cache.get(4))        # returns "a"
