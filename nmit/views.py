from django.shortcuts import render
from nmit.models import student,gpa
# Create your views here.
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

def aboutus(request):
    return render(request,'aboutus.html')

def namewise(request):
    result = {}
    if request.method == 'POST':
        sname = request.POST.get('name', False)
        result = list(student.objects.filter(name__contains=sname))
        print(result)
        return render(request,'namewise.html',{'result':result})
    return render(request,'namewise.html',{'result':result})

def result(request,id):
    name = student.objects.get(id = id)
    marks = gpa.objects.get(sname=name)
    return render(request,'result.html',{'marks':marks})
