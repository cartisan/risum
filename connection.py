import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

class Connection():
    url = 'http://www.mitfahrgelegenheit.de/'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    header = { 'User-Agent' : user_agent }
    
    def open_request(self, req):
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
            return response   
             
    def get_city_dict(self):
        req = urllib2.Request(self.url, None, self.header)
        soup = BeautifulSoup(self.open_request(req))
        
        # get a list of all cities from which rides are possible 
        # excluding the "All Cities" statement on position 0
        city_list = soup.find(id="LiftCityFromNatinal").findAll("option")[1:]

        return dict([(city.string , int(city["value"])) for city in city_list])
    
    def connect(self):
        values = {
          'city_from' : 69,
          'radius_from' : 0,
          'city_to' : 263,
          'radius_to' : 0,
          'date' : 'date',
          'day' : 6,
          'month' : 03,
          'year' : 2012,
          'tolerance' : 0
        }

        data = urllib.urlencode(values)
        req = urllib2.Request(self.url + 'mitfahrzentrale/Dresden/Potsdam.html/' + data, None, self.header)

        self.response = self.open_request(req)
        
    def response_to_str(self):
        return self.response.read()
    
    def dump_response_to_file(self):
        f = open('dump.html','w')
        f.write(self.response_to_str())


# response.read returns a string
# response.geturl gives real address e.g. after redirect 
# response.info gives a dict with details to the answer