import unittest
from base64 import b64decode
import os

from Astandy import StandClient
from Astandy.cipher import AstandyCipher


class AesTestCase(unittest.TestCase):

    def test_decrypt(self):
        client = StandClient('')
        client.cipher = AstandyCipher()
        decoded = client.cipher.decrypt(bytes.fromhex("F5AC1DBEDA9952AB5956923DE6754E58"))

        self.assertEqual(b"AES Hello :)", decoded)


    def test_encrypt(self):
        client = StandClient('')
        client.cipher = AstandyCipher()
        encoded = client.cipher.encrypt(b"AES Hello :)")

        self.assertEqual(bytes.fromhex("F5AC1DBEDA9952AB5956923DE6754E58"), encoded)
