from django.urls import path
from programme.views import *

app_name='programme'

urlpatterns = [
    # path('', home, name='accueil'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('tableau_bord/', tableau_bord, name='tableau_bord'),
    
]
