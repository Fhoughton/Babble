from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f'Account successfully registered.')
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form": form})

@login_required
def profile(request):
    if request.method == 'POST':
        userupdateform = UserUpdateForm(request.POST,instance=request.user)
        profileupdateform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if userupdateform.is_valid and profileupdateform.is_valid:
            userupdateform.save()
            profileupdateform.save()
            messages.success(request,f'Account successfully updated.')
            return redirect("Profile")

    else:
        userupdateform = UserUpdateForm(instance=request.user)
        profileupdateform = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'userupdateform' : userupdateform,
        'profileupdateform' : profileupdateform,
    }
    return render(request, 'users/profile.html', context)
