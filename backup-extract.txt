#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from nmit.models import student,gpa,subjects,marks

html_doc = '''
<?xml version="1.0" encoding="utf-8?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-gb" lang="en-gb" dir="ltr"  >
<head>
  <script type="text/javascript" src="/templates/exam1.0/js/template.js.php?v=1.0.0"></script>
  <title>Welcome to NMIT Online Results</title>
    <base href="https://nmitresults.contineo.in/index.php" />
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <meta name="generator" content="NMIT Bengalore" />
  <title>Welcome to Online Results</title>
  <link href="/templates/exam1.0/favicon.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
  <link rel="stylesheet" href="https://nmitresults.contineo.in/plugins/system/osolcaptcha/osolCaptcha/captchaStyle.css" type="text/css" />
  <script type="text/javascript">


		   				function reloadCapthcha(instanceNo)
						{
							var captchaSrc = "https://nmitresults.contineo.in/index.php?showCaptcha=True&instanceNo="+instanceNo+"&time="+ new Date().getTime();
							//alert(captachaSrc);
							//alert(document.getElementById('captchaCode'+instanceNo));
							document.getElementById('captchaCode'+instanceNo).src = captchaSrc ;
							//alert(document.getElementById('captchaCode'+instanceNo).src);
						}

  </script>


  <link rel="shortcut icon" href="/templates/exam1.0/images/favicon.jpg" type="image/x-icon" />
 <script type="text/javascript"></script>
</head>
<body >


<div id="system-message-container">
</div>


<link rel="stylesheet" href="/templates/exam1.0/assets/src/scss/css/uikit.min.css" />
    <link rel="stylesheet" href="/templates/exam1.0/assets/src/scss/css/style.css" />

    <script src="/templates/exam1.0/assets/js/uikit.min.js"></script>
    <script src="/templates/exam1.0/assets/js/uikit-icons.min.js"></script>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <div class="uk-container">
    <div class="box-layout">
    <div class="uk-section uk-section-muted btm-border">
    <div class="">
      <div class="uk-section uk-section-muted header-blde" style="z-index: 980;" uk-sticky="bottom: #offset">
        <div class="" uk-grid>
          <div class="uk-width-3-4@m uk-width-3-4@s">
            <div class="logo">
              <a href="/index.php" rel="home">
                <div class="logo-image">
                  <img src="/components/com_examresult/assets/images/nitte_logo.png" alt="logo" >
              </a>
              </div>

              </a>
            </div>
          </div>

        </div>
      </div>
    </div>
    <div style="text-align: right; padding-right: 10px; ">  <a href="#" title="Search Again" text-decoration:none; onclick="return submitdata('Y29udGluZW86MjAyMi0wNS0wNSAyMTo1MDozMw==')">Search Again</a> </div>

    <form action="http://nmitresults.contineo.in/" method="post" id="submitfrom">
      <input type="hidden" name="key" id="key" value="Y29udGluZW86MjAyMi0wNS0wNSAyMTo1MDozMw==">
     </form>
     <script>
     function submitdata(data1)
     {
       //alert("here");

       document.getElementById("key").value=data1;
       document.getElementById("submitfrom").submit();
       return false;
     }
     </script>



        <div class="uk-section uk-section-muted finance-sec">
        <div class="">
    <div class="mg-left" uk-grid>
        <div class="uk-width-1-3@l uk-width-1-3@m uk-width-1-1@s student-header red-bg">
            <div class="uk-card uk-card-body stu-data stu-data1">

                <h3 style="font-size:14pt;">T P MADHU PRAKASH</h3>
                <img class="uk-preserve-width uk-border" src="/images/students/1NT19IS176.png" alt="Student">
            </div>
        </div>
        <div class="uk-width-2-3@l uk-width-2-3@m uk-width-1-1@s student-header grey-bg">
            <div class="uk-card uk-card-body stu-data stu-data2">
                <h2>1NT19IS176</h2>
                <p>B.E - IS, Sem 5</p>
            </div>
        </div>
    </div>
</div>
<br>

<div class="detail3">
             <div class="uk-child-width-1-2@s uk-child-width-1-2@m uk-child-width-1-4@l uk-grid-match uk-grid" uk-grid="">
                <div class="uk-first-column">
                    <div class="uk-card uk-card-default uk-card-body credits-sec1">
                      <h3>Credits Registered</h3>
                      <p>22</p>
                    </div>
                </div>
                <div>
                    <div class="uk-card uk-card-default uk-card-body credits-sec2">
                      <h3>Credits Earned</h3>
                      <p>22</p>
                    </div>
                </div>
                <div>
                    <div class="uk-card uk-card-default uk-card-body credits-sec3">
                      <h3>SGPA</h3>
                      <p>8.59</p>
                    </div>
                </div>
               <div>
                  <div class="uk-card uk-card-default uk-card-body credits-sec4">
                    <h3>CGPA</h3>
                    <p>8.86</p>
                  </div>
              </div>
            </div>


            </div>


            <div class="uk-section uk-section-muted attendance-sec">
        <div class="uk-container ">
          <h3 class="uk-heading-small att" style="padding-left : 10px;">
           Feb.22 - Provisional Result<!-- <a href="/index.php/component/report/?task=getReport&amp;id=procard&amp;usn=1NT19IS176"><span class="uk-label print-sheet">Print Provisional Grade Card <span uk-icon="print" class="edit-icon uk-icon"><svg width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" data-svg="print"><polyline fill="none" stroke="#000" points="4.5 13.5 1.5 13.5 1.5 6.5 18.5 6.5 18.5 13.5 15.5 13.5"></polyline><polyline fill="none" stroke="#000" points="15.5 6.5 15.5 2.5 4.5 2.5 4.5 6.5"></polyline><rect fill="none" stroke="#000" width="11" height="6" x="4.5" y="11.5"></rect><rect width="8" height="1" x="6" y="13"></rect><rect width="8" height="1" x="6" y="15"></rect></svg></span></span></a> -->
          </h3>
          <div>
            <div class="result-table">
              <div class="uk-grid uk-grid-stack" uk-grid="">
                <div class="uk-width-1-1 uk-first-column">
                  <div class="uk-card uk-card-body result-data">
                    <div class="uk-overflow-auto">
                    <table class="uk-table uk-table-striped res-table">
                      <caption>Result <span class="uk-label color-red"> SGPA: 8.59</span></caption>
                      <thead>
                        <tr>
                          <th>COURSE CODE
                          </th>
                          <th>COURSE NAME</th>
                          <th>Credits Reg.</th>
                          <th>Credits Earned	</th>
                          <th>CIE</th>
                          <th>SEE  </th>
                          <th>Total  </th>
                          <th>Grade</th>
                        </tr>
                      </thead>
                      <tbody>

                                                <tr>
                          <td>18IS51</td>
                          <td>DATABASE MANAGEMENT SYSTEM</td>
                          <td>4.00</td>
                          <td>4.00</td>
                         <td>47.00</td>
                          <td>34.00</td>
                          <td>81.00</td>
                          <td>A</td>
                        </tr>
                                              <tr>
                          <td>18IS52</td>
                          <td>OPERATING SYSTEMS</td>
                          <td>4.00</td>
                          <td>4.00</td>
                         <td>39.00</td>
                          <td>35.00</td>
                          <td>74.00</td>
                          <td>B</td>
                        </tr>
                                              <tr>
                          <td>18IS53</td>
                          <td>THEORY OF COMPUTATION</td>
                          <td>4.00</td>
                          <td>4.00</td>
                         <td>38.00</td>
                          <td>40.00</td>
                          <td>78.00</td>
                          <td>B</td>
                        </tr>
                                              <tr>
                          <td>18IS54</td>
                          <td>COMPUTER NETWORKS</td>
                          <td>4.00</td>
                          <td>4.00</td>
                         <td>38.00</td>
                          <td>35.00</td>
                          <td>73.00</td>
                          <td>B</td>
                        </tr>
                                              <tr>
                          <td>18ISE551</td>
                          <td>STATISTICS FOR DATA SCIENCE</td>
                          <td>3.00</td>
                          <td>3.00</td>
                         <td>46.00</td>
                          <td>40.00</td>
                          <td>86.00</td>
                          <td>A</td>
                        </tr>
                                              <tr>
                          <td>18ISL57</td>
                          <td>DATABASE MANAGEMENT SYSTEM LABORATORY</td>
                          <td>1.00</td>
                          <td>1.00</td>
                         <td>49.00</td>
                          <td>47.00</td>
                          <td>96.00</td>
                          <td>S</td>
                        </tr>
                                              <tr>
                          <td>18ISL58</td>
                          <td>JAVA APPLICATION DEVELOPMENT LABORATORY</td>
                          <td>2.00</td>
                          <td>2.00</td>
                         <td>46.00</td>
                          <td>47.00</td>
                          <td>93.00</td>
                          <td>S</td>
                        </tr>
                                           </tbody>
                    </table>
                  </div>
                  </div>
                </div>
              </div>
            </div>
             <div class="cn-detailed-info cn-exam-fees">

           <br>
            <div class="cn-note-section" style="text-align: justify;">
				<h3 class="uk-heading-line uk-text-center"><span class="glow">DISCLAIMER</span></h3>
            <p> The results published on this web site are provisional and are provided for immediate information to the examinees. These results may not be used as official confirmation of your achievement. While all efforts have been made to make the information available on this website as authentic as possible, Nitte Meenakshi Institute of Technology, <a href="http://www.contineo.in" target="_blank">contineo, e-Sutra chronicles Pvt. Ltd</a> or any of  their staff will not be responsible for any loss caused by shortcoming, defect or inaccuracy in the information provided on this website. Please contact the Examination Department for the final official results.</p>
            </div>

       </div>
  </div>  </div>
  </div>
      <footer>
        <div class="uk-clearfix">
          <div class="uk-float-left">
            <p class="uk-text-left">
              Copyright © Powered By <a href="http://www.contineo.in/" target="_blanks">Contineo</a>
            </p>
          </div>
          <div class="uk-float-right">
            <p class="uk-text-right terms"><a href="#!">Terms of Service</a> | <a href="#!">Privacy Policy</a></p>
          </div>
        </div>
      </footer>


		         				 <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-72409989-1', 'auto');
  ga('send', 'pageview');

</script>
</body>
</html>
<!--Generated On 2022-05-05 21:50:33 By Contineo-->
'''
soup = bs(html_doc, 'html.parser')

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
rows = soup.find("table",{'class':'uk-table uk-table-striped res-table'}).find("tbody").find_all("tr")

len = len(rows)

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
    temp.save()
except:
    temp1 = gpa(sname=s, sgpa=sgpa1, cgpa=cgpa1, branch=branch1)
    temp1.save()
for i in range(0,len):
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

        # exec(open("test.py").read())
