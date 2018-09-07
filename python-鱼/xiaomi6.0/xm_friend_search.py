# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 16:48
# @Author  : ZKL
# @Email   : 837497936@qq.com
import uiautomator2 as u2
import time, sys, json
import xm_module
from public.Swipeclass import Swipeclass
from public.Hproseclass import Hproseclass


def search(num, series):
    d = xm_module.boot_device(series, software='io.virtualapp', sleep_time=5)
    res = d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook")
    for x in range(res.count):
        try:
            time.sleep(3)
            print('{}正在启动设备{}'.format(series, x+1))
            d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook", instance=x).click()
            time.sleep(8)
            if d(text=u"OK").exists or d(text=u"Remember Password").exists:
                d.double_click(0.754, 0.964)
            if d(text=u"Create New Facebook Account").exists or d(text=u"Tap to Log In").exists or d(text=u"Create New Facebook Account").exists or d(text=u"CREATE NEW FACEBOOK ACCOUNT").exists or d(text=u"Welcome to Facebook!").exists or d(text=u"GET STARTED").exists:
                print('{}设备{}账号出错即将退出!'.format(series, x+1))
                time.sleep(1.5)
                xm_module.back(d)
                continue
            # names = ["Emma", "Larissa", "Edith","Joyce","Ashley","May","Ivy","Hailey","Stella","Gloria","Amy","Jessie","Lucy","Amanda","Jennifer","Abby","Chelsea","Lorraine","Marian","Anne","Loren","Bella","Sarah","Colin","Kate"]
            names = ["Emma"]
            for name in names:
                # 点击搜索框
                selement = d(resourceId="com.facebook.katana:id/(name removed)", text=u"Search")
                if not selement:
                    print("{}设备{}, 无法找到输入框, 可能是版本问题造成定位不确定, 即将退出!".format(series, x+1))
                    xm_module.back(d)
                    continue
                selement.click_exists(timeout=10)
                time.sleep(3)
                if d(text="Confirm").exists:
                    d(text="Confirm").click_exists(timeout=5)
                # 输入查找人名称# 输入查找人名称
                selement.clear_text()
                time.sleep(3)
                selement.send_keys(name)
                time.sleep(5)
                d.press('enter')
                time.sleep(8)
                d(className="android.view.ViewGroup", instance=3).click()
                time.sleep(8)
                d(className="android.view.ViewGroup", instance=12).click()
                time.sleep(3)
                d(resourceId="com.facebook.katana:id/(name removed)", description=u"Search").click()
                time.sleep(2)
            xm_module.back(d)
            time.sleep(2)
            continue
        except Exception as e:
            print(e)
            print('{}第{}个设备的元素未找到即将退出!>>>>>>'.format(series, x+1))
            xm_module.back(d)
            continue

    time.sleep(6)
    print("search friend play over ...")
    time.sleep(3)
    d.app_stop('com.facebook.katana')
    d.press('home')
    time.sleep(1)
    d.screen_off()

