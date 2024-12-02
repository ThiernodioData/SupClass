// Récupère l'élément avec l'ID 'onOffInternet' et le stocke dans une variable
const divOnOffInternet = document.getElementById('onOffInternet');

// Ajoute une classe 'hide' à l'élément pour le masquer initialement
divOnOffInternet.classList.add('hide');
// Cache l'élément en définissant sa propriété 'display' à 'none'
divOnOffInternet.style.display = 'none';

// Fonction appelée lorsque l'utilisateur passe hors ligne (offline)
function handleOffline() {
    // Ajoute une classe 'offline' à l'élément pour indiquer qu'il est hors ligne
    divOnOffInternet.classList.add('offline');
    // Modifie le contenu HTML de l'élément pour afficher un message d'alerte et un bouton de fermeture
    divOnOffInternet.innerHTML = `
        <h1>Ce projet nécessite une connexion Internet pour fonctionner de manière optimale, car il dépend de ressources en ligne telles que des icônes et d'autres éléments !</h1>
        <button id="btnOnOffClose" class="new-product">Fermer Pop-up</button>
    `;
    // Affiche l'élément en définissant sa propriété 'display' à 'flex'
    divOnOffInternet.style.display = 'flex';

    // Récupère le bouton avec l'ID 'btnOnOffClose'
    const btnOnOffInternet = document.getElementById('btnOnOffClose');
    // Ajoute un écouteur d'événement sur le bouton pour gérer le clic
    btnOnOffInternet.addEventListener('click', (event) => {
        // Empêche le comportement par défaut du clic (par exemple, la soumission d'un formulaire)
        event.preventDefault();
        // Cache l'élément 'divOnOffInternet' après le clic sur le bouton
        divOnOffInternet.style.display = 'none';
    });
}

// Ajoute un écouteur d'événement pour détecter quand l'utilisateur passe hors ligne
window.addEventListener('offline', handleOffline);

// Ajoute un écouteur d'événement pour charger la page
window.addEventListener('load', () => {
    // Si l'utilisateur est hors ligne au moment du chargement, déclenche la fonction 'handleOffline'
    if (!navigator.onLine) {
        handleOffline();
    }
});

// Ajoute un écouteur d'événement pour détecter quand l'utilisateur revient en ligne (online)
window.addEventListener('online', () => {
    // Supprime la classe 'offline' et ajoute une classe 'online' à l'élément
    divOnOffInternet.classList.remove('offline');
    divOnOffInternet.classList.add('online');
    // Modifie le contenu HTML de l'élément pour afficher un message indiquant que la connexion est rétablie
    divOnOffInternet.innerHTML = `
        <h1>Connexion Internet rétablie. Le projet fonctionnera désormais de manière optimale, car il dépendait de ressources en ligne telles que des icônes et d'autres éléments !</h1>
    `;
    // Affiche l'élément en définissant sa propriété 'display' à 'flex'
    divOnOffInternet.style.display = 'flex';

    // Après un délai de 3 secondes, cache l'élément à nouveau
    setTimeout(() => {
        divOnOffInternet.style.display = 'none';
    }, 3000);
});
