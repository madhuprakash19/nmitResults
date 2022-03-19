from django.shortcuts import render
from nmit.models import student,gpa
# Create your views here.
def home(request):
    topper5 = list(gpa.objects.order_by('-sgpa')[:10:1])
    is5 = list(gpa.objects.filter(branch = 'B.E - IS, Sem 5').order_by('-sgpa')[:10:1])
    cs = list(gpa.objects.filter(branch = 'B.E - CS, Sem 5').order_by('-sgpa')[:10:1])
    ec = list(gpa.objects.filter(branch = 'B.E - EC, Sem 5').order_by('-sgpa')[:10:1])
    me = list(gpa.objects.filter(branch = 'B.E - ME, Sem 5').order_by('-sgpa')[:10:1])
    ae = list(gpa.objects.filter(branch = 'B.E - AE, Sem 5').order_by('-sgpa')[:10:1])
    ee = list(gpa.objects.filter(branch = 'B.E - EE, Sem 5').order_by('-sgpa')[:10:1])
    return render(request,'home.html',{'topper5':topper5,'is5':is5,'cs':cs,'ec':ec,'me':me,'ae':ae,'ee':ee})
