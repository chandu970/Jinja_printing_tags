from django.shortcuts import render

# Create your views here.
def RC(request):
    D={'Hero':'Ramcharan','AHero':'NTR'}
    return render(request,'Ram.html',context=D)