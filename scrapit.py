import os
from hashlib import sha1

import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:30.0) " + 
                  "Gecko/20100101 Firefox/30.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}

CACHE_DIR = os.path.join(os.path.dirname(__file__), 'cache')


def url_to_filename(url):
    """ Make a URL into a filename, using SHA1 hashes. """

    hash_file = sha1(url.encode('utf-8')).hexdigest() + '.html'
    return os.path.join(CACHE_DIR, hash_file)


def store_local(url, content):
    """ Save a local copy of the file. """

    # If the cache directory does not exist, make one.
    if not os.path.isdir(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    # Save to disk.
    local_path = url_to_filename(url)
    with open(local_path, 'wb') as f:
        f.write(content)


def load_local(url):
    """ Read a local copy of a URL. """

    local_path = url_to_filename(url)
    if not os.path.exists(local_path):
        return None

    with open(local_path, 'rb') as f:
        return f.read()


def get_content(url):
    """ Wrap requests.get() """

    content = load_local(url)
    if content is None:
        response = requests.get(url, headers=HEADERS)
        content = response.content
        store_local(url, content)
    return content
