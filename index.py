import requests
import json
import time
'''
可直接部署在华为云函数流
函数执行入口填：index.main_handler
触发器用cron表达式：0 30 23 * * ?
每天23:30执行
设置项
'''
'''腾讯视频签到'''
push = '1' # 是否微信机器人推送，1为是，0为否，选择0则后面三项失效
corpid = 'ww0fc7f0b4e'  # 企业ID
secret = 'j-F4DeIhMtbbB321PWHtCrRitwqxwU'  # 应用的凭证密钥
agentid = 1000006 #应用id

'''cookie项'''
vdevice_qimei36='066ab9df659c7906c26c0a32100012316509'
vqq_appid='101795054'
vqq_openid='3E68D4BDBAEE6BF42D90C2B9087CB42E'
vqq_access_token='2B36FC406803D3FBA77CE255E3959216'
main_login='qq'



def ten_video():
    cookie='vdevice_qimei36='+vdevice_qimei36+';vqq_appid='+vqq_appid+';vqq_openid='+vqq_openid+';vqq_access_token='+vqq_access_token+';main_login='+main_login
    url_1='https://vip.video.qq.com/rpc/trpc.new_task_system.task_system.TaskSystem/CheckIn?rpc_data=%7B%7D'
    headers_1={'user-agent':'Mozilla/5.0 (Linux; Android 11; M2104K10AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046237 Mobile Safari/537.36 QQLiveBrowser/8.7.85.27058',
             'Content-Type':'application/json',
             'referer':'https://film.video.qq.com/x/vip-center/?entry=common&hidetitlebar=1&aid=V0%24%241%3A0%242%3A8%243%3A8.7.85.27058%244%3A3%245%3A%246%3A%247%3A%248%3A4%249%3A%2410%3A&isDarkMode=0',
             'cookie':cookie
             }
    response_1 = requests.get(url_1,headers=headers_1)
    res_1 = json.loads(response_1.text)
    url_2='https://vip.video.qq.com/rpc/trpc.new_task_system.task_system.TaskSystem/ProvideAward?rpc_data=%7B%22task_id%22:1%7D'
    headers_2={'user-agent':'Mozilla/5.0 (Linux; Android 11; M2104K10AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046237 Mobile Safari/537.36 QQLiveBrowser/8.7.85.27058',
             'Content-Type':'application/json',
             'referer':'https://film.video.qq.com/x/vip-center/?entry=common&hidetitlebar=1&aid=V0%24%241%3A0%242%3A8%243%3A8.7.85.27058%244%3A3%245%3A%246%3A%247%3A%248%3A4%249%3A%2410%3A&isDarkMode=0',
             'cookie':cookie
             }
    response_2 = requests.get(url_2,headers=headers_2)
    res_2 = json.loads(response_2.text)
    time_1 = int(time.time())
    time_2 = time.localtime(time_1)
    now = time.strftime("%Y-%m-%d %H:%M:%S", time_2)
    log = "腾讯视频会员签到执行任务\n----------raindrop----------\n" + now
    try:
        log = log + "\n签到获得积分:" + str(res_1['check_in_score'])
    except:
        log=log+"\n腾讯视频签到异常，返回内容："+str(res_1)
        print(res_1)
    try:
        log = log + "\n观看获得积分:" + str(res_2['check_in_score'])
    except:
        log=log+"\n腾讯视频领取观看积分异常,返回内容："+str(res_2)
        print(res_2)
    url='https://vip.video.qq.com/rpc/trpc.new_task_system.task_system.TaskSystem/ReadTaskList?rpc_data=%7B%22business_id%22:%221%22,%22platform%22:3%7D'
    headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; M2104K10AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046237 Mobile Safari/537.36 QQLiveBrowser/8.7.85.27058',
             'Content-Type':'application/json',
             'referer':'https://film.video.qq.com/x/vip-center/?entry=common&hidetitlebar=1&aid=V0%24%241%3A0%242%3A8%243%3A8.7.85.27058%244%3A3%245%3A%246%3A%247%3A%248%3A4%249%3A%2410%3A&isDarkMode=0',
             'cookie':cookie
             }
    response = requests.get(url,headers=headers)
    res = json.loads(response.text)
    try:
        lis=res["task_list"]
        log = log + '\n--------任务状态----------'
        for i in lis:
            log=log+'\ntask_title:'+i["task_maintitle"]+'\nsubtitle:'+i["task_subtitle"]+'\ntask_button_desc:'+i["task_button_desc"]
    except:
        log = log + "获取状态异常，可能是cookie失效"
        print(res)
    print(push_a(log))



def push_a(content):
    print(content)
    if push == '0':
        print('不推送')
    else:
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + secret
        access_token = requests.get(url)
        access_token = json.loads(access_token.text)
        print(access_token, type(access_token))
        access_token = access_token.get("access_token")
        token = 'c8avSOlP-d5wLBuws4LmmsIjgmnCrUfPA16ftSCAJM4'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
        data = json.dumps({
            "touser": "@all",
            "msgtype": "text",
            "agentid": agentid,
            "text": {
                "content": content
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        })
        resp = requests.post(url, data=data, headers={'Content-Type': 'application/json'})
        return (json.loads(resp.text).get('errmsg'))


def main():
    ten_video()


def main_handler(event, context):
    return main()


if __name__ == '__main__':
    main()
