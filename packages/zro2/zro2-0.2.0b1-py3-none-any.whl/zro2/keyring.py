from functools import cache
import platform

@cache
def os_keyring():
    if platform.system() == "Windows":
        from keyring.backends.Windows import WinVaultKeyring
        return WinVaultKeyring()
    elif platform.system() == "Darwin":
        from keyring.backends.macOS import Keyring
        return Keyring()
    elif platform.system() == "Linux":
        from keyring.backends.SecretService import Keyring
        return Keyring()