import pandas as pd


produtos = {
     'nomes' : ['xbox', 'music', 'pc', 'cum'],
     'amount' : [1, 221, 2, '50L'],
     'available' : [False, True, False, True]
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
print("")
tabela.rename(columns = {'Amount' : 'AMOUNT', 'Names' : 'NAMES'}, inplace = True)
print(f'\n tabela após CAPSLOCK \n{tabela}')
print("")
print(f'\n {tabela.info()} \n')
print("END OF CODE")