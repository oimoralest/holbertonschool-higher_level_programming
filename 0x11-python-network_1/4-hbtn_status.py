#!/usr/bin/python3
"""This script fetches https://intranet.hbtn.io/status using requests module"""
import requests


if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n "
          "\t-type: {}\n "
          "\t-content: {}".format(type(response.text), response.text))
