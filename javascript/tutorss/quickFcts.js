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


const starts = (x) => x.startsWith("ok") //if i don't use '{}' in the code, it will be a function to 'return' a statement
console.log(starts("ok bro"))


//map, filter, reduce are methods, not functions(comparing it to pythons built in functions).
myDenseArray = [1, 3, 29, 4, 25, 6, 10, 50]

var filteringAndSumming = (arr) => arr.filter(x => x%2 !== 0).reduce((x, z) => x + z) //filter filtering by odd numbers, reduce is summing it all
console.log(filteringAndSumming(myDenseArray))

var doubling = (arr) => arr.map(x => x*2)//iterating trough all, doubling the values
console.log(doubling(myDenseArray))


//sort also takes a function as a arg, to evaluate the sorting. it can't sort numbers by itself
console.log("sorting:")
arr1 = Array(1, 20, 15, 80, 37, 75, 1050)
console.log(arr1)

arr1.sort(function(a, b){return a - b})//the contrary for descending order
console.log(arr1)