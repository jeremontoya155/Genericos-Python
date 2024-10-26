import requests


def datos_web(url):
    try:
        datos = requests.get(url)
        if datos.status_code == 200:
            return datos.json()
        else:
            print(f"Error en {datos.status_code}")
            return -1
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")
        return None


print(datos_web("https://jsonplaceholder.typicode.com/posts/1"))
