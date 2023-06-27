//a function attributed to a var(making it the var reference)
var anAnonimous = function(){
    return 0
}

//an Arrow function: 'var' 'varName' = (args) => {return} 'value'.
var anArrow = () => "THIS"

//can do commands with it
var anArrow = (a) => console.log("wow " + a)

const integratingIt = () => { //should be const all times
    anArrow('atila')
    console.log(1+1)
}//a better way to write functions quickly
