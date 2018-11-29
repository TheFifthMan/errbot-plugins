from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import os,requests
from datetime import datetime 

class Bing(BotPlugin):
    """
    bing
    """
    @botcmd
    def bing(self,msg,args):
        url = 'https://api.isoyu.com/'
        if not os.path.exists('img'):
            os.mkdir('img')
        if args == 'mm':
            r = requests.get(url+'mm_images.php',allow_redirects=True,verify=False)
        elif args == 'aru':
            r = requests.get(url+'ARU_GIF_S.php',allow_redirects=True,verify=False)
        elif args == "bao":
            r = requests.get(url+'bao_images.php',allow_redirects=True,verify=False)
        else:
            r = requests.get(url+'bing_images.php',allow_redirects=True,verify=False)
        
        path = 'img/'+str(int(datetime.timestamp(datetime.now())))+'.jpg'
        with open(path,'wb') as f:
            f.write(r.content)
        stream = self.send_stream_request(msg.frm,open(path,'rb'),name=str(int(datetime.timestamp(datetime.now())))+'.jpg',stream_type='application/x-jpg')
            
