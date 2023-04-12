import os
import subprocess

dir = os.getcwd()
rpath = os.path.dirname(os.path.realpath(__file__))

print(f"At: { dir }")
name = str(input("Name of project: "))
raylib = int(input("Do you wanna use raylib? [0, 1]: "))
path = f"{dir}/{name}"

os.system(f"mkdir {dir}/{name}")
os.system(f"mkdir {path}/libs")
os.system(f"mkdir {path}/src")
os.system(f"touch {path}/src/main.c")
os.system(f"git init {path}")
os.system(f"cd {path} && git submodule add https://github.com/dssgabriel/vec.git {path}/libs/vec/ && cd {dir}")
os.system(f"touch {path}/.gitignore")

# gitignore
with open(f"{rpath}/gitignore.txt", "r") as f:
    gitignore = f.read()
with open(f"{path}/.gitignore", "w") as f:
    f.write(gitignore)

# src/main.c
outsrc = ""
if raylib == 0:
    with open(f"{rpath}/ctemp.txt", "r") as f:
        fc = f.read()

    outsrc = fc
else:
    with open(f"{rpath}/craytemp.txt", "r") as f:
        fc = f.read()

    outsrc = fc.replace("$PROJECT$", name)

with open(f"{path}/src/main.c", "w") as f:
    f.write(outsrc)

# run.sh
with open(f"{rpath}/runscript.txt", "r") as f:
    script = f.read().replace("$PROJECT$", name)

with open(f"{path}/run.sh", "w") as f:
    f.write(script)

os.system(f"chmod +x {path}/run.sh")

# premake5.lua
outBuildText = ""

if raylib == 0:
    with open(f"{rpath}/premaketemp.txt", "r") as f:
        fc = f.read()

    outBuildText = fc.replace("$PROJECT$", name)
else:
    with open(f"{rpath}/premakeraytemp.txt", "r") as f:
        fc = f.read()

    outBuildText = fc.replace("$PROJECT$", name)

with open(f"{path}/premake5.lua", "w") as f:
    f.write(outBuildText)
