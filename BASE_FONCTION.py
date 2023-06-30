from connexion import db
def checkPersonneExist(id):

    status = False
    cursor = db.get_cursor()
    reqs = f"SELECT * FROM personne WHERE id = {id}"
    cursor.execute(reqs)
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True
    else:
        return False

def checkParamPost(params):
    keys = ["id", "nom", "prenom"]
    status = False
    if all(key in params for key in keys):
        return True
    else:
        return False

def checkParamPut(params):
    keys = ["nom", "prenom"]
    status = False
    if all(key in params for key in keys):
        return True
    else:
        return False
