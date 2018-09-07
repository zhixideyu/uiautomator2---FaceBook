# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 17:45
# @Author  : ZKL
# @Email   : 837497936@qq.com
import uiautomator2 as u2
import time, sys, json
import xm_module, random
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
            time.sleep(1.5)
            if d(text=u"Create New Facebook Account").exists or d(text=u"Tap to Log In").exists or d(text=u"Create New Facebook Account").exists or d(text=u"CREATE NEW FACEBOOK ACCOUNT").exists:
                print('{}设备{}账号出错即将退出!'.format(series, x+1))
                time.sleep(1.5)
                xm_module.back(d)
                continue
            # group_names = xm_module.test_string(file_path='C:\\Users\\Administrator\\Documents\\Tencent Files\\837497936\\FileRecv')[x * 10: x * 10 + 10]
            # group_names = ['Funny YG']
            # for group_name in group_names[x * 10: x * 10+10]:
            group_names = []
            for group_name in group_names:
                selement = d(resourceId="com.facebook.katana:id/(name removed)", text=u"Search")
                selement.click_exists(timeout=10)
                time.sleep(3)
                if d(text="Confirm").exists:
                    d(text="Confirm").click_exists(timeout=5)
                selement.clear_text()
                time.sleep(3)
                selement.send_keys(group_name)
                time.sleep(5)
                d.press('enter')
                time.sleep(8)
                d.swipe(0.852, 0.14, 0.104, 0.137, 0.1)
                d(className="android.view.ViewGroup", instance=6).click()
                time.sleep(8)
                # number = random.randint(1, 2)
                for y in range(num):
                    try:
                        d(description=u"Join group request button", className="android.view.ViewGroup", instance=y).click()
                    except Exception as e:
                        print('没有{}这样的小组!'.format(group_name))
                        break
                    time.sleep(5)
                    if d(description=u"SEND TO ADMINS").exists or d(text=u"Request to Join").exists:
                        d.press('back')
                        time.sleep(2)
                        d(resourceId="com.facebook.katana:id/(name removed)", text=u"LEAVE THIS PAGE").click()
                    time.sleep(2)
                time.sleep(3)
                d(resourceId="com.facebook.katana:id/(name removed)", description=u"Search").click()
                time.sleep(3)
            xm_module.back_home(d, stop_app='com.github.shadowsocks', start_app='io.virtualapp')
            time.sleep(2)
            continue
        except Exception as e:
            print(e)
            print('{}第{}个设备的元素未找到即将退出!>>>>>>'.format(series, x+1))
            xm_module.back_home(d, stop_app='com.github.shadowsocks', start_app='io.virtualapp')
            continue
    time.sleep(6)
    print("{}>>>>>>Add group  over".format(series))
    time.sleep(3)
    d.app_stop('io.virtualapp')
    d.press('home')
    time.sleep(1)
    d.screen_off()




