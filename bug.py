import urllib.request
def download(url):
    return  urllib.request.urlopen(url).read()