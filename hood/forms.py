from django import forms
from .models import Profile,Post,Business
from cloudinary.forms import CloudinaryFileField

class AddProfileForm(forms.ModelForm):
    avatar= CloudinaryFileField(
        options = {
            'crop':'thumb',
            'width':200,
            'height':200,
            'folder':'avatars'
        },
        required=False
    )
    class Meta:
        model=Profile
        exclude=('user',)

class AddBusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner']

class AddPostForm(forms.ModelForm):
    image= CloudinaryFileField(
        options = {
            'crop':'thumb',
            'width':300,
            'height':300,
            'folder':'avatars'
        },
        required=False
    )
    class Meta:
        model=Post
        exclude=['poster']

class ChangeLocationForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['hood']
        

