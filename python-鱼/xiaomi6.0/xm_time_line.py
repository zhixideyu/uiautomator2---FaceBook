# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 14:52
# @Author  : ZKL
# @Email   : 837497936@qq.com
import uiautomator2 as u2
import xm_module, threading
import time, sys, json, random, pymysql
from public.Swipeclass import Swipeclass
from public.Hproseclass import Hproseclass
import xm_add_friend


def like(num, series):
    d = xm_module.boot_device(series, software='io.virtualapp', sleep_time=5)
    swipe = Swipeclass(d)
    res = d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook")
    for x in range(res.count):
        try:
            time.sleep(3)
            print('{}正在启动设备{}'.format(series, x+1))
            d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook", instance=x).click_exists(timeout=15)
            time.sleep(8)
            if d(text=u"OK").exists or d(text=u"Remember Password").exists:
                d.double_click(0.754, 0.964)
                time.sleep(5)
            if d(text=u"Create New Facebook Account").exists or d(text=u"Tap to Log In").exists or d(text=u"Create New Facebook Account").exists or d(text=u"CREATE NEW FACEBOOK ACCOUNT").exists or d(text=u"Welcome to Facebook!").exists or d(text=u"GET STARTED").exists:
                print('{}设备{}账号出错即将或者没有任何好友推荐退出!'.format(series, x+1))
                time.sleep(1.5)
                xm_module.back(d)
                continue
            i = 0
            while True:
                data = d(text="Like")
                if data:
                    for c in data:
                        if d(descriptionStartsWith="Like Button Pressed").exists:
                            continue
                        ex = random.randint(0, 9)
                        if ex > 6:
                            c.click()
                            i += 1
                            if d(descriptionStartsWith="Selected, Friend Requests").exists:
                                time.sleep(2)
                                d(resourceId="com.facebook.katana:id/news_feed_tab").click_exists(timeout=15)
                if i >= 6:
                    xm_module.back(d)
                    break
                swipe.swipeUp(d, 0.1)
                time.sleep(random.randint(1, 5))
        except Exception as e:
            print('{}第{}个设备的元素未找到即将退出!>>>>>>'.format(series, x+1))
            xm_module.back(d)
            continue
    time.sleep(6)
    print("{}>>>>>>Time line  over".format(series))
    time.sleep(3)
    d.app_stop('io.virtualapp')
    d.press('home')
    time.sleep(1)
    d.screen_off()

