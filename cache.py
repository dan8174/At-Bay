from cacheout import Cache
from consts import *


class CacheManager:

    cache = Cache()
    cache_ttl = CACHE_TTL

    def set_val(self, key: str, val: dict):
        self.cache.set(key, val, ttl=self.cache_ttl)

    def get_val(self, key: str) -> dict:
        if key in self.cache:
            return self.cache.get(key)

        return POSSIBLE_STATUSES[NOT_FOUND]

