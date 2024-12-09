// Sélection des éléments
const body = document.body;
const sidebar = document.querySelector('.main-sidebar');
const openSidebar = document.querySelector('#openSidebar');
const closeSidebar = document.querySelector('#closeSidebar');
const toggleTheme = document.querySelector('.toggle-theme');
const light = toggleTheme.children[0];
const dark = toggleTheme.children[1];
const inputFields = document.querySelectorAll('.percentage p');
const dashboardIcon = document.getElementById('dashboard-icon');
const icons_bare_onglet = document.querySelectorAll('ul.list-items img');
const icons_bare_header=''

const imagePath = "{% static 'images/' %}"; // Définir le chemin de base pour les images

// Ajout des écouteurs d'événements
openSidebar.addEventListener('click', toggleSidebar);
closeSidebar.addEventListener('click', toggleSidebar); // Utilisation de la même fonction pour ouvrir/fermer
toggleTheme.addEventListener('click', changeTheme);

// Fonction pour basculer la barre latérale
function toggleSidebar() {
    if (sidebar.style.left === '0%') {
        sidebar.style.left = '-100%';
    } else {
        sidebar.style.left = '0%';
    }
}

// Fonction pour changer le thème
function changeTheme(event) {
    if (event.target === light) {
        lightMode();
    } else if (event.target === dark) {
        darkMode();
    }
}

// Fonction pour activer le mode sombre
function darkMode() {
    body.classList.add('dark-mode');
    light.classList.remove('active');
    dark.classList.add('active');
    
    updateIcons('dark'); // Mise à jour des icônes en mode sombre
    updateIconesHeader('dark')
}

// Fonction pour activer le mode clair
function lightMode() {
    body.classList.remove('dark-mode');
    dark.classList.remove('active');
    light.classList.add('active');
    
    updateIcons('light'); // Mise à jour des icônes en mode clair;
    updateIconesHeader('light')
}

// Configuration des cercles de progression
/*inputFields.forEach((e, i) => {
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
});*/



// Fonction pour afficher la date et l'heure actuelles avec le mois en chaîne de caractères et les heures, minutes, secondes en deux chiffres

function afficherDateHeure() {
    var maintenant = new Date();
    var jour = maintenant.getDate();
    var mois = maintenant.getMonth(); // Les mois sont indexés de 0 à 11
    var annee = maintenant.getFullYear();
    var heures = maintenant.getHours().toString().padStart(2, '0');
    var minutes = maintenant.getMinutes().toString().padStart(2, '0');
    var secondes = maintenant.getSeconds().toString().padStart(2, '0');

    // Tableau des mois
    var moisNoms = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"];

    // Utilisation du tableau pour récupérer le nom du mois
    var moisTexte = moisNoms[mois];

    // Formatage de la date et de l'heure
    var dateHeureFormat = jour + " " + moisTexte + " " + annee + " " + heures + ":" + minutes + ":" + secondes;

    // Insertion dans l'élément avec l'ID 'dateHeureAffichage'
    document.getElementById("dateHeureAffichage").innerText = dateHeureFormat;
}
// Mettre à jour la date et l'heure toutes les secondes
setInterval(afficherDateHeure, 1000);



// Barre d'onglet : Fonction pour changer les icônes dynamiquement en fonction du mode (clair ou sombre)
function updateIcons(mode) {
    icons_bare_onglet.forEach((icon, index) => {
        const iconNumber = index + 1;
        if (mode === 'dark') {
            icon.src = `${imagePath}icon${iconNumber}_light.png`; // Utiliser la variable imagePath
        } else {
            icon.src = `${imagePath}icon${iconNumber}.png`; // Utiliser la variable imagePath
        }
    });
}



// Barre d'header : Fonction pour changer les icônes dynamiquement en fonction du mode (clair ou sombre)
function updateIconesHeader(mode) {
    const icones = document.querySelectorAll('.header-right .info img.icone');
    
    icones.forEach((icone, index) => {
        const iconNumber = index + 1;
        if (mode === 'dark') {
            icone.src = `${imagePath}icon_h_${iconNumber}_dart.png`; // Utiliser la variable imagePath
        } else {
            icone.src = `${imagePath}icon_h_${iconNumber}.png`; // Utiliser la variable imagePath
        }
    });
}


// Appliquer le thème sombre si le système est en mode sombre
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    darkMode();
}else{
    lightMode()
}

document.addEventListener("DOMContentLoaded", function() {
    // Initialisation de l'icône au chargement de la page (mode clair par défaut)
    dashboardIcon.src = "../static/images/admin.jpg";
});






















