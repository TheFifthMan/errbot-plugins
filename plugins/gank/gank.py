# coding: utf-8 
from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class Gank(BotPlugin):
    """
    gank
    """

    @botcmd
    def gank_help(self,msg,args):
        content = "```\n# get today news \n!gank today\n# get 福利 \n !gank --type=fuli --count=10 --page=1\n```".encode('utf-8').decode('utf-8')
        return content