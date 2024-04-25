from django import forms
from django.contrib.auth.models import User
from todoapp.models import todoModel

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model=todoModel
        fields=['task','description']

class TodoEditForm(forms.ModelForm):
    class Meta:
        model=todoModel
        fields=['task','description','status']
        widgets={
            'task':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'})
        }

    
    