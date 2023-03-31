#!/usr/bin/python3
"""Script that takes 2 arguments in order to solve this challenge."""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    repo_name = args[1]
    owner = args[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    r = requests.get(url)
    commits = r.json()[:10]
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
