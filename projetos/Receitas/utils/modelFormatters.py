#Formatadores de string para models

from django.db.models import Model

def formatCategoryName(entryCategory) -> str:
    return f"{entryCategory.get_categoryType_display()} ({entryCategory.categoryType})"


def formatReceitaName(entryReceita) -> str:  # Deve só rearranjar o default + nome da receita
    return f"Receita({entryReceita.idPage}) -- {entryReceita.titleReceita}"
