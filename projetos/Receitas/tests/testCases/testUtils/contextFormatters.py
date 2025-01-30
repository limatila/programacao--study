
from projetos.Receitas.utils.contextGenerators import MAIN_BASE_CONTEXT

def filterDefaultContextKeys(generatedContext: dict[str, bool]) -> dict:
    # Exiting
    if len(generatedContext) == len(MAIN_BASE_CONTEXT):
        print("[Warn] Contexto não precisa ser filtrado.")
        return generatedContext

    return {
        key: value 
        for key, value in generatedContext.items()
        if key in MAIN_BASE_CONTEXT
    }