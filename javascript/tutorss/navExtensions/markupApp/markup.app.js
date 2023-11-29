//DOMs
textInput = document.getElementById("inp1")
saveInputButton = document.getElementById("saveInpButton")
saveTabButton = document.getElementById("saveTabButton")
linkShow = document.getElementById("linkShowEl")

websiteLinks = [];
//functions
const saveInput = () => {
    if(textInput.value.length === 0){ //err if input is empty
        alert("Empty Input!");
        throw console.error("Empty Input! function not executed.")
    }

    websiteLinks.push(textInput.value)

    //TODO: show it.
    totalTextContent = "";
    for(i = 0; i < websiteLinks.length; i++){
        totalTextContent += websiteLinks[i] + "\n"
    }

    linkShow.innerText = totalTextContent //user innerText for escaping literals.

    textInput.value = null //clear
};


const resetSaves = () => {
    websiteLinks = [];
    linkShow.textContent = null;
    textInput.value = null;
};


const saveTab = () =>{ //!how to chose a tab?
    
};