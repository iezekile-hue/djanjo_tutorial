from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-input'}))