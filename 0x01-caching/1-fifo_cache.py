#!/usr/bin/env python3
"""
FIFO Cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO dictionary cache"""

    def __init__(self):
        super().__init__()
        self.fifo_keys = []  # key track of key set/del order

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
        self.fifo_keys.append(key) if key not in self.fifo_keys else None

        if len(self.fifo_keys) > self.MAX_ITEMS:
            dkey = self.fifo_keys.pop(0)
            del self.cache_data[dkey]
            print("DISCARD:", dkey)
