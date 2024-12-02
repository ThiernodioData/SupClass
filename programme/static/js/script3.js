// Sélection des éléments HTML par leur ID
const container = document.getElementById('container');
const setup = document.getElementById('setup');
const inputNumStud = document.getElementById('numStudents');
const btnSaisiUser = document.getElementById('enterStudents');
const btnRandomUser = document.getElementById('usePredefinedList');
const contentForm = document.getElementById('attendanceForm');
const form = document.getElementById('studentsForm');
// const btnPdf = document.getElementById('generatePdf'); // Bouton pour générer un PDF, commenté pour le moment
const small = document.getElementById('small');
const choixDepartement = document.getElementById('choixDepartement');
const choixNiveau = document.getElementById('choixNiveau');
const choixMatiere = document.getElementById('choixMatiere');
const logo = document.getElementById('logo');

// Cache le formulaire de saisie des étudiants au départ
contentForm.classList.add('hide');

// Ajoute un écouteur d'événement pour le bouton de saisie des utilisateurs
btnSaisiUser.addEventListener('click', saisiUser);

// Ajoute une classe pour l'ordre du formulaire
form.classList.add('order');

// Recharge la page lorsque l'utilisateur clique sur le logo
logo.addEventListener('click', () => {
    window.location.reload();
});

// Fonction qui retourne la date du jour au format local
function dateToDay() {
    let t = new Date();
    let date = t.toLocaleDateString();
    return date;
}

let listEtudiant = []; // Liste des étudiants

// Fonction appelée lorsque l'utilisateur entre le nombre d'étudiants à saisir
function saisiUser() {
    let inputValue = inputNumStud.value;
    if (inputValue === "") {
        // Si le champ est vide, affiche un message d'erreur
        small.innerText = "Le champ nombre d'étudiants ne peut pas être vide";
        small.style.color = "red";
    } else {
        small.innerText = "";
        setup.classList.add('hide'); // Cache la configuration
        contentForm.classList.remove('hide'); // Affiche le formulaire de saisie

        let currentDate = new Date();
        let dateStr = currentDate.toLocaleDateString();

        // Affiche les informations de département, niveau et matière
        form.innerHTML = `
            <h4>Département: ${choixDepartement.value}</h4>
            <h4>Niveau: ${choixNiveau.value}</h4>
            <h4>Matière: ${choixMatiere.value}</h4>
            <h4>Date: ${dateStr}</h4>
        `;

        // Génère un formulaire pour chaque étudiant à saisir
        for (let i = 0; i < inputValue; i++) {
            let studentDiv = document.createElement('div');
            studentDiv.classList.add('student-input');

            studentDiv.innerHTML = `
                <h2>Veuillez saisir les informations pour l'étudiant N°: ${i + 1}</h2>
                <label for="nom${i}">Nom:</label>
                <input type="text" id="nom${i}" name="nom${i}" required>
                <label for="prenom${i}">Prénom:</label>
                <input type="text" id="prenom${i}" name="prenom${i}" required>
            `;
            
            form.appendChild(studentDiv);
        }

        // Crée un bouton pour enregistrer les étudiants saisis
        let submitButton = document.createElement('button');
        submitButton.innerText = 'Enregistrer les étudiants';
        submitButton.type = 'button'; 
        submitButton.classList.add('new-product');
        submitButton.addEventListener('click', (e) => {
            e.preventDefault();
            saveStudents(inputValue);
        });

        form.appendChild(submitButton);
    }
}

// Fonction pour sauvegarder les informations des étudiants saisis
function saveStudents(numStudents) {
    listEtudiant = [];

    for (let i = 0; i < numStudents; i++) {
        let nom = document.getElementById(`nom${i}`).value;
        let prenom = document.getElementById(`prenom${i}`).value;
        listEtudiant.push({ nom, prenom });
    }
    
    console.log(listEtudiant); 
    createAttendanceForm();
}

// Liste prédéfinie d'étudiants
const listEtudPredefinie = [
    { nom: 'Diallo', prenom: 'Amadou Tidiane' },
    // Autres étudiants prédéfinis
];

// Ajoute un écouteur d'événement pour utiliser la liste prédéfinie
btnRandomUser.addEventListener('click', randomUser);

// Fonction pour remplir le formulaire avec une liste d'étudiants prédéfinie
function randomUser() {
    setup.classList.add('hide');
    contentForm.classList.remove('hide');

    form.innerHTML = ''; 

    form.innerHTML = `
        <h4>Département: ${choixDepartement.value}</h4>
        <h4>Niveau: ${choixNiveau.value}</h4>
        <h4>Matière: ${choixMatiere.value}</h4>
        <h4>Date: ${dateToDay()}</h4>
    `;

    listEtudiant = listEtudPredefinie;

    listEtudiant.forEach((etudiant, index) => {
        const studentDiv = document.createElement('div');
        studentDiv.classList.add('student');

        studentDiv.innerHTML = `
            <label class="lb1">${etudiant.nom} ${etudiant.prenom}</label>
            <label class="lb2"><input class="ipt1" type="radio" name="student${index}" value="present" required> Présent</label>
            <label class="lb3"><input class="ipt2" type="radio" name="student${index}" value="absent" required> Absent</label>
            <label class="lb4"><input class="ipt3" type="radio" name="student${index}" value="absentJustified" required> Absent Justifié</label>
        `;

        form.appendChild(studentDiv);
    });

    let btnPdf = document.createElement('button');
    btnPdf.classList.add('generatePdf', 'new-product');
    btnPdf.innerHTML = "Générer le PDF";
    btnPdf.addEventListener('click', generatePDF);
    form.appendChild(btnPdf);
    form.classList.add('order')
}

// Fonction pour créer un formulaire de présence après saisie des étudiants
function createAttendanceForm() {
    form.innerHTML = ''; 
    form.innerHTML = `
        <h4>Département: ${choixDepartement.value}</h4>
        <h4>Niveau: ${choixNiveau.value}</h4>
        <h4>Matière: ${choixMatiere.value}</h4>
        <h4>Date: ${dateToDay()}</h4>
    `;

    listEtudiant.forEach((etudiant, index) => {
        const studentDiv = document.createElement('div');
        studentDiv.classList.add('student');

        studentDiv.innerHTML = `
            <label class="lb1">${etudiant.nom} ${etudiant.prenom}</label>
            <label class="lb2"><input class="ipt1" type="radio" name="student${index}" value="present" required> Présent</label>
            <label class="lb3"><input class="ipt2" type="radio" name="student${index}" value="absent" required> Absent</label>
            <label class="lb4"><input class="ipt3" type="radio" name="student${index}" value="absentJustified" required> Absent Justifié</label>
        `;

        form.appendChild(studentDiv);
    });

    let btnPdf = document.createElement('button');
    btnPdf.classList.add('generatePdf', 'new-product');
    btnPdf.innerHTML = "Générer le PDF";
    btnPdf.addEventListener('click', generatePDF);
    
    // Ajoute un délai de 3 secondes avant d'ajouter le bouton PDF
    setTimeout(()=>{
        form.appendChild(btnPdf);
    }, 3000);  
    
    form.classList.add('order')
}

// Fonction pour générer un PDF de la présence des étudiants
function generatePDF() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    let date = new Date();
    let today = date.toLocaleDateString();

    // Ajoute le texte de base au PDF
    doc.text("Présence des Étudiants", 70, 10);
    doc.text(`Département: ${choixDepartement.value}`, 10, 20);
    doc.text(`Niveau: ${choixNiveau.value}`, 10, 30);
    doc.text(`Matière: ${choixMatiere.value}`, 10, 40);
    doc.text(`Date: ${today}`, 10, 50);

    const studentDivs = form.querySelectorAll('.student');
    let y = 60;

    let department = choixDepartement.value;
    let storageKey = `stockageEtudiant${department}`;
    let storedData = JSON.parse(localStorage.getItem(storageKey)) || [];

    // Ajoute les informations des étudiants au PDF et les stocke localement
    studentDivs.forEach((div, index) => {
        const nameLabel = div.querySelector('.lb1').textContent;
        const status = div.querySelector('input[type="radio"]:checked').value;
        doc.text(`${nameLabel} : ${status}`, 10, y);
        y += 10;
        
        let studentInfo = {
            nom: listEtudiant[index].nom,
            prenom: listEtudiant[index].prenom,
            niveau: choixNiveau.value,
            matiere: choixMatiere.value,
            departement: choixDepartement.value,
            status: status,
            date: dateToDay()
        };
        storedData.push(studentInfo);
    });

    localStorage.setItem(storageKey, JSON.stringify(storedData));
    doc.save('presence_etudiants.pdf');
}