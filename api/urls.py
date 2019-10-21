from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from django.urls import path


urlpatterns = [
    #User
    path('auth/login/', obtain_auth_token, name='auth_user_login'),
    path('auth/register/', CreateUserAPIView.as_view(), name='auth_user_create'),
    path('auth/logout/', LogoutUserAPIView.as_view(),name='auth_user_logout'),
    #Questions
    path('questions/', QuestionsList.as_view(),name='questions_list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(),name='question-detail'),
    #Stands
    path('stands/', StandList.as_view(),name='stand_list'),
    path('stands/<int:pk>/', StandDetail.as_view(),name='stand-detail'),
    #StandDescriptions
    path('descriptions/', StandDescriptionList.as_view(),name='descriptions_list'),
    path('descriptions/<int:stand>/<int:knowledge>/', StandDescriptionDetail.as_view(),name='description-detail'),
]

