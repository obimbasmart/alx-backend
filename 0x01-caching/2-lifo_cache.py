#!/usr/bin/env python3
"""
LIFO Cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """FIFO dictionary cache"""

    def __init__(self):
        super().__init__()
        self.lifo_keys = []  # key track of key set/del order

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:
            return

        self.cache_data[key] = item
        if key in self.lifo_keys:
            del self.lifo_keys[self.lifo_keys.index(key)]

        self.lifo_keys.insert(0, key)
        if len(self.lifo_keys) > self.MAX_ITEMS:
            dkey = self.lifo_keys.pop(1)
            del self.cache_data[dkey]
            print("DISCARD:", dkey)
