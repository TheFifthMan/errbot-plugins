# coding: utf-8 
from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import requests

class Gank(BotPlugin):
    """
    gank
    """

    @botcmd
    def gank_help(self,msg,args):
        content = "```\n# get today news \n!gank today\n# get 福利 \n !gank --type=fuli --count=10 --page=1\n```"
        return content
    @botcmd
    def gank_today(self,msg,args):
        content = ""
        url = "http://gank.io/api/today"
        r = requests.get(url,verify=False)
        res = r.json()
        categories = res['category']
        results = res['results']
        for category in categories:
            for result in results[category]:
                des = result['desc']
                res_url = result['url']
                content += "```"+des+"\n"+"refer: "+res_url+"```\n"
        
        return content
    
    @arg_botcmd('--type',dest="set type for what your want",type=str)
    @arg_botcmd('--count', dest='the number of result', type=int, default=5)
    def gank(self,msg,args):
        return type