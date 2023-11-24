from app2.views import *
from django.urls import path
app_name='bye'
urlpatterns=[
    path('venky/',venky,name='venky')
]