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