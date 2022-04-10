import json
import re
import sys

import requests


def get_links():
    pattern = re.compile(r"https://[a-z.]*/wiki/")
    inp = input()
    out = input()
    try:
        source = inp[len(pattern.search(inp).group(0)[:-1]) + 1:].replace(' ', '_')
    except:
        print("WRONG LINK IN SOURCE")
        sys.exit(1)
    try:
        destination = out[len(pattern.search(out).group(0)[:-1]) + 1:].replace(' ', '_')
    except:
        print("WRONG LINK IN DESTINATION")
        sys.exit(1)
    return source, destination


def parser(source):
    try:
        parsed = requests.get(
            f"https://en.wikipedia.org/w/api.php?action=query&prop=links&pllimit=max&format=json&titles={source}")
    except:
        if parsed.status_code != 200:
            print("ERROR IN REQUEST")
        sys.exit(1)
    parsed = json.loads(parsed.text)['query']['pages']
    parsed = dict(list(parsed.items())[0][1])['links']
    links = []
    for i in parsed:
        links.append(i['title'].replace(' ', '_'))
    return links
