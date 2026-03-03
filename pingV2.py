import subprocess
from tkinter import *
from threading import Thread
import customtkinter
import tkinter as tk  # Aqui importamos o tkinter para usar PhotoImage

def ping_server(server_ip):
    
    # Command to ping the server
    command = ['ping', server_ip, '-n', '1', '-l', '32']

    try:
        # Executa o comando de ping e captura a saída
        output = subprocess.run(command, capture_output=True, text=True)
        
        # Extrai o MS e os Bytes da resposta vinda do CMD
        # Caso o idioma do CMD esteja em inglês
        if "time=" in output.stdout and "bytes" in output.stdout:
            time_ms = output.stdout.split('time=')[1].split('ms')[0].strip()
            byte_cmd = output.stdout.split('bytes=')[1].split(' ')[0].strip()
            result_label.configure(text=f"Ping: {time_ms} ms")
        
        # Caso o idioma do CMD esteja em Português
        elif "tempo=" in output.stdout:
            time_ms = output.stdout.split('tempo=')[1].split('ms')[0].strip()
            byte_cmd = output.stdout.split('bytes=')[1].split(' ')[0].strip()
            result_label.configure(text=f"Ping: {time_ms} ms")
            
        else:
            result_label.configure(text="Falha ao obter ping.")

    except subprocess.CalledProcessError:
        result_label.configure(text="Erro ao executar ping no servidor.")

def iniciar_ping(ip_server):
    server_ip = ip_server
    result_label.configure(text="Testando...")
    Thread(target=ping_server, args=(server_ip,)).start()
    
def league_of_legends():
    ping = "dynamodb.sa-east-1.amazonaws.com"
    iniciar_ping(ping)

def valorant():
    ping = "dynamodb.sa-east-1.amazonaws.com"
    iniciar_ping(ping)
    
def fortnite():
    ping = "dynamodb.sa-east-1.amazonaws.com"
    iniciar_ping(ping)


# Aparência da interface gráfica
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Criação da interface gráfica
root = customtkinter.CTk()
root.title("Testar Ping")

# icone para o app
root.after(201, lambda :root.iconbitmap("icone.ico"))

# Esta linha de código faz iniciar maximizado
root.after(0, lambda: root.state('zoomed'))

# Centralizando o título e diminuindo o espaço
title = customtkinter.CTkLabel(root, text="SELECIONE O JOGO:", font=('arial', 40, 'bold'), text_color="linen")
title.place(relx=0.5, rely=0.3,anchor="center") # Diminui o pady para o título ficar mais próximo dos botões

# Frame que irá conter os botões
button_frame = customtkinter.CTkFrame(root, fg_color="transparent")
button_frame.grid(row=1, column=0, columnspan=3, pady=0)  # Menos espaço entre título e botões

# Variável para a cor dos botões
cor_btn = "linen"

# Criando os botões dentro do frame
lol_img = PhotoImage(file="lol.png")
lol_button = customtkinter.CTkButton(button_frame, width=80, height=80, text="", image=lol_img, command=league_of_legends, fg_color=cor_btn)
lol_button.grid(row=0, column=0, padx=15)

valorant_img = PhotoImage(file="valorant.png")
valorant_button = customtkinter.CTkButton(button_frame, width=80, height=80, text="", image=valorant_img, command=valorant, fg_color=cor_btn)
valorant_button.grid(row=0, column=1, padx=15)

fortnite_img = PhotoImage(file="fortnite.png")
fortnite_button = customtkinter.CTkButton(button_frame, width=80, height=80, text="", image=fortnite_img, command=fortnite, fg_color=cor_btn)
fortnite_button.grid(row=0, column=2, padx=15)

# Mostra o resultado do ping
result_label = customtkinter.CTkLabel(root, text="", font=('arial', 25, 'italic'), text_color="linen", fg_color="transparent")
result_label.place(relx=0.5, rely=0.7,anchor="center")

# CRIADOR

criador = customtkinter.CTkLabel(root,text="Desenvolvido por: ArthurVDev",font=('arial', 15, 'italic'), text_color="linen", fg_color="transparent")
criador.place(relx=0.5, rely=0.9,anchor="center")

# Configurando o grid para centralizar os elementos
root.grid_rowconfigure(0, weight=1)  # Centraliza a linha do título
root.grid_rowconfigure(1, weight=1)  # Centraliza a linha dos botões
root.grid_rowconfigure(2, weight=1)  # Centraliza a linha do resultado
root.grid_columnconfigure(0, weight=1)  # Centraliza a coluna 0
root.grid_columnconfigure(1, weight=1)  # Centraliza a coluna 1
root.grid_columnconfigure(2, weight=1)  # Centraliza a coluna 2

# Loop do tkinter
root.mainloop()
