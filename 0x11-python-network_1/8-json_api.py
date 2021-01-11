#!/usr/bin/python3
"""This script takes a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv


if __name__ == '__main__':
    q = ""
    if len(argv) > 1:
        q = argv[1]
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        if len(response.json()) > 0:
            if type(response.json()) is dict:
                print('[{}] {}'.format(
                    response.json().get('id'), response.json().get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
