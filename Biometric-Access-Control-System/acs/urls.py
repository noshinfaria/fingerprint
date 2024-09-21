# from django.urls import path

# from . import views
# app_name = 'acs'

# urlpatterns = [
#     # Ex: localhost:7000
#     # path('', views.index, name='index'),

#     # Ex: localhost:7000/auth
#     path('', views.auth, name='auth'),

#     # Ex: localhost:7000/develop
#     path('develop/', views.develop, name='develop'),
# ]

from django.urls import path
from . import views

app_name = 'acs'

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('develop/', views.develop, name='develop'),
]

