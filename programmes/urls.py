from django.urls import path
from programmes.views import *

app_name='programme'

urlpatterns = [
    # path('', connexiom, name='accueil'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('tableau_bord/', tableau_bord, name='tableau_bord'),
    
]
