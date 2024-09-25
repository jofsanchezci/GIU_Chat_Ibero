import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Configurar el cliente
HOST = '127.0.0.1'
PORT = 50001

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# Función para recibir mensajes del servidor
def receive_messages():
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje == 'NOMBRE':
                cliente.send(nombre.encode('utf-8'))
            else:
                chat_window.config(state=tk.NORMAL)
                chat_window.insert(tk.END, mensaje + "\n")
                chat_window.config(state=tk.DISABLED)
                chat_window.yview(tk.END)
        except:
            print("Error al recibir el mensaje")
            cliente.close()
            break

# Función para enviar mensajes al servidor
def send_message():
    mensaje = message_entry.get()
    cliente.send(f"{nombre}: {mensaje}".encode('utf-8'))
    message_entry.delete(0, tk.END)

# Función para cerrar el chat
def on_closing():
    cliente.close()
    root.quit()

# Interfaz gráfica
root = tk.Tk()
root.title("Chat Cliente")
root.geometry("400x500")

# Ventana de chat
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Campo de entrada del mensaje
message_entry = tk.Entry(root, font=("Arial", 14))
message_entry.pack(padx=10, pady=10, fill=tk.X)

# Botón de enviar
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack(padx=10, pady=10)

# Captura el nombre del cliente
nombre = None
while not nombre:
    nombre = input("Ingresa tu nombre: ")

# Iniciar el hilo para recibir mensajes
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Manejar el cierre de la ventana
root.protocol("WM_DELETE_WINDOW", on_closing)

# Iniciar la interfaz gráfica
root.mainloop()
