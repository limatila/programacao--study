# True/False checkers for context generation
from projetos.Receitas.utils.contextGenerators import MAIN_BASE_CONTEXT

def checkAllFalse_NotFound(pageDetails_NotFound: dict[str, bool]) -> bool:
    for value in pageDetails_NotFound.values():
        if value == True:
            return False
    
    return True