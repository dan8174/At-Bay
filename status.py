from cache_handler import CacheHandler


def get_status(scan_id: str) -> str:
    return CacheHandler.cache.get_val(scan_id)['status']
