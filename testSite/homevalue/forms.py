from django import forms

class ValueForm(forms.Form):
    addy = forms.CharField(label="",initial="Address",max_length=100)
