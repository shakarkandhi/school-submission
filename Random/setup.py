from cx_Freeze import setup, Executable

base = None

executables = [Executable("hypo.py", base=base)]

packages = ["idna","math"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Dia",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
