from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import requests

class Hitbot(BotPlugin):
    """
    hitbot
    """

    @botcmd
    def hitbot(self,msg,args):
        url = "https://v1.hitokoto.cn/?encode=text"
        r = requests.get(url,verify=False)
        return r.text