import urllib
import urllib2

url = 'http://www.mitfahrgelegenheit.de/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request(url, None, headers)

try:
    response = urllib2.urlopen(req)
    html = response.read()
    print html
except urllib2.HTTPError, e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except urllib2.URLError, e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason