from django.shortcuts import render,redirect
from .form import RegistrationForm	       #created this
from django.contrib.auth.decorators import login_required


def registration(request):
    if request.method=='POST':
                #No csrf token required here
        form=RegistrationForm(request.POST)
        if form.is_valid():	#django performs checks for you with this
            form.save()         #automatically saves the user
            return redirect('movie-home')

    else:				#we go to this when we are registering for first time, actually on registration page, then when submit the post happens
        form=RegistrationForm()

    return render(request,'users/registration.html',{'form': form})

