// Sélection des éléments HTML par leurs ID ou classes pour interagir avec eux
const body = document.body; // Corps du document pour appliquer des thèmes
const sidebar = document.querySelector('.main-sidebar'); // Sidebar principale
const openSidebar = document.querySelector('#openSidebar'); // Bouton pour ouvrir la sidebar
const closeSidebar = document.querySelector('#closeSidebar'); // Bouton pour fermer la sidebar
const toggleTheme = document.querySelector('.toggle-theme'); // Bouton pour changer le thème
const light = toggleTheme.children[0]; // Icône du thème clair
const dark = toggleTheme.children[1]; // Icône du thème sombre
const inputFields = document.querySelectorAll('.percentage p'); // Champs d'affichage des pourcentages
const card1 = document.getElementById('card1'); // Première carte pour le tableau de bord
const card2 = document.getElementById('card2'); // Deuxième carte pour le tableau de bord
const card3 = document.getElementById('card3'); // Troisième carte pour le tableau de bord
const ongletTableauBord = document.getElementById('tableauBord'); // Onglet pour le tableau de bord
const ongletActiveTab = document.querySelector('#tableauBord .active'); // Onglet actif pour le tableau de bord
const dashboardBody1 = document.getElementById('dashBody1'); // Première section du tableau de bord
const dashboardBody2 = document.getElementById('dashBody2'); // Deuxième section du tableau de bord

const seDeconnecter = document.getElementById('seDeconnecter'); // Bouton pour se déconnecter

// Masque la deuxième section du tableau de bord au démarrage
dashboardBody2.style.display = 'none';

// Gestionnaire d'événement pour l'onglet du tableau de bord
ongletTableauBord.addEventListener('click', addTableauBord);
function addTableauBord() {
    ongletActiveTab.classList.add('active'); // Ajoute la classe 'active' à l'onglet du tableau de bord
    dashboardBody1.style.display = 'block'; // Affiche la première section du tableau de bord
    dashboardBody2.style.display = 'none'; // Masque la deuxième section du tableau de bord
}

// Gestionnaires d'événements pour les cartes du tableau de bord
card1.addEventListener('click', () => {
    remplissageTableau('ESITECH'); // Remplit le tableau pour le département ESITECH
});
card2.addEventListener('click', () => {
    remplissageTableau('MERCURE'); // Remplit le tableau pour le département MERCURE
});
card3.addEventListener('click', () => {
    remplissageTableau('TRANSPORT'); // Remplit le tableau pour le département TRANSPORT
});

// Remplit automatiquement le tableau avec les données du département ESITECH lors du chargement de la page
window.addEventListener('load', () => {
    remplissageTableau('ESITECH');
});

// Fonction pour remplir le tableau avec les données du localStorage
function remplissageTableau(department) {
    const tableau = document.querySelector('.recent-orders tbody'); // Sélection du tableau des commandes récentes
    tableau.innerHTML = ''; // Réinitialise le contenu du tableau

    // Récupère les données stockées dans le localStorage
    const data = JSON.parse(localStorage.getItem(`stockageEtudiant${department}`)) || [];

    // Remplit le tableau avec les données récupérées
    data.forEach(item => {
        const row = document.createElement('tr'); // Crée une nouvelle ligne pour le tableau
        // Ajoute les cellules de la ligne avec les informations des étudiants
        row.innerHTML = `
            <td>${item.nom}</td>
            <td>${item.prenom}</td>
            <td>${item.niveau}</td>
            <td>${item.matiere}</td>
            <td class="${item.statut === 'present' ? 'text-green' : item.statut === 'absent' ? 'text-red' : 'text-yellow'}">${item.statut}</td>
            <td>${item.date}</td>
        `;
        tableau.appendChild(row); // Ajoute la ligne au tableau
    });
}

// Gestionnaire d'événements pour le changement de département
document.getElementById('choixDepartement').addEventListener('change', function() {
    const selectedDepartment = this.value; // Récupère la valeur du département sélectionné
    remplissageTableau(selectedDepartment); // Remplit le tableau avec les données du département sélectionné
});

// Remplit le tableau avec le département par défaut lors du chargement de la page
window.onload = function() {
    const defaultDepartment = document.getElementById('choixDepartement').value; // Récupère la valeur du département par défaut
    remplissageTableau(defaultDepartment); // Remplit le tableau avec les données du département par défaut
};

// Gestionnaires d'événements pour ouvrir et fermer la sidebar
openSidebar.addEventListener('click', openSidebarFunction);
closeSidebar.addEventListener('click', closeSidebarFunction);

function openSidebarFunction() {
    sidebar.style.left = '0%'; // Affiche la sidebar en modifiant sa position
}

function closeSidebarFunction() {
    sidebar.style.left = '-100%'; // Masque la sidebar en modifiant sa position
}

// Gestionnaire d'événements pour changer le thème entre clair et sombre
toggleTheme.addEventListener('click', changeTheme);

function changeTheme() {
    if (body.classList.contains('dark-mode')) {
        lightMode(); // Passe en mode clair si le mode sombre est activé
    } else {
        darkMode(); // Passe en mode sombre si le mode clair est activé
    }
}

// Gestion de l'affichage des pourcentages dans les cercles de progression
inputFields.forEach((e, i) => {
    let val = parseInt(e.textContent); // Récupère la valeur du pourcentage
    let circle = document.getElementById(`circle${i + 1}`); // Sélectionne le cercle de progression correspondant
    let r = circle.getAttribute('r'); // Récupère le rayon du cercle
    let circ = Math.PI * 2 * r; // Calcule la circonférence du cercle
    let counter = 0; // Initialisation du compteur
    let fillValue = (circ * (100 - val)) / 100; // Calcule la valeur de remplissage du cercle
    setInterval(() => {
        if (counter === val) {
            clearInterval(); // Arrête l'intervalle lorsque le pourcentage est atteint
        } else {
            counter += 1; // Incrémente le compteur
            e.innerText = counter + '%'; // Met à jour le texte avec le pourcentage
            circle.style.strokeDashoffset = fillValue; // Met à jour le remplissage du cercle
        }
    }, 1000 / val); // Vitesse de l'animation
});

// Active le mode sombre si le thème préféré de l'utilisateur est sombre
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    darkMode();
}

// Fonctions pour activer le mode sombre ou clair
function darkMode() {
    body.classList.add('dark-mode');
    light.classList.remove('active');
    dark.classList.add('active');
}

function lightMode() {
    body.classList.remove('dark-mode');
    dark.classList.remove('active');
    light.classList.add('active');
}

// Gestionnaire d'événements pour la déconnexion
seDeconnecter.addEventListener('click', (event) => {
    event.preventDefault();
    window.location.href = 'Connexion.html'; // Redirige vers la page de connexion
});
