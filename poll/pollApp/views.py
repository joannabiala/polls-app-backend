from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from poll.pollApp.models import Poll, Question, Answer, UsersAnswers
from poll.pollApp.serializers import PollSerializer, QuestionSerializer, AnswerSerializer, UserSerializer, \
    UsersAnswersSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UsersAnswersViewSet(viewsets.ModelViewSet):
    queryset = UsersAnswers.objects.all()
    serializer_class = UsersAnswersSerializer
