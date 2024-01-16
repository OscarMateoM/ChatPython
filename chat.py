import socket

def start_server():
    host = ''  # Escucha en todas las interfaces de red
    port = 8080  # Puerto de escucha

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen()
    print(f"Servidor escuchando en {host}:{port}")

    cliente, direccion = servidor.accept()
    print(f"Conexión establecida desde {direccion}")

    try:
        while True:
            datos_recibidos = cliente.recv(1024)
            if not datos_recibidos:
                break
            print(f"Datos recibidos: {datos_recibidos.decode('utf-8')}")
            mensaje = "Hola, cliente. ¡Conexión exitosa!"
            cliente.send(mensaje.encode('utf-8'))

    except Exception as e:
        print(f"Error de conexión: {e}")

    finally:
        cliente.close()
        servidor.close()
        print("Conexión cerrada")

def start_client():
    host = 'localhost'
    puerto = 8080

    s = socket.socket()

    try:
        s.connect((host, puerto))
        print("Conectado al servidor")

        while True:
            mens = input("Mensaje desde Cliente a Servidor >> ")
            s.send(mens.encode('utf-8'))

    except Exception as e:
        print(f"Error de conexión: {e}")

    finally:
        s.close()
        print("Conexión cerrada")

def menu():
    while True:
        print("1. Iniciar servidor")
        print("2. Iniciar cliente")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            start_server()
        elif opcion == '2':
            start_client()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intentelo de nuevo.")

if __name__ == "__main__":
    menu()
