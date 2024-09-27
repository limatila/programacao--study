from typing import Any
from faker import Faker
from random import choice, randint

fake = Faker()
foods: list[Any] = ['pizza', 'burger', 'sushi', 'pasta', 'salad', 'dessert', 'steak', 'sandwich', 'soup']
def getRandomImageTuple() -> tuple[int, int]:
    return (randint(500,1024), randint(800, 2098))

def main(num: int = 0) -> dict[Any, Any]:
    firstNameGenerated: str = fake.first_name()
    lastNameGenerated: str = fake.last_name()
    randomFood:str = choice(foods)
    imagePos1, imagePos2 = getRandomImageTuple();
    return {
        "idPage": num,
        "titleReceita": randomFood,
        "imageReceita": f"https://loremflickr.com/{imagePos1}/{imagePos2}/food,cook",
        "userName": firstNameGenerated + lastNameGenerated,
        "userFirstName": firstNameGenerated,
        "userLastName": lastNameGenerated,
        "userEmail": fake.email(),
        "publicationDate": fake.date_time(end_datetime="now").strftime("%d/%m/%Y"),
        "description": fake.paragraph(nb_sentences=3)
    }

if __name__ == "__main__":
    print(main().get("publicationDate"))
    print("** Fake Data Generated **")