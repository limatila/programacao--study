//DOMs
textInput = document.getElementById("inp1")
saveInputButton = document.getElementById("saveInpButton")
saveTabButton = document.getElementById("saveTabButton")
linkShow = document.getElementById("linkShowEl")

websiteLinks = [];
//functions
const saveInput = () =>{
    if(textInput.value.length === 0){
        alert("Empty Input!");
        throw console.error("Empty Input! function not executed.")
    }

    websiteLinks.push(textInput.value)

    //TODO: show it.
    totalContent = ""
    for(i = 0; i < websiteLinks.length; i++){
        totalContent += websiteLinks[i] + "\n"
    }

    linkShow.innerText = totalContent //user innerText for escaping literals.
    linkShow.hidden = false

    textInput.value = null //clear
};

const saveTab = () =>{

};