myObj = {
    'name': 'Atila',
    'age': 18,
    'baby': false,
    'phrase': 'little boy, big man',
};

//copying attributes to vars:
var {name : a, age : b, baby : c, phrase : d} = myObj;
//'vars type' {'what to copy : copy to'} = 'the actual object with the attributes'
console.log(d)

mySecObj = {
    'room': {
        'name': 'this attribute should be logged'
    }
}
var {name : l} = mySecObj.room; //for deep copy
console.log(l)
//this creates a separated reference, vars won't change values together.

//can also nest it like this:
var {room : {name : k}} = mySecObj //copia 'room' para memoria seguinte, e copia o attr 'name' para a var seguinte, o nome do objeto sendo atribuido '='
console.log(k)


//you can skip values in arrays:
arr1 = [1, 2, 3, 4, 5]
const [x, y, ,z] = arr1 //only included variables are considered trough the order
console.log(x, y, z)


//returning to some Obj operations, it's possible to grab only parts of the obj:
function logAttrs({name, phrase}){ //this can be a fast grab, rather then typing the whole Obj name
    console.log(name, 'stands for:', phrase)
    console.log("END OF CODE")
}
logAttrs(myObj)