from cache_handler import CacheHandler
from consts import *
import requests


def process():
    ids_for_scans = []
    for scan_id in CacheHandler.cache.cache:
        if CacheHandler.cache.get_val(scan_id)['status'] == POSSIBLE_STATUSES[ACCEPTED]:
            ids_for_scans.append(scan_id)

    for scan_id in ids_for_scans:
        url = CacheHandler.cache.get_val(scan_id)['url']
        new_data = {"url": url, "status": POSSIBLE_STATUSES[RUNNING]}
        CacheHandler.cache.set_val(scan_id, new_data)
        try:
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                new_data = {"url": url, "status": POSSIBLE_STATUSES[COMPLETE]}
                CacheHandler.cache.set_val(scan_id, new_data)
            else:
                new_data = {"url": url, "status": POSSIBLE_STATUSES[ERROR]}
                CacheHandler.cache.set_val(scan_id, new_data)
        except Exception as e:
            new_data = {"url": url, "status": POSSIBLE_STATUSES[ERROR]}
            CacheHandler.cache.set_val(scan_id, new_data)
            print(f'error: {str(e)}')
