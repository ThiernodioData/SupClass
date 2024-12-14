from django.contrib import admin

from .models import Niveau, Matiere, Salle, Batiment, Utilisateur, Notification,EmploiDuTemps, ReleveDeNote, Archive, EspaceEchange, Message, CahierAbsence

admin.site.register(Niveau)
admin.site.register(Matiere)
admin.site.register(Salle)
admin.site.register(Batiment)
admin.site.register(Utilisateur)
admin.site.register(Notification)
admin.site.register(EmploiDuTemps)
admin.site.register(ReleveDeNote)
admin.site.register(Archive)
admin.site.register(EspaceEchange)
admin.site.register(Message)
admin.site.register(CahierAbsence)
