MAIN_BASE_CONTEXT = {"isHomeMenu": False, #TODO: Padronizar em: receita-card.html, def generateContext, home-receitas.html, models.py(?)
                     "isReceitaDetail": False,
                     "isCategoryMenu": False,
                     "isCollectionMenu": False}

#Geradores padronizados de 'Context's para Views.py


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
            generatedContext.update({"isHomeMenu": True})
        case 2:
            generatedContext.update({"isReceitaDetail": True})
        case 3:
            generatedContext.update({"isCategoryMenu": True})
        case 4:
            generatedContext.update({"isCollectionMenu": True})
        case _:
            raise Exception(
                "Bad choice for genMainContext generator. Only allowed integers between 1 and 4."
            )

    return generatedContext