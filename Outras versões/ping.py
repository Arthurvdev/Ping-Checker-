import subprocess
from tkinter import *
from threading import Thread
import customtkinter
import customtkinter as ctk



def ping_server(server_ip):
    # Command to ping the server
    command = ['ping', server_ip, '-n', '1']

    try:
        # Executa o comando de ping e captura a saída
        output = subprocess.run(command, capture_output=True, text=True)
        
        # Extrai o MS e os Bytes da resposta vinda do CMD
        
        #caso o idioma do CMD esteja em inglês
        if "time=" in output.stdout and "bytes" in output.stdout:
            time_ms = output.stdout.split('time=')[1].split('ms')[0].strip()
            byte_cmd = output.stdout.split('bytes=')[1].split(' ')[0].strip()
            result_label.configure(text=f"Ping: {time_ms} ms | Bytes: {byte_cmd}")
        
        #caso o idioma do CMD esteja em Português
        elif "tempo=" in output.stdout:
            time_ms = output.stdout.split('tempo=')[1].split('ms')[0].strip()
            byte_cmd = output.stdout.split('bytes=')[1].split(' ')[0].strip()
            result_label.configure(text=f"Ping: {time_ms} ms | Bytes: {byte_cmd}")
            
        else:
            result_label.configure(text="Falha ao obter ping.")

    except subprocess.CalledProcessError:
        result_label.configure(text="Erro ao executar ping no servidor.")

def iniciar_ping():
    server_ip = ip_entry.get()
    result_label.configure(text="Testando...")
    Thread(target=ping_server, args=(server_ip,)).start()

# Aparência da interface gráfica

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Cria a interface grafica

root = customtkinter.CTk()
root.title("Testar Ping")

# Esta linha de código faz iniciar maximizado
root.after(0, lambda:root.state('zoomed'))


# Envia o input que desejo para o ip entry
title = customtkinter.CTkLabel(root, text="Server IP ou Domínio:")
title.place(relx=0.5, rely=0.3,anchor="center")

ip_entry = customtkinter.CTkEntry(root, width=200, height=30)
ip_entry.place(relx=0.5, rely=0.4,anchor="center")
ip_entry.insert(0, "187.16.216.69")  # IP padrão do Server LoL BR

#dynamodb.sa-east-1.amazonaws.com (server lol, valorant, apex, fortnite)


# Botão para inicar o teste de ping
ping_button = customtkinter.CTkButton(root,width=200, height=30, text="test", command=iniciar_ping)
ping_button.place(relx=0.5, rely=0.5,anchor="center")


lol_img = PhotoImage(file="lol.png")
test_button = customtkinter.CTkButton(root,width=200, height=30, text="",image=lol_img)
test_button.place(relx=0.5, rely=0.8,anchor="center")

# Mostra o resultado do ping
result_label = customtkinter.CTkLabel(root, text="")
result_label.place(relx=0.5, rely=0.6,anchor="center")



# Loop do tkinter padrão :)

root.mainloop()
