#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from nmit.models import student,gpa,subjects,marks
import pyautogui as pg
import time
import pyperclip

# exec(open("test.py").read())

usn = [
"1NT19AE051",
"1NT19AE052",
"1NT19AE053",
"1NT19AE054",
"1NT19AE055",
"1NT19AE056",
"1NT19AE057",
"1NT19AE058",
"1NT19AE059",
"1NT19AE060",
"1NT19AE061",
"1NT19AE062",
"1NT19AE063",
"1NT19AE064",
"1NT19AE065",
"1NT19AE066",
"1NT19AE067",
"1NT19AE068",
"1NT19AE069",
"1NT19AE070",
"1NT19AE071",
"1NT19AE072",
"1NT19AE073",
"1NT19AE074",
"1NT19AE075",
"1NT19AE076",
"1NT19AE077",
"1NT19AE078",
"1NT19AE079",
"1NT19AE080",
"1NT19AE081",
"1NT19AE082",
"1NT19AE083",
"1NT19AE084",
"1NT19AE085",
"1NT19AE086",
"1NT19AE087",
"1NT19AE088",
"1NT19AE089",
"1NT19AE090",
"1NT19AE091",
"1NT19AE092",
"1NT19AE093",
"1NT19AE094",
"1NT19AE095",
"1NT19AE096",
"1NT19AE097",
"1NT19AE098",
"1NT19AE099",
"1NT19AE100",


]

captcha = str(input('Enter captcha'))

for j in usn:
    pg.moveTo(1029, 429, duration=0.3)
    pg.click(1029, 429)
    pg.typewrite(j)

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
            temp = student.objects.get(usn=usn1)
        except:
            temp = student(name=name1, usn=usn1, branch=branch1)
            temp.save()
        s = student.objects.get(usn=usn1)
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
