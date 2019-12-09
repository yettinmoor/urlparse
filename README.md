# urlparse

A simple Python utility that translates input into a URL a browser can use. Reads `bookmarks` and `searchengines` in `.config/urlparse`. If input does not match a bookmark/search engine and is not a URL, urlparse will by default return a search URL for the first search engine.

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
