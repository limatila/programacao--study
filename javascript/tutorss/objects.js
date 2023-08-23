var myDog = {       //like python's dict
    'name': 'Luna',
    'colorSkin': 'orange yellowed',
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


//simple attributing(see arrow function in 'quickFcts.js'):
const myObjHas = (name, use) => ({name, use}) //function 
var thisObj = myObjHas('pen', '2 days')
console.log(thisObj)


//a obj can store functions inside it.
myDog.bark = (pont) => { 
    if (pont in "ABCDEFGHIKKLMNOPQRSTUVWXYZ"){
        throw console.error('not permited')
    } else {
        console.log('bark'+pont)
    }
}


//classes: o molde para os objetos criados a partir dela
class addDog{
    constructor(name, colorSkin, bites, age){
        this.name = name
        this.colorSkin = colorSkin
        this.bites = Boolean(bites)
        this.age = parseInt(age)
        console.log("new dog added")
    }

    bark(pont){
        console.log('bark'+pont)
    }
    
}

const mySecDog = new addDog('Átila', 'black', false, 9.0) //now this is real OOP.


//method chaining: using two consecutive methods
class stringTreatment{
    constructor(str){
        this.primaryValue = str //setup a string to work with
        console.log("new string treatment added")
    }

    addThing = (thing) => {
        this.primaryValue += thing
        return this     //return entire object to be readed
    }

    capitalizeString = () => {
        this.initial = this.primaryValue.charAt(0).toUpperCase() //?: really need to use 'this.' in every var?
        this.final = this.primaryValue.slice(1)
        this.primaryValue = this.initial + this.final  
        return this.primaryValue    //returning only the value, not the object. won't be able to chain another method.
    }
}

thisString = new stringTreatment("essa String aki")
console.log(thisString.addThing(' é massa').capitalizeString(), ';it\'s a chained processed method')
console.log(thisString.initial)

//prototype: