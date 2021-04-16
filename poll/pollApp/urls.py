from rest_framework import routers
from django.urls import path, include

from poll.pollApp import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, basename="user")
router.register(r'poll', views.PollViewSet, basename="tasks")
router.register(r'question', views.QuestionViewSet, basename="list")
router.register(r'answer', views.AnswerViewSet, basename='answer')
router.register(r'usersanswers', views.UsersAnswersViewSet, basename='usersanswers')
router.register(r'registration', views.RegistrationViewSet, basename='registration')


urlpatterns = [
    path('', include(router.urls)),
]
