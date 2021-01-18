from django import forms
class MyForm(forms.Form):
    date = forms.DateField( validators=[present_or_future_date])