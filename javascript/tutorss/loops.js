i = 0
var ArrayOfVars = []

while(i < 5){
    varName = "var" + String(i)
    ArrayOfVars.push(varName)
    i++
}

i = 0 //need to reset
for(i; i<5; i++){
    console.log(ArrayOfVars[i])
}

//can reset(or declare) in for loop
for(i = 0; i<=5; i++){
    if(i%2 != 0){   //only odds
        console.log(i)
    }
}
a
console.log('')
i = 0//execute loop once before checking again
do {
    i++
    console.log(i)
} while (i<10)

