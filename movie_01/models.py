from django.db import models


class movies01(models.Model):
    # dropdown_choices = (
    #     ('option1', '1'),
    #     ('option2', '2'),
    #     ('option3', '3'),
    #     ('option4', '4'),
    #     ('option5', '5')
    # )
    Title = models.CharField(max_length=30)
    Poster = models.ImageField()
    Genre = models.CharField(max_length=20)
    Year = models.DateField()
    Release = models.DateField()
    Metacritic = models.CharField(max_length=20)
    Rating = models.FloatField()
    # Rate = models.CharField(max_length=5, choices=dropdown_choices)
    Runtime = models.CharField(max_length=20)
