#include "limine.h"

__attribute__((used, section(".limine_requests")))
static volatile struct limine_framebuffer_request fb_request = {
    .id = LIMINE_FRAMEBUFFER_REQUEST_ID,
    .revision = 0
};

static struct limine_framebuffer* fb;

void kmain()
{
    if (fb_request.response == 0x00 || fb_request.response->framebuffer_count == 0)
        return;

    fb = fb_request.response->framebuffers[0];

    InitFramebuffer(fb->width, fb->height, fb->pitch, fb->address);

    CleanScreen();

    Print("Um pequeno salto para o homem. Um salto gigantesco para a humanidade\n\n", 0xFFFFFFFF);
    Print("-Neil Armstrong 2", 0xFF00FFFF);

    while (1)
    {

    }
}
