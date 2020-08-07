# web client fetches web page, given a url
## when asked, it checks it cache for the web page 

#first request: fetches from interwebs
#2nd request: returns from cache

#why?
## faster
## decreases load on web server
## security
## cuts down calls to APIS

# hash table usage to make a web client cache???
## URL could be the key
## web page data could be the value

#problems with our naive implementation?
## 'every successful complex systerm will be found to have evolved from a simple system'
## what if the actual page changes?  our data will be old - stale
## no size limitation - end up storing the whole internet

#how to solve these problems?
#How to solve stale data in cache?
## timeout: after a week, go and fetch again, even if it's already in cache

#size limitation: problem of storing too much
## monetize??
## LRU cache - set a max number of items
## timestamp every item

import urllib.request

url = 'https://www.google.com'

cache = {}

page = None

#check if we have previously gotten this url, if not go fetch it
if url in cache:
    page = cache[url]

#if not go fetch it:
else:
    print('getting from server')
    
    #fetch the data
    resp = urllib.request.urlopen(url)
    data = resp.read()
    #put in the cache
    cache[url] = data

    page = cache[url]

print(page)
