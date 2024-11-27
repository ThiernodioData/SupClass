from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
# Pour les slugs qui servent à slugifier notre code python/django

# Create your models here.

# Table Niveau

class Niveau(models.Model):
nom = models.CharField(max_length=50) 
description = models.TextField() 
slug = models.SlugField(unique=True, blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.nom)
        super(Niveau, self).save(*args, **kwargs)

def __str__(self):
    return self.nom

# Table Matiere

class Matiere(models.Model):
nom = models.CharField(max_length=100) 
description = models.TextField() 
niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE) 
professeur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE) 
slug = models.SlugField(unique=True, blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.nom)
        super(Matiere, self).save(*args, **kwargs)

def __str__(self):
    return self.nom

# Table Salle

class Salle(models.Model):
nom = models.CharField(max_length=50) 
capacite = models.IntegerField() 
batiment = models.ForeignKey('Batiment', on_delete=models.CASCADE)
slug = models.SlugField(unique=True, blank=True) 

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.nom)
        super(Salle, self).save(*args, **kwargs)

def __str__(self):
    return self.nom

# Table Batiment

class Batiment(models.Model): 
nom = models.CharField(max_length=100) 
adresse = models.CharField(max_length=255) 
slug = models.SlugField(unique=True, blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.nom)
        super(Batiment, self).save(*args, **kwargs)

def __str__(self):
    return self.nom

# Table Utilisateur

class Utilisateur(models.Model):
    ROLE_CHOICES = [ 
        ('administrateur', 'Administrateur'),
        ('professeur', 'Professeur'),
        ('etudiant', 'Etudiant'),
        ('chef_classe', 'Chef de Classe'),
    ] 
nom = models.CharField(max_length=50)
prenom = models.CharField(max_length=50) 
email = models.EmailField(max_length=100, unique=True)
mot_de_passe = models.CharField(max_length=255) 
role = models.CharField(max_length=50, choices=ROLE_CHOICES)
date_creation = models.DateTimeField(auto_now_add=True) 
niveau_id = models.ForeignKey('Niveau', on_delete=models.CASCADE)
matricule = models.CharField(max_length=50, unique=True)
photo = models.ImageField(upload_to='photos/', blank=True, null=True)
slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(f'{self.nom}-{self.prenom}')
        super(Utilisateur, self).save(*args, **kwargs)

def __str__(self):
    return f'{self.nom} {self.prenom}'
        
# Table Notification
        
class Notification(models.Model):
    TYPE_NOTIFICATION_CHOICES = [
        ('general', 'General'),
        ('individuel', 'Individuel'),
        ('classe', 'Classe'),
        ('niveau', 'Niveau'),
    ]
utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)   
titre = models.CharField(max_length=100)
message = models.TextField()
type_notification = models.CharField(max_length=50, choices=TYPE_NOTIFICATION_CHOICES) 
date_creation = models.DateTimeField(auto_now_add=True)
lu = models.BooleanField(default=False)
slug = models.SlugField(unique=True, blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(f'{self.titre}-{self.date_creation}')
        super(Notification, self).save(*args, **kwargs)

def __str__(self):
    return f'Notification: {self.titre} pour {self.utilisateur.nom}'

# Table EmploiDuTemps

class EmploiDuTemps(models.Model):
niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE)
matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)
salle = models.ForeignKey('Salle', on_delete=models.CASCADE)
date = models.DateField() 
heure_debut = models.TimeField() 
heure_fin = models.TimeField() 
titre_lesson = models.CharField(max_length=100) 
contenu_lesson = models.TextField() 
duree_faite = models.TimeField() 
signature_prof = models.CharField(max_length=100) 
commentaire = models.TextField(null=True, blank=True) 
modifie_par = models.ForeignKey('Utilisateur', on_delete=models.CASCADE) 
ressource = models.FileField(upload_to='ressources/', blank=True, null=True)
assignation = models.BinaryField(upload_to='assignations/',null=True, blank=True) 
slug = models.SlugField(max_length=200,unique=True, blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(f'{self.titre_lesson}-{self.date}')
        super(EmploiDuTemps, self).save(*args, **kwargs)

def __str__(self):
    return f'{self.titre_lesson} ({self.date})'

# Table ReleveDeNote

class ReleveDeNote(models.Model):
utilisateur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)
note_cour = models.FloatField() 
note_examen = models.FloatField() 
moyenne = models.FloatField(default=0) 
commentaire = models.TextField(null=True, blank=True) 
date_ajout = models.DateTimeField(auto_now_add=True) 
slug = models.SlugField(unique=True, blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(f'{self.utilisateur.nom}-{self.matiere.nom}-{self.date_ajout}')
        super(ReleveDeNote, self).save(*args, **kwargs)

def __str__(self):
    return f'Relevé de notes pour {self.utilisateur.nom} en {self.matiere.nom}'

# Table Archive

class Archive(models.Model):
matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)
titre = models.CharField(max_length=100) 
contenu = models.TextField() 
ressource = models.BinaryField(upload_to='ressources/', blank=True, null=True)
assignation = models.BinaryField(upload_to='assignations/', blank=True, null=True)
date_archive = models.DateTimeField(auto_now_add=True) 
slug = models.SlugField(unique=True, blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(f'{self.titre}-{self.date_archive}')
        super(Archive, self).save(*args, **kwargs)

def __str__(self):
    return self.titre

# Table EspaceEchange

class EspaceEchange(models.Model):
niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE) 
contenu = models.TextField() 
date_message = models.DateTimeField(auto_now_add=True) 
auteur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE) 
slug = models.SlugField(unique=True, blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(f'{self.auteur.nom}-{self.date_message}')
        super(EspaceEchange, self).save(*args, **kwargs)

def __str__(self):
    return f'Message de {self.auteur.nom} ({self.date_message})'

# Table Message

class Message(models.Model): 
expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes') 
destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_recus') 
contenu = models.TextField() 
date_envoi = models.DateTimeField(auto_now_add=True) 
lu = models.BooleanField(default=False)
slug = models.SlugField(unique=True, blank=True) 

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(f'{self.expediteur.nom}-{self.destinataire.nom}-{self.date_envoi}')
        super(Message, self).save(*args, **kwargs)


def __str__(self):
    return f'Message de {self.expediteur.nom} à {self.destinataire.nom} ({self.date_envoi})'

# Table CahierAbsence

class CahierAbsence(models.Model): 
emploi_du_temps = models.ForeignKey('EmploiDuTemps', on_delete=models.CASCADE) 
utilisateur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE) 
present = models.BooleanField() 
date = models.DateField() 
note_absence = models.TextField(null=True, blank=True) 
slug = models.SlugField(unique=True, blank=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(f'{self.utilisateur.nom}-{self.date}')
        super(CahierAbsence, self).save(*args, **kwargs)


def __str__(self):
    return f'Absence de {self.utilisateur.nom} le {self.date}'