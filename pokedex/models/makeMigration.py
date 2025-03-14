#Automated migration -- execute for fast migrating experience
#PLEASE RUN THIS FILE AT ROOT DIR (/programacao--study/)
#Will execute despite the models have changed or not

#! Add new models to models/__init__.py (via import) 
from os import system as cmd
import datetime

migrationMessage = str(input("Please enter a migration message\t->"))

result = cmd(f"alembic revision --autogenerate -m \"{migrationMessage}\"")

result_2: int = -10
if result == 0:
    choiceMigrateNow = str(input("migration created. Migrate Now? (y/N)\t->"))
    if choiceMigrateNow.lower().startswith("y"):
        result_2 = cmd("alembic upgrade head")

#Logging
if result == 0 and result_2 == 0:
    with open('migration-history.log', 'a') as file:
        now = datetime.datetime.now()
        file.write(f"\n[{now}] -- Migration sucessfull: {migrationMessage}")
elif result_2 != 0:
    with open('migration-history.log', 'a') as file:
        now = datetime.datetime.now()
        file.write(f"\n[{now}] -- Migration created (ready to migrate): {migrationMessage}")
        print("Migration created. Migrate with: \'alembic upgrade head\'")