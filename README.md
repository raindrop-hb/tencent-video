# 腾讯视频自动签到领取v力值

<p align="center">
    <a href="https://github.com/raindrop-hb"><img alt="Author" src="https://img.shields.io/badge/author-raindrop-blueviolet"/></a>
    <img alt="PHP" src="https://img.shields.io/badge/code-Python-success"/>
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
![image](https://user-images.githubusercontent.com/72308008/227908303-62c321e8-dfb9-4421-bcab-7a3a1caf73ea.png)

1.电脑访问https://film.video.qq.com/x/vip-center/?entry=common&hidetitlebar=1&aid=V0%24%241%3A0%242%3A8%243%3A8.7.85.27058%244%3A3%245%3A%246%3A%247%3A%248%3A999%249%3A%2410%3A&isDarkMode=0

2.按F12，点全部-标头，刷新一下，随便找一个数据包，在请求标头里有cookie
