from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
# Create your models here.


# Table User 
class Utilisateur(AbstractUser):
    ROLES = (
        ('administrateur' , 'Administrateur'),
        ('enseignant', 'Enseignant'),
        ('etudiant', 'Etudiant'),
        ('chef_classe', 'Chef de Classe')
    )

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLES)
    date_creation = models.DateTimeField(auto_now_add=True)
    niveau_id = models.ForeignKey('Niveau', on_delete=models.CASCADE)
    matricule = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.nom}-{self.prenom}-{self.matricule}')
            super().save(*args, **kwargs)

# Class EmploisDuTemps      
class EmploiDuTemps(models.Model):
    niveau_id = models.ForeignKey('Niveau', on_delete=models.CASCADE)
    matiere_id = models.ForeignKey('Matiere', on_delete=models.CASCADE)
    salle_id = models.ForeignKey('Salle', on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    titre_lesson = models.CharField(max_length=100)
    contenu_lesson = models.TextField()
    duree_faite = models.TimeField()
    signature_prof = models.CharField(max_length=100)
    commentaire = models.TextField()
    modifier_par = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    ressource = models.FileField(upload_to='ressources/', blank=True, null=True)
    affectation = models.FileField(upload_to='affectations/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.niveau_id}-{self.date}-{self.heure_debut}')
        super().save(*args, **kwargs)


# models MATIERE

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    niveau_id = models.ForeignKey('Niveau', on_delete=models.CASCADE)
    professeur_id = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

# Modele Salle 

class Salle(models.Model):
    nom = models.CharField(max_length=50)
    capacite = models.IntegerField()
    batiment_id = models.ForeignKey('Batiment', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

# Modele Batiment 

class Batiment(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

# Modele ReleveDeNote 

class ReleveDeNote(models.Model):
    utilisateur_id = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    matiere_id = models.ForeignKey('Matiere', on_delete=models.CASCADE)
    note_cour = models.FloatField()
    note_examen = models.FloatField()
    moyenne = models.FloatField(default=0)
    commentaire = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.utilisateur_id}-{self.matiere_id}-{self.date_ajout}')
        super().save(*args, **kwargs)

# Modele CahierAbsence

class CahierAbsence(models.Model):
    emploi_du_temps_id = models.ForeignKey('EmploiDuTemps', on_delete=models.CASCADE)
    utilisateur_id = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    present = models.BooleanField()
    date = models.DateField()
    note_absence = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.emploi_du_temps_id}-{self.utilisateur_id}-{self.date}')
        super().save(*args, **kwargs)

# Model Archive 

class Archive(models.Model):
    matiere_id = models.ForeignKey('Matiere', on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    ressource = models.FileField(upload_to='ressources/', blank=True, null=True)
    assignation = models.FileField(upload_to='assignations/', blank=True, null=True)
    date_archive = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.matiere_id}-{self.titre}')
        super().save(*args, **kwargs)

# Modele Message

class Message(models.Model):
    expediteur_id = models.ForeignKey('Utilisateur', related_name= 'expediteur', on_delete=models.CASCADE )
    destinataire_id = models.ForeignKey('Utilisateur', related_name='destinataire', on_delete=models.CASCADE)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True,blank=True,null=True)
 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.expediteur_id}-{self.date_envoi}')
        super().save(*args, **kwargs)
            
# Modele Notification 

class Notification(models.Model):
    TYPES_NOTIFICATION = (
        ('general', 'General'),
        ('individuel', 'Individuel'),
        ('classe', 'Classe'),
        ('niveau', 'Niveau')
    )

    utilisateur_id = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    message = models.TextField()
    type_notification = models.CharField(max_length=20, choices=TYPES_NOTIFICATION)
    date_creation = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.utilisateur_id}-{self.date_creation}')
        super().save(*args, **kwargs)


# EspaceEchange 

class EspaceEchange(models.Model):
    niveau_id = models.ForeignKey('Niveau', on_delete=models.CASCADE)
    contenu = models.TextField()
    date_message = models.DateTimeField(auto_now_add=True)
    auteur_id = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.niveau_id}-{self.date_message}-{self.auteur_id}')
        super().save(*args, **kwargs)