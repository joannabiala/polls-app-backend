from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Poll(models.Model):
    poll_name = models.TextField()
    poll_description = models.TextField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class UsersAnswers(models.Model):
    answer_date = models.DateTimeField()
    user_answers = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Question(models.Model):
    question_description = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Answer(models.Model):
    answer_description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
