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
    # 1: Menu
    # 2: Simple Menu
    # 3: Receita Detailed
    # 4: Collection Menu
    ## Diferenças: Menu para visualizar cards de receitas, Detail para visualizar amplicação do card.

    match (pageToContext):
        case None:
            pass
        case "DefaultMenu":
            generatedContext.update({"isDefaultMenu": True}) # Home
        case "SimpleMenu":
            generatedContext.update({"isSimpleMenu": True}) # Users / Categorias
        case "ReceitaDetail":
            generatedContext.update({"isReceitaDetail": True})
        case "CollectionMenu":
            generatedContext.update({"isDefaultMenu": True})
            generatedContext.update({"isCollectionMenu": True})
        case _:
            raise Exception(
                "Bad choice for genMainContext generator. " +
                "Allowed: \"DefaultMenu\", \"SimpleMenu\", \"ReceitaDetail\", \"CollectionMenu\"."
            )

    return generatedContext


def genNotFoundContext(pageToContext: int) -> str:
    ##Pra cada 404:
    # 1: Menu -- receitas não encontradas
    # 2: Simple Menu -- receitas não encontradas
    # 3: Receita Detailed -- receita não encontrada
    # 4: Collection Menu -- coleções não encontradas
    ## Diferenças: Menu para visualizar cards de receitas, Detail para visualizar amplicação do card.

    match (pageToContext):
        case None:
            return None
        case "DefaultMenu":
            return "não há receitas aqui"
        case "SimpleMenu":
            return "não há receitas aqui"
        case "ReceitaDetail":
            return "essa receita não existe"
        case "CollectionMenu":
            return "não há coleções aqui"
        case _:
            raise Exception(
                "Bad choice for genMainContext generator. " +
                "Allowed: \"DefaultMenu\", \"SimpleMenu\", \"ReceitaDetail\", \"CollectionMenu\"."
            )
