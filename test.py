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
"1NT21EC001",
"1NT21EC002",
"1NT21EC003",
"1NT21EC004",
"1NT21EC005",
"1NT21EC006",
"1NT21EC007",
"1NT21EC008",
"1NT21EC009",
"1NT21EC010",
"1NT21EC011",
"1NT21EC012",
"1NT21EC013",
"1NT21EC014",
"1NT21EC015",
"1NT21EC016",
"1NT21EC017",
"1NT21EC018",
"1NT21EC019",
"1NT21EC020",
"1NT21EC021",
"1NT21EC022",
"1NT21EC023",
"1NT21EC024",
"1NT21EC025",
"1NT21EC026",
"1NT21EC027",
"1NT21EC028",
"1NT21EC029",
"1NT21EC030",
"1NT21EC031",
"1NT21EC032",
"1NT21EC033",
"1NT21EC034",
"1NT21EC035",
"1NT21EC036",
"1NT21EC037",
"1NT21EC038",
"1NT21EC039",
"1NT21EC040",
"1NT21EC041",
"1NT21EC042",
"1NT21EC043",
"1NT21EC044",
"1NT21EC045",
"1NT21EC046",
"1NT21EC047",
"1NT21EC048",
"1NT21EC049",
"1NT21EC050",
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
