#coding:utf-8 
from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import requests,json

class Tuling(BotPlugin):
    """
    tuling bot
    """

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports

        You should delete it if your plugin doesn't use any configuration like this
        """
        return {'apikey': "Changeme"}

    @botcmd
    def tuling(self,msg,args):
        if len(args) == 0:
            text = ""
        else:
            text = args
        url = "http://openapi.tuling123.com/openapi/api/v2"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }
        payload = {
            "reqType":0,
            "perception": {
                "inputText": {
                    "text": text
                }
            },
            "userInfo": {
                "apiKey": self.config['apikey'],
                "userId": "1"
            }
        }
        response = requests.request("POST", url, data=json.dumps(payload,ensure_ascii=False).encode('utf-8'), headers=headers)
        try:
            return response.json().get('results')[0].get('values').get('text')
        except Exception as e:
            return response.text