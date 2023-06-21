var myDog = {       //like python's dict
    'name': 'Luna',
    'color skin': 'orange yellowed',
    'bites': true,
    'age': 3.2
}
console.log(myDog)


console.log(myDog.bites)
myPhrase = (myDog.name + ' was a happy dog, it\'s ' + myDog.bites + ' that she bited a lot.')
console.log(myPhrase)
console.log(myDog['color skin']) //only to use with numbers or with spaces between

//i can nest it infinitely ;). don't forget the ',' after each attribute
var myTought_Rn = {
    'myStudies':{
        'completed': ['Python'],
        'ongoing': ['Javascript', 'Html5'],
        'planned': ['C', 'Python.Pandas', 'Typescript', 'React']
    },
    
    'maybeLove': 'Anna..',
    
    'musics':{
        'drum': 'needing to practice.. it\'s so cool..',
        'favorites':{
            'rock': ['SOAD', 'metallica', 'queens of the stone age'],
            'mpb': ['geraldo vandré', 'rita lee', 'o rappa', 'lenine'],
            'hiphop': ['criolo', 'ice cube', 'racionais'],
            'funk': 'os mais estourados possíveis.'
        },
        'singin': 'i\'m already doing it.'
    }
}

console.log(myTought_Rn.musics.favorites.hiphop[2]) //oque é oque é, clara e salgada


function soma(num){     //defining random fct
    value = num + 2
    console.log(value)
    return 'the fct was called'   //in browser the returned value will always be logged
}

myTought_Rn.myStudies.myFunction = {     //adding to object memory
    'mySoma': soma
}
//can call here or in the console.