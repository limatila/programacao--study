myList = ['ok', 'gabu', 'átila', 'miosina', 'actinina', 'íris', 'mão']
console.log(myList.sort()) //not ideal, consider EN language.

orderedInPort = myList.sort(
    (a,b) => a.localeCompare(b)
) //compare with the current language. acentuados vêm depois.

console.log(orderedInPort) 

