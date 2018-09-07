# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 11:34
# @Author  : ZKL
# @Email   : 837497936@qq.com
import uiautomator2 as u2
from public.Swipeclass import Swipeclass
from public.Hproseclass import Hproseclass
import time, sys, json, random, pymysql, requests
import urllib.request
import re
import pymysql


db = pymysql.connect(
    host='',
    user='',
    password='',
    port=3306,
    db='',
    use_unicode=True,
    charset=''
)


def register():
    try:
        services = 'ebd4f2f67d83'
        start_time = time.time()
        d = u2.connect_usb(services)
        d.screen_off()
        d.screen_on()
        time.sleep(1)
        swipe = Swipeclass(d)
        swipe.swipeUp(d, 0.1)
        time.sleep(3)
        d.app_start('io.virtualapp')
        # d.app_start('com.facebook.katana')
        print('正在启动io.virtualapp')
    except Exception as e:
        print(e)
        sys.exit()
    time.sleep(5)
    print('virtualapp启动成功!')
    time.sleep(5)
    res = d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook")
    print('一共有%s个设备' %(res.count))
    for x in range(1,2):
        try:
            time.sleep(1)
            print('正在启动设备{}'.format(x+1))
            d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook", instance=x).click_exists(timeout=15)
            time.sleep(15)
            if d(text=u"Continue").exists:
                d(text=u"Continue").click_exists(timeout=5)
            elif d(text=u"CONTINUE").exists:
                d(text=u"CONTINUE").click_exists(timeout=5)
            time.sleep(2)
            if d(resourceId="com.facebook.katana:id/(name removed)", text=u"CREATE NEW FACEBOOK ACCOUNT").exists:
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"CREATE NEW FACEBOOK ACCOUNT").click_exists(timeout=15)
            else:
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"Create New Facebook Account").click_exists(timeout=15)
            time.sleep(2)
            if d(resourceId="com.facebook.katana:id/(name removed)", text=u"Join Facebook").exists:
                d(text=u"Next").click_exists(timeout=5)
            else:
                d(scrollable=True).scroll.to(text="Next")
                d(text=u"Next").click_exists(timeout=5)
            time.sleep(3)
            first_name = rdm(1, 2)
            last_name = rdm(2, 3)
            if d(resourceId="com.facebook.katana:id/(name removed)", text=u"First Name").exists:
                print("First name ....")
                d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.EditText").send_keys(last_name)
                time.sleep(2)
                d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.EditText", instance=1).send_keys(first_name)
                d(text="Next").click_exists(timeout=5)
            time.sleep(2)
            name = last_name+first_name
            if d(text="What's Your Birthday?").exists:
                print("Birthday......")
            number = random.randint(1989, 1998)
            # number = 指定年份
            print('出生年份随机数为{}'.format(number))
            time.sleep(0.5)
            while True:
                # 出生日期的年份
                year_number = int(
                    d(className="android.widget.LinearLayout").child(className="android.widget.NumberPicker",instance=2).child(className="android.widget.EditText").get_text())
                print(year_number)
                if year_number == number:
                    print('已选定指定年份!')
                    break
                if year_number > number:
                    d.double_click(0.681, 0.28)
                    time.sleep(0.5)
                elif year_number < number:
                    d.double_click(0.677, 0.492)
                    time.sleep(0.5)
                time.sleep(1.5)
            # 长按时间
            click_time = round(random.uniform(0.7, 2), 1)
            click_time2 = round(random.uniform(0.7, 3.5), 1)
            time.sleep(0.25)
            # 月份
            # 上   下
            count_list = [0.285, 0.451]
            d.long_click(0.509, random.choice(count_list), click_time)
            time.sleep(0.25)
            # 日
            # 上   下
            count2_list = [0.28,  0.447]
            d.long_click(0.319, random.choice(count2_list), click_time2)
            time.sleep(2)
            year = d(className="android.widget.LinearLayout").child(className="android.widget.NumberPicker",
                                                                           instance=2).child(
                className="android.widget.EditText").get_text()
            month = d(className="android.widget.LinearLayout").child(className="android.widget.NumberPicker",
                                                                           instance=0).child(
                className="android.widget.EditText").get_text()
            day = d(className="android.widget.LinearLayout").child(className="android.widget.NumberPicker",
                                                                           instance=1).child(
                className="android.widget.EditText").get_text()
            birthday = str(year) + '年'+ str(month) + '月'+str(day) + '日'
            time.sleep(2)
            d(text="Next").click_exists(timeout=5)
            response = requests.get('http://api.codedw.com/api/do.php?action=loginIn&name=meyou2&password=131liuhan!')
            time.sleep(5)
            d(resourceId="com.facebook.katana:id/(name removed)", text=u"Female").click_exists(timeout=5)
            d(text="Next").click_exists(timeout=5)
            time.sleep(3)
            phone = getphone()
            if phone.isdigit():
                print()
                print('设备%s 手机号 %s' % (x, phone))
            else:
                time.sleep(3)
                phone = getphone()
            print(phone)
            print("Phone / Email input  ....")
            d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.EditText").send_keys(phone)
            time.sleep(2)
            d(text="Next").click_exists(timeout=5)
            time.sleep(2)
            password = rdm(8)
            d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.EditText").send_keys(password)
            print(password)
            time.sleep(2)
            d(text="Next").click_exists(timeout=5)
            time.sleep(2)
            if d(text=u"Finish Signing Up").exists:
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"Sign Up").click_exists(timeout=5)
            time.sleep(20)
            if d(resourceId="com.facebook.katana:id/(name removed)", text=u"Save Password").exists:
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"Save Password").click(timeout=30)
            code = getcode(phone)
            print(code)
            with open('record.txt', 'a', encoding='utf-8') as f:
                f.write('\n')
                f.write("设备{}第{}个 账号:{} 密码:{} 验证码:{} 生日:{}".format(services, x+1, phone, password, code, birthday))
                f.write('\n')
            cursor = db.cursor()
            insert_sql = "INSERT INTO meu_xiaomi(series, mobile, position, password, name, birthday)VALUE('{}', '{}', '{}', '{}', '{}', '{}')".format(services, phone, x+1, password, name, birthday)
            cursor.execute(insert_sql)

            db.commit()
            time.sleep(8)

            d.app_stop('com.facebook.katana')
            time.sleep(2)
            d.app_stop('io.virtualapp')
            time.sleep(2)
            d.app_start('io.virtualapp')
            time.sleep(3)
            d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook", instance=x).click_exists(timeout=15)
            time.sleep(5)
            if d(resourceId="com.facebook.katana:id/(name removed)", text=u"Save Password").exists:
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"Save Password").click_exists(timeout=15)
                time.sleep(15)
                d(resourceId="io.virtualapp:id/item_app_name", text=u"Facebook", instance=x).click()
            if d(resourceId="com.facebook.katana:id/(name removed)", text=u"Skip").exists:
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"Skip").click_exists(timeout=5)
                time.sleep(2)
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"Done").click_exists(timeout=5)
                time.sleep(2)
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"Confirmation code").send_keys(code)
                time.sleep(2)
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"Confirm").click()
                time.sleep(5)
                d(resourceId="com.facebook.katana:id/(name removed)", text=u"OK").click()
            while True:
                d.click(0.123, 0.152)
                time.sleep(2)
                if d(resourceId="com.facebook.katana:id/(name removed)", text=u"Continue").exists:
                    d(resourceId="com.facebook.katana:id/(name removed)", text=u"Continue").click()
                    break
                d.click(0.863, 0.149)
                time.sleep(2)
            time.sleep(2)
            d(resourceId="com.facebook.katana:id/(name removed)", text=u"Confirmation code").send_keys(code)
            time.sleep(2)
            d(resourceId="com.facebook.katana:id/(name removed)", text=u"Confirm").click()
            time.sleep(8)
            print('设备{}第{}个注册成功!'.format(services, x + 1))
            time.sleep(2)
            d.press('back')
            time.sleep(2)
            d.press('back')
            time.sleep(2)
        except Exception as e:
            print("{}设备出错".format(services))
            print(e)
            continue


def getphone():
    get_url = 'http://api.codedw.com/api/do.php?action=getPhone&token=xxxx&sid=xxxx'
    req = urllib.request.urlopen(get_url)
    print(req)
    ret = req.read()
    ret = ret.decode("UTF-8")
    print(ret)

    data = ret.split('|')

    return data[1]


def getcode(phone):
    time.sleep(5)
    phone = str(phone)

    for i in range(10):
        get_url =  "http://api.codedw.com/api/do.php?action=getMessage&token=xxxx&sid=xxxx&phone=%s"% (phone)

        req = urllib.request.urlopen(get_url)

        ret = req.read()
        ret = ret.decode("UTF-8")
        print(ret)
        data = ret.split('|')

        code = False

        if data[0] == '1':
            code = data[1]
            print(code)
            code = re.sub("\D", "", code)
            break
        else:
            time.sleep(5)
    return code


def rdm(num=6, ty=1):
    salt = ''
    if ty == 1:
        seed = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ"

        sa = []

        for i in range(num):
            sa.append(random.choice(seed))

        salt = ''.join(sa)
    elif ty == 2:

        index = random.randint(0, 80)
        seed = ['Molly', 'Amy', 'Claire', 'Emily', 'Katie', 'Medeline', 'Katelyn',
                'Emma', 'Abigail', 'Carly', 'Jenna', 'Heather', 'Katherine', 'Caitlin',
                'Kaitlin', 'Holly', 'Allison', 'Kaitlyn', 'Hannah', 'Kathryn', 'sarah',
                'emily', 'jessica', 'lauren', 'ashley', 'amanda', 'megan', 'samantha',
                'hannah', 'rachel', 'nicole', 'taylor', 'elizabeth', 'katherine', 'madison',
                'jennifer', 'alexandra', 'brittany', 'danielle', 'rebecca', 'macy', 'maggie',
                'mandy', 'mango', 'mani', 'maple', 'margie', 'marsha', 'maria', 'mary', 'may',
                'maya', 'megan', 'melissa', 'michelle', 'miki', 'mimi', 'mona', 'sally', 'sammi',
                'sandra', 'sandy', 'selina', 'sara', 'sarah', 'serena', 'shadow', 'sharon', 'sheila',
                'sherry', 'shirley', 'sky', 'sophie', 'stella', 'stephanie', 'stephy', 'jade', 'janice',
                'jannet', 'janny', 'jasmine']
        sa = seed[index]
        salt = ''.join(sa)
    elif ty == 3:
        index = random.randint(0, 12)
        seed = ['Richardson', 'Churchill', 'Johnson', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Martinson', 'Anderson', 'Wilson']

        sa = seed[index]
        salt = ''.join(sa)

    return salt


register()
