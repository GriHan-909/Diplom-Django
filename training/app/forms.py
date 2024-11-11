from django import forms



class UserLogin(forms.Form):
    email = forms.CharField(max_length=30, label='Введите email')
    password = forms.CharField(max_length=15, label='Введите пароль')


class UserRegister(forms.Form):
    email = forms.CharField(max_length=30, label='Введите email')
    password = forms.CharField(max_length=15, label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.IntegerField(max_value=101, label='Введите свой возраст')

