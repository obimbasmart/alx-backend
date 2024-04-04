#!/usr/bin/env python3
"""
LRU Cache - Least Recently Used Caching Strategy
"""

from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU dictionary cache"""

    def __init__(self):
        super().__init__()
        self.__lru_keys = []

    def get(self, key):
        """ Get an item by key
        """
        item = self.cache_data.get(key)
        if item:
            del self.__lru_keys[self.__lru_keys.index(key)]
            self.__lru_keys.append(key)
        return item

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:
            return

        self.cache_data[key] = item
        if key not in self.__lru_keys:
            self.__lru_keys.append(key)

        if len(self.__lru_keys) > self.MAX_ITEMS:
            dkey = self.__lru_keys.pop(0)
            del self.cache_data[dkey]
            print("DISCARD:", dkey)
