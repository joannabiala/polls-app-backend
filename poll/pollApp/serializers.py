from django.contrib.auth.models import User, Group
from rest_framework import serializers

from poll.pollApp.models import Poll, UsersAnswers


class RegisteredUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'required': True, 'read_only': True}}
        owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}
        owner = serializers.ReadOnlyField(source='owner.email')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'poll_name', 'poll_description']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'question_description']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'answer_description']


class UsersAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersAnswers
        fields = ['id', 'answer_date', 'user_answers']
