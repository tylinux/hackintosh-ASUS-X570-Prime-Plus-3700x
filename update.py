#!/usr/bin/env python3
import requests
import json


def request_github_release(author: str, repo: str, current_version: str) -> str:
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    url = f'https://api.github.com/repos/{author}/{repo}/releases'
    print(url)
    result = requests.get(url, headers).json()


if __name__ == "__main__":
    request_github_release('acidanthera', 'OpenCorePkg', '0.5.9')
