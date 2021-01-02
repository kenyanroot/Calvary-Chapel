from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    phone = forms.CharField(label='Your name', max_length=100,widget=forms.TextInput( attrs={'class': 'form-control'}))

    # first_name=forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'})),
    # last_name= forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'})),
    # password1= forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control'})),
    # password2= forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control'})),
    # file = forms.FieldField(widget=forms.FileInput(attrs={'class': 'rounded_list'}))


    class Meta:
        model = User
        fields = ('email','first_name', 'last_name','password')


        widgets = {

            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }