myVar = '2' + 2 //22, not doing math
myInt = parseInt(myVar)
console.log(myInt + 2) //24, doing math

//can use it with radixs(uma especificação de qual sistema está sendo usado):
function convertInt(str){
    return parseInt(str, 2) //esta var, para a base '2'(binario)
} 

binaryVar = '10010' //16 + 2.
newVar = convertInt(binaryVar)