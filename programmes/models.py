from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
# Pour les slugs qui servent à générer des URL conviviales

# Create your models here.

# Table Niveau

class Niveau(models.Model):
    nom = models.CharField(max_length=50) # Nom du niveau
    description = models.TextField() # Description du niveau
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug:
            self.slug = slugify(self.nom) # Générer un slug basé sur le nom
        super(Niveau, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return self.nom

# Table Matiere

class Matiere(models.Model):
    nom = models.CharField(max_length=100) # Nom de la matière
    description = models.TextField() # Description de la matière
    niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE) # Référence au niveau
    professeur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE) # Référence au professeur
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug:
            self.slug = slugify(self.nom) # Générer un slug basé sur le nom
        super(Matiere, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return self.nom

# Table Salle

class Salle(models.Model):
    nom = models.CharField(max_length=50) # Nom de la salle
    capacite = models.IntegerField() # Capacité de la salle
    batiment = models.ForeignKey('Batiment', on_delete=models.CASCADE) # Référence au bâtiment
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(self.nom) # Générer un slug basé sur le nom
        super(Salle, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return self.nom

# Table Batiment

class Batiment(models.Model): 
    nom = models.CharField(max_length=100) # Nom du batiment
    adresse = models.CharField(max_length=255) # Adresse du bâtiment
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(self.nom) # Générer un slug basé sur le nom
        super(Batiment, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return self.nom

# Table Utilisateur

class Utilisateur(models.Model):
    ROLE_CHOICES = [ 
        ('administrateur', 'Administrateur'),
        ('professeur', 'Professeur'),
        ('etudiant', 'Etudiant'),
        ('chef_classe', 'Chef de Classe'),
    ] 
    nom = models.CharField(max_length=50) # Nom de l'utilisateur
    prenom = models.CharField(max_length=50) # Prenom de l'utilisateur
    email = models.EmailField(max_length=100, unique=True) # Email de l'utilisateur
    mot_de_passe = models.CharField(max_length=255) # Mot de passe de l'utilisateur
    role = models.CharField(max_length=50, choices=ROLE_CHOICES) # Rôle de l'utilisateur
    date_creation = models.DateTimeField(auto_now_add=True) # Date de création du compte
    niveau_id = models.ForeignKey('Niveau', on_delete=models.CASCADE) # Référence au niveau
    matricule = models.CharField(max_length=50, unique=True) # Matricule de l'utilisateur
    photo = models.ImageField(upload_to='media/images/', blank=True, null=True) # Photo de l'utilisateur
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(f'{self.nom}-{self.prenom}') # Générer un slug basé sur le nom et prénom
        super(Utilisateur, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return f'{self.nom} {self.prenom}'
        
# Table Notification
        
class Notification(models.Model):
    TYPE_NOTIFICATION_CHOICES = [
        ('general', 'General'),
        ('individuel', 'Individuel'),
        ('classe', 'Classe'),
        ('niveau', 'Niveau'),
    ]
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE) # Référence à l'utilisateur
    titre = models.CharField(max_length=100) # Titre de la notification
    message = models.TextField() # Message de la notification
    type_notification = models.CharField(max_length=50, choices=TYPE_NOTIFICATION_CHOICES) # Type de notification
    date_creation = models.DateTimeField(auto_now_add=True) # Date de creation de la notification
    lu = models.BooleanField(default=False) # Indicateur de lecture
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(f'{self.titre}-{self.date_creation}') # Générer un slug basé sur le titre et la date de création
        super(Notification, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return f'Notification: {self.titre} pour {self.utilisateur.nom}'

# Table EmploiDuTemps

class EmploiDuTemps(models.Model):
    niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE) # Référence au niveau
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE) # Référence à la matiere
    salle = models.ForeignKey('Salle', on_delete=models.CASCADE) # Référence à la salle
    date = models.DateField() # Date du cours
    heure_debut = models.TimeField() # Heure de debut du cours
    heure_fin = models.TimeField() # Heure de fin du cours
    titre_lesson = models.CharField(max_length=100) # Titre de la leçon
    contenu_lesson = models.TextField() # Contenu de la leçon
    duree_faite = models.TimeField() # Durée effectuée
    signature_prof = models.CharField(max_length=100) # Signature du professeur
    commentaire = models.TextField(null=True, blank=True) #Commentaire
    modifie_par = models.ForeignKey('Utilisateur', on_delete=models.CASCADE) # Référence à l'utilisateur qui a modifié
    ressource = models.FileField(upload_to='ressources/', blank=True, null=True) # Ressources liées au cours
    assignation = models.BinaryField(null=True, blank=True)
    slug = models.SlugField(max_length=200,unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(f'{self.titre_lesson}-{self.date}') # Générer un slug basé sur le titre de la leçon et la date
        super(EmploiDuTemps, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return f'{self.titre_lesson} ({self.date})'

# Table ReleveDeNote

class ReleveDeNote(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE) # Référence à l'utilisateur
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE) # Référence à la matiere
    note_cour = models.FloatField() # Note de cours
    note_examen = models.FloatField() # Note d'examen'
    moyenne = models.FloatField(default=0) # Moyenne des notes
    commentaire = models.TextField(null=True, blank=True) # Commentaire
    date_ajout = models.DateTimeField(auto_now_add=True) # Date d'ajout de la note
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(f'{self.utilisateur.nom}-{self.matiere.nom}-{self.date_ajout}') # Générer un slug basé sur l'utilisateur, la matière et la date d'ajout
        super(ReleveDeNote, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return f'Relevé de notes pour {self.utilisateur.nom} en {self.matiere.nom}'

# Table Archive

class Archive(models.Model):
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE) # Référence à la matière
    titre = models.CharField(max_length=100) # Titre de l'archive
    contenu = models.TextField() # Contenu de l'archive
    ressource = models.BinaryField(blank=True, null=True) # Ressource associée à l'archive
    assignation = models.BinaryField(blank=True, null=True) # Assignation associée à l'archive
    date_archive = models.DateTimeField(auto_now_add=True) # Date d'archivage
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(f'{self.titre}-{self.date_archive}') # Générer un slug basé sur le titre et la date d'archivage
        super(Archive, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return self.titre

# Table EspaceEchange

class EspaceEchange(models.Model):
    niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE) # Référence au niveau
    contenu = models.TextField() # Contenu de l'échange
    date_message = models.DateTimeField(auto_now_add=True) # Date du message
    auteur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE) # Référence à l'auteur
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(f'{self.auteur.nom}-{self.date_message}') # Générer un slug basé sur l'auteur et la date du message
        super(EspaceEchange, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.

    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return f'Message de {self.auteur.nom} ({self.date_message})'

# Table Message

class Message(models.Model): 
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes') # Référence à l'expéditeur
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_recus') # Référence au destinataire
    contenu = models.TextField() # Contenu du message
    date_envoi = models.DateTimeField(auto_now_add=True) # Date d'envoi du message
    lu = models.BooleanField(default=False) # Indicateur de lecture
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(f'{self.expediteur.nom}-{self.destinataire.nom}-{self.date_envoi}') # Générer un slug basé sur l'expéditeur, le destinataire et la date d'envoi
        super(Message, self).save(*args, **kwargs)  # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.


    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return f'Message de {self.expediteur.nom} à {self.destinataire.nom} ({self.date_envoi})'

# Table CahierAbsence

class CahierAbsence(models.Model): 
    emploi_du_temps = models.ForeignKey('EmploiDuTemps', on_delete=models.CASCADE) # Référence à l'emploi du temps
    utilisateur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE) # Référence à l'utilisateur
    present = models.BooleanField() # Indicateur de présence
    date = models.DateField() # Date de l'absence
    note_absence = models.TextField(null=True, blank=True) # Note d'absence
    slug = models.SlugField(unique=True, blank=True) # Slug pour l'URL

    def save(self, *args, **kwargs): # Cette méthode est utilisée pour personnaliser le comportement de sauvegarde d'un modèle.
        if not self.slug: # Cette condition vérifie si le champ slug n'a pas encore été défini.
            self.slug = slugify(f'{self.utilisateur.nom}-{self.date}') # Générer un slug basé sur l'utilisateur et la date
        super(CahierAbsence, self).save(*args, **kwargs) # s'assure que les modifications apportées au modèle sont correctement enregistrées dans la base de données.


    def __str__(self): # Cette méthode définit la représentation en chaîne de caractères de l'objet. Elle est utilisée par Django dans ses interfaces et lors des conversions en chaîne de caractères.
        return f'Absence de {self.utilisateur.nom} le {self.date}'