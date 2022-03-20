#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

usn = [
"1NT18IS051",
"1NT18IS052",
"1NT18IS053",
"1NT18IS054",
"1NT18IS055",
"1NT18IS056",
"1NT18IS057",
"1NT18IS058",
"1NT18IS059",
"1NT18IS060",
"1NT18IS061",
"1NT18IS062",
"1NT18IS063",
"1NT18IS064",
"1NT18IS065",
"1NT18IS066",
"1NT18IS067",
"1NT18IS068",
"1NT18IS069",
"1NT18IS070",
"1NT18IS071",
"1NT18IS072",
"1NT18IS073",
"1NT18IS074",
"1NT18IS075",
"1NT18IS076",
"1NT18IS077",
"1NT18IS078",
"1NT18IS079",
"1NT18IS080",
"1NT18IS081",
"1NT18IS082",
"1NT18IS083",
"1NT18IS084",
"1NT18IS085",
"1NT18IS086",
"1NT18IS087",
"1NT18IS088",
"1NT18IS089",
"1NT18IS090",
"1NT18IS091",
"1NT18IS092",
"1NT18IS093",
"1NT18IS094",
"1NT18IS095",
"1NT18IS096",
"1NT18IS097",
"1NT18IS098",
"1NT18IS099",
"1NT18IS100",


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
    pg.moveTo(17, 48, duration=0.2)
    pg.click(17, 48)
