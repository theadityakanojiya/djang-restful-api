from django.urls import path
from.views import allUsers,addUser,userDetail


urlpatterns =[
    path('users/', allUsers, name='allUser'),
    path('users/create', addUser, name='addUser'),
    path('users/<int:pk>', userDetail, name='userDetail'),
] 