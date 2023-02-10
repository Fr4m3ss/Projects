from django import forms
from .models import Review
from django.core.validators import MaxValueValidator,MinValueValidator

from movies.models import Movie


movies=[]
for movie in Movie.objects.all():
    movies.append((movie.Title,movie.Title))	#requires weird tuple form like this


class ReviewForm(forms.ModelForm):
    MovieTitle=forms.CharField(label='Select Movie',widget=forms.Select(choices=movies) )
    Title=forms.CharField()
    Content=forms.CharField()
    Rating=forms.IntegerField()
    class Meta:
        model = Review
        fields=['MovieTitle','Title','Content','Rating']		#These are what will make everything save corectly-not what's shown on screen
