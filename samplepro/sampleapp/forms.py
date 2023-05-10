from django import forms
from . models import PersonalDetails
class personForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = '__all__'