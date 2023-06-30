import json

from connexion import db
from fastapi import FastAPI,HTTPException, status
from pydantic import BaseModel
from BASE_FONCTION import checkPersonneExist, checkParamPost, checkParamPut

app = FastAPI()

@app.get("/")
def allPersonne():
    reqs = f"SELECT * FROM personne;"
    clients = []
    cursor = db.get_cursor()
    cursor.execute(reqs)
    results = cursor.fetchall()
    for result in results:
        clients.append(result)
    cursor.close()
    return clients

@app.get("/items/{id}")
def getPersonne(id:int):
    reqs = f"SELECT * FROM personne WHERE id = {id}"
    cursor = db.get_cursor()
    cursor.execute(reqs)
    result = cursor.fetchone()
    cursor.close()
    if result:
        client = result
        return client
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=("id not found"))

@app.post("/post_item")
def postPersonne(per:dict):
    cursor = db.get_cursor()
    reqs = "INSERT INTO personne (id, nom, prenom) VALUES (%s, %s, %s)"
    if checkParamPost(per):
        id = per['id']
        nom = per['nom']
        prenom = per['prenom']
        data = (id, nom, prenom)
        if checkPersonneExist(id) == True:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Client already exist")
        else:
            cursor.execute(reqs, data)
            db.get_connection().commit()
            cursor.close()

        return {"status_post":"Client insert succesfully"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Bad request")

@app.put("/edit/{id}")
def updatePersonne(id:int,params:dict):
    cursor = db.get_cursor()
    reqs = "UPDATE personne SET nom=%s, prenom=%s where id = %s;"

    if checkParamPut(params):
        nom = params['nom']
        prenom = params['prenom']
        data = (nom, prenom, id)

        cursor.execute(reqs, data)
        db.get_connection().commit()
        cursor.close()

        return {"status_post": 200}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Bad parameters")

@app.delete("/delete/{id}")
def deletePersonne(id:int):
    cursor = db.get_cursor()
    reqs = f"DELETE from personne where id = {id};"

    cursor.execute(reqs)
    db.get_connection().commit()
    cursor.close()

    return {"status_post": 200}



