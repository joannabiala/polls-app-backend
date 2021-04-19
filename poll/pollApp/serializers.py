from django.contrib.auth.models import User, Group
from rest_framework import serializers

from poll.pollApp.models import Poll, UsersAnswers, Question, Answer


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


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_description']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_description', 'answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)
        return question


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ['id', 'poll_name', 'poll_description', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        poll = Poll.objects.create(**validated_data)
        for question_data in questions_data:
            question_serializer = QuestionSerializer(data=question_data)
            question_serializer.is_valid()
            question_serializer.save(poll=poll)
        return poll


class UsersAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersAnswers
        fields = ['id', 'answer_date', 'user_answers']
