#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from nmit.models import student,gpa,subjects,marks
import pyautogui as pg
import time
import pyperclip

# exec(open("test.py").read())

usn = [
"1NT19CV101",
"1NT19CV102",
"1NT19CV103",
"1NT19CV104",
"1NT19CV105",
"1NT19CV106",
"1NT19CV107",
"1NT19CV108",
"1NT19CV109",
"1NT19CV110",
"1NT19CV111",
"1NT19CV112",
"1NT19CV113",
"1NT19CV114",
"1NT19CV115",
"1NT19CV116",
"1NT19CV117",
"1NT19CV118",
"1NT19CV119",
"1NT19CV120",
"1NT19CV121",
"1NT19CV122",
"1NT19CV123",
"1NT19CV124",
"1NT19CV125",
"1NT19CV126",
"1NT19CV127",
"1NT19CV128",
"1NT19CV129",
"1NT19CV130",
"1NT19CV131",
"1NT19CV132",
"1NT19CV133",
"1NT19CV134",
"1NT19CV135",
"1NT19CV136",
"1NT19CV137",
"1NT19CV138",
"1NT19CV139",
"1NT19CV140",
"1NT19CV141",
"1NT19CV142",
"1NT19CV143",
"1NT19CV144",
"1NT19CV145",
"1NT19CV146",
"1NT19CV147",
"1NT19CV148",
"1NT19CV149",
"1NT19CV150",


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
