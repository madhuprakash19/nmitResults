#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import pyautogui as pg
import time
import pyperclip
from nmit.models import student,gpa

# exec(open("dataextraction.py").read())

usn = [
"1NT21IS001",
"1NT21IS002",
"1NT21IS003",
"1NT21IS004",
"1NT21IS005",
"1NT21IS006",
"1NT21IS007",
"1NT21IS008",
"1NT21IS009",
"1NT21IS010",
"1NT21IS011",
"1NT21IS012",
"1NT21IS013",
"1NT21IS014",
"1NT21IS015",
"1NT21IS016",
"1NT21IS017",
"1NT21IS018",
"1NT21IS019",
"1NT21IS020",
"1NT21IS021",
"1NT21IS022",
"1NT21IS023",
"1NT21IS024",
"1NT21IS025",
"1NT21IS026",
"1NT21IS027",
"1NT21IS028",
"1NT21IS029",
"1NT21IS030",
"1NT21IS031",
"1NT21IS032",
"1NT21IS033",
"1NT21IS034",
"1NT21IS035",
"1NT21IS036",
"1NT21IS037",
"1NT21IS038",
"1NT21IS039",
"1NT21IS040",
"1NT21IS041",
"1NT21IS042",
"1NT21IS043",
"1NT21IS044",
"1NT21IS045",
"1NT21IS046",
"1NT21IS047",
"1NT21IS048",
"1NT21IS049",
"1NT21IS050",
    ]

captcha = str(input('Enter captcha'))

for i in usn:
    # num=str(i)
    # num = num.zfill(3)
    # i="1NT18IS"+str(num)
    pg.moveTo(1005, 535, duration=0.3)
    pg.click(1005, 535)
    pg.hotkey('ctrl', 'a')
    pg.typewrite(i)

    pg.moveTo(998, 570, duration=0.3)
    pg.click(998, 570)
    pg.hotkey('ctrl', 'a')
    pg.typewrite(captcha)

    pg.moveTo(1218, 680, duration=0.3)
    pg.click(1218, 680)
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
