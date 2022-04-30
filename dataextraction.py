#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

usn = [
"1NT20CV001",
"1NT20CV002",
"1NT20CV003",
"1NT20CV004",
"1NT20CV005",
"1NT20CV006",
"1NT20CV007",
"1NT20CV008",
"1NT20CV009",
"1NT20CV010",
"1NT20CV011",
"1NT20CV012",
"1NT20CV013",
"1NT20CV014",
"1NT20CV015",
"1NT20CV016",
"1NT20CV017",
"1NT20CV018",
"1NT20CV019",
"1NT20CV020",
"1NT20CV021",
"1NT20CV022",
"1NT20CV023",
"1NT20CV024",
"1NT20CV025",
"1NT20CV026",
"1NT20CV027",
"1NT20CV028",
"1NT20CV029",
"1NT20CV030",
"1NT20CV031",
"1NT20CV032",
"1NT20CV033",
"1NT20CV034",
"1NT20CV035",
"1NT20CV036",
"1NT20CV037",
"1NT20CV038",
"1NT20CV039",
"1NT20CV040",
"1NT20CV041",
"1NT20CV042",
"1NT20CV043",
"1NT20CV044",
"1NT20CV045",
"1NT20CV046",
"1NT20CV047",
"1NT20CV048",
"1NT20CV049",
"1NT20CV050",
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
