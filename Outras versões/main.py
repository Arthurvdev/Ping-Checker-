import subprocess
import tkinter as tk
from threading import Thread

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
            result_label.config(text=f"Ping: {time_ms} ms | Bytes: {byte_cmd}")
        
        #caso o idioma do CMD esteja em Português
        elif "tempo=" in output.stdout:
            time_ms = output.stdout.split('tempo=')[1].split('ms')[0].strip()
            byte_cmd = output.stdout.split('bytes=')[1].split(' ')[0].strip()
            result_label.config(text=f"Ping: {time_ms} ms | Bytes: {byte_cmd}")
            
        else:
            result_label.config(text="Falha ao obter ping.")

    except subprocess.CalledProcessError:
        result_label.config(text="Erro ao executar ping no servidor.")

def iniciar_ping():
    server_ip = ip_entry.get()
    result_label.config(text="Testando...")
    Thread(target=ping_server, args=(server_ip,)).start()

# Cria a interface grafica
root = tk.Tk()
root.title("Testar Ping")


# Envia o input que desejo para o ip entry
tk.Label(root, text="Server IP ou Domínio:").pack(pady=5)
ip_entry = tk.Entry(root)
ip_entry.pack(pady=5)
ip_entry.insert(0, "187.16.216.69")  # IP padrão do Server LoL BR

# Botão para inicar o teste de ping
ping_button = tk.Button(root, text="Verificar ping", command=iniciar_ping)
ping_button.pack(pady=10)

# Mostra o resultado do ping
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Loop do tkinter padrão :)
root.mainloop()
