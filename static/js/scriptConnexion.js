// Sélection des éléments HTML par leur ID pour interagir avec eux dans le script
const container1 = document.getElementById('container1'); // Conteneur principal pour basculer entre connexion et inscription
const btnLogin = document.getElementById('signIn'); // Bouton pour afficher le formulaire de connexion
const btnSign = document.getElementById('signUp'); // Bouton pour afficher le formulaire d'inscription

const inputNomNewCompt = document.getElementById('nomCreer'); // Champ pour entrer le nom lors de la création d'un nouveau compte
const inputEmailNewCompt = document.getElementById('emailCreer'); // Champ pour entrer l'email lors de la création d'un nouveau compte
const inputPwdNewCompt = document.getElementById('pwdCreer'); // Champ pour entrer le mot de passe lors de la création d'un nouveau compte
const btnNewCompt = document.getElementById('btnCreerCompte1'); // Bouton pour créer un nouveau compte

const inputEmailCompt = document.getElementById('emailConnexion'); // Champ pour entrer l'email lors de la connexion
const inputPwdCompt = document.getElementById('pwdConnexion'); // Champ pour entrer le mot de passe lors de la connexion
const btnConnexion = document.getElementById('btnConexion1'); // Bouton pour se connecter

// Gestionnaire d'événements pour afficher le formulaire de connexion
btnLogin.addEventListener('click', () => {
    container1.classList.remove('panel-active'); // Supprime la classe 'panel-active' pour basculer sur le formulaire de connexion
});

// Gestionnaire d'événements pour afficher le formulaire d'inscription
btnSign.addEventListener('click', () => {
    container1.classList.add('panel-active'); // Ajoute la classe 'panel-active' pour basculer sur le formulaire d'inscription
});

// Gestionnaire d'événements pour la tentative de connexion
btnConnexion.addEventListener('click', (event) => {
    event.preventDefault(); // Empêche le comportement par défaut du bouton (qui serait de soumettre un formulaire)

    // Vérifie si l'email et le mot de passe saisis correspondent à un utilisateur admin ou prof
    if(inputEmailCompt.value == "admin@sup.sn" && inputPwdCompt.value == 1234){
        window.location.href = 'admin.html'; // Redirige vers la page admin
    }
    if(inputEmailCompt.value == "prof@sup.sn" && inputPwdCompt.value == 1234){
        window.location.href = 'adminProf.html'; // Redirige vers la page admin pour les profs
    }

    // Réinitialise les champs de connexion
    inputEmailCompt.value = "";
    inputPwdCompt.value = "";
});

// Gestionnaire d'événements pour la création d'un nouveau compte
btnNewCompt.addEventListener('click', (event) => {
    event.preventDefault(); // Empêche le comportement par défaut du bouton (soumission de formulaire)

    // Vérifie si tous les champs de création de compte sont vides
    if(inputEmailNewCompt.value == "" && inputPwdNewCompt.value == "" && inputNomNewCompt.value == ""){
        // Réinitialise les champs de création de compte
        inputEmailNewCompt.value = "";
        inputPwdNewCompt.value = "";
        inputNomNewCompt.value = "";
    }

    // Vérifie si les informations de compte saisies correspondent à un utilisateur spécifique
    if(inputEmailNewCompt.value == "user@sup.sn" && inputPwdNewCompt.value == 1234 && inputNomNewCompt.value == "user"){
        window.location.href = 'adminUser.html'; // Redirige vers la page utilisateur
    }

    // Réinitialise les champs de création de compte après la tentative
    inputEmailNewCompt.value = "";
    inputPwdNewCompt.value = "";
    inputNomNewCompt.value = "";
});
