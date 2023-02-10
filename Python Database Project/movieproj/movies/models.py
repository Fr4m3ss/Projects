from django.db import models

class Movie(models.Model):
    Title=models.CharField(max_length=50)
    Synopsis=models.TextField()
    Imageurl=models.TextField()

    def __str__(self):
        return self.Title

