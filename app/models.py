from django.db import models
from django import forms

## Create your models here.

def validate_name(value):
    if value[0].lower()=='a':
        raise forms.ValidationError("Should not start with a")


def validate_length(value):
    if len(value)<5:
        raise forms.ValidationError("length should be greaterthan 5")


class Topic(models.Model):
    topic_name  = models.CharField(max_length=100, primary_key=True, validators=[validate_name,validate_length])

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name  = models.ForeignKey(Topic, on_delete=models.CASCADE, validators=[validate_name,validate_length])
    name = models.CharField(max_length=100, primary_key=True, validators=[validate_name,validate_length])
    url = models.URLField()

    def __str__(self):
        return self.name

class Access_Record(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE, validators=[validate_name,validate_length])
    date = models.DateField()
    author = models.CharField(max_length=100, validators=[validate_name,validate_length])

    def __str__(self):
        return self.author



