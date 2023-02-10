from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


class Review(models.Model):
    MovieTitle=models.TextField(default='no title')
    Title=models.CharField(max_length=20)
    Content=models.TextField()
    Rating=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    Date=models.DateTimeField(default=timezone.now)		#automatically get the time when saving something
    TheUser=models.CharField(default='no name',max_length=30)



    def __str__(self):		#will see title on the admin page
        return self.Title

