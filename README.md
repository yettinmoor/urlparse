# urlparse

A simple Python utility that translates input into a URL a browser can use. Reads `bookmarks` and `searchengines` in `.local/share/urlparse`. If input does not match a bookmark/search engine and is not a URL, urlparse will by default return a search URL for the first search engine.

### Note

Since creating this program, I have written a much more concise shell script that achieves the same purpose. It uses the same search engine & bookmark format and file location. I have written in at the bottom of this readme.

## Example commands
```shell
$ urlparse nf
netflix.com

$ urlparse osm stockholm
https://www.openstreetmap.org/search?query=stockholm

$ urlparse python
https://duckduckgo.com/?q=python
```

## Example formats

### `bookmarks`

```
git github.com
yt youtube.com
nf netflix.com
```

### `searchengines`

```
d https://duckduckgo.com/?q=%s
yt https://www.youtube.com/results?search_query=%s
osm https://www.openstreetmap.org/search?query=%s
```

## Equivalent shell script
```shell
#!/usr/bin/env sh

[ -z "$1" ] && exit 1

# Check url
echo "$1" | grep -E '^(http://|https://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+.*$' && exit

# Check searchengines
se=$( grep "^$1 " ~/.local/share/urlparse/searchengines | cut -d' ' -f2 )
if [ ! -z "$se" ]; then shift; printf "$se" "$*"; exit; fi

# Check bookmarks
bm=$( grep "^$1 " ~/.local/share/urlparse/bookmarks | cut -d' ' -f2 )
if [ ! -z "$bm" ]; then echo "$bm"; exit; fi

# Default to first search engine
printf "$( head -n 1 ~/.local/share/urlparse/searchengines | cut -d' ' -f2 )" "$*"
```
