import requests

# URL de la API (ajusta si es necesario)
BASE_URL = "http://127.0.0.1:8000"

def registrar_usuario():
    url = f"{BASE_URL}/register"
    data = {
        "username": "usuario123",
        "full_name": "Usuario Ejemplo",
        "email": "usuario@email.com",
        "password": "contraseña_segura"
    }
    response = requests.post(url, json=data)
    print("\n📌 Respuesta del registro:")
    print(response.json())

def iniciar_sesion():
    url = f"{BASE_URL}/login"
    data = {
        "username": "usuario123",
        "password": "contraseña_segura"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        token = response.json().get("access_token")
        print("\n🔑 Token obtenido:")
        print(token)
        return token
    else:
        print("\n❌ Error en login:")
        print(response.json())
        return None

def obtener_perfil(token):
    url = f"{BASE_URL}/profile"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("\n👤 Perfil del usuario:")
    print(response.json())

if __name__ == "__main__":
    print("🚀 Iniciando Cliente API")
    
    # 1. Registrar usuario (opcional si ya está registrado)
    registrar_usuario()

    # 2. Iniciar sesión y obtener token
    token = iniciar_sesion()

    # 3. Obtener perfil (solo si el login fue exitoso)
    if token:
        obtener_perfil(token)
