from django.urls import path
from programme.views import *

app_name='programmes'
urlpatterns=[
    path('',home,name='home'),
]