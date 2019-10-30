from rest_framework import generics, status
from api.models import Question, Profile, Stand, StandDescription
from api.serializers import *
from rest_framework.response import Response
from api.models import Profile

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view

class QuestionsList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class StandList(generics.ListAPIView):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer
    
    def get_queryset(self):
        owner_id = self.kwargs.get('user_id')
        stands = Stand.objects.filter(owner__id=owner_id)
        return stands

class StandAdd(generics.ListCreateAPIView):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer


class ProfileUpdate(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, format=None):
        profile = Profile.objects.get(username=request.data['username'])
        profile.age = request.data['age']
        profile.name = request.data['name']
        profile.knowledge = request.data['knowledge']
        profile.save()
        return Response(status=status.HTTP_200_OK)

class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        username = self.kwargs.get('username')
        user = Profile.objects.filter(username=username).first()
        return user

class StandDescriptionAdd(generics.ListCreateAPIView):
    queryset = StandDescription.objects.all()
    serializer_class = AddDescriptionSerializer

class StandDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StandDescription.objects.all()
    serializer_class = StandDescriptionSerializer

    def get_object(self):
        stand_id = self.kwargs.get('stand')
        knowledge_id = self.kwargs.get('knowledge')
        description = StandDescription.objects.filter(stand__id=stand_id, knowledge=knowledge_id).first()
        return description