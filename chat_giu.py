import tkinter as tk
from tkinter import scrolledtext

# Crear la ventana principal
root = tk.Tk()
root.title("Chat Simulado")
root.geometry("400x500")

# Función para enviar el mensaje y actualizar el cuadro de texto
def send_message():
    user_message = message_entry.get()
    if user_message.strip() != "":
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "Tú: " + user_message + "\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        
        # Respuesta simulada
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "ChatBot: Estoy aquí para ayudarte.\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        
        message_entry.delete(0, tk.END)

# Configurar la ventana de texto del chat
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Campo de entrada para el mensaje
message_entry = tk.Entry(root, font=("Arial", 14))
message_entry.pack(padx=10, pady=10, fill=tk.X)

# Botón para enviar el mensaje
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack(padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
