from utilitaries import * #* Para todos os modulos
# from utilitaries import calculations as calcs #selecionando cada modulo, não precisando ser especificado em '__all__''

calculations.add(10, 279)

#depois de adicionado em '__all__'
equation_on_two_degree(1, 2, 3)


class Book:
	title = "Senhor dos Anéis";
	def read():
		print("reading...")
		
#outros modulos que foram tambem carregados
aBook = Book()
print(formattings.formatNameAttr(aBook))