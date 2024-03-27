import socket
import time
from typing import Callable, Awaitable
from asyncio import StreamReader, StreamWriter
import asyncio


class ExitRequest(Exception): ...


class AsyncTCPServer:
    def __init__(self, port: int, client_handler: Callable[[StreamReader, StreamWriter], Awaitable[None]],
                 limit: int = 50):
        self.client_handler = client_handler
        self.port = port
        self.limit = limit

    async def start(self, restart: bool = True) -> None:
        while True:
            try:
                print('Starting server...')
                await self._start()
                break
            except (ExitRequest, KeyboardInterrupt):
                break
            except Exception as e:
                print(f'Critical Error: {e}')
                if not restart:
                    break
                print('Restarting in 5 seconds...')
                time.sleep(5)
        print('Exited')

    async def _start(self) -> None:
        server = await asyncio.start_server(self.client_handler, '', self.port, limit=self.limit)
        addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
        print(f'Serving on {addrs}')
        print(f'Is serving: {server.is_serving()}')
        async with server:
            try:
                await server.serve_forever()
            except KeyboardInterrupt:
                raise ExitRequest

            # server.sockets


class Pipe:
    def __init__(self):
        self.streams = []
        self.tasks = []
        self.futures = []

    async def __aenter__(self, *_, **__):
        return self

    async def __aexit__(self, *_, **__):
        async with asyncio.TaskGroup() as tg:
            for f in self.futures:
                self.tasks.append(tg.create_task(f))
        await self.close()

    async def close(self) -> None:
        for t in self.tasks:
            if not t.cancelled():
                t.cancel()
        for s in self.streams:
            if isinstance(s, StreamWriter):
                s.close()
                await s.wait_closed()
        self.tasks.clear()
        self.futures.clear()
        self.streams.clear()

    def simplex(self, src: StreamReader, dst: StreamWriter):
        self.futures.append(self._redirect_simplex(src, dst))

    def duplex(self, src_dst_1: tuple[StreamReader, StreamWriter], src_dst_2: tuple[StreamReader, StreamWriter]):
        self.simplex(src_dst_1[0], src_dst_2[1])
        self.simplex(src_dst_2[0], src_dst_1[1])

    async def _redirect_simplex(self, src: StreamReader, dst: StreamWriter) -> None:
        self.streams.append(src)
        self.streams.append(dst)
        try:
            while not dst.is_closing() and not src.at_eof():
                dst.write(await src.read(65565))
                await dst.drain()
        except (asyncio.CancelledError, ConnectionError, KeyboardInterrupt):
            dst.close()
        except Exception as e:
            print(f'Error: streams pipe rised: {e}')
            raise
        finally:
            dst.close()
            await dst.wait_closed()

# pass
