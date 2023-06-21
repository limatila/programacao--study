//easy random decimal number:

function randPercentage(){
    soma = Math.floor(Math.random() * 1000)   //floor arredonda, random randomiza. 
                                            //multiplicando por 10 pra mostrar o valor porque só mostra a primeira casa
    soma/=10 //1000 / 10 = 100%! 
    return soma
}

console.log(randPercentage())