#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

usn = [
"1NT19IS051",
"1NT19IS052",
"1NT19IS053",
"1NT19IS054",
"1NT19IS055",
"1NT19IS056",
"1NT19IS057",
"1NT19IS058",
"1NT19IS059",
"1NT19IS060",
"1NT19IS061",
"1NT19IS062",
"1NT19IS063",
"1NT19IS064",
"1NT19IS065",
"1NT19IS066",
"1NT19IS067",
"1NT19IS068",
"1NT19IS069",
"1NT19IS070",
"1NT19IS071",
"1NT19IS072",
"1NT19IS073",
"1NT19IS074",
"1NT19IS075",
"1NT19IS076",
"1NT19IS077",
"1NT19IS078",
"1NT19IS079",
"1NT19IS080",
"1NT19IS081",
"1NT19IS082",
"1NT19IS083",
"1NT19IS084",
"1NT19IS085",
"1NT19IS086",
"1NT19IS087",
"1NT19IS088",
"1NT19IS089",
"1NT19IS090",
"1NT19IS091",
"1NT19IS092",
"1NT19IS093",
"1NT19IS094",
"1NT19IS095",
"1NT19IS096",
"1NT19IS097",
"1NT19IS098",
"1NT19IS099",
"1NT19IS100"
    ]

captcha = str(input('Enter captcha'))

for i in usn:
    pg.moveTo(1029, 429, duration=0.2)
    pg.click(1029, 429)
    pg.typewrite(i)

    pg.moveTo(1029, 458, duration=0.2)
    pg.click(1029, 458)
    pg.typewrite(captcha)

    pg.moveTo(1176, 546, duration=0.2)
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
            print("in stu try")
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
    pg.moveTo(17, 48, duration=0.2)
    pg.click(17, 48)
