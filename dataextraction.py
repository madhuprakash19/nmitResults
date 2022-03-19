#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

usn = [
"1NT19CV101",
"1NT19CV102",
"1NT19CV103",
"1NT19CV104",
"1NT19CV105",
"1NT19CV106",
"1NT19CV107",
"1NT19CV108",
"1NT19CV109",
"1NT19CV110",
"1NT19CV111",
"1NT19CV112",
"1NT19CV113",
"1NT19CV114",
"1NT19CV115",
"1NT19CV116",
"1NT19CV117",
"1NT19CV118",
"1NT19CV119",
"1NT19CV120",
"1NT19CV121",
"1NT19CV122",
"1NT19CV123",
"1NT19CV124",
"1NT19CV125",
"1NT19CV126",
"1NT19CV127",
"1NT19CV128",
"1NT19CV129",
"1NT19CV130",
"1NT19CV131",
"1NT19CV132",
"1NT19CV133",
"1NT19CV134",
"1NT19CV135",
"1NT19CV136",
"1NT19CV137",
"1NT19CV138",
"1NT19CV139",
"1NT19CV140",
"1NT19CV141",
"1NT19CV142",
"1NT19CV143",
"1NT19CV144",
"1NT19CV145",
"1NT19CV146",
"1NT19CV147",
"1NT19CV148",
"1NT19CV149",
"1NT19CV150",

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
