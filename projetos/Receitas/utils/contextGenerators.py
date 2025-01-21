#Geradores padronizados de 'Context's para Views.py

MAIN_BASE_CONTEXT = {
    "isDefaultMenu": False,
    "isSimpleMenu": False,
    "isReceitaDetail": False,
    "isCollectionMenu": False,
}

def genMainContext(pageToContext: int) -> dict[str, bool]:
    generatedContext = dict(MAIN_BASE_CONTEXT)

    ##Pra cada view:
    # 1: Home Menu
    # 2: Receita Detailed
    # 3: Category Menu
    # 4: Collection Menu
    ## Diferenças: Menu para visualizar cards de receitas, Detail para visualizar amplicação do card.

    match (pageToContext):
        case 1:
            generatedContext.update({"isDefaultMenu": True}) #Home, Lista - Coleções
        case 2:
            generatedContext.update({"isSimpleMenu": True}) # Users / Coleções / Categorias
        case 3:
            generatedContext.update({"isReceitaDetail": True})
        case 4:
            generatedContext.update({"isCollectionMenu": True})
        case _:
            raise Exception(
                "Bad choice for genMainContext generator. Only allowed integers between 1 and 4."
            )

    return generatedContext


def genNotFoundContext(pageToContext: int) -> str:
    ##Pra cada 404:
    # 1: Home Menu -- receitas não encontradas
    # 2: Receita Detailed -- receita não encontrada
    # 3: Category Menu -- receitas não encontradas
    # 4: Collection Menu -- coleções não encontradas
    ## Diferenças: Menu para visualizar cards de receitas, Detail para visualizar amplicação do card.

    match (pageToContext):
        case 1:
            return "não há receitas aqui"
        case 2:
            return "essa receita não existe"
        case 3:
            return "não há receitas aqui"
        case 4:
            return "não há coleções aqui"
        case _:
            raise Exception(
                "Bad choice for genMainContext generator. Only allowed integers between 1 and 4."
            )
