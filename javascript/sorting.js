myList = ['ok', 'gabu', 'átila', 'miosina', 'actinina', 'íris', 'mão']
console.log(myList.sort()) //not ideal, consider EN language.

orderedInPort = myList.sort(
    (a,b) => a.localeCompare(b)
) //compare with the current language. acentuados vêm depois.

console.log(orderedInPort) 

inorderedInPort = myList.sort(
    (a,b) => b.localeCompare(a)
) //inverted

console.log(inorderedInPort)


const numbs = [1, 18, 17, 3, 90]
console.log(numbs.sort(), "not ideal") //will bug out

//specify the goal for better precision
console.log(numbs.sort(
    (a,b) => a-b
))
console.log(numbs.sort(
    (a,b) => ((b**3)-a) //1 no final porq 1³ = 1, 1 < o resto
)) 
//sorting WILL change the original var. need to create a copy, or use a local scope to avoid changes. const won't prevent it.

