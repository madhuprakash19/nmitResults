from django.shortcuts import render
from nmit.models import student,gpa
# Create your views here.
def home(request):
    a = list(gpa.objects.filter(branch = 'B.E - IS, Sem 5'))
    return render(request,'home.html',{'a':a})
