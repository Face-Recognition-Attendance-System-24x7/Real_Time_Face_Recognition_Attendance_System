'''
    This module contains a class that interacts with the File class to perform file operations,
    such as reading, creating, and returning file data based on specific requirements.
'''

# This module requires the following dependencies to function properly.
from app.storages.file import File

from app.controllers.password_manager import CaesarCipher, HashedPassword


class FileManager:
    '''
        This class provides methods for accessing and storing data in both binary and text files.
    '''
    default_file_content = {
        'islogout': False,
        'user_name': '',
        'user_password': '',
        'department': '',
        'subuser_name': '',
        'subuser_password': '',
        'isdashboard': '',
        'ismainuser': ''
    }
    text_file_path = '../assets/license/terms_and_conditions.txt'
    binary_file_path = '../assets/user_config.bat'

    def __init__(self):
        '''
            Initializes the FileManager instance by setting the binary file path and
            loading data from the binary file.
        '''
        self.binary_file_path = FileManager.binary_file_path
        self.data = File.read_binary(self.binary_file_path)

    def check_correct_format(self) -> bool:
        '''
            Checks whether the stored data in the binary file matches the format
            defined by FileManager.default_file_content (only keys are compared, not values).

            :return: True if the format is the same, otherwise False.
        '''
        if self.data:
            return set(self.data.keys()) == set(FileManager.default_file_content.keys())
        return False

    def get_islogout(self) -> bool:
        '''
            Returns the 'islogout' value from the binary file content.

            :return: The value of 'islogout'.
        '''
        return self.data.get('islogout', False)

    def get_user_name(self) -> str:
        '''
            Returns the 'user_name' value from the binary file content.

            :return: The value of 'user_name'.
        '''
        return self.data.get('user_name', '')

    def get_user_password(self) -> str:
        '''
            Returns the 'user_password' value from the binary file content.

            :return: The value of 'user_password'.
        '''
        return CaesarCipher.decrypt(self.data.get('user_password', ''))

    def get_department(self) -> str:
        '''
            Returns the 'department' value from the binary file content.

            :return: The value of 'department'.
        '''
        return self.data.get('department', '')
    def get_subuser_name(self) -> str:
        '''
            Returns the 'subuser_name' value from the binary file content.

            :return: The value of 'subuser_name'.
        '''
        return self.data.get('subuser_name', '')

    def get_subuser_password(self) -> str:
        '''
            Returns the 'subuser_password' value from the binary file content.

            :return: The value of 'subuser_password'.
        '''
        return CaesarCipher.decrypt(self.data.get('subuser_password', ''))

    def get_isdashboard(self) -> str:
        '''
            Returns the 'isdashboard' value from the binary file content.

            :return: The value of 'isdashboard'.
        '''
        return self.data.get('isdashboard', '')

    def get_ismainuser(self) -> str:
        '''
            Returns the 'ismainuser' value from the binary file content.

            :return: The value of 'ismainuser'.
        '''
        return self.data.get('ismainuser', '')

    def get_all_data(self) -> dict:
        '''
            Returns the entire dictionary of the binary file content, with decrypted passwords.

            :return: The entire data stored in the binary file.
        '''
        self.data['user_password'] = CaesarCipher.decrypt(self.data.get('user_password', ''))
        self.data['subuser_password'] = CaesarCipher.decrypt(self.data.get('subuser_password', ''))
        return self.data

    @staticmethod
    def check_file_exists() -> bool:
        '''
            Checks whether the binary file exists.

            :return: True if the file exists, otherwise False.
        '''
        return File.file_exists(FileManager.binary_file_path)

    @staticmethod
    def create_file(file_content: dict = None) -> bool:
        '''
            Creates a binary file using the provided file content or the default file content
            if none is provided, and saves it to the binary file path.

            :param file_content: A dictionary containing the content to be stored in the file.
            :return: True if the file was successfully created, otherwise False.
        '''
        if file_content is None:
            file_content = FileManager.default_file_content
        return File.create_binary(FileManager.binary_file_path, file_content)

    @staticmethod
    def read_terms_and_conditions_file() -> list:
        '''
            Reads the terms and conditions text file.

            :return: A list of lines from the file if successful, otherwise 'No Data Found!'.
        '''
        data = File.read_text(FileManager.text_file_path)
        return data if data else 'No Data Found!'