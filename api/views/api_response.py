from rest_framework import generics
from api.models import Question, Profile, Stand, StandDescription
from api.serializers import *
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

class StandDetail(generics.ListCreateAPIView):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        username = self.kwargs.get('username')
        user = Profile.objects.filter(username=username).first()
        return user

class StandDescriptionList(generics.ListCreateAPIView):
    queryset = StandDescription.objects.all()
    serializer_class = StandDescriptionSerializer

class StandDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StandDescription.objects.all()
    serializer_class = StandDescriptionSerializer

    def get_object(self):
        stand_id = self.kwargs.get('stand')
        knowledge_id = self.kwargs.get('knowledge')
        description = StandDescription.objects.filter(stand__id=stand_id, knowledge=knowledge_id).first()
        return description