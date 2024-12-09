from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def connexion(request):
    context = {
    'niveaux': []  # Vous pouvez ajouter des données ici si nécessaire
    }
    return render(request, 'connexion.html', context)
def tableau_bord(request):
    return render(request, 'tableau_bord.html')

# def acceuil(request):
#     return render(request, 'utilisateurs/index.html')

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

@login_required
def user_logout(request):
    logout(request)
    return redirect('programme:login')  # Redirige vers la page de connexion