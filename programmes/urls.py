from django.urls import path
from programmes.views import *

app_name = 'programme'

urlpatterns = [
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('tableau_bord/', tableau_bord, name='tableau_bord'),
    path('utilisateur/', utilisateur, name='utilisateur'),
    path('niveau/', niveau, name='niveau'),
    path('matiere/', matiere, name='matiere'),
    path('batiment/', batiment, name='batiment'),
    path('emargements/', emargements, name='emargements'),
    path('addnote/', addnote, name='addnote'),
    path('shownote/', shownote, name='shownote'),
    path('salles/', salles, name='salles'),
    path('liste_absences/', liste_absences, name='liste_absences'),
    path('espace-echange/<slug:niveau_slug>/',espace_echange, name='espace_echange'),
    path('emplois_du_temps/', emplois_du_temps, name='emplois_du_temps'),
]