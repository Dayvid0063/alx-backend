#!/usr/bin/env python3


"""LFUCache Module"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class implements a LFU caching system"""
    def __init__(self):
        """Initialization"""
        super().__init__()
        self.frequency = []
        self.usage = []

    def put(self, key, item):
        """
        Cache a key-value pair.
        Evicts LFU items if cache exceeds maximum capacity.
        """
        size = len(self.cache_data)
        if key is None or item is None:
            return

        if size >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            lfu = min(self.frequency.values())
            lfk = [u for u, v in self.frequency.items() if v == lfu]

            if len(lfk) > 1:
                l_rf = {u: self.usage[u] for u in lfk}
                rmv = min(l_rf, key=l_rf.get)
            else:
                rmv = lfk[0]

            print(f"DISCARD: {rmv}")
            del self.cache_data[rmv]
            del self.frequency[rmv]
            del self.usage[rmv]

        if key in self.cache_data:
            del self.usage[key]
        self.usage[key] = None
        self.frequency[key] += 1
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets value linked to given key, or None if key not found.
        Update usage and frequency for accessed key.
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
