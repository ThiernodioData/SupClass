from django import forms
from .models import *

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'email', 'mot_de_passe', 'role', 'niveau_id', 'matricule', 'photo']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control fs-4', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control fs-4', 'placeholder': 'Prénom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control fs-4', 'placeholder': 'Email'}),
            'mot_de_passe': forms.PasswordInput(attrs={'class': 'form-control fs-4', 'placeholder': 'Mot de passe'}),
            'role': forms.Select(attrs={'class': 'form-select fs-4'}),
            'niveau_id': forms.Select(attrs={'class': 'form-select fs-4'}),
            'matricule': forms.TextInput(attrs={'class': 'form-control fs-4', 'placeholder': 'Matricule'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control fs-4'}),
        }



class NiveauForm(forms.ModelForm):
    class Meta:
        model = Niveau
        fields = ['nom', 'description']  # Les champs à inclure dans le formulaire
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Nom du niveau',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Description du niveau',
                'rows': 5,
            }),
        }


class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['nom', 'description', 'niveau', 'professeur']  # Les champs du formulaire
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Nom de la matière',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Description de la matière',
                'rows': 5,
            }),
            'niveau': forms.Select(attrs={
                'class': 'form-select fs-4',
            }),
            'professeur': forms.Select(attrs={
                'class': 'form-select fs-4',
            }),
        }


class SalleForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['nom', 'capacite', 'batiment']  # Les champs à afficher dans le formulaire
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Nom de la salle',
            }),
            'capacite': forms.NumberInput(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Capacité de la salle',
            }),
            'batiment': forms.Select(attrs={
                'class': 'form-select fs-4',
            }),
        }
        
        

class BatimentForm(forms.ModelForm):
    class Meta:
        model = Batiment
        fields = ['nom', 'adresse']  # Les champs du formulaire
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Nom du bâtiment',
            }),
            'adresse': forms.TextInput(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Adresse du bâtiment',
            }),
        }
        
        
        
 

class ReleveDeNoteForm(forms.ModelForm):
    class Meta:
        model = ReleveDeNote
        fields = ['utilisateur', 'matiere', 'note_cour', 'note_examen', 'commentaire']  # Les champs inclus dans le formulaire
        widgets = {
            'utilisateur': forms.Select(attrs={
                'class': 'form-select fs-4',
            }),
            'matiere': forms.Select(attrs={
                'class': 'form-select fs-4',
            }),
            'note_cour': forms.NumberInput(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Note de cours',
            }),
            'note_examen': forms.NumberInput(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Note d\'examen',
            }),
            'commentaire': forms.Textarea(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Commentaire (facultatif)',
                'rows': 3,
            }),
        }



class CahierAbsenceForm(forms.ModelForm):
    class Meta:
        model = CahierAbsence
        fields = ['emploi_du_temps', 'utilisateur', 'present', 'date', 'note_absence']
        widgets = {
            'emploi_du_temps': forms.Select(attrs={
                'class': 'form-select fs-4',
            }),
            'utilisateur': forms.Select(attrs={
                'class': 'form-select fs-4',
            }),
            'present': forms.CheckboxInput(attrs={
                'class': 'form-check-input fs-4',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control fs-4',
                'type': 'date',
            }),
            'note_absence': forms.Textarea(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Note sur l\'absence...',
                'rows': 3,
            }),
        }
