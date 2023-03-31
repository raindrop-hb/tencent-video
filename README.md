# 腾讯视频自动签到领取v力值

<p align="center">
    <a href="https://github.com/raindrop-hb"><img alt="Author" src="https://img.shields.io/badge/author-raindrop-blueviolet"/></a>
    <img alt="PHP" src="https://img.shields.io/badge/code-Python-success"/></a><a href="https://jq.qq.com/?_wv=1027&k=fzhZMSbP"><img alt="QQ群" src="https://img.shields.io/badge/QQ-交流群-blackviolet"/></a>
</p>
通过腾讯视频官方接口，每天自动签到并领取v力值，并将结果push到微信。

一个账号平均耗时为半分钟左右。放在服务器运行不需要人工干预，支持无服务器的云函数部署，每天自动push相关信息。

![Q5JF92NR0@Q3$8RF~62`VR6_tmb](https://user-images.githubusercontent.com/72308008/227907256-883946c0-96ae-41eb-a058-7a8cb4b548f5.jpg)


------
目前已实现功能：


- [x] 每天自动执行
- [x] 推送到微信

如有其他好的建议请提交issues

## 环境要求
python 3.6 

## 华为函数工作流 部署
### 操作方法

1.事件函数

2.运行时：python3.6

3.代码复制上去

4.设置-
函数执行入口：index.main_handler

5.触发器-创建触发器-定时触发器-cron表达式：0 30 23 * * ? 每天23点30执行，可以自行修改

### 设置项

push：0为关闭推送，1为企业微信推送

corpid：企业ID

secret：应用的凭证密钥

agentid：应用id

cookie：腾讯pc登录时的cookie

### 抓取腾讯视频cookie
![R`{QKUUBWW3M)VI7GLW 0KE_tmb](https://user-images.githubusercontent.com/72308008/229112182-62ec4420-c12b-44f8-805c-d2657fca0338.png)

工具HttpCanary，腾讯视频

1打开腾讯视频，打开抓包软件，有root就用HttpCanary，没root用电脑fiddler开热点给手机抓包，具体可以百度

2。手机腾讯视频签到，成功后找https://vip.video.qq.com/rpc/trpc.new_task_system.task_system.TaskSystem/CheckIn?rpc_data=%7B%7D的包，cookie只要这几个vdevice_qimei36、
vqq_appid、
vqq_openid、
vqq_access_token、
main_login。这些都是固定的，出现图形验证就去腾讯视频手动签一次到就行了
![image](https://user-images.githubusercontent.com/72308008/229113603-d6cd00f3-e67e-4db3-8f12-76a97a4af31e.png)

