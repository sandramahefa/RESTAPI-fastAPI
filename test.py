from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    email: str

    # def __init__(self,name,age,email):
    #     self.name = name
    #     self.age = age
    #     self.email = email
    def get_name(self):
        return self.name

# Création d'une instance de modèle
person_data = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

person = Person(**person_data)
print(person.get_name())