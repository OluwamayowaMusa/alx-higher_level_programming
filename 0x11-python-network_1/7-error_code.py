#!/usr/bin/python3
""" Handling Exceptions using requests package

"""
import sys
import requests
from requests.exceptions import HTTPError


def error(url=None):
    """ Handling HTTPError

    Args:
        url (str): URL passed
    """

    if url:
        try:
            response = requests.get(url)
            response.raise_get_status()
            print(response.text)
        except HTTPError as e:
            print("Error code: {}".format(e.response.status_code))


if __name__ == "__main__":
    error(url=sys.argv[1])
