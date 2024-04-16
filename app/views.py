from django.shortcuts import render, redirect

from .models import Users

def home(request):
    return render(request, 'users/home.html')

def users(request):
    if request.method == 'POST':
        newUser = Users()
        newUser.name = request.POST.get('name', newUser.name)
        newUser.email = request.POST.get('email', newUser.email)
        newUser.save()

    users = {
        'users': Users.objects.all()
    }
    return render(request, 'users/users.html', users)

def delete_user(request, user_id):
    user = Users.objects.get(pk=user_id)
    user.delete()
    return redirect('users')
