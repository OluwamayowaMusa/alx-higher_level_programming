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
        data = response.json()
        result = []
        for user in data:
            result.append((user["sha"], user["commit"]["author"]["name"], user["commit"]["author"]["date"]))
        data = sorted(result, key=lambda item: item[2], reverse=True)
        for user in data[:10]:
            print(f"{user[0]}: {user[1]}")


if __name__ == "__main__":
    github_commit(url="https://api.github.com/repos/"
                  "{}/{}/commits".format(sys.argv[2], sys.argv[1]),
                  user="OluwamayowaMusa",
                  passwd="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")
