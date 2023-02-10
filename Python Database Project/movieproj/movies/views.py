from django.shortcuts import render

from .models import Movie
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from reviews.models import Review


class MovieListView(LoginRequiredMixin,ListView):	#LoginRequiredMixin used to sent someone to login screen if they arent logged in and try to manually enter a url
    model=Movie
    template_name='movies/moviehome.html'
    context_object_name='movies'

class MovieDetailView(LoginRequiredMixin,DetailView):
    model=Movie

    def get_context_data(self,*args,**kwargs):				#using this fxn to put data in html file
        context=super(MovieDetailView,self).get_context_data(*args,**kwargs)
        TheReviews=[]
        for rev in Review.objects.all():			#only adding the reviews for that given movie
            if rev.MovieTitle==str(context['object']):
                TheReviews.append(rev)


        context['TheReviews']=TheReviews
        return context
