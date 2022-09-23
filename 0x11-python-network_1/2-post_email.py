#!/usr/bin/python3
""" Using the POST Method to upload data to the server

"""
import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode


def post(url=None, data=None):
    """ Post data with email=<value> to server

    Arsg:
        url (str): URL passed
        data (str): Data to upload
    """

    if url and data:
        user_dict = {'email': data}
        url_encoded_data = urlencode(user_dict)
        post_data = url_encoded_data.encode("utf-8")
        request = Request(url, data=post_data)
        with urlopen(request) as response:
            print(response.read().decode("utf-8"))


if __name__ == "__main__":
    post(sys.argv[1], sys.argv[2])
