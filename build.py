import subprocess
from pathlib import Path
import json

CFG = json.loads(Path("../cache/config.json").read_text())

# Compile
subprocess.run([
    CFG["COMPILER"],
    f'--target={CFG["TARGET"]}',
    *CFG["FLAGS"].split(),
    "-c",
    "src/init/main.c",
    "-o", "kernel.o"
], check=True)

# Link
subprocess.run([
    CFG["LINKER"],
    "-T", "linker.ld",
    "kernel.o",
    "-o", "KERNEL_X64.elf"
], check=True)

# Send the kernel to the Master
print("""{
    "master": {
        "KERNEL_X64.elf": ""
    }
}""")