import subprocess
from pathlib import Path
import json

CFG = json.loads(Path("../cache/config.json").read_text())

Path("cache").mkdir(parents=True, exist_ok=True)
Path("build").mkdir(parents=True, exist_ok=True)

# Compile
subprocess.run([
    CFG["COMPILER"],
    f'--target={CFG["TARGET"]}',
    *CFG["FLAGS"].split(),
    "-c",
    "src/init/main.c",
    "-o", "cache/kernel.o"
], check=True)

# Link
subprocess.run([
    CFG["LINKER"],
    "-T", "linker.ld",
    "cache/kernel.o",
    "-o", "build/KERNEL_X64.elf"
], check=True)

# Send the kernel to the Master
print("""{
    "master": {
        "build/KERNEL_X64.elf": ""
    }
}""")