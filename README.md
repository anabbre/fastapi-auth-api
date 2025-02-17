# 📌 API de Autenticación con FastAPI y JWT  


🚀 **Descripción**  
Esta es una API de autenticación desarrollada con **FastAPI** que implementa **JWT (JSON Web Token)** para la gestión de usuarios. Permite el **registro, inicio de sesión y acceso a un perfil protegido** con autenticación.  



## 📂 Estructura del Proyecto  
📦 fastapi-auth-api/ 
┣ 📄 main.py → Código principal de la API. 
┣ 📄 auth.py → Lógica de autenticación (JWT y contraseñas). 
┣ 📄 models.py → Esquemas de datos y validaciones. 
┣ 📄 database.py → Simulación de base de datos (por ahora en memoria). 
┣ 📄 requirements.txt → Librerías necesarias. 
┣ 📄 README.md → Este archivo.



## 🛠️ Tecnologías Usadas  
✅ **FastAPI** → Framework para construir APIs rápidas y eficientes.  
✅ **Pydantic** → Validación de datos.  
✅ **bcrypt** → Cifrado de contraseñas.  
✅ **PyJWT** → Manejo de tokens JWT para autenticación.  
✅ **SQLite (opcional)** → Base de datos ligera para persistencia de usuarios.  



# 🚀 Instalación y configuración

## 1. Clonar el repositorio 
```bash
git clone https://github.com/anabbfre/fastapi-auth-api.git
cd fastapi-auth-api
```

## 2. Crear y activar un entorno virutal (opcional pero recomendado)
```python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

## 3. Instalar dependencias 
```pip install -r requirements.txt
```

## 4. Ejecutar el servidor
```uvicorn main:app --reload
```




**Accede a la API en http://127.0.0.1:8000/docs para probar los endpoints desde Swagger UI**.



🔑 **Endpoints Disponibles**
📝 Registro de usuario
📌 Ruta: POST /register
📌 Descripción: Permite crear un nuevo usuario.
📌 Cuerpo de la solicitud (JSON):
{
  "username": "usuario123",
  "full_name": "Usuario Ejemplo",
  "email": "usuario@email.com",
  "password": "contraseña_segura"
}
📌 Respuesta esperada:
{
  "message": "Usuario registrado correctamente"
}



🔐 **Iniciar sesión**
📌 Ruta: POST /login
📌 Descripción: Permite a un usuario autenticarse y obtener un token JWT.
📌 Parámetros (form-data):

username: usuario123
password: contraseña_segura
📌 Respuesta esperada:
{
  "access_token": "eyJhbGciOiJIUz...",
  "token_type": "bearer"
}



🔒 **Obtener perfil del usuario autenticado**
📌 Ruta: GET /profile
📌 Descripción: Devuelve la información del usuario autenticado.
📌 Encabezado requerido:
Authorization: Bearer <token_jwt>
📌 Respuesta esperada:
{
  "username": "usuario123",
  "full_name": "Usuario Ejemplo"
}



🛠️ **Herramientas Adicionales**
📌 Swagger UI: http://127.0.0.1:8000/docs
📌 ReDoc: http://127.0.0.1:8000/redoc

Ambas interfaces permiten probar la API de manera interactiva.




📜 **Licencia**
Este proyecto es de código abierto bajo la licencia MIT.
