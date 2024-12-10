from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def connexion(request):
    context = {
        'niveaux': []  # Vous pouvez ajouter des données ici si nécessaire
    }
    return render(request, 'connexion.html', context)

@login_required
def tableau_bord(request):
    return render(request, 'tableau_bord.html')

@login_required
def emplois_du_temps(request):
    return render(request, 'emplois_du_temps.html')

@login_required
def eleves(request):
    return render(request, 'eleves.html')

@login_required
def enseignants(request):
    return render(request, 'enseignants.html')

@login_required
def cours(request):
    return render(request, 'cours.html')

@login_required
def emargements(request):
    return render(request, 'emargements.html')

@login_required
def notes(request):
    return render(request, 'notes.html')

@login_required
def salles(request):
    return render(request, 'salles.html')

@login_required
def classe(request):
    return render(request, 'classe.html')

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