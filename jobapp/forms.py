from .models import JobAdvert
from django import forms




class JobAdvertForm(forms.ModelForm):
    class Meta:
        model = JobAdvert
        fields = '__all__'
