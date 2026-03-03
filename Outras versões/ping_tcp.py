import socket
import tkinter as tk
from threading import Thread
import customtkinter
import time

def check_tcp_latency_real_time(server_url):
    try:
        server_address = (server_url, 443)  # Porta 443 para HTTPS
        
        latencies = []  # Lista para armazenar as latências medidas

        while True:
            start_time = time.time()

            # Tentativa de conexão
            try:
                with socket.create_connection(server_address, timeout=5):
                    latency = (time.time() - start_time) * 1000  # convertendo para ms
                    latencies.append(latency)  # Adiciona a latência à lista
            except (socket.timeout, socket.gaierror, ConnectionRefusedError):
                result_label.configure(text="Erro ao conectar ao servidor.")
                break

            # Calculando a média das latências (ou a média das últimas 10 medições)
            if latencies:
                average_latency = sum(latencies) / len(latencies)
                result_label.configure(text=f"Latência média: {int(average_latency)} ms")

            # Espera 1 segundo antes de medir novamente
            time.sleep(1)

    except Exception as e:
        result_label.configure(text=f"Erro inesperado: {str(e)}")

def iniciar_teste():
    server_url = url_entry.get()
    result_label.configure(text="Testando...")
    Thread(target=check_tcp_latency_real_time, args=(server_url,)).start()

# Aparência da interface gráfica
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Cria a interface gráfica
root = customtkinter.CTk()
root.title("Testar Latência do Servidor")

# Esta linha de código faz iniciar maximizado
root.after(0, lambda: root.state('zoomed'))

# Envia o input que desejo para o url_entry
title = customtkinter.CTkLabel(root, text="Server URL:")
title.place(relx=0.5, rely=0.3, anchor="center")

url_entry = customtkinter.CTkEntry(root, width=300, height=30)
url_entry.place(relx=0.5, rely=0.4, anchor="center")
url_entry.insert(0, "dynamodb.sa-east-1.amazonaws.com")  # URL padrão do Server LoL BR

# Botão para iniciar o teste de latência
ping_button = customtkinter.CTkButton(root, width=200, height=30, text="Verificar latência", command=iniciar_teste)
ping_button.place(relx=0.5, rely=0.5, anchor="center")

# Mostra o resultado do teste
result_label = customtkinter.CTkLabel(root, text="")
result_label.place(relx=0.5, rely=0.6, anchor="center")

# Loop do tkinter padrão
root.mainloop()
