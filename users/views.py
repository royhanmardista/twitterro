from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
# navigation guard in vue
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'GET' :
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form' : form})
    elif request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account is created, you are now able to login')
            return redirect('login')
        else :
            return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request) : 
    return render(request, 'users/profile.html')