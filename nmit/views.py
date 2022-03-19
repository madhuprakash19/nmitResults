from django.shortcuts import render
from nmit.models import student,gpa
# Create your views here.
def home(request):
    topper5 = list(gpa.objects.order_by('-sgpa')[:10:1])
    is5 = list(gpa.objects.filter(branch = 'B.E - IS, Sem 5').order_by('-sgpa')[:10:1])
    cs5 = list(gpa.objects.filter(branch = 'B.E - CS, Sem 5').order_by('-sgpa')[:10:1])
    ec5 = list(gpa.objects.filter(branch = 'B.E - EC, Sem 5').order_by('-sgpa')[:10:1])
    me5 = list(gpa.objects.filter(branch = 'B.E - ME, Sem 5').order_by('-sgpa')[:10:1])
    ae5 = list(gpa.objects.filter(branch = 'B.E - AE, Sem 5').order_by('-sgpa')[:10:1])
    ee5 = list(gpa.objects.filter(branch = 'B.E - EE, Sem 5').order_by('-sgpa')[:10:1])
    cv5 = list(gpa.objects.filter(branch = 'B.E - CV, Sem 5').order_by('-sgpa')[:10:1])
    return render(request,'home.html',{'topper5':topper5,'is5':is5,'cs5':cs5,'ec5':ec5,'me5':me5,'ae5':ae5,'ee5':ee5,'cv5':cv5})

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
