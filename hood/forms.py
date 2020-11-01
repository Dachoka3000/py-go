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
        

