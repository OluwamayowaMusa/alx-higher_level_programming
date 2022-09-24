#!/usr/bin/python3
""" Interacting with Github API

"""
import sys
import requests


def github_api(url=None, user=None, passwd=None):
    """ Interacting with Github api using Basic Authentication

    Args:
        url (str): URL passed
        user (str): UserName
        passwd (str): Password of user
    """

    if url and user and passwd:
        response = requests.get(url, auth=(user, passwd))
        print(response.json().get("id"))


if __name__ == "__main__":
    github_api(url="https://api.github.com/user", user=sys.argv[1],
               passwd=sys.argv[2])
