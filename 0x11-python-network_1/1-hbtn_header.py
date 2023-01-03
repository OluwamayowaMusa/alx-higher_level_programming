#!/usr/bin/python3
""" Using the getheader property of response

"""
import sys
from urllib.request import urlopen


def header(url=None):
    """ Get the value of X-Request-ID

    Args:
        url (str): URL passed
    """

    if url:
        with urlopen(url) as response:
            print(response.getheader('X-Request-Id'))


if __name__ == "__main__":
    header(url=sys.argv[1])
