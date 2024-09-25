import socket
import threading

# Datos del servidor
HOST = '127.0.0.1'  # Localhost
PORT = 50001         # Puerto del servidor

# Configurar el socket del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clientes = []
nombres = []

# Función para enviar mensajes a todos los clientes conectados
def broadcast(mensaje, cliente):
    for cl in clientes:
        if cl != cliente:
            try:
                cl.send(mensaje)
            except:
                cl.close()
                clientes.remove(cl)

# Función para manejar a cada cliente
def handle_client(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            broadcast(mensaje, cliente)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            nombre = nombres[index]
            broadcast(f'{nombre} ha salido del chat.'.encode('utf-8'), cliente)
            nombres.remove(nombre)
            break

# Función para recibir nuevos clientes
def receive():
    while True:
        cliente, direccion = server.accept()
        print(f"Conectado con {direccion}")

        cliente.send("NOMBRE".encode('utf-8'))
        nombre = cliente.recv(1024).decode('utf-8')
        nombres.append(nombre)
        clientes.append(cliente)

        print(f"Nombre del cliente es {nombre}")
        broadcast(f"{nombre} se ha unido al chat.".encode('utf-8'), cliente)
        cliente.send('Conectado al servidor.'.encode('utf-8'))

        hilo = threading.Thread(target=handle_client, args=(cliente,))
        hilo.start()

print("Servidor escuchando...")
receive()
