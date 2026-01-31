OUTPUT_FORMAT(elf64-x86-64)
ENTRY(kmain)

PHDRS {
    text   PT_LOAD FLAGS(5); /* RX */
    rodata PT_LOAD FLAGS(4); /* R */
    data   PT_LOAD FLAGS(6); /* RW */
}

SECTIONS {
    . = 0xffffffff80000000;

    phys = 0x100000;

    /* ---------------- TEXT ---------------- */
    .text : AT(phys) ALIGN(0x1000) {
        *(.text .text.*)
    } :text
    phys += SIZEOF(.text);

    /* ---------------- RODATA ---------------- */
    .rodata : AT(phys) ALIGN(0x1000) {
        *(.rodata .rodata.*)
    } :rodata
    phys += SIZEOF(.rodata);

    /* ---------------- DATA ---------------- */
    .data : AT(phys) ALIGN(0x1000) {
        *(.data .data.*)

        KEEP(*(.limine_requests))
        KEEP(*(.requests))
        KEEP(*(.requests_start_marker))
        KEEP(*(.requests_end_marker))
    } :data
    phys += SIZEOF(.data);

    /* ---------------- BSS ---------------- */
    .bss (NOLOAD) : ALIGN(0x1000) {
        *(COMMON)
        *(.bss .bss.*)
    } :data

    /DISCARD/ : {
        *(.eh_frame*)
        *(.note*)
        *(.comment*)
    }
}
