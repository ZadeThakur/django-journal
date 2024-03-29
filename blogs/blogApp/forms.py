from django import forms
from django.contrib.auth.models import User
from blogApp.models import userModel, journalModel

class FormName(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email','password')
    
class journalForm(forms.ModelForm):

    class Meta():
        model=journalModel
        fields=('userId','datetime','journalEntry')