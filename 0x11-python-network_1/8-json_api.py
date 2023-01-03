#!/usr/bin/python3
""" Using JSON format in requests package

"""
import sys
import requests


def json_api(url=None, data=None):
    """ Using the JSON format

    """

    if url:
        response = requests.post(url, data={'q': data})
        try:
            user_dict = response.json()
            if user_dict:
                print(f"[{user_dict['id']}] {user_dict['name']}")
            else:
                print("No result")
        except Exception as e:
            print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        json_api(url="http://0.0.0.0:5000/search_user", data="")
    else:
        json_api(url="http://0.0.0.0:5000/search_user", data=sys.argv[1])
