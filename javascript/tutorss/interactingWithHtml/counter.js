countDisplay = document.getElementById("countEl") //DOM(Document Object Model), taking the value from HTML to modify it here

var count = 0 //starting value

const increment = () => { //to increase the value
    count++; 
    countDisplay.innerText = count
    console.log(countDisplay);
    
}

const decrement = () => { //to decrease it
    count--;
    countDisplay.innerText = count
    console.log(countDisplay)

}

const reset = () => { //to reset the count
    count = 0;
    countDisplay.innerText = count;
    console.clear()
    console.log("Contagem Resetada: " + count)

}

const editCount = (val) => { //quick edit the count number, only console
    count = val
    countDisplay.innerText = count
}


//saving our countings(should attribute to a file later)
const save = () =>{
    //could update it to produce tables
    saved = document.getElementById('saves')
    saved.innerText += "\n\\"+ count
        
    console.log("saved a count value")
    
}
const saveReset = () =>{ //for cleaning
    saved.innerText = "Your Saves: "  
}

const failPurchase = () =>{ //purposely fails a purchase, for demonstration
    purchaseText = document.getElementById("fail")
    purchaseText.textContent = "This purchase has failed. Please contact us."
    console.log("Purchase function Exec.")
}

const changeNikeHeader = () => { //changes the nike header with 'outerHTML' brute editing
    myText = document.getElementById("changeInputText")
    myHeader = document.getElementById("nikeHeader")

    myHeader.outerHTML = `<h2 id="nikeHeader">${myText.value}</h2>`
    console.log("The Nike header was changed!")
}
