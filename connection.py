import urllib
import urllib2

class Connection():
    
    def connect(self):
        url = 'http://www.mitfahrgelegenheit.de/mitfahrzentrale/Dresden/Potsdam.html/'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        header = { 'User-Agent' : user_agent }
        
        values = {
          'city_from' : 69,
          'radius_from' : 0,
          'city_to' : 263,
          'radius_to' : 0,
          'date' : 'date',
          'day' : 3,
          'month' : 03,
          'year' : 2012,
          'tolerance' : 0
        }

        data = urllib.urlencode(values)
        # req = urllib2.Request(url+data, None, header)
        req = urllib2.Request(url, data, header)  # clean POST request doesn't not work

        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            return None
        except urllib2.URLError, e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            return None
        else:
            self.response = response
            return req
            
    def response_to_str(self):
        return self.response.read()
    
    def dump_response_to_file(self):
        f = open('dump.html','w')
        f.write(self.response_to_str())

c = Connection()
req = c.connect()
print(req.data)
print(req.get_method())
c.dump_response_to_file()
print(c.response.geturl())
# response.read returns a string
# response.geturl gives real address e.g. after redirect 
# response.info gives a dict with details to the answer