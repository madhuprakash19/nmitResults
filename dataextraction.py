#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

# usn = [
# "11NT21IS001-T",
# "11NT21IS002-T",
# "11NT21IS003-T",
# "11NT21IS004-T",
# "11NT21IS005-T",
# "11NT21IS006-T",
# "11NT21IS007-T",
# "11NT21IS008-T",
# "11NT21IS009-T",
# "11NT21IS010-T",
# "11NT21IS011-T",
# "11NT21IS012-T",
# "11NT21IS013-T",
# "11NT21IS014-T",
# "11NT21IS015-T",
# "11NT21IS016-T",
# "11NT21IS017-T",
# "11NT21IS018-T",
# "11NT21IS019-T",
# "11NT21IS020-T",

#     ]

captcha = str(input('Enter captcha'))

for i in range(1,50):
    num=str(i)
    num = num.zfill(3)
    i="1NT18IS"+str(num)
    pg.moveTo(1029, 429, duration=0.3)
    pg.click(1029, 429)
    pg.hotkey('ctrl', 'a')
    pg.typewrite(i)

    pg.moveTo(1029, 458, duration=0.3)
    pg.click(1029, 458)
    pg.hotkey('ctrl', 'a')
    pg.typewrite(captcha)

    pg.moveTo(1176, 546, duration=0.3)
    pg.click(1176, 546)
    time.sleep(0.5)
    pg.hotkey('ctrl', 'u')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'w')

    html_doc = pyperclip.paste()
    soup = bs(html_doc, 'html.parser')
    try:
        div_name = soup.find('div',
                             {'class': 'uk-card uk-card-body stu-data stu-data1'
                             })
        div_usn = soup.find('div',
                            {'class': 'uk-card uk-card-body stu-data stu-data2'
                            })
        div_sgpa = soup.find('div',
                             {'class': 'uk-card uk-card-default uk-card-body credits-sec3'
                             })
        div_cgpa = soup.find('div',
                             {'class': 'uk-card uk-card-default uk-card-body credits-sec4'
                             })
        branch1 = str(div_usn.p.text)
        name1 = str(div_name.h3.text)
        usn1 = str(div_usn.h2.text)
        sgpa1 = str(div_sgpa.p.text)
        cgpa1 = str(div_cgpa.p.text)

        try:
            # print("in stu try")
            temp = student.objects.get(usn=usn1)
        except:
            # print("in stu except")
            temp = student(name=name1, usn=usn1, branch=branch1)
            temp.save()
        s = student.objects.get(usn=usn1)
        # print(s)
        try:
            # print("in gpa try")
            temp = gpa.objects.get(sname=s)
            # print("able to get")
            temp.sgpa = sgpa1
            temp.cgpa = cgpa1
            temp.branch = branch1
            temp.save()
        except:
            # print("in gpa except")
            temp1 = gpa(sname=s, sgpa=sgpa1, cgpa=cgpa1, branch=branch1)
            # print("temp1")
            temp1.save()
            # print("gpa done")
    except:
        # print("ok")
        m = open('nulldata.txt', 'a')
        temp2 = i + ',Data not found\n'
        m.write(temp2)
        m.close()
    pg.moveTo(17, 48, duration=0.5)
    pg.click(17, 48)
