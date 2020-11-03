from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('addprofile/',views.addprofile,name='addprofile'),
    path('profile/',views.profile,name='profile'),
    path('addbusiness/',views.addbusiness,name='addbusiness'),
    path('business/',views.business,name='business'),
    path('searchbusiness/',views.filterbusiness, name='searchbusiness'),
    path('posts/<int:hood_id>/',views.posts, name='posts'),
    path('addposts/<int:hood_id>/',views.addpost,name='addpost'),
    path('contacts/<int:hood_id>/',views.hoodcontacts,name='contacts'),
    path('local/', views.onlylocal, name='local'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)