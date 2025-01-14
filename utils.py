import requests,json

def sendMsgToWechat(token:str,title:str,text:str,template:str) -> None :
    '''
    token:PushPlus token
    title:text's title
    text:text's body
    template:html,txt,json,markdown
    Send message to Wechat(SMS,E-mail,Dingtalk...) via PushPlus.
    default channel is wechat
    '''
    url = "http://www.pushplus.plus/send"
    data={
        'token':token,
        'title':title,
        'content':text,
        'template':template

    }
    response=requests.post(url=url,
                           data = (
                                    json.dumps(data).encode(encoding='utf-8')
                                    ),
                           )

def sendMsgToNtfy(title,text,priority,topic):
    url="https://push.ecust.icu/"
    requests.post(url,
        data=json.dumps({
            "topic": f"{topic}",
            "message": f"{text}",
            "title": f"{title}",
            "tags": ["loudspeaker","earth_asia"],
            "priority": 4
        }).encode(encoding='utf-8')
    )
