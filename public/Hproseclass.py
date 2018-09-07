#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time, json, random
import hprose

class Hproseclass(object):


    def __init__ (self, row):

        self.row = row




    # 启动模拟器 
    def start(self,ip, index):

        # 启动模拟器
        ret = self.hprose_client(ip, index)

        isopen = False

        rn = 12

        while rn>1:
            rn -= 1
            time.sleep(3)
            isopen = self.hprose_isrunning(ip, index) # 判断模拟是否启动完毕

            if isopen:
                time.sleep(2)
                self.hprose_atx(ip, index)
                time.sleep(6)
                break

        if isopen:

            return True
        else:
            return False


    # 调用启动模拟器
    def hprose_client(self, ip, index, ty='open'):
        print("启动模拟器 IP  : "+ip+"  Index : "+ str(index))
        client = hprose.HttpClient('http://'+ip+':8181/')

        d = {'type': ty, 'data': index}
        data = json.dumps(d)

        return client.send_data(data)

    # 判断模拟器是否启动完成
    def hprose_isrunning(self, ip, index):
        client = hprose.HttpClient('http://'+ip+':8181/')

        return client.is_running(index)

    # 发送 ATX-agent 启动 http
    def hprose_atx(self, ip, index):
        client = hprose.HttpClient('http://'+ip+':8181/')


        la = random.randint(699999,999990)

        ln = random.randint(390000,599999)

        point = "126.%d,37.%d" % (la,  ln)

        return client.run_atx(index, point)

    # 获取当前运行的模拟器数量
    def hprose_num(self, ip):
        client = hprose.HttpClient('http://'+ip+':8181/')

        return client.get_running(11)
