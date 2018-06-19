from django import forms
from .models import Homeinfo
from dal import autocomplete

class ValueForm(forms.Form):
    addy = forms.CharField(label="",initial="Address",max_length=100)

class valAutoForm(forms.ModelForm):
    theAddy = forms.ModelChoiceField(
        queryset=Homeinfo.objects.all(),
        widget=autocomplete.ModelSelect2(url='Homeinfo')
        )
    class Meta:
        model = Homeinfo
        fields = ('address',)
