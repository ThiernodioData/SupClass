from django.urls import path
from programmes.views import *

app_name = 'programme'

urlpatterns = [
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('tableau_bord/', tableau_bord, name='tableau_bord'),
    path('eleves/', eleves, name='eleves'),
    path('enseignants/', enseignants, name='enseignants'),
    path('cours/', cours, name='cours'),
    path('emargements/', emargements, name='emargements'),
    path('notes/', notes, name='notes'),
    path('salles/', salles, name='salles'),
    path('classe/', classe, name='classe'),
    path('emplois_du_temps/', emplois_du_temps, name='emplois_du_temps'),
]