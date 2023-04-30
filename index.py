#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# Copyright (C) 2023 , Inc. All Rights Reserved
# @Time    : 2023/4/18 0:51
# @Author  : raindrop
# @Email   : 1580925557@qq.com
# @File    : index.py

import requests
import json
import time
import re
import push
import os
'''
可直接部署在华为云函数流
函数执行入口填：index.main_handler
触发器用cron表达式：0 30 23 * * ?
每天23:30执行
设置项
'''
'''腾讯视频签到'''




def ten_video(tag,qimei36,appid,openid,access_token,vuserid,login,ip):
    #cookie='vdevice_qimei36='+qimei36+';vqq_appid='+appid+';vqq_openid='+openid+';vqq_access_token='+access_token+';main_login='+login
    cookie = 'vdevice_qimei36='+qimei36+';vqq_appid=' + appid + ';vqq_openid=' + openid + ';vqq_access_token=' + access_token + ';main_login=' + login + ';vqq_vuserid=' + vuserid + ';ip=' + ip
    log=''
    time_1 = int(time.time())
    time_2 = time.localtime(time_1)
    now = time.strftime("%Y-%m-%d %H:%M:%S", time_2)
    log = "腾讯视频会员签到执行任务\n--------------raindrop--------------\n" + now + '\ntag:' + tag
    #积分查询
    url_3 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_vscore_user_mashup&cmd=&otype=xjson&type=1'
    headers_3 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2104K10AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046237 Mobile Safari/537.36 QQLiveBrowser/8.7.85.27058',
        'Content-Type': 'application/json',
        'cookie': cookie
    }
    response_3 = requests.get(url_3, headers=headers_3)
    try:
        res_3 = json.loads(response_3.text)
        log = log + "\n会员等级:" + str(res_3['lscore_info']['level']) + "\n积分:" + str(
            res_3['cscore_info']['vip_score_total']) + "\nV力值:" + str(res_3['lscore_info']['score'])
    except:
        try:
            res_3 = json.loads(response_3.text)
            log = log + "\n腾讯视频领获取积分异常,返回内容:\n" + str(res_3)
            print(res_3)
        except:
            log = log + "\n腾讯视频获取积分异常,无法返回内容"
    url_3 = 'https://vip.video.qq.com/rpc/trpc.query_vipinfo.vipinfo.QueryVipInfo/GetVipUserInfoH5'
    headers_3 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2104K10AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046237 Mobile Safari/537.36 QQLiveBrowser/8.7.85.27058',
        'Content-Type': 'text/plain;charset=UTF-8',
        'cookie': cookie
    }
    data = '{"geticon":1,"viptype":"svip|nfl","platform":8}'
    response_3 = requests.post(url_3, data=data, headers=headers_3)
    try:
        res_3 = json.loads(response_3.text)
        log = log + "\n开始时间:" + str(res_3['beginTime']) + "\n到期时间:" + str(
            res_3['endTime'])
        if res_3['endmsg'] != '':
            log = log + '\nendmsg:' + res_3['endmsg']
        print(log)
    except:
        try:
            res_3 = json.loads(response_3.text)
            log = log + "\n腾讯视频领获取积分异常,返回内容:\n" + str(res_3)
            print(res_3)
        except:
            log = log + "\n腾讯视频获取积分异常,无法返回内容"
    # 签到
    url_1 = 'https://vip.video.qq.com/rpc/trpc.new_task_system.task_system.TaskSystem/CheckIn?rpc_data=%7B%7D'
    headers_1 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2104K10AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046237 Mobile Safari/537.36 QQLiveBrowser/8.7.85.27058',
        'Content-Type': 'application/json',
        'referer': 'https://film.video.qq.com/x/vip-center/?entry=common&hidetitlebar=1&aid=V0%24%241%3A0%242%3A8%243%3A8.7.85.27058%244%3A3%245%3A%246%3A%247%3A%248%3A4%249%3A%2410%3A&isDarkMode=0',
        'cookie': cookie
        }
    response_1 = requests.get(url_1, headers=headers_1)
    try:
        res_1 = json.loads(response_1.text)
        log = log + "\n签到获得v力值:" + str(res_1['check_in_score'])
        print(res_1)
    except:
        try:
            res_1 = json.loads(response_1.text)
            log = log + "\n腾讯视频签到异常，返回内容：\n" + str(res_1)
            print(res_1)
        except:
            log = log + "\n腾讯视频签到异常，无法返回内容"
    # 观看
    url_2 = 'https://vip.video.qq.com/rpc/trpc.new_task_system.task_system.TaskSystem/ProvideAward?rpc_data=%7B%22task_id%22:1%7D'
    headers_2 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2104K10AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046237 Mobile Safari/537.36 QQLiveBrowser/8.7.85.27058',
        'Content-Type': 'application/json',
        'referer': 'https://film.video.qq.com/x/vip-center/?entry=common&hidetitlebar=1&aid=V0%24%241%3A0%242%3A8%243%3A8.7.85.27058%244%3A3%245%3A%246%3A%247%3A%248%3A4%249%3A%2410%3A&isDarkMode=0',
        'cookie': cookie
        }
    response_2 = requests.get(url_2, headers=headers_2)
    try:
        res_2 = json.loads(response_2.text)
        log = log + "\n观看获得v力值:" + str(res_2['provide_value'])
        print(res_2)
    except:
        try:
            res_2 = json.loads(response_2.text)
            log = log + "\n腾讯视频领取观看v力值异常,返回内容:\n" + str(res_2)
            print(res_2)
        except:
            log = log + "\n腾讯视频领取观看v力值异常,无法返回内容"

    #任务状态
    url='https://vip.video.qq.com/rpc/trpc.new_task_system.task_system.TaskSystem/ReadTaskList?rpc_data=%7B%22business_id%22:%221%22,%22platform%22:3%7D'
    headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; M2104K10AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046237 Mobile Safari/537.36 QQLiveBrowser/8.7.85.27058',
             'Content-Type':'application/json',
             'referer':'https://film.video.qq.com/x/vip-center/?entry=common&hidetitlebar=1&aid=V0%24%241%3A0%242%3A8%243%3A8.7.85.27058%244%3A3%245%3A%246%3A%247%3A%248%3A4%249%3A%2410%3A&isDarkMode=0',
             'cookie':cookie
             }
    response = requests.get(url,headers=headers)
    try:
        res = json.loads(response.text)
        lis=res["task_list"]
        log = log + '\n---------v力值任务状态----------'
        for i in lis:
            if i["task_button_desc"]=='已完成':
                log=log+'\n标题:'+i["task_maintitle"]+'\n状态:'+i["task_subtitle"]
    except:
        log = log + "获取状态异常，可能是cookie失效"
    print(push.main(log))

def config():
    path = os.getcwd()
    if path == '/opt/function':
        path = 'code/'
    else:
        path = ''
    with open(path + 'config.json', encoding='utf-8') as f:
        account = f.read()
    a=account.count('/*')
    for i in range(a):
        x=account.find('/*')
        y=account.find('*/')+2
        account=account[:x]+account[y:]
    account=json.loads(account)
    return account

def main():
    configs = config()
    a=configs["users"]
    for user in a:      
        if eval(user['enable']):
            ten_video(user['tag'],user['vdevice_qimei36'],user['vqq_appid'],user['vqq_openid'],user['vqq_access_token'],user['vqq_vuserid'],user['main_login'],user['ip'])

def main_handler(event, context):
    return main()


if __name__ == '__main__':
    main()
