#!/usr/bin/python3
""" Using the module urllib.error to catch Error
    associated with sending HTTP request
"""
import sys
from urllib.request import urlopen
from urllib.error import HTTPError


def error(url=None):
    """ Handles HTTPError

    Args:
        url (str): URL passed
    """

    if url:
        try:
            with urlopen(url) as response:
                encoding = response.headers.get_content_charset()
                print(response.read().decode(encoding))
        except HTTPError as e:
            print("Error code: {}".format(e.code))


if __name__ == "__main__":
    error(url=sys.argv[1])
