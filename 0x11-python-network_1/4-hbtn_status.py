#!/usr/bin/python3
""" Using the requests package to send HTTP requests

"""
import requests


def status(url=None):
    """ Send GET HTTP request to web server

    """

    if url:
        response = requests.get(url)
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    status(url="https://alx-intranet.hbtn.io/status")
