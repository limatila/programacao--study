#DO NOT RUN THIS FILE ALONE!

from .calculations import equation_on_two_degree 

#listagem de todos os modulos a serem importados com operador *
__all__: list[str] = [
 "calculations", 
 "formattings",
 "equation_on_two_degree", #para importar a função/variavel completa 
]

if __name__ != "__main__": #fora do init
    print(f"utilitaries imported")