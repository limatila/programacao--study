from sqlmodel import SQLModel, select, Session

from pokedex.models import *
from pokedex.dependencies import get_engine, DB_ENGINE_CHOICE

#! Startup data: only execute once!
if __name__ == "__main__":
    engine = get_engine(DB_ENGINE_CHOICE)

    #Create tables by defined models.py
    SQLModel.metadata.create_all(engine)
    
    #adding first 4 pokemons
    with Session(engine) as session:
        session.add_all([
            Pokemon(id=1, name="Bulbasaur", weight=6.9, height=0.7, ),
            Pokemon(id=2, name="Ivysaur", weight=13.0, height=1.0),
            Pokemon(id=3, name="Venusaur", weight=100.0, height=2.0),
            Pokemon(id=4, name="Charmander", weight=8.5, height=0.6)
        ])
        session.commit()

    #pokemon ability Tackle (common in pokemons 1 and 3)
    with Session(engine) as session: 
        session.add(Ability(name="Tackle", effect="damage", generation=1))
        session.commit()

    #adding compatibility to pokemons 1 and 3
    with Session(engine) as session:
        #* Selecting Tackle ability
        tackleStatement = select(Ability).where(Ability.name == "Tackle")
        tackleAbility = session.exec(statement=tackleStatement).one_or_none() #.fetchall(), .all(), .one(), .first(), and some more
        print(tackleAbility)

        session.add(AbilityCompatibility(FK_pokemon_id=1, FK_ability_id=tackleAbility.id))
        session.add(AbilityCompatibility(FK_pokemon_id=3, FK_ability_id=tackleAbility.id))
        session.commit()

    #adding categorys to the Tackle ability + testing select querys
    with Session(engine) as session:
        categoryToAdd = AbilityCategory(name="Normal", color="#B6B6A8")
        session.add(categoryToAdd)
        session.commit()

        physicalStatement = select(AbilityCategory).where(AbilityCategory.name == categoryToAdd.name)
        physicalCategory = session.exec(physicalStatement).one_or_none() #getting back from db

        #from time import sleep; sleep(15); #see in db, manually

        if physicalCategory:
            tackleStatement = select(Ability).where(Ability.name == "Tackle")
            tackleAbilityToAdd = session.exec(tackleStatement).one_or_none()

            tackleAbilityToAdd.FK_category = physicalCategory.id #* UPDATE
            session.add(tackleAbilityToAdd)
            session.commit()
        
