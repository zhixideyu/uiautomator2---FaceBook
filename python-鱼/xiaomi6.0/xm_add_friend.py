# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 18:46
# @Author  : ZKL



import uiautomator2 as u2
import time, sys, json, random
import xm_module
from public.Swipeclass import Swipeclass
from public.Hproseclass import Hproseclass


def friend(num, series):
    d = xm_module.boot_device(series, software='io.virtualapp', sleep_time=5)
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
            if d(text=u"Create New Facebook Account").exists or d(text=u"Tap to Log In").exists or d(text=u"Create New Facebook Account").exists or d(text=u"CREATE NEW FACEBOOK ACCOUNT").exists:
                print('{}设备{}的账号出错即将退出!'.format(series, x+1))
                time.sleep(1.5)
                xm_module.back(d)
                continue
            d.double_click(0.292, 0.151)
            time.sleep(3)
            if d(descriptionStartsWith="Selected, Notifications, Tab 2 of 5").exists or d(description=u"Manage the notification's settings").exists:
                d.double_click(0.5, 0.15)
            elif d(resourceId="com.facebook.katana:id/(name removed)", description=u"Selected, Notifications, Tab 2 of 4").exists:
                d.double_click(0.624, 0.151)
            elif d(resourceId="com.facebook.katana:id/(name removed)", description=u"Friend Requests, Tab 3 of 4").exists:
                d.double_click(0.617, 0.15)
            time.sleep(7)
            if d(resourceId="com.facebook.katana:id/(name removed)", description=u"Find Friends").exists:
                d(resourceId="com.facebook.katana:id/(name removed)", description=u"Find Friends").click()
            else:
                d.click(0.048, 0.944)
                time.sleep(5)
                d(resourceId="com.facebook.katana:id/(name removed)", description=u"Find Friends").click()
            time.sleep(2)
            d(resourceId="com.facebook.katana:id/(name removed)", text=u"Friend Suggestions").click()
            time.sleep(5)
            i = 0
            while i < num:
                name_element = d(className="android.widget.ListView").child(className="android.view.ViewGroup").child(
                    className="android.widget.LinearLayout").child(className="android.widget.FrameLayout").child(
                    className="android.widget.TextView")
                if not name_element.exists:
                    print('{}设备{}No suggestions to show!'.format(series, x+1))
                    break
                name_str = name_element.get_text()
                if xm_module.judge_pure_english(keyword=name_str) == True:
                    i += 1
                    if d(text=u"Add Friend").exists:
                        d(text=u"Add Friend").click()
                    else:
                        d(text=u"ADD FRIEND").click()
                    print("%s符合要求,已添加!" %(name_str))
                    time.sleep(2)
                else:
                    if d(text=u"Remove").exists:
                        d(text=u"Remove").click()
                    else:
                        d(text=u"REMOVE").click()
                    print("%s不符合要求, 已删除!" %(name_str))
                    time.sleep(2)
            xm_module.back(d)
            time.sleep(1)
        except Exception as e:
            print(e)
            print('{}第{}个设备的元素未找到即将退出!>>>>>>'.format(series, x+1))
            xm_module.back(d)
            continue
    time.sleep(6)
    print("{}>>>>>>Friend Add  over".format(series))
    time.sleep(3)
    d.app_stop('io.virtualapp')
    d.press('home')
    time.sleep(1)
    d.screen_off()
    RLock.release()

