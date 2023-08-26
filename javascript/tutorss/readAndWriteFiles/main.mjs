import { readFile, writeFile, appendFile, readdir } from "fs"; //import file system module



//path, encoding, function
readFile("c:\\Users\\uiuiudy\\Desktop\\programacionesss\\javascript\\tutorss\\readAndWriteFiles\\output.txt", 'utf-8', (err, data) => {
    if(err){
        console.log(err)
        return;
    }
    var a = 2+2
    console.log(a, data) //anything here
})


var contentToFile = "Adding THis! aaaaaba" //in .mjs, all vars must be specified


//path, content, err handling
//can be fs.appendfile, same args
writeFile("c:\\Users\\uiuiudy\\Desktop\\programacionesss\\javascript\\tutorss\\readAndWriteFiles\\output.txt",
             contentToFile,
             err => {
    if(err){console.err}
    }
)

//do not read and write in the same time. will bug and not read properly


appendFile("c:\\Users\\uiuiudy\\Desktop\\programacionesss\\javascript\\tutorss\\readAndWriteFiles\\output.txt",
            "\nIm Appending This Rn", err => {if(err){console.err}})

//list all files
readdir("c:\\Users\\uiuiudy\\Desktop\\programacionesss\\javascript\\tutorss\\readAndWriteFiles", (err, content) => {if(err){console.err}; console.log(content)})
