#!/usr/bin/env python
import os, re, sys


def parse(search_terms):

    if not search_terms or search_terms == '-h':
        sys.stderr.write('Usage: urlparse [-h] search_terms.\n')
        exit(1)

    config_dir = os.path.join(os.getenv('HOME'), '.local', 'share', 'urlparse')

    # Check search engines
    try:
        engine, *search = search_terms.split(' ')
        with open(os.path.join(config_dir, 'searchengines'), 'r') as f:
            for engine_key, engine_url in [l.rstrip().split(' ') for l in f.readlines()]:
                if engine == engine_key:
                    return engine_url % ' '.join(search)

    except FileNotFoundError:
        sys.stderr.write('searchengines file not found.\n')
        exit(1)

    # Check bookmarks
    try:
        with open(os.path.join(config_dir, 'bookmarks'), 'r') as f:
            for bookmark_key, bookmark_url in [l.rstrip().split(' ') for l in f.readlines()]:
                if search_terms == bookmark_key:
                    return bookmark_url

    except FileNotFoundError:
        sys.stderr.write('bookmarks file not found.\n')
        exit(1)

    # Check if url
    url_regex = "^(http://|https://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+.*$"
    if re.search(url_regex, search_terms):
        return search_terms

    # Finally return default search
    with open(os.path.join(config_dir, 'searchengines'), 'r') as f:
        try:
            default_engine = f.readline().rstrip().split(' ')[1]
            return default_engine % search_terms
        # No search engine
        except IndexError:
            sys.stderr.write('Search engine list empty. Input your default search engine into {}.\n'.format(f.name))
            exit(1)


if __name__ == '__main__':
    result = parse(' '.join(sys.argv[1:]))
    print(result)
