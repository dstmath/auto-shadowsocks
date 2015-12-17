# auto-shadowsocks
parse the url "http://www.ishadowsocks.com/" to get free account automically.

linux/osX用户教程
guide:

1 .安装shadowsocks 命令行版本你
参考链接：https://shadowsocks.org/en/download/clients.html

2 .安装chrome和chrmo插件switchyproxy
参考链接：http://blog.viemon.com/chromeshadowsocksproxy-switchyshrp%E7%AE%80%E6%98%8E%E6%95%99%E7%A8%8B/
注：只需要安装完插件即可，不需要后面的步骤。
3.运行脚本
python crawler.py

TODO:
1.目前http://www.ishadowsocks.com 这个网站的免费帐号6小时更新一次，下个版本计划加入定时任务每隔一定时间去重新获取一次帐号；

2.http://www.ishadowsocks.com 提供了三个帐号，计划实现自动切换三个帐号功能选择最优帐号。
