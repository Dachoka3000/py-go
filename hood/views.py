from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'hood/home.html')

def about(request):
    return render(request,'hood/about.html')

# def addprofile(request):
#     home=form-cleaned_data(neighbourhood)
        # prohome=Hood.objects.get(name=home)
        # hood=prohome
