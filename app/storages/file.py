'''
    This module contains a class designed to manage file operations such as
    creating, reading, and checking the existence of files.
'''

# This module requires the following dependencies to function properly.
import os
import pickle
from typing import Any, List, Optional

class File:
    '''
        This class provides methods for handling both binary and text files,
        including creating, reading, and verifying their existence.
    '''

    @staticmethod
    def create_binary(file_path: str, data: Any) -> bool:
        '''
            Creates a new binary file or updates an existing one.

            :param file_path: The path of the file to create or update.
            :param data: The data to be stored in the file.
            :return: True if the file was successfully created or updated, otherwise False.
        '''
        try:
            with open(file_path, 'wb') as file:
                pickle.dump(data, file)
            return True
        except Exception as e:
            return False

    @staticmethod
    def read_binary(file_path: str) -> Optional[Any]:
        '''
            Reads data from a binary file.

            :param file_path: The path of the binary file to read.
            :return: The data read from the file, or None if an error occurred.
        '''
        try:
            with open(file_path, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            return None

    @staticmethod
    def read_text(file_path: str) -> Optional[List[str]]:
        '''
            Reads content from a text file.

            :param file_path: The path of the text file to read.
            :return: A list containing the lines of the file, or None if an error occurred.
        '''
        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except Exception as e:
            return None
    @staticmethod
    def file_exists(file_path: str) -> bool:
        '''
        Checks if the file exists at the specified path.

        :param file_path: The path of the file to check.
        :return: True if the file exists, otherwise False.
        '''
        return os.path.exists(file_path)