from requests import session,get
from user_agent import generate_user_agent as g


class deep_link:
    """
    just add your url and the class check the url :>
    """
    def __init__(self,url:str) -> None:
        if 'xnxx' in url:
            self.xnxx(url)
        elif 'pornhub' in url:
            self.pornhub(url)

    def pornhub(self,url):
        try:
            s = session().get(url=url,headers={'User-Agent':g()}).text
            url = s.split('"quality":"720"')[1].split('{"defaultQuality":720,"format":"hls","videoUrl":"')[1].split('"')[0].replace('\\','')
            return {'ok':'true','url':url,'dev':'instagram : @m3ghos'}

        except:
            return {'ok':'false','msg':'maybe url is wrong','dev':'instagram : @m3ghos'}

    def xnxx(self,url):
        try:
            s = session().get(url=url,headers={'User-Agent':g()}).text
            url = s.split('html5player.setVideoUrlHigh(\'')[1].split('\');')[0]
            return url
        except:
            return {'ok':'false','msg':'maybe url is wrong','dev':'instagram : @m3ghos'}
    
    def pin_porn(self,page:str,ipp:str):
        """
        with this function use radint
        to make random number
        and use it for ipp and page :>
        """
        api = f'https://pin.porn/api/videoInfo/?ipp={ipp}&from_page={page}'
        s = get(api).json()
        return s

