from django.shortcuts import render, redirect
from .forms import UserRegister, UserLogin, UserProfileForm
from .models import User, UserProfile

user_inner = {}

# Create your views here.
def log_in(request):
    global user_inner
    user_inner = {}
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
                    user_inner['email'] = email
                    user_inner['used'] = True
                    return redirect('base_page/')
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
    emails =tuple(item.email for item in User.objects.all())
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            info = {}
            context = {'info': info, 'form': form}
            if password==repeat_password and email not in emails:
                User.objects.create(email=email, password=password)
                UserProfile.objects.create(email=email)
                return redirect(log_in)
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request,'registration.html', context)
            elif email in emails:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration.html', context)
    else:
        form = UserRegister()
    return render(request, 'registration.html', {'form': form})


def profile_view(request):
    if user_inner and user_inner['used']:
        user_profile = UserProfile.objects.get(email=user_inner['email'])
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                context = {'user_profile': user_profile, 'form': form, 'success': 'Изменения сохранены!'}
                name = form.cleaned_data['name']
                last_name = form.cleaned_data['last_name']
                age = form.cleaned_data['age']

                user_profile.name = name
                user_profile.last_name = last_name
                user_profile.age = age
                user_profile.save()
                return render(request, 'profile.html', context)
        else:
            form = UserProfileForm()
            context = {'user_profile': user_profile, 'form': form}
            return render(request, 'profile.html', context)
    else:
         return redirect(log_in)
