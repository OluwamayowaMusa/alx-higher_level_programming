#!/usr/bin/python3
""" Getting the headers in response using the requests package

"""
import sys
import requests


def header(url=None):
    """ Get the value of X-Request-Id

    Args:
        url (str): URL passed
    """

    if url:
        response = requests.get(url)
        print(response.headers["X-Request-Id"])


if __name__ == "__main__":
    header(url=sys.argv[1])
