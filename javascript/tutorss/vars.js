//var declaring:
let This_is_a_LOCAL_Var = "wont be able to be used in global \
scope, if it's declared in local scope, \
and cannot be set twice"
var this_is_a_GLOBAL_Var = "will be able to be used in every other scope"
const this_Var_cannot_change = "it's really unmodifiable."

const this_Array_can_be_changed = [3, 2, 1]//with bracket notation
this_Array_can_be_changed[2] = "can"
Object.freeze(this_Array_can_be_changed)//prevent mutation in all cases. won't raise error

//don't declare varNames like this, plz
//use CAPSLOCK for constants.


//nums and math------------------------------------------------------------
var myVar = 2
myVar++                         //adding one, and subs
myVar--; console.log(myVar)
myVar /=2; console.log(myVar)   //quick divisor
myVar *=10; console.log(myVar)  //quick multip

aNum = '12'
aNum = parseInt(aNum)   //convert a possible number to Int, if there are any other characters in the front, it'll give NaN
console.log(aNum + 100)
//parseFloat also exists


//arrays-------------------------------------------------------------------
var myArray = [true, myVar, 27, 'Atila']
console.log(myVar + myArray[2], 'is my Sum')    //concatenação com , entre str e vars, e com + entre 2 strs

myArray.push(myVar); console.log(myArray)       //appending, myVar is '10'
console.log(myArray.length, "is the array length")
//.shift removes the first el.; .pop removes the last el.
//.unshift returns the el. to the first position of the array


//strings------------------------------------------------------------------
var myStr = "FirstLine\n\t\\SecondLine\nThirdLine" //see escaping literals
console.log(myStr)

myStrSplited = myStr.split("\n")       //need to assign it
console.log(myStrSplited)
myStrSliced = myStr.slice(3,8)
console.log(myStrSliced)


//equality-----------------------------------------------------------------
var val1 = 10
var val2 = "10"
console.log(val1 == val2)   //em js, caracteres iguais são avaliados com '=='
console.log(val1 === val2)  //para avaliar entre classes, use '==='
//!= e !== para inequações

//copying------------------------------------------------------------------