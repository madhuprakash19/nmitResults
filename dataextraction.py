#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

usn = [
"1NT18CV101",
"1NT18CV102",
"1NT18CV103",
"1NT18CV104",
"1NT18CV105",
"1NT18CV106",
"1NT18CV107",
"1NT18CV108",
"1NT18CV109",
"1NT18CV110",
"1NT18CV111",
"1NT18CV112",
"1NT18CV113",
"1NT18CV114",
"1NT18CV115",
"1NT18CV116",
"1NT18CV117",
"1NT18CV118",
"1NT18CV119",
"1NT18CV120",
"1NT18CV121",
"1NT18CV122",
"1NT18CV123",
"1NT18CV124",
"1NT18CV125",
"1NT18CV126",
"1NT18CV127",
"1NT18CV128",
"1NT18CV129",
"1NT18CV130",
"1NT18CV131",
"1NT18CV132",
"1NT18CV133",
"1NT18CV134",
"1NT18CV135",
"1NT18CV136",
"1NT18CV137",
"1NT18CV138",
"1NT18CV139",
"1NT18CV140",
"1NT18CV141",
"1NT18CV142",
"1NT18CV143",
"1NT18CV144",
"1NT18CV145",
"1NT18CV146",
"1NT18CV147",
"1NT18CV148",
"1NT18CV149",
"1NT18CV150",

    ]

captcha = str(input('Enter captcha'))

for i in usn:
    pg.moveTo(1029, 429, duration=0.3)
    pg.click(1029, 429)
    pg.typewrite(i)

    pg.moveTo(1029, 458, duration=0.3)
    pg.click(1029, 458)
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
