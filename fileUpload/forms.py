from django import forms
from fileUpload.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields="__all__"
        
