from cache_handler import CacheHandler
from consts import *
import uuid
import concurrent.futures
import process
import status


def scan(url: str):
    unique_scan_id = uuid.uuid4().hex
    url_status = POSSIBLE_STATUSES[ACCEPTED]
    data = {"url": url, "status": url_status}
    CacheHandler.cache.set_val(unique_scan_id, data)
    print(f'{url} was scanned')


urls = ['http://example1.com',
        'http://example2.com',
        'http://example3.com']

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(scan, urls)

print(f'Finish scanned all urls')

process.process()
for scan_id in CacheHandler.cache:
    print(f'status of {scan_id} is {status.get_status(scan_id)}')
    print(f'url of {scan_id} is {CacheHandler.cache.get_val(scan_id)["url"]}')


