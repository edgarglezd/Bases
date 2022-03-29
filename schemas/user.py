def userEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": item.get("name"),
        "email": item.get("email"),
        "password": item.get("password")
    }
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

    