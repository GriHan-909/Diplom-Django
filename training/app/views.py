from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister, UserLogin
from .models import User

# Create your views here.
def log_in(request):
    emails =tuple(item.email for item in User.objects.all())
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            info = {}
            context = {'info': info, 'form': form}
            if email in emails:
                user = User.objects.get(email=email)
                if password==user.password and email==user.email:
                    return render(request, 'base_page.html')
                elif password != user.password:
                    info['error'] = 'Пароль не верный'
                    return render(request,'log_in.html', context)
                elif email != user.email:
                    info['error'] = 'Email не верный'
                    return render(request, 'log_in.html', context)
            else:
                info['error'] = 'Email не верный'
                return render(request, 'log_in.html', context)
    else:
        form = UserLogin()
    return render(request, 'log_in.html', {'form': form})

def sign_up_by_django(request):
    users = User.objects.all()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info = {}
            context = {'info': info, 'form': form}
            if password==repeat_password and age > 14 and email not in users:
                User.objects.create(email=email, password=password, age=age)
                return render(request,'base_page.html')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request,'registration.html', context)
            elif int(age) < 14:
                info['error'] = 'Вы должны быть старше 14'
                return render(request, 'registration.html', context)
            elif email in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration.html', context)
    else:
        form = UserRegister()
    return render(request, 'registration.html', {'form': form})


# def sign_up_by_html(request):
#     users = ['Gregory', 'Alex', 'Anna', 'Victor']
#     info = {}
#     context = {
#         'info': info
#     }
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = request.POST.get('age')

#         if password==repeat_password and int(age) > 18 and username not in users:
#             return HttpResponse(f'Приветствуем, {username}!')
#         elif password != repeat_password:
#             info['error'] = 'Пароли не совпадают'
#             return render(request, 'app/registration.html', context)
#         elif int(age) < 18:
#             info['error'] = 'Вы должны быть старше 18'
#             return render(request, 'app/registration.html', context)
#         elif username in users:
#             info['error'] = 'Пользователь уже существует'
#             return render(request, 'app/registration.html', context)


#     else:
#         return render(request, 'app/registration.html')