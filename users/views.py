from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationFrom, UserUpdateForm


def register(request):
    if request.method == "POST":

        form = UserRegistrationFrom(request.POST)

        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был создан, введите имя пользователя и пароль для авторизации')
            return redirect('user')
    else:
        form = UserRegistrationFrom()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    if request.method == "POST":
        update_user = UserUpdateForm(data=request.POST, instance=request.user)

        print(request.user.profile)
        if update_user.is_valid():
            update_user.save()

            messages.success(request, f'Ваш аккаунт юыл успешно обновлен')
            return redirect('profile')

    else:
        update_user = UserUpdateForm(instance=request.user)

    context = {
        'title': 'Профиль пользователя ' + str(request.user).title(),
        'update_user': update_user,
    }

    return render(request, 'users/profile.html', context=context)
