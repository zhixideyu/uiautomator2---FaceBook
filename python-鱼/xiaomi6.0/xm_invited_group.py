# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 10:01
# @Author  : ZKL
# @Email   : 837497936@qq.co


import uiautomator2 as u2
import xm_module, json
import time
from public.Swipeclass import Swipeclass


def invited(mission):
    for mis in mission:
        series = mis['android_ip']
        num = json.loads(mis['data'])['num']
        place_number = mis['number']
        group_name = json.loads(mis['data'])['name']
        group_name_list = group_name.split(',')
        d = xm_module.boot_device(series, software='io.virtualapp', sleep_time=5)
        swipe = Swipeclass(d)
        res = d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook")
        for x in range(place_number, place_number+1):
            try:
                time.sleep(3)
                print('{}正在启动设备{}'.format(series, x))
                d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook", instance=x-1).click()
                time.sleep(8)
                if d(text=u"OK").exists or d(text=u"Remember Password").exists:
                    d.double_click(0.754, 0.964)
                    time.sleep(1.5)
                if d(text=u"Create New Facebook Account").exists or d(text=u"Tap to Log In").exists or d(text=u"Create New Facebook Account").exists or d(text=u"CREATE NEW FACEBOOK ACCOUNT").exists:
                    print('{}设备{}的账号出错即将退出!'.format(series, x))
                    time.sleep(1.5)
                    xm_module.back(d)
                    continue
                if d(resourceId="com.facebook.katana:id/(name removed)", description=u"More, Tab 4 of 4").exists:
                    d(resourceId="com.facebook.katana:id/(name removed)", description=u"More, Tab 4 of 4").click_exists(timeout=15)
                elif d(resourceId="com.facebook.katana:id/(name removed)", description=u"More, Tab 5 of 5").exists:
                    d(resourceId="com.facebook.katana:id/(name removed)", description=u"More, Tab 5 of 5").click_exists(
                        timeout=15)
                else:
                    d.double_click(0.895, 0.156)
                time.sleep(2)
                d(scrollable=True).scroll.to(description=u"Groups")
                d(description=u"Groups").click(timeout=15)
                time.sleep(5)
                d.double_click(0.146, 0.151)
                time.sleep(5)
                if d(text=u"You aren't in any Facebook Groups.").exists or d(text=u"You're not in any Facebook Groups.").exists:
                    print('设备{}没有加入任何小组, 即将退出!'.format(x))
                    xm_module.back(d)
                    continue
                # group_info = d(resourceId="com.facebook.katana:id/(name removed)", className="android.support.v7.widget.RecyclerView").child(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.FrameLayout")
                # time.sleep(1)
                # print(group_info.count)
                # group_name_list = []
                #
                # for y in range(group_info.count):
                #     group_name_element = d(resourceId="com.facebook.katana:id/(name removed)",
                #                    className="android.support.v7.widget.RecyclerView").child(
                #         resourceId="com.facebook.katana:id/(name removed)", className="android.widget.FrameLayout",
                #         instance=y).child(className="android.widget.TextView")
                #     if group_name_element.count == 2:
                #         group_name = d(resourceId="com.facebook.katana:id/(name removed)",
                #                        className="android.support.v7.widget.RecyclerView").child(
                #             resourceId="com.facebook.katana:id/(name removed)", className="android.widget.FrameLayout",
                #             instance=y).child(className="android.widget.TextView", instance=1).get_text()
                #     else:
                #         group_name = d(resourceId="com.facebook.katana:id/(name removed)",
                #                        className="android.support.v7.widget.RecyclerView").child(
                #             resourceId="com.facebook.katana:id/(name removed)", className="android.widget.FrameLayout",
                #             instance=y).child(className="android.widget.TextView").get_text()
                #     group_name_list.append(group_name)
                # print("小组名称:{}".format(group_name_list))
                # group_name_list = ['Funny  YG']
                for group in group_name_list:
                    d(scrollable=True).scroll.to(text=u"{}".format(group))
                    if not d(text=u"{}".format(group)).exists:
                        print('没有{}这样的小组'.format(group))
                        swipe.swipeUp(d, 0.5)
                        time.sleep(2)
                        continue
                    time.sleep(3)
                    d(text=u"{}".format(group)).click(timeout=15)
                    time.sleep(3)
                    d.double_click(0.979, 0.432)
                    time.sleep(1)
                    if d(description=u"Add Members").exists:
                        d(description=u"Add Members").click_exists(timeout=15)
                    else:
                        d(className="android.view.ViewGroup", instance=7).click_exists(timeout=15)
                    time.sleep(8)
                    quit = False
                    h = 0
                    while True:
                        infos = d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.CheckBox")
                        h += 1
                        if infos:
                            i = 0
                            for n in range(infos.count):
                                if n == 7:
                                    break
                                infos[n].click()
                                time.sleep(1.5)
                                i += 1
                                if i * h >= num:
                                    time.sleep(2)
                                    # print('准备点了')
                                    d(resourceId="com.facebook.katana:id/(name removed)", text=u"Done").click(timeout=15)
                                    d.press('back')
                                    time.sleep(2)
                                    d.press('back')
                                    quit = True
                                    time.sleep(1)
                                    break
                        if quit == True:
                            break
                        swipe.swipeUp(d, 0.5)
                xm_module.back(d)
            except Exception as e:
                print(e)
                print('第{}个设备的元素未找到即将退出!>>>>>>'.format(x))
                xm_module.back(d)
                continue
        time.sleep(6)
        print("{}>>>>>>invited group  over".format(series))
        time.sleep(3)
        d.app_stop('io.virtualapp')
        d.press('home')
        time.sleep(1)
        d.screen_off()






