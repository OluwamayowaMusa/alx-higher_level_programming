#!/usr/bin/python3
""" Using Sending POST request using the requests package

"""
import sys
import requests


def post(url=None, data=None):
    """ POST data to web server

    Args:
        url (str): URL passed
        data (str): value of email passed
    """

    if url and data:
        response = requests.post(url, data={"email": data})
        print(response.text)


if __name__ == "__main__":
    post(url=sys.argv[1], data=sys.argv[2])
