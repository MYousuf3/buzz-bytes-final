const auth = firebase.auth();
const db = firebase.firestore();
const statusCheck = document.getElementById("nameCheck0");
const goalInput = document.getElementById("goal");
const provider = new firebase.auth.GoogleAuthProvider();
const userRef = db.collection("users");
const hallRef = db.collection("halls");
const westVillageRef = db.collection("halls").doc("west-village");
const naveRef = db.collection("halls").doc("north-ave-dining-hall");
const brittainRef = db.collection("halls").doc("brittain");

const dietInput = document.getElementById("dropdown-1");
const restrictionsInput = document.getElementById("dropdown-3");

let startVal = statusCheck.innerHTML;
console.log(startVal);
let unsubscribe;

if (statusCheck.innerHTML != startVal) {
    window.location.href = "page3.html";
}


function googleLogin() {
    console.log(auth.signInWithPopup(provider));
    
}

function googleLogout() {
    console.log(auth.signOut());
    console.log("signed out");
}

/*
async function britBreakfast(async) {
    const snapshot = await brittainRef.get();
    console.log(snapshot.data().breakfast);
    const paragraph = document.getElementById("result-paragraph");
    paragraph.innerHTML = snapshot.data().breakfast.toString();
}
async function willageBreakfast(async) {
    const snapshot = await westVillageRef.get();
    console.log(snapshot.data().breakfast);
    const paragraph = document.getElementById("result-paragraph");
    paragraph.innerHTML = snapshot.data().breakfast.toString();
}
async function naveBreakfast(async) {
    const snapshot = await naveRef.get();
    console.log(snapshot.data().breakfast);
    const paragraph = document.getElementById("result-paragraph");
    paragraph.innerHTML = snapshot.data().breakfast.toString();
}
async function britLunch(async) {
    const snapshot = await brittainRef.get();
    console.log(snapshot.data().lunch);
    const paragraph = document.getElementById("result-paragraph");
    paragraph.innerHTML = snapshot.data().lunch;
}
async function willageLunch(async) {
    const snapshot = await westVillageRef.get();
    console.log(snapshot.data().lunch);
    const paragraph = document.getElementById("result-paragraph");
    paragraph.innerHTML = snapshot.data().lunch;
}
async function naveLunch(async) {
    const snapshot = await naveRef.get();
    console.log(snapshot.data().lunch);
    const paragraph = document.getElementById("result-paragraph");
    paragraph.innerHTML = snapshot.data().lunch;
}
async function britDinner(async) {
    const snapshot = await brittainRef.get();
    console.log(snapshot.data().dinner);
    const paragraph = document.getElementById("result-paragraph");
    paragraph.innerHTML = snapshot.data().dinner;
}
async function willageDinner(async) {
    const snapshot = await westVillageRef.get();
    console.log(snapshot.data().dinner);
    const paragraph = document.getElementById("result-paragraph");
    paragraph.innerHTML = snapshot.data().dinner;
}
async function naveDinner(async) {
    const snapshot = await naveRef.get();
    console.log(snapshot.data().dinner);
    const paragraph = document.getElementById("result-paragraph");
    paragraph.innerHTML = snapshot.data().dinner;
}

function submit() {
    // Get the selected values from the first set
    var set1Value = document.querySelector('input[name="set1"]:checked').value;
    
    // Get the selected values from the second set
    var set2Value = document.querySelector('input[name="set2"]:checked').value;
    if (set1Value == "brittain") {
        if (set2Value == "breakfast")
            britBreakfast();
        if (set2Value == "lunch")
            britLunch();
        if (set2Value == "dinner")
            britDinner();
    }
    if (set1Value == "north-ave-dining-hall") {
        if (set2Value == "breakfast")
            naveBreakfast();
        if (set2Value == "lunch")
            naveLunch();
        if (set2Value == "dinner")
            naveDinner();
    }
    if (set1Value == "west-village") {
        if (set2Value == "breakfast")
            willageBreakfast();
        if (set2Value == "lunch")
            willageLunch();
        if (set2Value == "dinner")
            willageDinner();
    }
}
*/

function signIn() {
    window.location.href = "page3.html";
}


auth.onAuthStateChanged(async user => {
    if (user) {
        console.log(user.displayName);
        const snapshot = await userRef.where('email', '==', user.email).get();
        if (snapshot.empty) {
            userRef.add({
                name: user.displayName,
                email: user.email,
                height: 70,
                weight: 140,
                sexMale: true,
                activity: 4,
                goal: dietInput.value,
                restrictions: restrictionsInput.value  
            });
          }
          snapshot.forEach(doc => {
            console.log(doc.id, '=>', doc.data());
          });
          statusCheck.innerHTML = user.displayName;
          //window.location.href = "page3.html";
        }
    else {
        statusCheck.innerHTML = "Not Signed in.";
    }
})

