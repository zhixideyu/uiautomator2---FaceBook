# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 16:45
# @Author  : ZKL
# @Email   : 837497936@qq.com
import subprocess, re, threading, json, time, datetime
import uiautomator2 as u2
from public.Swipeclass import Swipeclass
from multiprocessing import Pool, Lock
from apscheduler.schedulers.blocking import BlockingScheduler
import xm_friend_search, xm_add_friend, xm_time_line, xm_invited_group, xm_add_group, xm_share_post, xm_module
devices_list = []


# 获取设备序列号以及设备数量
def finddevices():
    data = subprocess.Popen('adb devices', stdout=subprocess.PIPE, universal_newlines=True)
    data_info = data.stdout.read()
    devices = re.findall(r'(.*?)\s+device', data_info)
    if len(devices) > 1:
        deviceIds = devices[1:]
        print('共找到%s个手机' % str(len(devices) - 1))
        for i in deviceIds:
            devices_list.append(i)
            print('ID为%s' % i)
        return deviceIds
    else:
        print('没有找到手机，请检查')
        return


if __name__ == '__main__':
    time_start = time.time()
    finddevices()
    # group_names_list = []
    # with open('C:\\Users\\Administrator\\Desktop\\python-鱼\\xiaomi6.0\\pet_201808291748.txt') as f:
    #     for line in f.88readlines():
    #         if line == '\n':
    #             continue
    #         string = line.strip('\n')
    #         group_names_list.append(string)
    print("""
请选择:

1.搜索好友------xm_friend_search

2.添加好友------xm_add_friend

3.点赞----------xm_time_line

4.邀请进组------xm_invited_group

5.添加小组------xm_add_group

6.分享主页到小组-xm_share_post
    """)
    num2 = int(input('请输入同时执行机器的数量: '))
    num1 = int(input('请输入数量: '))
    number = int(input('请输入序号: '))
    if number == 1:
        mission = xm_friend_search.search
    elif number == 2:
        mission = xm_add_friend.friend
    elif number == 3:
        mission = xm_time_line.like
    elif number == 4:
        mission = xm_invited_group.invited
    elif number == 5:
        mission = xm_add_group.search
    pool = Pool(num2)
    for x in range(len(devices_list)):
        # group_names = xm_module.test_string(file_path='C:\\Users\\Administrator\\Desktop\\python-鱼\\xiaomi6.0\\groups.txt')[x * 50: x * 50+50]
        pool.apply_async(func=mission, args=(num1, devices_list[x]))
    pool.close()
    pool.join()
    time_end = time.time()
    print('%.1f' % (time_end - time_start))
    print('所有任务已结束!')
    pool.terminate()


