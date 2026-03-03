from cx_Freeze import setup, Executable
import sys

# Configuração para inclusão das imagens
build_exe_options = {
    "packages": ["os"],
    "include_files": ["lol.png", "valorant.png", "fortnite.png"]  # Adicione suas imagens aqui
}

# Configuração do executável
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Testar Ping",
    version="1.0",
    description="Testar Ping",
    options={"build_exe": build_exe_options},
    executables=[Executable("testarping.py", base=base, icon="icone.ico")]
)
