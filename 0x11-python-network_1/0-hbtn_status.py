#!/usr/bin/python3
"""Fetch web response
"""
import urllib.request


def main():
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status'
                                ) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == '__main__':
    main()
