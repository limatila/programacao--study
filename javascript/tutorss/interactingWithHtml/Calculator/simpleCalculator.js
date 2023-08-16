//how to implement functions with a function?

function calculate(method){
    var num1 = document.getElementById("num1Input").value
    var num2 = document.getElementById("num2Input").value
    num1 = parseInt(num1); num2 = parseInt(num2) //elements in html will ALWAYS be treated as string

    var total = 0

    switch(method){
        case 'add':{ //needs fix: adding is handling as a string
            total = num1 + num2
            console.log("added: " + total)
            break;
        }
        case 'subtract':{
            total = num1-num2
            console.log("subtracted: " + total)
            break;
        }
        case 'multiply':{
            total = num1*num2
            console.log("multiplied: " + total)
            break;
        }
        case 'divide':{
            total = num1/num2
            console.log("divided: " + total)
            break;
        }
        default:{console.log("select a valid calculation"); //TODO: const pow 
                return "Not possible. Check console.";
                break}
    }
    result = document.getElementById("calcResult") 
    result.innerText = total
}

//how to use a seperated function to modify the p?

const reset = () =>{
    document.getElementById("calcResult").textContent = 0
    document.getElementById("num1Input").value = null
    document.getElementById("num2Input").value = null

    console.log("RESETED.")
}

getRandom = (max) => { //recursive functions will have max memory limits. NOT A SAFE WAY
    let rand = Math.random()
    console.log('random is' + rand)
    val = Math.floor(rand * max); 
    if(val == 0){
        getRandom(max)
    }
    return val

}