from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User
from .forms import AddProfileForm,AddBusinessForm,AddPostForm
from .models import Profile,Post,Business,Hood,Contact
from cloudinary.forms import cl_init_js_callbacks      
from .filters import BusinessFilter

# Create your views here.
def homepage(request):
    hoods = Hood.objects.all()
    return render(request,'hood/home.html', {"hoods":hoods})

def about(request):
    return render(request,'hood/about.html')

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    businesses = Business.objects.filter(owner=current_user)
    posts = Post.objects.filter(poster=current_user)
    return render(request,'hood/profile.html',{"current_user":current_user,"profile":profile,"businesses":businesses,"posts":posts})

@login_required(login_url='/accounts/login/')
def addbusiness(request):
    current_user=request.user

    if request.method=="POST":
        form=AddBusinessForm(request.POST)
        if form.is_valid():
            new_business=form.save(commit=False)
            new_business.owner=current_user
            new_business.save()
            return redirect('business')
    else:
        form=AddBusinessForm()
    return render(request,'hood/addbusiness.html',{"current_user":current_user,"form":form})

@login_required(login_url='/accounts/login/')
def business(request):
    businesses=Business.objects.all()
    return render(request,'hood/business.html', {"businesses":businesses})

@login_required(login_url='/accounts/login/')
def filterbusiness(request):
    if request is None:
        return Business.objects.none()
    filter_list = Business.objects.all()
    business_filter = BusinessFilter(request.GET, queryset=filter_list)
    return render(request,'hood/searchbusiness.html',{"filter":business_filter})

@login_required(login_url='/accounts/login/')
def posts(request,hood_id):
    hood=Hood.objects.get(id=hood_id)
    postups=hood.posts.all()
    return render(request, 'hood/postarea.html',{"hood":hood,"postups":postups})

@login_required(login_url='/accounts/login/')
def addpost(request,hood_id):
    hood = Hood.objects.get(id=hood_id)
    current_user=request.user
    form=AddPostForm()

    if request.method == 'POST':
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.area = hood
            new_post.poster=current_user
            new_post.save()
            return redirect('posts')
        else:
            form=AddPostForm()
    return render(request, 'hood/addpost.html',{"form":form,"hood":hood,"current_user":current_user})


            

# def addprofile(request):
#     home=form-cleaned_data(neighbourhood)
        # prohome=Hood.objects.get(name=home)
        # hood=prohome
