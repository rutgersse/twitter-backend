from django import forms

class keyword(forms.Form):
    word = forms.CharField( label='Enter the keyword', max_length=100 )