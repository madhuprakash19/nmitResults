#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from nmit.models import student,gpa,subjects,marks
import pyautogui as pg
import time
import pyperclip

# exec(open("test.py").read())

usn = [
"11NT21AI001-T",
"11NT21AI002-T",
"11NT21AI003-T",
"11NT21AI004-T",
"11NT21AI005-T",
"11NT21AI006-T",
"11NT21AI007-T",
"11NT21AI008-T",
"11NT21AI009-T",
"11NT21AI010-T",
"11NT21AI011-T",
"11NT21AI012-T",
"11NT21AI013-T",
"11NT21AI014-T",
"11NT21AI015-T",
"11NT21AI016-T",
"11NT21AI017-T",
"11NT21AI018-T",
"11NT21AI019-T",
"11NT21AI020-T",
"11NT21AI021-T",
"11NT21AI022-T",
"11NT21AI023-T",
"11NT21AI024-T",
"11NT21AI025-T",
"11NT21AI026-T",
"11NT21AI027-T",
"11NT21AI028-T",
"11NT21AI029-T",
"11NT21AI030-T",
"11NT21AI031-T",
"11NT21AI032-T",
"11NT21AI033-T",
"11NT21AI034-T",
"11NT21AI035-T",
"11NT21AI036-T",
"11NT21AI037-T",
"11NT21AI038-T",
"11NT21AI039-T",
"11NT21AI040-T",
"11NT21AI041-T",
"11NT21AI042-T",
"11NT21AI043-T",
"11NT21AI044-T",
"11NT21AI045-T",
"11NT21AI046-T",
"11NT21AI047-T",
"11NT21AI048-T",
"11NT21AI049-T",
"11NT21AI050-T",

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
