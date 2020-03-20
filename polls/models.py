import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
    # Field ↓        Model↓
    question_text = models.CharField(max_length=500)
    def __str__(self):
        return self.question_text

    # Field ↓          ↓Model
    published_date = models.DateTimeField('Date Published')

    def published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date <= now


class Choice(models.Model):
    # more info regarding field options
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    # subclass of Models
    # https://docs.djangoproject.com/en/3.0/ref/models/instances/#django.db.models.Model
    # Field↓     ↓Model
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Field↓      Model↓
    choice_text = models.CharField(max_length=450)

    def __str__(self):
        return self.choice_text

    # ↓Field ↓Model
    votes = models.IntegerField(default=0)

