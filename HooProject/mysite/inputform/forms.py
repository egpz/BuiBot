from django import forms

# Create the form the user will enter their code in 
class InputForm(forms.Form):
    input_code = forms.CharField(widget=forms.Textarea(attrs={'class':'centered'}))


