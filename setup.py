from cx_Freeze import setup, Executable
import sys

# Lista de arquivos para incluir: ("origem", "destino_na_pasta_final")
files = ["edge.png", "blueStacks.png"] 

build_exe_options = {
    "include_files": files,
    # Outras opções podem ser adicionadas aqui conforme necessário
}
executables = [
    Executable("main.py", base=None, icon="icone.ico") # Substitua pelo nome do seu script
]
setup(
    name="Recompensas",
    version="8.0",
    description="Programa de pesquisa automática",
    options={"build_exe": build_exe_options},
    executables=executables
)
