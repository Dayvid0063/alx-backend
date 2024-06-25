#!/usr/bin/env python3


"""MRUCache Module"""


from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRUCache class - MRU caching system"""
    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        else:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru = next(reversed(self.cache_data))
            del self.cache_data[mru]
            print(f"DISCARD: {mru}")

    def get(self, key):
        """Gets item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
