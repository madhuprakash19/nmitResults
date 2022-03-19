#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

usn = [
"1NT19IS001",
"1NT19IS002",
"1NT19IS003",
"1NT19IS004",
"1NT19IS005",
"1NT19IS006",
"1NT19IS007",
"1NT19IS008",
"1NT19IS009",
"1NT19IS010",
"1NT19IS011",
"1NT19IS012",
"1NT19IS013",
"1NT19IS014",
"1NT19IS015",
"1NT19IS016",
"1NT19IS017",
"1NT19IS018",
"1NT19IS019",
"1NT19IS020",
"1NT19IS021",
"1NT19IS022",
"1NT19IS023",
"1NT19IS024",
"1NT19IS025",
"1NT19IS026",
"1NT19IS027",
"1NT19IS028",
"1NT19IS029",
"1NT19IS030",
"1NT19IS031",
"1NT19IS032",
"1NT19IS033",
"1NT19IS034",
"1NT19IS035",
"1NT19IS036",
"1NT19IS037",
"1NT19IS038",
"1NT19IS039",
"1NT19IS040",
"1NT19IS041",
"1NT19IS042",
"1NT19IS043",
"1NT19IS044",
"1NT19IS045",
"1NT19IS046",
"1NT19IS047",
"1NT19IS048",
"1NT19IS049",
"1NT19IS050"

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
            print("in stu except")
            temp = student(name=name1, usn=usn1, branch=branch1)
            temp.save()
        s = student.objects.get(usn=usn1)
        print(s)
        try:
            print("in gpa try")
            temp = gpa.objects.get(sname=s)
            print("able to get")
            temp.sgpa = sgpa1
            temp.cgpa = cgpa1
            temp.branch = branch1
            temp.save()
        except:
            print("in gpa except")
            temp1 = gpa(sname=s, sgpa=sgpa1, cgpa=cgpa1, branch=branch1)
            print("temp1")
            temp1.save()
            print("gpa done")
    except:
        print("ok")
        m = open('nulldata.txt', 'a')
        temp2 = i + ',Data not found\n'
        m.write(temp2)
        m.close()
    pg.moveTo(17, 48, duration=0.2)
    pg.click(17, 48)
