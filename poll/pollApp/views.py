from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.permissions import AllowAny

from poll.pollApp.models import Poll, Question, Answer, UsersAnswers
from poll.pollApp.serializers import PollSerializer, QuestionSerializer, AnswerSerializer, UserSerializer, \
    UsersAnswersSerializer, RegisteredUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = RegisteredUserSerializer
    permission_classes = [AllowAny]

class PollViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UsersAnswersViewSet(viewsets.ModelViewSet):
    queryset = UsersAnswers.objects.all()
    serializer_class = UsersAnswersSerializer
