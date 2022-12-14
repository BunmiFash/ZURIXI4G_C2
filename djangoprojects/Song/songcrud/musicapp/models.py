
from django.db import models
import datetime
# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField(default=datetime.date.today)
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)    

    def __str__(self):
        return self.song_id