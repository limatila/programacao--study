function callValue_byNumber(num){
    switch(num){
        case 1:
            return 'one'  
        case 2:
            return 'two'
        case 3:
            return 'three'
        default:    //will execute if the cases don't match.
            return 'not in the list, only 1-3'            
    }
}

console.log(callValue_byNumber(3))
console.log(callValue_byNumber((3-2))) //doing math
console.log('')

function toTheLastNumber(num){
    switch(num){
        case 6: console.log('six')
        case 5: console.log('five')
        case 4: console.log('four')
        case 3: console.log('three')
        case 2: 
            return 'two'    //notice that returning will always 'break' the checks    
        case 1: console.log('one')
        default:
            return 'starts on Six.'
    }
}

console.log(toTheLastNumber(6)) //need the 'console.log' to see 'case 2'

console.log('')

function isDiaUtil(numDay){
    answer = ''
    switch(numDay){     //o main use da switch é alternar entre casos com respostas repetidas
        case 'dom':
        case 'sab':
            answer = 'não é dia útil, stream apenas hehe'
            break
        case 'seg':
        case 'ter':
        case 'qua':
        case 'qui':
        case 'sex':
            answer = 'é um dia útil, hora de trabalhar hehe'
            break
        default: console.log('escolha os dias da semana: dom, seg, ter, qua, qui, sex, sab')
    }
    return answer
}

console.log(isDiaUtil('seg')) 
