# -*- coding: utf-8 -*-
__author__ = 'toor'

import urllib2
from HTMLParser import HTMLParser
import os
import threading

str_address = r'服务器地址:'
str_port = r'端口:'
str_password = r'密码:'
str_crypt_method = r'加密方式:'
str_status = '状态:'
str_warn = r'注意:'

youtube = r'https://www.youtube.com'
accout_size = 3

class SSAccountParser(HTMLParser):
    dicts = []
    index = 0

    def __init__(self):
        HTMLParser.__init__(self)
        self.init_dicts()

    def init_dicts(self):
        for i in range(0, accout_size):
            accout_dict = {}
            self.dicts.append(accout_dict)

    def handle_startendtag(self, tag, attrs):
        HTMLParser.handle_startendtag(self, tag, attrs)

    def handle_starttag(self, tag, attrs):
        HTMLParser.handle_starttag(self, tag, attrs)
        if tag == "section":
            for k, v in attrs:
                if v == "free":
                    print("k ==============" + k)

    def handle_data(self, data):
        HTMLParser.handle_data(self, data)
        if str_address in data:
            self.dicts[self.index]['server'] = data[data.find(':') + 1:]

        elif str_port in data:
            self.dicts[self.index]['server_port'] = data[data.find(':') + 1:]
        elif str_password in data:
            self.dicts[self.index]['password'] = data[data.find(':') + 1:]
        elif str_crypt_method in data:
            self.dicts[self.index]['method'] = data[data.find(':') + 1:]
            self.index += 1

    def handle_endtag(self, tag):
        HTMLParser.handle_endtag(self, tag)

    def handle_comment(self, data):
        HTMLParser.handle_comment(self, data)

    def get_accounts(self):
        return self.dicts


# 连接之前kill sslocal进程
def kill_process_by_name(name):
    return os.system('pkill -9 ' + name)

def start_parse():

    html_content = urllib2.urlopen("http://www.ishadowsocks.com").read()
    ssaccountparser = SSAccountParser()
    ssaccountparser.feed(html_content)

    accounts = ssaccountparser.get_accounts()

    #accounts[0]：US
    #accounts[1]：HK
    #accounts[2]：JP

    account = accounts[0]
    print(account)

    kill_result = kill_process_by_name('sslocal')
    print("kill return = " + str(kill_result))

    os.system('sslocal -s ' + account['server'] + ' -p ' + account['server_port'] + ' -k ' + account['password'] + '&')
    #休眠5s 再去打开youtube
    #threading._sleep(5)
    print("=====finish=========")

start_parse()
