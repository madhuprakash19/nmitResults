#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

usn = [
"1NT19AE001",
"1NT19AE002",
"1NT19AE003",
"1NT19AE004",
"1NT19AE005",
"1NT19AE006",
"1NT19AE007",
"1NT19AE008",
"1NT19AE009",
"1NT19AE010",
"1NT19AE011",
"1NT19AE012",
"1NT19AE013",
"1NT19AE014",
"1NT19AE015",
"1NT19AE016",
"1NT19AE017",
"1NT19AE018",
"1NT19AE019",
"1NT19AE020",
"1NT19AE021",
"1NT19AE022",
"1NT19AE023",
"1NT19AE024",
"1NT19AE025",
"1NT19AE026",
"1NT19AE027",
"1NT19AE028",
"1NT19AE029",
"1NT19AE030",
"1NT19AE031",
"1NT19AE032",
"1NT19AE033",
"1NT19AE034",
"1NT19AE035",
"1NT19AE036",
"1NT19AE037",
"1NT19AE038",
"1NT19AE039",
"1NT19AE040",
"1NT19AE041",
"1NT19AE042",
"1NT19AE043",
"1NT19AE044",
"1NT19AE045",
"1NT19AE046",
"1NT19AE047",
"1NT19AE048",
"1NT19AE049",
"1NT19AE050",



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
