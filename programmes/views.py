from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Utilisateur,Niveau,CahierAbsence  # Remplacez par le nom de votre modèle
from .forms import *
from django.contrib import messages
from datetime import date
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
def connexion(request):
    context = {
        'niveaux': []  # Vous pouvez ajouter des données ici si nécessaire
    }
    return render(request, 'connexion.html', context)

@login_required




def tableau_bord(request):
    niveaux = ["Licence 1", "Licence 2", "Licence 3", "Master"]
    niveau_filtre = request.GET.get('niveau', 'Licence 1')  # Par défaut "Licence 1"

    # Filtrer les absences pour le niveau sélectionné
    absences = CahierAbsence.objects.filter(utilisateur__niveau_id__nom=niveau_filtre)

    context = {
        'niveaux': niveaux,        # Liste des niveaux pour les boutons
        'niveau_filtre': niveau_filtre,  # Niveau actuellement sélectionné
        'absences': absences,      # Absences pour le niveau sélectionné
    }

    return render(request, 'tableau_bord.html', context)





@login_required
def emplois_du_temps(request):
    return render(request, 'emplois_du_temps.html')


@login_required
def matiere(request):
    if request.method == 'POST':
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programme:tableau_bord')  # Redirige vers la page tableau_bord (assurez-vous que cette URL existe)

    else:
        form = MatiereForm()
    return render(request, 'matiere.html', {'form': form})



@login_required


def utilisateur(request):
    if request.method == 'POST':  # Si le formulaire est soumis
        form = UtilisateurForm(request.POST, request.FILES)  # Récupère les données du formulaire
        if form.is_valid():  # Vérifie la validité des données
            form.save()  # Enregistre l'utilisateur dans la base de données
            return redirect('tableau_bord')  # Redirige vers la page tableau_bord (assurez-vous que cette URL existe)
    else:
        form = UtilisateurForm()  # Initialise un formulaire vide pour un affichage initial
    return render(request, 'utilisateur.html', {'form': form})  # Affiche la page avec le formulaire

@login_required
def enseignants(request):
    return render(request, 'enseignants.html')

@login_required
def niveau(request):
    if request.method == 'POST':
        form = NiveauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tableau_bord')  # Redirigez vers la page tableau_bord
    else:
        form = NiveauForm()
    return render(request, 'niveau.html', {'form': form})


@login_required
def emargements(request):
    return render(request, 'emargements.html')


@login_required
def addnote(request):
    if request.method == 'POST':
        form = ReleveDeNoteForm(request.POST)
        if form.is_valid():
            releve = form.save(commit=False)
            # Calcul automatique de la moyenne
            releve.moyenne = (releve.note_cour + releve.note_examen) / 2
            releve.save()
            return redirect('programme:tableau_bord')  # Redirige vers la page tableau_bord après succès
    else:
        form = ReleveDeNoteForm()
    return render(request, 'addnote.html', {'form': form})


@login_required
def shownote(request):
    # Filtrage par niveau (paramètre passé dans l'URL)
    niveau_filtre = request.GET.get('niveau', None)  # Récupérer le paramètre 'niveau'
    
    if niveau_filtre:
        notes = ReleveDeNote.objects.filter(utilisateur__niveau_id__nom=niveau_filtre)
    else:
        notes = ReleveDeNote.objects.all()  # Si aucun filtre, afficher toutes les notes

    niveaux = Niveau.objects.all()  # Récupérer tous les niveaux pour les cartes

    context = {
        'notes': notes,
        'niveaux': niveaux,
        'niveau_filtre': niveau_filtre,
    }
    return render(request, 'shownote.html', context)



@login_required
def salles(request):
    if request.method == 'POST':
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programme:tableau_bord')  # Redirige vers la page tableau_bord après la soumission du formulaire
    else:
        form = SalleForm()
    return render(request, 'salles.html', {'form': form})

@login_required
def batiment(request):
    if request.method == 'POST':
        form = BatimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programme:tableau_bord')  # Redirige vers la page tableau_bord après la soumission du formulaire
    else:
        form = BatimentForm()
    return render(request, 'batiment.html', {'form': form})



@login_required

def liste_absences(request):
    niveau_filtre = request.GET.get('niveau', None)
    matiere_filtre = request.GET.get('matiere', None)
    niveaux = Niveau.objects.all()
    matieres = Matiere.objects.filter(niveau__nom=niveau_filtre) if niveau_filtre else Matiere.objects.none()
    etudiants = Utilisateur.objects.filter(role='etudiant', niveau_id__nom=niveau_filtre) if niveau_filtre else Utilisateur.objects.none()

    # Calculer l'absence pour chaque étudiant
    today = date.today()
    absences = {}
    if niveau_filtre and matiere_filtre:
        for etudiant in etudiants:
            # Vérifier si l'étudiant a une absence aujourd'hui pour la matière filtrée
            absence = CahierAbsence.objects.filter(
                utilisateur=etudiant,
                date=today,
                emploi_du_temps__matiere__nom=matiere_filtre
            ).exists()
            absences[etudiant.id] = absence

    context = {
        'niveaux': niveaux,
        'matieres': matieres,
        'etudiants': etudiants,
        'niveau_filtre': niveau_filtre,
        'matiere_filtre': matiere_filtre,
        'absences': absences,
    }
    return render(request, 'emergement.html', context)










def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('programme:tableau_bord')  # Redirige vers le tableau de bord
            else:
                return render(request, 'connexion.html', {'error': "L'utilisateur est désactivé"})
        else:
            return render(request, 'connexion.html', {'error': "Nom d'utilisateur ou mot de passe incorrect"})
    else:
        return render(request, 'connexion.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('programme:login')  # Redirige vers la page de connexion

