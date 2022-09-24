#!/usr/bin/python3
""" Getting the most recent commits in a respository using GITHUB api

"""
import sys
import requests


def github_commit(url=None, user=None, passwd=None):
    """ Using the Github api

    Args:
        url (str): URL passsed
        user (str): UserName of User
        passwd (str): Password of user
    """

    if url and user and passwd:
        response = requests.get(url, auth=(user, passwd))
        data = response.headers
        print(data)
        print(response.status_code)
        print(data.get("GitHub-Authentication-Token-Expiration"))


if __name__ == "__main__":
    github_commit(url="https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2]),
                  user="OluwamayowaMusa",
                  passwd="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")
                         

