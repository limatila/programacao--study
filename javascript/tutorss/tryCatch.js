//To avoid realtime errors that stop the execution of the code.
const a = 2
try{
    a = 15
} catch(err) { //if error occurs, will be put on 'err'
    console.error("error ocurred! " + err.name + " " + err.message + "\n" + err.stack) //3 different error properties to log. Name, Message, or full error stack.
} 

console.log("\na is " + a)

b = [a, ]
const appendToB = (indexPrompt) => {
    try {               //try to compute this
        console.log("\nappending...")
        b.append(indexPrompt)
        console.log("finished trying succesfully!") //never gets here after an error

    } catch (err) {     //catches an error
        console.log(err.message)

    } finally {         //always will execute!
        console.log("\npushing...")
        b.push(indexPrompt)

    } 
}
appendToB(10)
console.log("b is " + b)


//creating costum errors:
function costumError(message){ //as an object
    this.message = message + ", gg not good";
    this.name = "customError";
    this.stack = `${this.name}: ${this.message}` //full error stack
} //will be breakable in the 3 different properties mentioned in line 7.

try {
    console.log("")
    throw new costumError(" happened") //!: but how do i create a condition for the error to happen?
} catch (errCostum) {
    console.error(errCostum.name + errCostum.message)
} finally {
    console.log("for sure an error happened... or not, i know nothing.")
} 

//generic error
throw new Error("last line error!") 