//how to implement functions with a function?

const calculate = (method) => {
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
    document.getElementById("randomMaxInput").value = null

    console.log("RESETED.")
}


function generator(max){let rand = Math.random()
    val = Math.round(rand * max); 
    if(val <= 1){
        getRandom(max)
    }
    return val
}

const getRandom = () => { //recursive functions will have max memory limits. NOT A SAFE WAY

    var genInput = document.getElementById("randomMaxInput").value

    let random_1 = generator(genInput)
    let random_2 = generator(genInput)

    num1 = random_2
    num2 = random_1

    document.getElementById("num1Input").value = num1
    document.getElementById("num2Input").value = num2 
    console.log("Random numbers generated:", num1, num2)
} //! fix huge amout of stacks in low input number