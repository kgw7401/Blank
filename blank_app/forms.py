from django import forms
from django.db.models import fields
from .models import  BlankContent

class BlankContentCreateForm(forms.ModelForm):
    class Meta:
        model = BlankContent
        fields = "__all__"
        widgets = {'new_blank': forms.HiddenInput}

class BlankContentUpdateForm(forms.ModelForm):
    class Meta:
        model = BlankContent
        fields = "__all__"
        widgets = {'new_blank': forms.HiddenInput}
