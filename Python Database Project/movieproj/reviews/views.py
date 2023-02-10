from django.shortcuts import render,redirect
from .form import ReviewForm
from django import forms
from django.contrib.auth.models import User
from movies.models import Movie
from django.contrib.auth.decorators import login_required

@login_required    #decorator used so someone can't just enter in the url of this and have acces-sends them to login screen if they try
def LeaveReview(request):
    model=Movie
    if request.method=='POST':
        form=ReviewForm(request.POST)
        form.instance.TheUser=request.user	#setting user to currently logged in user

        if form.is_valid():			#django performs checks for you with this
            form.save()      			#automatically saves the 
            return redirect('movie-home')

    else:
        form=ReviewForm()

    return render(request,'reviews/review.html',{'form': form})
