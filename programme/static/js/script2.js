// Sélection des éléments du DOM pour les manipulations
const body = document.body;
const sidebar = document.querySelector('.main-sidebar');
const openSidebar = document.querySelector('#openSidebar');
const closeSidebar = document.querySelector('#closeSidebar');
const toggleTheme = document.querySelector('.toggle-theme');
const light = toggleTheme.children[0];
const dark = toggleTheme.children[1];
const inputFields = document.querySelectorAll('.percentage p');
const card1 = document.getElementById('card1');
const card2 = document.getElementById('card2');
const card3 = document.getElementById('card3');
const ongletTableauBord = document.getElementById('tableauBord');
const ongletCahierText = document.getElementById('cahierText');
const ongletActiveTab = document.querySelector('#tableauBord .active');
const ongletActiveCahier = document.querySelector('#cahierText .active');
const dashboardBody1 = document.getElementById('dashBody1'); // Section du tableau de bord
const dashboardBody2 = document.getElementById('dashBody2'); // Section du cahier de texte
const addNewDeparment = document.getElementById('addNewDeparment');
const addNewDeparment2 = document.getElementById('addNewDeparment2');
const seDeconnecter = document.getElementById('seDeconnecter');

// Masquer le deuxième tableau de bord (dashBody2) au chargement de la page
dashboardBody2.style.display = 'none';
// Retirer la classe 'active' de l'onglet cahier de texte au chargement de la page
ongletActiveCahier.classList.remove('active')

// Ajouter un événement pour activer l'onglet du tableau de bord
ongletTableauBord.addEventListener('click', addTableauBord);

function addTableauBord() {
    ongletActiveTab.classList.add('active');
    ongletActiveCahier.classList.remove('active');

    // Afficher le tableau de bord et masquer le cahier de texte
    dashboardBody1.style.display = 'block';
    dashboardBody2.style.display = 'none';
};

// Ajouter un événement pour activer l'onglet du cahier de texte
ongletCahierText.addEventListener('click', addCahierText);

function addCahierText() {
    ongletActiveTab.classList.remove('active');
    ongletActiveCahier.classList.add('active');

    // Masquer le tableau de bord et afficher le cahier de texte
    dashboardBody1.style.display = 'none';
    dashboardBody2.style.display = 'flex';
};

// Ajouter des événements pour remplir le tableau en fonction du département sélectionné
card1.addEventListener('click', () => {
    remplissageTableau('ESITECH');
});
card2.addEventListener('click', () => {
    remplissageTableau('MERCURE');
});
card3.addEventListener('click', () => {
    remplissageTableau('TRANSPORT');
});

// Remplir le tableau par défaut avec les données de l'ESITECH au chargement de la page
window.addEventListener('load', () => {
    remplissageTableau('ESITECH');
});

// Fonction pour remplir le tableau avec les données du localStorage
function remplissageTableau(department) {
    const tableau = document.querySelector('.recent-orders tbody');
    tableau.innerHTML = ''; // Vider le tableau existant

    // Récupérer les données du localStorage
    const data = JSON.parse(localStorage.getItem(`stockageEtudiant${department}`)) || [];

    // Remplir le tableau avec les données récupérées
    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.nom}</td>
            <td>${item.prenom}</td>
            <td>${item.niveau}</td>
            <td>${item.matiere}</td>
            <td class="${item.statut === 'present' ? 'text-green' : item.statut === 'absent' ? 'text-red' : 'text-yellow'}">${item.statut}</td>
            <td>${item.date}</td>
        `;
        tableau.appendChild(row);
    });
}

// Gérer le changement de département pour remplir le tableau en conséquence
document.getElementById('choixDepartement').addEventListener('change', function() {
    const selectedDepartment = this.value;
    remplissageTableau(selectedDepartment);
});

// Appel initial pour remplir le tableau avec le département par défaut
window.onload = function() {
    const defaultDepartment = document.getElementById('choixDepartement').value;
    remplissageTableau(defaultDepartment);
};

// Ajouter des événements pour ouvrir et fermer la barre latérale
openSidebar.addEventListener('click', openSidebarFunction);
closeSidebar.addEventListener('click', closeSidebarFunction);
toggleTheme.addEventListener('click', changeTheme);

function openSidebarFunction() {
    sidebar.style.left = '0%';
}

function closeSidebarFunction() {
    sidebar.style.left = '-100%';
}

// Changer le thème entre clair et sombre
function changeTheme() {
    if (body.classList.contains('dark-mode')) {
        lightMode();
    } else if (!body.classList.contains('dark-mode')) {
        darkMode();
    }
}

// Mise à jour des champs d'entrée en fonction du thème
inputFields.forEach((e, i) => {
    let val = parseInt(e.textContent);
    let circle = document.getElementById(`circle${i + 1}`);
    let r = circle.getAttribute('r');
    let circ = Math.PI * 2 * r;
    let counter = 0;
    let fillValue = (circ * (100 - val)) / 100;
    setInterval(() => {
        if (counter === val) {
            clearInterval();
        } else {
            counter += 1;
            e.innerText = counter + '%';
            circle.style.strokeDashoffset = fillValue;
        }
    }, 1000 / val);
});

// Si le système préfère le mode sombre, activer le mode sombre automatiquement
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    darkMode();
}

// Activer le mode sombre
function darkMode() {
    body.classList.add('dark-mode');
    light.classList.remove('active');
    dark.classList.add('active');
}

// Activer le mode clair
function lightMode() {
    body.classList.remove('dark-mode');
    dark.classList.remove('active');
    light.classList.add('active');
}

// Ajouter un nouvel événement pour activer l'onglet cahier de texte
addNewDeparment.addEventListener('click', () => {
    addCahierText();
});

addNewDeparment2.addEventListener('click', () => {
    addCahierText();
});

// Ajouter un événement pour gérer la déconnexion de l'utilisateur
seDeconnecter.addEventListener('click', (event) => {
    event.preventDefault();
    window.location.href = 'Connexion.html';
});
