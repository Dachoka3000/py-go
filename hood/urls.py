from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('addprofile/',views.addprofile,name='addprofile'),
    path('profile/',views.profile,name='profile'),
    path('addbusiness/',views.addbusiness,name='addbusiness'),
    path('business/',views.business,name='business'),
]