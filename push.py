#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# Copyright (C) 2023 , Inc. All Rights Reserved
# @Time    : 2023/4/18 0:51
# @Author  : raindrop
# @Email   : 1580925557@qq.com
# @File    : push.py


import requests, json,os

def config():
    path = os.getcwd()
    if path == '/opt/function':
        path = 'code/'
    else:
        path = ''
    with open(path + 'config.json', encoding='utf-8') as f:
        account = f.read()
    a = account.count('/*')
    print(a)
    for i in range(a):
        x = account.find('/*')
        y = account.find('*/') + 2
        account = account[:x] + account[y:]
    account = json.loads(account)
    return account


def WeCom(content):
    wx = config()["push"]["WeCom"]
    print(content)
    if not eval(wx["push"]):
        print('企业微信不推送')
    else:
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + wx['corpid'] + '&corpsecret=' + wx['secret']
        access_token = requests.get(url)
        access_token = json.loads(access_token.text)
        access_token = access_token.get("access_token")
        token = 'c8avSOlP-d5wLBuws4LmmsIjgmnCrUfPA16ftSCAJM4'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
        data = json.dumps({
            "touser": "@all",
            "msgtype": "text",
            "agentid": wx['agentid'],
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


def Ding(content):
    ding = config()["push"]["Ding"]
    print(content)
    if not eval(ding["push"]):
        print('钉钉不推送')
    else:
        appkey = config()['push']['Ding']['appkey']
        appsecret = config()['push']['Ding']['appsecret']
        access_token = requests.get('https://oapi.dingtalk.com/gettoken?appkey=' + appkey + '&appsecret=' + appsecret)
        access_token = access_token.text
        access_token = json.loads(access_token)
        access_token = access_token["access_token"]
        url = 'https://oapi.dingtalk.com/robot/send?access_token=78c8b773c0796732273b1a65a6360fa20982dafccf13a7950ec88a0b54d18201'
        headers = {
            'x-acs-dingtalk-access-token': access_token,
            'Content-Type': 'application/json'
        }
        data = {
            'text': {'content': content},
            'msgtype': 'text',
            'msgKey': 'sampleText'
        }
        res = requests.post(url=url, headers=headers, json=data)
        return (json.loads(res.text).get('errmsg'))

def main(content):
    Ding(content)
    WeCom(content)


