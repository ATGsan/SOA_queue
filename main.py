from graber import get_links, parser

if __name__ == "__main__":
    source, destination = get_links()
    links = parser(source)
