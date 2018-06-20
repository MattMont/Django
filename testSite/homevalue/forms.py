from django import forms
from .models import Homeinfo
from dal import autocomplete
from django.urls import reverse_lazy

class ValueForm(forms.Form):
    addy = forms.CharField(label="",initial="Address",max_length=100)

class valAutoForm(forms.ModelForm):
    Address = forms.ModelChoiceField(
        queryset=Homeinfo.objects.all(),
        widget=autocomplete.ModelSelect2(url='homeAutoComplete')
        )
    class Meta:
        model = Homeinfo
        fields = ('address',)

# Another Form Test
class valAuto(forms.ModelForm):
    class Meta:
        model = Homeinfo
        fields = ('address',)
        widgets = {
            'address': autocomplete.ListSelect2(url='homeAutoComplete')
        }
