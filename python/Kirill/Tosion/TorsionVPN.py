import asyncio
from asyncio import StreamReader, StreamWriter

import netw
import tunnel1
from configurator import SystemConfigurator


class AsyncHTTPProxyLocalHub(netw.AsyncTCPServer):
    def __init__(self, browser_port: int, tunnel_key: int, tunnel_host: str, tunnel_port: int, browser_limit: int = 50):
        super().__init__(port=browser_port, client_handler=self._handle_browser, limit=browser_limit)
        self._tunnel_port = tunnel_port
        self._tunnel_host = tunnel_host
        self._tunnel_key = tunnel_key

    async def _handle_browser(self, browser_reader: StreamReader, browser_writer: StreamWriter):
        I = f'[{id(browser_reader)}]\t'
        print(I, 'Client connected.')
        try:
            tunnel_reader, tunnel_writer = await tunnel1.open_encrypted_connection(self._tunnel_host, self._tunnel_port,
                                                                                   self._tunnel_key)
            print(I, 'Tunnel established.')
            async with tunnel_writer, netw.Pipe() as pipe:
                pipe.duplex((browser_reader, browser_writer), (tunnel_reader, tunnel_writer))
                print(I, 'Piping browser into tunnel.')
        except KeyboardInterrupt:
            print(I, 'KeyboardInterrupt')
            return
        except Exception as e:
            print(I, f'Error: {e}')
            raise
        finally:
            if not browser_writer.is_closing():
                browser_writer.close()
            await browser_writer.wait_closed()
            print(I, 'Terminated connection.')


def main():
    # test HTTP: http://neverssl.com

    # SERVER = '127.0.0.1'
    SERVER = '89.19.217.55'
    with SystemConfigurator():
        try:
            asyncio.run(
                AsyncHTTPProxyLocalHub(browser_port=12345, tunnel_key=17, tunnel_host=SERVER,
                                       tunnel_port=12346).start())
        except KeyboardInterrupt:
            print('Exit with SigTerm.')


if __name__ == '__main__':
    main()
