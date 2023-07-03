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
var {name : z} = mySecObj.room; //for deep copy
console.log(z)
//this creates a separated referece, vars won't change values together.