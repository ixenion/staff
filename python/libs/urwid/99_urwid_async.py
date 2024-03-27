import asyncio
import urwid

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(key)

async def payload(txt):
    for i in range(100):
        await asyncio.sleep(2)
        txt.set_text(repr(i))

async def async_loop_run(loop):
    loop.run()

txt = urwid.Text(u"Showing some different alignment modes")
fill = urwid.Filler(txt, 'top')

aloop = asyncio.get_event_loop()

ev_loop = urwid.AsyncioEventLoop(loop=aloop)
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit, event_loop=ev_loop)
aloop.create_task(payload(txt))
loop.run()

