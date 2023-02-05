from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=64)
    level = models.IntegerField()
    sentence = models.TextField(max_length=512)

    def __str__(self) -> str:
        return self.word
