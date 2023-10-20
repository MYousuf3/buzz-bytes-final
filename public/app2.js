const auth = firebase.auth();
const db = firebase.firestore();
const statusCheck = document.getElementById("nameCheck");
const goalInput = document.getElementById("goal");
const provider = new firebase.auth.GoogleAuthProvider();
const userRef = db.collection("users");
const hallForm = document.getElementById("hallDropdown");
const timeForm = document.getElementById("timingDropdown");
const optionOne = document.getElementById("option-one");
const optionTwo = document.getElementById("option-two");
const optionThree = document.getElementById("option-three");

const listOne = document.getElementById("listOne");
const listTwo = document.getElementById("listTwo");
const listThree = document.getElementById("listThree");

let unsubscribe;
let calGoal;
let restrictions;


function googleLogin() {
    console.log(auth.signInWithPopup(provider));
    
}

function googleLogout() {
    console.log(auth.signOut());
    console.log("signed out");
    window.location.href = "index.html";
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

async function genMeal() {
    let hall = hallForm.value;
    let timing = timeForm.value;
    
    const url = `http://172.20.10.2:8000/api/${hall}/${timing}/${calGoal}/['${restrictions}']`;

    const response = await fetch(url);
    const meals = await response.json();
    console.log(meals["meals"]);

    const allOptions = [optionOne, optionTwo, optionThree];
    const allLists = [listOne, listTwo, listThree];

    for (var i = 0; i < 3; i++) {
        allOptions[i].innerHTML = meals["meals"][i]["totalCalories"] + " calories";

        for (const [foodName, foodDetails] of Object.entries(meals["meals"][i]["constituentFoods"])) {
            var entry = document.createElement("li");
            entry.appendChild(document.createTextNode(foodName + " / Serving: " + foodDetails["serving"]));
            allLists[i].appendChild(entry)
            console.log(foodName, foodDetails["calories"]);
        }
    }

}



auth.onAuthStateChanged(async user => {
    if (user) {
        console.log(user.displayName);
        const snapshot = await userRef.where('email', '==', user.email).get();
          snapshot.forEach(doc => {
            console.log(doc.id, '=>', doc.data());
            calGoal = doc.data().goal;
            restrictions = doc.data().restrictions;
            statusCheck.innerHTML = user.displayName;
          });
          
        }
    else {
        statusCheck.innerHTML = "Not Signed in.";
    }
})

