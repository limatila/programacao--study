import pandas as pd
from fcts import tspac, endCode, line
produtos = {
     'nomes' : ['xbox', 'music', 'pc',],
     'amount' : [1, 221, 10],
     'available' : [False, True, False]
}

   
tabela = pd.DataFrame(produtos)
print(tabela)
tabela = tabela.drop('available', axis=1)
print(f'\n tabela depois de dropar availables:  \n{tabela}')
print("")
tabela.rename(columns = {'nomes' : 'Names'}, inplace = True)
print(f'\n tabela depois de renomear nomes para inglês: \n{tabela}')
print("")
tabela.rename(columns = {'amount' : 'Amount'}, inplace = True)
print(f'\n tabela depois de capitalizar amount: \n{tabela}')

tabela.rename(columns = {'Amount' : 'AMOUNT', 'Names' : 'NAMES'}, inplace = True)
print(f'\n tabela após CAPSLOCK \n{tabela}')

tspac(); line(25)
print(tabela.describe())

tspac()
endCode()