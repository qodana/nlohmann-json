import shutil
import subprocess as sp
from pathlib import Path

shutil.copy2("CMakeLists.txt.disabled", "CMakeLists.txt")
sp.run(["cmake", "-S", ".", "-B", "build", "-D", "CMAKE_EXPORT_COMPILE_COMMANDS=1"], check=True)
Path("CMakeLists.txt").unlink()
Path("build/compile_commands.json").rename("compile_commands.json")
