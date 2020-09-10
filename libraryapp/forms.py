from django import forms
from .models import Book ,Memberships
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude=['librarian',]
        # 'librarian']
        #fields = '__all__'


class MembershipsForm(forms.ModelForm):
    class Meta:
        model = Memberships
        fields = '__all__'
        #ordering=['name']
        #exclude = ['memberships',]


class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class SignupForm(forms.ModelForm):
    #email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }





#class SignupForm(UserCreationForm):
#    email = forms.EmailField(max_length=200, help_text='Required')
#    class Meta:
#        model = User
#        fields = ('username', 'email', 'password1', 'password2')
