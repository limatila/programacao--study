# JSON explanation

*A JSON file (JavaScript Object Notation) can store any variables or configs that could be loaded to a variable in JS.
*Also, It's supported by various languages.

It's variables are stored in the common Object Notation, with key-value pairs.
1. [] start an Array
2. {} start an Object

* A Json can store one value in a key-value object, or contain an general Array.
* A Object can be used to store multiple key-value pair values.
* ALL Json **MUST** be wraped in one array to assign multiple objects, which serves the whole file. then, create objects that store the vars.
* For importing, the script must be flagged in the page as a " type = 'module' ". A whole set of rules must be applied to program in JS Modules.

### Then, to import as a var and assign to another single var in JS:
    import 'data' from "./thisFile.json" assert { type: 'json' }
    var myImportedData = Object.assign(data)

### To convert an object to JSON string and save it:
    stringified = JSON.stringify(myImportedData) // or 'data.
    