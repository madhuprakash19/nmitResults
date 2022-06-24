#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from nmit.models import student,gpa,subjects,marks
import pyautogui as pg
import time
import pyperclip

# exec(open("test.py").read())

usn = [
"11NT21EC200-T",
"11NT21EC201-T",
"11NT21EC202-T",
"11NT21EC203-T",
"11NT21EC204-T",
"11NT21EC205-T",
"11NT21EC206-T",
"11NT21EC207-T",
"11NT21EC208-T",
"11NT21EC209-T",
"11NT21EC210-T",
"11NT21EC211-T",
"11NT21EC212-T",
"11NT21EC213-T",
"11NT21EC214-T",
"11NT21EC215-T",
"11NT21EC216-T",
"11NT21EC217-T",
"11NT21EC218-T",
"11NT21EC219-T",
"11NT21EC220-T",
"11NT21EC221-T",
"11NT21EC222-T",
"11NT21EC223-T",
"11NT21EC224-T",
"11NT21EC225-T",
"11NT21EC226-T",
"11NT21EC227-T",
"11NT21EC228-T",
"11NT21EC229-T",
"11NT21EC230-T",
"11NT21EC231-T",
"11NT21EC232-T",
"11NT21EC233-T",
"11NT21EC234-T",
"11NT21EC235-T",
"11NT21EC236-T",
"11NT21EC237-T",
"11NT21EC238-T",
"11NT21EC239-T",
"11NT21EC240-T",
"11NT21EC241-T",
"11NT21EC242-T",
"11NT21EC243-T",
"11NT21EC244-T",
"11NT21EC245-T",
"11NT21EC246-T",
"11NT21EC247-T",
"11NT21EC248-T",
"11NT21EC249-T",

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
