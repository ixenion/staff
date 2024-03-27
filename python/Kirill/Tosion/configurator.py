import os
from abc import ABC, abstractmethod

import safe_exit

HOST = '127.0.0.1'
PORT = 12345

try:
    import winreg


    def set_windows_registry_proxy(enabled: bool, host: str | None, port: int | None) -> None:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings', 0,
                             winreg.KEY_ALL_ACCESS)
        try:
            if host and port:
                winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, f'{host}:{port}')
            else:
                winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, '')
            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, int(enabled))
        finally:
            winreg.CloseKey(key)


except ImportError:
    def set_windows_registry_proxy(*_, **__) -> None:
        pass


def set_environment_variable(name: str, value: str | None) -> None:
    if value:
        os.environ[name] = value
    else:
        del os.environ[name]


class ISystemConfigurator(ABC):
    @abstractmethod
    def setup(self) -> None: ...

    @abstractmethod
    def reset(self) -> None: ...

    def __enter__(self):
        self.setup()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.reset()


class WindowsRegistryConfigurator(ISystemConfigurator):

    def setup(self) -> None:
        set_windows_registry_proxy(True, HOST, PORT)

    def reset(self) -> None:
        set_windows_registry_proxy(False, None, None)


class EnvironmentVariablesConfigurator(ISystemConfigurator):
    def setup(self) -> None:
        # TODO: only works in current process tree
        print('[WARNING]',
              f'Environment variables currently are set per process - may not work. Trye setting manually: HTTP_PROXY=http://{HOST}:{PORT} and HTTPS_PROXY=https://{HOST}:{PORT}')
        set_environment_variable('HTTP_PROXY', f'http://{HOST}:{PORT}')
        set_environment_variable('HTTPS_PROXY', f'https://{HOST}:{PORT}')

    def reset(self) -> None:
        pass


class SystemConfigurator(ISystemConfigurator):
    def __init__(self):
        self.configurators = [WindowsRegistryConfigurator(), EnvironmentVariablesConfigurator()]

    def setup(self) -> None:
        print('System proxy setup.')
        [configurator.setup() for configurator in self.configurators]
        safe_exit.register(self.reset)

    def reset(self) -> None:
        [configurator.reset() for configurator in self.configurators]
        print('System proxy reset.')
