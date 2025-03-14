from sqlmodel import select
from models import *
from .models import get_engine, Session

#! Startup data: only execute once!
if __name__ == "__main__":
    pgsql = get_engine("pgsql")

    #pokemons 3 and 4
    with Session(pgsql) as session:
        session.add(Pokemon(id=3, name="Venusaur"))
        session.add(Pokemon(id=4, name="Charmander"))
        session.commit()

    #pokemon ability Tackle (common in pokemons 1 and 3)
    with Session(pgsql) as session: 
        session.add(Ability(name="Tackle", effect="damage", generation=1))
        session.commit()

    #adding compatibility to pokemons 1 and 3
    with Session(pgsql) as session:
        #* Selecting Tackle ability
        tackleStatement = select(Ability).where(Ability.name == "Tackle")
        tackleAbility = session.exec(statement=tackleStatement).one_or_none() #.fetchall(), .all(), .one(), .first(), and some more
        print(tackleAbility)

        session.add(AbilityCompatibility(FK_pokemon_id=1, FK_ability_id=tackleAbility.id))
        session.add(AbilityCompatibility(FK_pokemon_id=3, FK_ability_id=tackleAbility.id))
        session.commit()

    #adding categorys to the Tackle ability
    with Session(pgsql) as session:
        categoryToAdd = AbilityCategory(name="Normal", color="#B6B6A8")
        session.add(categoryToAdd)
        session.commit()

        physicalStatement = select(AbilityCategory).where(AbilityCategory.name == categoryToAdd.name)
        physicalCategory = session.exec(physicalStatement).one_or_none() #getting back from db

        #from time import sleep; sleep(15); #see in db, manually

        if physicalCategory:
            tackleStatement = select(Ability).where(Ability.name == "Tackle")
            tackleAbilityToAdd = session.exec(tackleStatement).one_or_none()

            tackleAbilityToAdd.FK_category_1 = physicalCategory.id #* UPDATE
            session.add(tackleAbilityToAdd)
            session.commit()
        
