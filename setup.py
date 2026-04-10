from cx_Freeze import setup, Executable
import sys

files = ["edge.wan", "blueStacks.wan"] 

build_exe_options = {
    "include_files": files,
}
executables = [
    Executable("Recompensas.py", base=None, icon="icon.wan")
]
setup(
    name="Recompensas",
    version="8.0",
    description="Programa de pesquisa automática",
    options={"build_exe": build_exe_options},
    executables=executables
)
