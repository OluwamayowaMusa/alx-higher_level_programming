#!/usr/bin/python3
""" Getting the most recent commits in a respository using GITHUB api

"""
import sys
import requests


def github_commit(url=None):
    """ Using the Github api

    Args:
        url (str): URL passsed
    """

    if url:
        response = requests.get(url)
        data = response.json()
        result = []
        for user in data:
            result.append((user["sha"], user["commit"]["author"]["name"], user["commit"]["author"]["date"]))
        data = sorted(result, key=lambda item: item[2], reverse=True)
        for user in data[:10]:
            print(f"{user[0]}: {user[1]}")


if __name__ == "__main__":
    github_commit(url="https://api.github.com/repos/"
                  "{}/{}/commits".format(sys.argv[2], sys.argv[1]))
