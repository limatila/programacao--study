function Foo(){
    console.log('foo printed')
    return "f" //will be adressed in the Foo() ocurrence memory
}

function foo2(){
    localVar = 2
    return localVar    //o return vai trazer a variavel para o Global Scope
}

console.log(foo2())
localVar++
console.log(localVar) //will work here after 'foo2' is called, because it was returned in the function
// if the var wasn't returned, it would stay on the function

//to keep in local, indenpendently of the return command, use let
function foo3(){
    let myArray = [2, true]
    return myArray
}

console.log(foo3())
try {   //see later on in 'tryCatch.js'
    myArray.push([10])
    console.log(myArray)
} catch(RefereceError) {  //arg is wrong..
    console.log("Reference Error dealed.")  //the 'myArray' isn't defined in global scope
}