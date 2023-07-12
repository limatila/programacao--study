countDisplay = document.getElementById("countEl") //DOM, taking the value from HTML to modify it here

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

const editCount = (val) => { //quick edit the count number
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