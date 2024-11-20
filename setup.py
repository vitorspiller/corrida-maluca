# pip install cx_freeze
import cx_Freeze

executables = [
    cx_Freeze.Executable(script="main.py", icon="assets/icone.ico")
]
cx_Freeze.setup(
    name = "Corrida Maluca",
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    }, executables =  executables
)
#python geraSetup.py build || python geraSetup.py bdist_msi