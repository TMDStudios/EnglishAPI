from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=64)
    level = models.IntegerField()
    sentence = models.TextField(max_length=512)
    regular = models.CharField(max_length=8, null=True)
    conjugation = models.CharField(max_length=64, null=True)

    def __str__(self) -> str:
        return self.word

class Time(models.Model):
    name = models.CharField(max_length=64)
    time = models.IntegerField()
    level = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
class Mistake(models.Model):
    word = models.CharField(max_length=64)
    issue = models.TextField(max_length=1023)
    author = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.word
    
class BannerClick(models.Model):
    banner = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.banner
    
class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    app_store = models.CharField(max_length=255, unique=True, null=True, blank=True)
    google_play = models.CharField(max_length=255, unique=True, null=True, blank=True)
    video = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    approved = models.SmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.app_store == None or self.app_store == "None" or self.app_store == "":
            self.app_store = str(Game.objects.last().pk+1)
        if self.google_play == None or self.google_play == "None" or self.google_play == "":
            self.google_play = str(Game.objects.last().pk+1)
        super(Game, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name