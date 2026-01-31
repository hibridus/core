import subprocess
from pathlib import Path
import json

CFG = json.loads(Path("../../cache/config.json").read_text())

Path("cache").mkdir(exist_ok=True)
Path("build").mkdir(exist_ok=True)

sources = [str(p) for p in Path(".").rglob("*.c")]
objects = []

# Compile
for src in sources:
    obj = "cache/" + src.replace("/", "_").replace(".c", ".o")
    objects.append(obj)

    subprocess.run([
        CFG["COMPILER"],
        f"--target={CFG['TARGET']}",
        *CFG["FLAGS"].split(),
        "-c", src,
        "-o", obj
    ], check=True)

# Link
subprocess.run([
    CFG["LINKER"],
    "-T", "linker.ld",
    *objects,
    "-o", "build/KERNEL_X64.elf"
], check=True)

# Send to the ISO
print("""{
    "master": {
        "build/KERNEL_X64.elf": ""
    }
}""")