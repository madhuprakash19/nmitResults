#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

usn = [
"1NT18CV001",
"1NT18CV002",
"1NT18CV003",
"1NT18CV004",
"1NT18CV005",
"1NT18CV006",
"1NT18CV007",
"1NT18CV008",
"1NT18CV009",
"1NT18CV010",
"1NT18CV011",
"1NT18CV012",
"1NT18CV013",
"1NT18CV014",
"1NT18CV015",
"1NT18CV016",
"1NT18CV017",
"1NT18CV018",
"1NT18CV019",
"1NT18CV020",
"1NT18CV021",
"1NT18CV022",
"1NT18CV023",
"1NT18CV024",
"1NT18CV025",
"1NT18CV026",
"1NT18CV027",
"1NT18CV028",
"1NT18CV029",
"1NT18CV030",
"1NT18CV031",
"1NT18CV032",
"1NT18CV033",
"1NT18CV034",
"1NT18CV035",
"1NT18CV036",
"1NT18CV037",
"1NT18CV038",
"1NT18CV039",
"1NT18CV040",
"1NT18CV041",
"1NT18CV042",
"1NT18CV043",
"1NT18CV044",
"1NT18CV045",
"1NT18CV046",
"1NT18CV047",
"1NT18CV048",
"1NT18CV049",
"1NT18CV050",

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
