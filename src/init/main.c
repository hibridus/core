#include "limine.h"

__attribute__((used, section(".limine_requests")))
static volatile struct limine_framebuffer_request fb_request = {
    .id = LIMINE_FRAMEBUFFER_REQUEST_ID,
    .revision = 0
};

static struct limine_framebuffer *fb;

void kmain()
{
    if (fb_request.response == 0x00 || fb_request.response->framebuffer_count == 0)
        return;

    fb = fb_request.response->framebuffers[0];

    uint64_t w     = fb->width;
    uint64_t h     = fb->height;
    uint64_t pitch = fb->pitch;
    uint32_t* addr = (uint32_t*)fb->address;

    for (uint64_t y = 0; y < h; y++)
    {
        for (uint64_t x = 0; x < w; x++)
        {
            addr[x + (y * (pitch / 4))] = 0xFFFFFFFF;
        }
    }
}
