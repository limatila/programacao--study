// develop title method based on the one from python. Evaluates Strings and Arrays.

function title(value){
    if (typeof(value) === 'string'){ //if a string (if array 'typeof' will return 'object')
        initial = value.charAt(0).toUpperCase()
        final = value.slice(1)
        value = initial + final
        return value
    } else if(Array.isArray(value) === true){  //if array
        for(i = 0; i < value.length; i++){
            initial = value[i].charAt(0).toUpperCase()
            final = value[i].slice(1)

            value[i] = initial + final
        } 
        return value
    } else {
        console.error("Conversion not possible.")
    }
}

console.log(title("atila"))