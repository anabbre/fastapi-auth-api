from pydantic import BaseModel, EmailStr

# Esquema de registro de usuario
class User(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str

# Esquema de usuario en la base de datos
class UserInDB(User):
    hashed_password: str

# Esquema de respuesta con el token
class Token(BaseModel):
    access_token: str
    token_type: str
