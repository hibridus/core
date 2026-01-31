clear

export PATH="$PATH:/home/artic/opt/cross/bin/"

x86_64-elf-gcc -ffreestanding -mno-red-zone -fno-pie -no-pie -nostdlib -fno-stack-protector -T linker.ld kernel.c -o kernel.elf

#x86_64-elf-gcc -ffreestanding -mno-red-zone -nostdlib kernel.c -o init.elf

mv kernel.elf ../../cache/iso_root/boot/init.elf