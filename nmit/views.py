from django.shortcuts import render
from nmit.models import student,gpa,missing,marks,subjects
from django.db.models import Count

# Create your views here.

def subject(request):
    check = 0
    temp = subjects.objects.all().order_by('-id')
    if request.method == 'POST':
        check=1
        x=[]
        y=[]
        sub = request.POST['subject']
        a = subjects.objects.get(code=sub)
        subject = a.name
        result = list(marks.objects.filter(subname=a)
        .values('grade')
        .annotate(dcount=Count('grade'))
        .order_by()
        )
        for i in result:
            x.append(list(i.values())[0])
            y.append(list(i.values())[1])
        return render(request,'subject.html',{'check':check,'x':x,'y':y,'subject':subject,'temp':temp})
    return render(request,'subject.html',{'check':check,'temp':temp})




def sem1(request):
    topper1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 1').order_by('-sgpa')[:10:1])
    is1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 1',sname__usn__contains='IS').order_by('-sgpa')[:10:1])
    cs1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 1',sname__usn__contains='CS').order_by('-sgpa')[:10:1])
    ec1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 1',sname__usn__contains='EC').order_by('-sgpa')[:10:1])
    cv1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 1',sname__usn__contains='CV').order_by('-sgpa')[:10:1])
    me1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 1',sname__usn__contains='ME').order_by('-sgpa')[:10:1])
    ae1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 1',sname__usn__contains='AE').order_by('-sgpa')[:10:1])
    ee1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 1',sname__usn__contains='EE').order_by('-sgpa')[:10:1])
    ai1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 1',sname__usn__contains='AD').order_by('-sgpa')[:10:1])
    return render(request,'sem1.html',{'topper1':topper1,'is1':is1,'cs1':cs1,'ec1':ec1,'me1':me1,'ae1':ae1,'ee1':ee1,'cv1':cv1,'ai1':ai1})

def sem2(request):
    topper1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2').order_by('-sgpa')[:10:1])
    is1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2',sname__usn__contains='IS').order_by('-sgpa')[:10:1])
    cs1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2',sname__usn__contains='CS').order_by('-sgpa')[:10:1])
    ec1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2',sname__usn__contains='EC').order_by('-sgpa')[:10:1])
    cv1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2',sname__usn__contains='CV').order_by('-sgpa')[:10:1])
    me1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2',sname__usn__contains='ME').order_by('-sgpa')[:10:1])
    ae1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2',sname__usn__contains='AE').order_by('-sgpa')[:10:1])
    ai1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2',sname__usn__contains='AD').order_by('-sgpa')[:10:1])
    ee1 = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2',sname__usn__contains='EE').order_by('-sgpa')[:10:1])
    return render(request,'sem2.html',{'topper1':topper1,'is1':is1,'cs1':cs1,'ec1':ec1,'me1':me1,'ae1':ae1,'ee1':ee1,'cv1':cv1,'ai1':ai1})



def sem3(request):
    topper3 = list(gpa.objects.filter(branch__in = ['B.E - IS, Sem 3','B.E - CS, Sem 3','B.E - EC, Sem 3','B.E - EE, Sem 3','B.E - ME, Sem 3','B.E - AE, Sem 3','B.E - CV, Sem 3']).order_by('-sgpa')[:10:1])
    is3 = list(gpa.objects.filter(branch = 'B.E - IS, Sem 3').order_by('-sgpa')[:10:1])
    cs3 = list(gpa.objects.filter(branch = 'B.E - CS, Sem 3').order_by('-sgpa')[:10:1])
    ec3 = list(gpa.objects.filter(branch = 'B.E - EC, Sem 3').order_by('-sgpa')[:10:1])
    me3 = list(gpa.objects.filter(branch = 'B.E - ME, Sem 3').order_by('-sgpa')[:10:1])
    ae3 = list(gpa.objects.filter(branch = 'B.E - AE, Sem 3').order_by('-sgpa')[:10:1])
    ee3 = list(gpa.objects.filter(branch = 'B.E - EE, Sem 3').order_by('-sgpa')[:10:1])
    cv3 = list(gpa.objects.filter(branch = 'B.E - CV, Sem 3').order_by('-sgpa')[:10:1])
    return render(request,'sem3.html',{'topper3':topper3,'is3':is3,'cs3':cs3,'ec3':ec3,'me3':me3,'ae3':ae3,'ee3':ee3,'cv3':cv3})

def sem5(request):
    topper5 = list(gpa.objects.filter(branch__in = ['B.E - IS, Sem 5','B.E - CS, Sem 5','B.E - EC, Sem 5','B.E - EE, Sem 5','B.E - ME, Sem 5','B.E - AE, Sem 5','B.E - CV, Sem 5']).order_by('-sgpa')[:10:1])
    is5 = list(gpa.objects.filter(branch = 'B.E - IS, Sem 5').order_by('-sgpa')[:10:1])
    cs5 = list(gpa.objects.filter(branch = 'B.E - CS, Sem 5').order_by('-sgpa')[:10:1])
    ec5 = list(gpa.objects.filter(branch = 'B.E - EC, Sem 5').order_by('-sgpa')[:10:1])
    me5 = list(gpa.objects.filter(branch = 'B.E - ME, Sem 5').order_by('-sgpa')[:10:1])
    ae5 = list(gpa.objects.filter(branch = 'B.E - AE, Sem 5').order_by('-sgpa')[:10:1])
    ee5 = list(gpa.objects.filter(branch = 'B.E - EE, Sem 5').order_by('-sgpa')[:10:1])
    cv5 = list(gpa.objects.filter(branch = 'B.E - CV, Sem 5').order_by('-sgpa')[:10:1])
    return render(request,'sem5.html',{'topper5':topper5,'is5':is5,'cs5':cs5,'ec5':ec5,'me5':me5,'ae5':ae5,'ee5':ee5,'cv5':cv5})


def sem7(request):
    topper7 = list(gpa.objects.filter(branch__in = ['B.E - IS, Sem 7','B.E - CS, Sem 7','B.E - EC, Sem 7','B.E - EE, Sem 7','B.E - ME, Sem 7','B.E - AE, Sem 7','B.E - CV, Sem 7']).order_by('-sgpa')[:10:1])
    is7 = list(gpa.objects.filter(branch = 'B.E - IS, Sem 7').order_by('-sgpa')[:10:1])
    cs7 = list(gpa.objects.filter(branch = 'B.E - CS, Sem 7').order_by('-sgpa')[:10:1])
    ec7 = list(gpa.objects.filter(branch = 'B.E - EC, Sem 7').order_by('-sgpa')[:10:1])
    me7 = list(gpa.objects.filter(branch = 'B.E - ME, Sem 7').order_by('-sgpa')[:10:1])
    ae7 = list(gpa.objects.filter(branch = 'B.E - AE, Sem 7').order_by('-sgpa')[:10:1])
    ee7 = list(gpa.objects.filter(branch = 'B.E - EE, Sem 7').order_by('-sgpa')[:10:1])
    cv7 = list(gpa.objects.filter(branch = 'B.E - CV, Sem 7').order_by('-sgpa')[:10:1])
    return render(request,'sem7.html',{'topper7':topper7,'is7':is7,'cs7':cs7,'ec7':ec7,'me7':me7,'ae7':ae7,'ee7':ee7,'cv7':cv7})

def sem6(request):
    topper6 = list(gpa.objects.filter(branch__in = ['B.E - IS, Sem 6','B.E - CS, Sem 6','B.E - EC, Sem 6']).order_by('-sgpa')[:10:1])
    is6 = list(gpa.objects.filter(branch = 'B.E - IS, Sem 6').order_by('-sgpa')[:10:1])
    cs6 = list(gpa.objects.filter(branch = 'B.E - CS, Sem 6').order_by('-sgpa')[:10:1])
    ec6 = list(gpa.objects.filter(branch = 'B.E - EC, Sem 6').order_by('-sgpa')[:10:1])
    me6 = list(gpa.objects.filter(branch = 'B.E - ME, Sem 6').order_by('-sgpa')[:10:1])
    ae6 = list(gpa.objects.filter(branch = 'B.E - AE, Sem 6').order_by('-sgpa')[:10:1])
    ee6 = list(gpa.objects.filter(branch = 'B.E - EE, Sem 6').order_by('-sgpa')[:10:1])
    cv6 = list(gpa.objects.filter(branch = 'B.E - CV, Sem 6').order_by('-sgpa')[:10:1])
    return render(request,'sem6.html',{'topper6':topper6,'is6':is6,'cs6':cs6,'ec6':ec6,'me6':me6,'ae6':ae6,'ee6':ee6,'cv6':cv6})


def aboutus(request):
    return render(request,'aboutus.html')

def namewise(request):
    result = {}
    if request.method == 'POST':
        sname = request.POST.get('name', False)
        result = list(student.objects.filter(name__contains=sname).order_by('-id'))
        return render(request,'namewise.html',{'result':result})
    return render(request,'namewise.html',{'result':result})

def result(request,id):
    name = student.objects.get(id = id)
    Dmarks = gpa.objects.get(sname=name)
    temp = float(Dmarks.sgpa)
    if temp > 8:
        color = "#52ff57"
    elif temp>6:
        color = "#fafa34"
    elif temp>4:
        color = "#f29c2c"
    else:
        color = "#f01313"
    data = list(marks.objects.filter(sname=name))
    return render(request,'result.html',{'Dmarks':Dmarks,'data':data,'color':color})

def branchwise(request):
    result = {}
    branch={}
    check = 0
    if request.method == 'POST':
        b = request.POST['branch']
        branch = b + " B.E - FY, Sem 2"
        check = 1
        result = list(gpa.objects.filter(branch = 'B.E - FY, Sem 2',sname__usn__contains=b).order_by('-sgpa'))
        return render(request,'branchwise.html',{'result':result,'branch':branch,'check':check})
    return render(request,'branchwise.html',{'result':result,'branch':branch,'check':check})

def missingusn(request):
    message = {}
    if request.method == 'POST':
        musn = request.POST.get('missingusn', False)
        smail = request.POST.get('email',False)
        message = 'Requested USN will be added to site soon'
        print(musn)
        temp = missing(usn = musn,mail = smail)
        temp.save()
        return render(request,'missingusn.html',{'message':message})
    return render(request,'missingusn.html',{'message':message})

def test(request):
    is6 = list(gpa.objects.filter(branch = 'B.E - CS, Sem 6').order_by('-cgpa'))
    return render(request,'test.html',{'res':is6})
















#
