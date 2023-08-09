//There are many ways to select elements from a page.

welcomeHeader = document.getElementById("welcome")//gets by the id that's provided in the element's tag
console.log("Welcome Header: ", welcomeHeader)

images = document.getElementsByClassName('totem')//gets by the class name(all of them)


console.log(document.querySelector('body'))//catch the element tag. Will only grab the first that appears

var links = document.querySelectorAll('link')//catch all the elements
console.log(links)// will place them in a 'NodeList'(like an array, can be acessed and modified.)

console.log(images)
const imgChanger = (inp) => { //modifying source attributes to change between photos. 2 buttons are included in 'javascript/live.html'
    switch(inp){
        case 'change':{
            images[1].src = "../html/images/totem.gif"
            console.log('changed!')
            break;
        }
        case 'reset':{
            images[1.].src = "/html/images/sucessor.png"
            console.log('reseted!')
            break;
        }
    }
    
}