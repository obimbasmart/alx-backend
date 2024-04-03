#!/usr/bin/env python3
"""
Basic Cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary cache"""

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
