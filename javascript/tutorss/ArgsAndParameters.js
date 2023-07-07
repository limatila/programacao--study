//args: o que é chamado
insertSomethin = (x) => x
console.log(insertSomethin('if this value is empty, it\'ll print the crude function'))

//parametros: o que é definido na própria função
function thisParam(value = 0){
    return value
}
console.log(thisParam())//if this value is empty, it'll print the value previously defined in the parameter


//spread operator: quantidade de argumentos flúida
insertVariousValues = (...args) => console.log(args)
insertVariousValues('1', '4', true, 3)

//can unpack some args using it:
theVars = [1, 2, 'WOWWWWW']
unpackingThis = (arr) => {
    final = [...arr, 2];
    arr[3] = 'ok'
    console.log(final) 
} //spread operator spreads the values and creates a copy
unpackingThis(theVars)


arr1 = [1, 2, 3, 4, 5]
//can spread op to take a part of an array
const [arr2, ...f] = arr1 //can only use it grabbing the last values. Still, i can skip values, no need for atributing it to a var
console.log(arr2, '+', f) 
