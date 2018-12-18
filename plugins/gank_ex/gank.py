#coding:utf-8
from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class Gank(BotPlugin):
    """
    https://gank.io/api/today
    """
    @botcmd
    def gank_help(self,msg,args):
        return """
        ```
        # 获取最新一天的干货 
        !gank today
        # 获取福利
        ！gank --type=福利 --count=10 --page=1

        ```
        """
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
                content += "```"+des+"\n"+"refer: "+res_url+"```"
        
        return content

    @arg_botcmd('--type',dest="set type for what your want",type=str)
    @arg_botcmd('--count', dest='the number of result', type=int, default=5)
    @arg_botcmd('--page',dest="the page of result",type=int,default=1)
    def gank(self,msg,args):
        url="http://gank.io/api/data/{type}/{count}/{page}".format(type=type,count=count,page=page)
        r = requests.get(url,verify=False)
        res = r.json()
        results = res['results']
        
        if type == "福利"：
            for result in results:
                id=result['id']
                img_url = result['url']
                r = requests.get(img_url,verify=False)
                path = 'img/'+id+'.jpg'
                with open(path,'wb')as f:
                    f.write(r.content)
                stream = self.send_stream_request(msg.frm,open(path,'rb'),name=id+'.jpg',stream_type='application/x-jpg')
        elif type == "":
            pass
        
        else:
            return "No command found!"
            

            
            
