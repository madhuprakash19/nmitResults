#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from nmit.models import student,gpa,subjects,marks
import pyautogui as pg
import time
import pyperclip

# exec(open("test.py").read())

captcha = str(input('Enter captcha'))
usn = [
"1NT21AE051",
"1NT21AE052",
"1NT21AE053",
"1NT21AE054",
"1NT21AE055",
"1NT21AE056",
"1NT21AE057",
"1NT21AE058",
"1NT21AE059",
"1NT21AE060",
"1NT21AE061",
"1NT21AE062",
"1NT21AE063",
"1NT21AE064",
"1NT21AE065",
"1NT21AE066",
"1NT21AE067",
"1NT21AE068",
"1NT21AE069",
"1NT21AE070",
"1NT21AE071",
"1NT21AE072",
"1NT21AE073",
"1NT21AE074",
"1NT21AE075",
"1NT21AE076",
"1NT21AE077",
"1NT21AE078",
"1NT21AE079",
"1NT21AE080",
"1NT21AE081",
"1NT21AE082",
"1NT21AE083",
"1NT21AE084",
"1NT21AE085",
"1NT21AE086",
"1NT21AE087",
"1NT21AE088",
"1NT21AE089",
"1NT21AE400",
"1NT21AE401",
"1NT21AE402",
"1NT21AE403",
"1NT21AE404",
"1NT21AE405",
"1NT21AE406",
"1NT21AE407",
"1NT21AE408",
"1NT21AE409",
    ]
for j in usn:
    # num=str(j)
    # num = num.zfill(3)
    # j="1NT19EE"+str(num)
    pg.moveTo(1005, 535, duration=0.3)
    pg.click(1005, 535)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pg.typewrite(j)

    pg.moveTo(998, 570, duration=0.3)
    pg.click(998, 570)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.1)
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

        div_Rcie = soup.find('div',
                             {'class': 'uk-card uk-card-default uk-card-body credits-sec1'
                             })
        div_Ecie = soup.find('div',
                             {'class': 'uk-card uk-card-default uk-card-body credits-sec2'
                             })
        Rcie = str(div_Rcie.p.text)
        Ecie = str(div_Ecie.p.text)
        branch1 = str(div_usn.p.text)
        name1 = str(div_name.h3.text)

        usn1 = str(div_usn.h2.text)
        sgpa1 = str(div_sgpa.p.text)
        cgpa1 = str(div_cgpa.p.text)
        rows = soup.find("table",{'class':'uk-table uk-table-striped res-table'}).find("tbody").find_all("tr")

        try:
            temp = student.objects.get(usn=usn1,sem=8)
        except:
            temp = student(name=name1, usn=usn1, branch=branch1,sem=6)
            temp.save()
        s = student.objects.get(usn=usn1,sem=6)
        try:
            temp = gpa.objects.get(sname=s)
            temp.sgpa = sgpa1
            temp.cgpa = cgpa1
            temp.branch = branch1
            temp.creditsReg = Rcie
            temp.creditsEarn = Ecie
            temp.save()
        except:
            temp1 = gpa(sname=s, sgpa=sgpa1, cgpa=cgpa1, branch=branch1)
            temp1.save()

        for i in range(0,len(rows)):
            Ecells = rows[i].find_all("td")
            Ecode = Ecells[0].get_text()
            Ecourse = Ecells[1].get_text()
            EcreditReg = Ecells[2].get_text()
            EcreditEarn = Ecells[3].get_text()
            Ecie = Ecells[4].get_text()
            Esee = Ecells[5].get_text()
            Etotal = Ecells[6].get_text()
            Egrade = Ecells[7].get_text()

            try:
                sub = subjects.objects.get(code=Ecode)
            except:
                sub = subjects(code=Ecode,name=Ecourse,credits=EcreditReg)
                sub.save()
            sub = subjects.objects.get(code=Ecode)
            try:
                score = marks.objects.get(sname=s,subname=sub)
                score.creditsEarned = EcreditEarn
                score.cie = Ecie
                score.see = Esee
                score.total = Etotal
                score.grade = Egrade
                score.save()
            except:
                score = marks(sname=s ,subname=sub ,creditsEarned=EcreditEarn ,cie=Ecie ,see=Esee ,total=Etotal ,grade=Egrade)
                score.save()
    except:
        print("ok")
    pg.moveTo(17, 48, duration=0.5)
    pg.click(17, 48)
