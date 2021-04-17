from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Poll(models.Model):
    poll_name = models.CharField(max_length=100, null=False, blank=False)
    poll_description = models.CharField(max_length=100, null=False, blank=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='poll')


class Question(models.Model):
    question_description = models.CharField(max_length=200, null=False, blank=False)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions")


class UsersAnswers(models.Model):
    answer_date = models.DateTimeField()
    user_answers = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Answer(models.Model):
    answer_description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer")


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
