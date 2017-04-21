from string import ascii_letters,digits
from random import sample , randint
class Codec:
    
    def __init__(self):
        self.url_dict = dict()


    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        char_list = string.ascii_letters + string.digits
        TINY_URL = 'http://tinyurl.com/'
        while True:
            url_key = random.sample(char_list,(random.randint(0,10)))
            if self.url_dict.get(''.join(url_key),None) == None:
                self.url_dict[''.join(url_key)] = longUrl
                break
        return (TINY_URL + ''.join(url_key))
        
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        longUrl = self.url_dict.get(shortUrl[19:],None)
        if longUrl != None:
            return longUrl
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))