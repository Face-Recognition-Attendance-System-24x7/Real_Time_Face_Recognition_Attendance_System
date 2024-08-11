'''
    This module provides classes for handling both two-way encryption (which can be reversed)
    and one-way encryption (which cannot be reversed) methods.
'''

# Required dependencies
import hashlib

class CaesarCipher:
    '''
        This class provides methods for two-way encryption using the Caesar cipher technique.
        The Caesar cipher shifts each character in the password by a fixed number of positions.
    '''
    shift = 3  # Number of positions to shift each character

    @staticmethod
    def encrypt(password: str) -> str:
        '''
            Encrypts a password using Caesar cipher.

            :param password: The plaintext password to encrypt.
            :return: The encrypted password.
        '''
        encrypted_password = ''.join(
            chr((ord(char) + CaesarCipher.shift - 32) % 95 + 32) for char in password
        )
        return encrypted_password

    @staticmethod
    def decrypt(encrypted_password: str) -> str:
        '''
            Decrypts a password that was encrypted using Caesar cipher.

            :param encrypted_password: The encrypted password to decrypt.
            :return: The decrypted (plaintext) password.
        '''
        decrypted_password = ''.join(
            chr((ord(char) - CaesarCipher.shift - 32) % 95 + 32) for char in encrypted_password
        )
        return decrypted_password


class HashedPassword:
    '''
        This class provides methods for one-way encryption using SHA-256 hashing combined with a pepper.
        The hashed password cannot be reversed to reveal the original plaintext password.
    '''
    pepper = 'face_24x7'  # A fixed string added to the password before hashing

    @staticmethod
    def hash_password_with_pepper(password: str) -> str:
        '''
            Hashes a password using SHA-256 along with a pepper for added security.

            :param password: The plaintext password to hash.
            :return: The hashed password as a hexadecimal string.
        '''
        # Combine the password with the pepper
        password_with_pepper = password + HashedPassword.pepper

        # Generate the SHA-256 hash of the combined password and pepper
        hashed_password = hashlib.sha256(password_with_pepper.encode()).hexdigest()

        return hashed_password
