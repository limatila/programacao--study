#Formatadores de querys para views

#TODO: query de Receitas.all() (restringindo tamanho por seção do Menu)

def topLikes(entryQueryReceita):
    return entryQueryReceita.order_by("-likes")
