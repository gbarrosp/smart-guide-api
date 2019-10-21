from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Question, Profile, Stand, StandDescription

class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class StandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stand
        fields = '__all__'

class StandDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StandDescription
        fields = '__all__'