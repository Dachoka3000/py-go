from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User
from .forms import AddProfileForm
from cloudinary.forms import cl_init_js_callbacks      


# Create your views here.
def homepage(request):
    
    return render(request,'hood/home.html')

def about(request):
    return render(request,'hood/about.html')

@login_required(login_url='login')
def addprofile(request):
    current_user=request.user

    if request.method=="POST":
        form = AddProfileForm(request.POST,request.FILES)
        if form.is_valid():
           new_profile= form.save(commit=False)
           new_profile.user=current_user
           new_profile.save()
           return redirect('profile')
    else:
        form=AddProfileForm()
    return render(request, 'hood/addprofile.html',{"form":form})
            

# def addprofile(request):
#     home=form-cleaned_data(neighbourhood)
        # prohome=Hood.objects.get(name=home)
        # hood=prohome
