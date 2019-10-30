from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from django.urls import path


urlpatterns = [
    #User
    path('auth/login/', obtain_auth_token, name='auth_user_login'),
    path('auth/register/', CreateUserAPIView.as_view(), name='auth_user_create'),
    path('auth/logout/', LogoutUserAPIView.as_view(),name='auth_user_logout'),
    path('user/<str:username>/', ProfileDetail.as_view(),name='user-detail'),
    #Questions
    path('questions/', QuestionsList.as_view(),name='questions_list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(),name='question-detail'),
    #Stands
    path('stands/list/<int:user_id>', StandList.as_view(),name='stand_list'),
    path('stands/', StandAdd.as_view(),name='stand-add'),
    #StandDescriptions
    path('descriptions/', StandDescriptionAdd.as_view(),name='descriptions_add'),
    path('descriptions/<int:stand>/<int:knowledge>/', StandDescriptionDetail.as_view(),name='description-detail'),
]

