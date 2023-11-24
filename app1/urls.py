from app1.views import *
from django.urls import path
app_name='hi'
urlpatterns=[
    path('balu/',balu,name='balu')
]