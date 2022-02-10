from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import ModelForm

from .models import User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('name','email')
        labels = {'email': 'E-mail'}
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        first, *last = self.cleaned_data['name'].split(' ')
        user.name = first
        user.last_name = " ".join(last)
        
        if commit:
            user.save()
        return user


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone')


# class SignUpForm(ModelForm):

#     name = forms.CharField(max_length=30, required=False)
#     fone = forms.CharField(max_length=30, required=False)
#     email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
#     class Meta:
#         model = User
#         fields = (
#             'name', 
#             'email', 
#             'fone'
#         )
#     def save(self):
#         print("aq")
#         user = User()
#         user.email = self.cleaned_data["email"]
#         user.first_name = self.cleaned_data["name"]
#         user.
#         print('emailll')
#         return user

# class RegisterForm(UserCreateForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'email', 'fone')
#     name = forms.CharField(label='Nome', max_length=100)
#     email = forms.EmailField(label='E-mail', max_length=100)
#     phone = forms.CharField(label='Telefone', max_length=100, required=False)
#     # password = forms.PasswordInput(label='Senha')

#     def save(self, commit=True):
#         print("CHEGOU1")
#         user = super().save(commit=False)
#         print("CHEGOU2")
#         first_name = self.cleaned_data['name']
#         username = self.cleaned_data['email']
#         fone = self.cleaned_data['phone']
#         print("CHEGOU3")
#         user.set_password(self.cleaned_data["password1"])
#         print("CHEGOU4")
#         if commit:
#             user.save()
