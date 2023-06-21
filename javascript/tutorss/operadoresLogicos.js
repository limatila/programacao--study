val1 = 1
val2 = 2
str1 = '1'

// &&: and
if(val1 == val2 && val1 == str1){
    console.log('okay')
} else {
    console.log('you need to satisfact both of the conditions')
}

// ||: or
if(val1 == str1 || val2 === str1){
    console.log('okay')
} else {
    console.log('you need to satisfact one of the conditions')
}

// ?: ternary operator
function checkCase(num){
    return 1 === num ? 'verdadeiro' : false
}        //condição, ?, oque retornar se verdadeiro, :, o que retornar se falso
console.log(checkCase(123))

function checkTernary(num){
    1 === num ? console.log(num) : newVar = 23; //can do anything, single comand code.
    console.log(newVar)
    
}     //can also nest the questions(like ELIFs)
checkTernary(true)


//  :xor

