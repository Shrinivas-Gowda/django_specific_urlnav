from django.shortcuts import render

# Create your views here.

def gettable1(request):
    return render(request,'table1.html')
