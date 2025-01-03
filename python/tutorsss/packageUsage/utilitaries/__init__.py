
#listagem de todos os modulos a serem importados com operador *
__all__: list[str] = [
 "calculations", 
 "formattings"
]

if __name__ != "__main__": #fora do init
    print(f"utilitaries imported")
else:									  #dentro do init
	print("python running!")