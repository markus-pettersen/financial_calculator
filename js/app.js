const investButton = document.querySelector("#investButton");
const bondButton = document.querySelector("#bondButton");
const investLink = document.querySelector("#investLink");
const bondLink = document.querySelector("#bondLink");
const investForm = document.querySelector("#investForm");
const bondForm = document.querySelector("#bondForm");

investButton.addEventListener("click", investCalc)
bondButton.addEventListener("click", bondCalc)
investLink.addEventListener("click", investSwitch)
bondLink.addEventListener("click", bondSwitch)

let investActive = true;

function investCalc(){
    let investCap = document.getElementById("investCap").value
    let investInterest = document.getElementById("investInterest").value / 100
    let investTime = document.getElementById("investTime").value
    let totalAmountSimp = investCap * (1 + (investInterest) * investTime)
    let totalAmountComp = investCap * Math.pow((1+ (investInterest)), investTime)
    if (isNaN(totalAmountSimp)){
        textOutput = 'Invalid input'
    } else {
        textOutput = 'Total amount:<br>'
                + totalAmountSimp.toFixed(2) + ' (simple)'
                + '<br>' + totalAmountComp.toFixed(2) + ' (compound)'
    }
    document.getElementById("investResult").innerHTML = textOutput
}

function bondCalc(){
    let bondProp = document.getElementById("bondProp").value
    let bondInterest = document.getElementById("bondInterest").value / 1200
    let bondTime = document.getElementById("bondTime").value
    let bondAmount = (bondInterest * bondProp) / (1 - Math.pow((1 + bondInterest), -bondTime))
    if (isNaN(bondAmount)){
        textOutput = 'Invalid input'
    } else {
        textOutput = 'Monthly payment: ' + bondAmount.toFixed(2)
    }
    document.getElementById("bondResult").innerHTML = textOutput
}

function investSwitch(){
    if (!investActive){
        investActive = true
        document.getElementById("investResult").innerText = ""
        investForm.classList.remove("inactive")
        bondForm.classList.add("inactive")
    }
}

function bondSwitch(){
    if (investActive){
        investActive = false
        document.getElementById("bondResult").innerText = ""
        investForm.classList.add("inactive")
        bondForm.classList.remove("inactive")
    }
}
