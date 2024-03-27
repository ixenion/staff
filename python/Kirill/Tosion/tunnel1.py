import asyncio
from asyncio import StreamReader, StreamWriter
from typing import Callable, Awaitable

import netw


def encrypt_data(data: bytes, key: int) -> bytes:
    return bytes([(b + key) % 256 for b in data])


def decrypt_data(data: bytes, key: int) -> bytes:
    return bytes([(b - key) % 256 for b in data])


def _test1():
    from random import randint
    for _ in range(1000):
        x = bytes([randint(0, 255) for _ in range(randint(5, 100))])
        y = encrypt_data(x, 17)
        z = decrypt_data(y, 17)
        assert x == z, f'{x}\n{y}\n{z}'


class EncryptedStreamReader:

    def __init__(self, key: int, reader: StreamReader):
        self.key = key
        self.reader = reader

    async def read(self, buffer: int) -> bytes:
        return decrypt_data(await self.reader.read(buffer), self.key)

    def at_eof(self):
        return self.reader.at_eof()


class EncryptedStreamWriter:
    def __init__(self, key: int, writer: StreamWriter):
        self.key = key
        self.writer = writer

    def write(self, data: bytes):
        return self.writer.write(encrypt_data(data, self.key))

    async def drain(self):
        await self.writer.drain()

    def close(self):
        return self.writer.close()

    def is_closing(self):
        return self.writer.is_closing()

    async def wait_closed(self):
        return await self.writer.wait_closed()

    async def __aenter__(self) -> None:
        return

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if not self.is_closing():
            self.close()
        await self.wait_closed()


async def open_encrypted_connection(target_host, target_port, key) -> tuple[
    EncryptedStreamReader, EncryptedStreamWriter]:
    reader, writer = await asyncio.open_connection(target_host, target_port)
    return EncryptedStreamReader(key, reader), EncryptedStreamWriter(key, writer)


class EncryptedServer(netw.AsyncTCPServer):
    def __init__(self, port: int,
                 client_handler: Callable[[EncryptedStreamReader, EncryptedStreamWriter], Awaitable[None]],
                 key: int, limit: int = 50):
        self.key = key
        self.encrypted_client_handler = client_handler
        super().__init__(port=port, client_handler=self._handle_client, limit=limit)

    async def _handle_client(self, reader: StreamReader, writer: StreamWriter):
        await self.encrypted_client_handler(EncryptedStreamReader(self.key, reader),
                                            EncryptedStreamWriter(self.key, writer))


async def main():
    k = 17

    async def echo():
        await asyncio.sleep(1)
        r, w = await open_encrypted_connection('127.0.0.1', 12345, k)
        print('Sending request...')
        w.write(b'Hello, world!')
        await w.drain()
        print('Waiting for response...')
        print('Received response:', await r.read(65565))
        w.close()
        await w.wait_closed()

    async def handle_client(r, w):
        print('Client connected')
        async with netw.Pipe() as p:
            p.simplex(r, w)
            print('Piping client streams')

    server = EncryptedServer(12345, handle_client, k)
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(server.start())
        t2 = tg.create_task(echo())


if __name__ == '__main__':
    asyncio.run(main())
    # _test1()
    pass
