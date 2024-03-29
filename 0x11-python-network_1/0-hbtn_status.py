#!/usr/bin/python3
"""" Using urllib standard libary
     for making requests
"""
from urllib.request import urlopen


def status(url=None):
    """ Open URL and read the content

    Args:
        url (str): URL passed
    """
    if url:
        with urlopen(url) as response:
            print("Body response:")
            body = response.read()
            print(f"\t- type: {type(body)}")
            print(f"\t- content: {body}")
            print(f"\t- utf8 content: {body.decode()}")


if __name__ == "__main__":
    status(url="https://alx-intranet.hbtn.io/status")
