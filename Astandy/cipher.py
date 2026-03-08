from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class AstandyCipher:
    START_KEY = b"key_abcdefghijkl"
    START_IV  = b"iv_abcdefghijklm"

    def __init__(self):
        self._aes_cipher = Cipher(
            algorithms.AES(AstandyCipher.START_KEY),
            modes.CBC(AstandyCipher.START_IV),
            backend=default_backend()
        )

    def new_aes_cipher(self, key, iv):
        """
        Create a new AES cipher for client

        :param key: AES key
        :param iv: Initialization vector
        """
        self._aes_cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        )


    def encrypt(self, data: bytes):
        """
        Encrypt data with client's AES cipher

        :param data: Data to encrypt
        :return: Encrypted data
        """
        encryptor = self._aes_cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded = padder.update(data) + padder.finalize()
        encrypted = encryptor.update(padded) + encryptor.finalize()

        return encrypted

    def decrypt(self, data: bytes):
        """
        Decrypt data with client's AES cipher

        :param data: Data to decrypt
        :return: Decrypted data
        """
        decryptor = self._aes_cipher.decryptor()
        decrypted_data = decryptor.update(data) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted = unpadder.update(decrypted_data) + unpadder.finalize()

        return decrypted