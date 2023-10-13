import data from './config.json' assert {type: "json"};

const myArraye = Object.assign(data); //an array in this example

console.log(myArraye);

//pick a obj from the array
var myObj = myArraye[2]

console.log(JSON.stringify(myObj));

//save the JSON back to the file after changes:
myObj.age = 57
console.log(myObj.age)

import { writeFile } from 'fs' assert {type: "json"};
function saveToFile(obj){
    
}