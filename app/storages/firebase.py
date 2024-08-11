'''
    This module contains a class designed to manage firebase operations such as
    storing, accessing data and images from both realtime database and storage.
'''

# This module requires the following dependencies to function properly.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, storage

cred = credentials.Certificate()
firebase_admin.initialize_app(cred, {
    'databaseURL' : '',
    'storageBucket' : ''
})

class Firebase:
    '''
        This class provides methods for handling Firebase Realtime Database and Storage operations,
        such as retrieving and storing data and images.
    '''
    root_path = 'Users'

    @staticmethod
    def load_data(path: list = None) -> dict:
        '''
            Retrieves data from the Firebase Realtime Database based on the specified path.

            :param path: A list specifying the path to the data to retrieve
                         e.g., ['user', 'department', 'subuser', 'students', 'studentId'].
            :return: A dictionary of the data retrieved from the specified path,
                     or an error message if an exception occurs.
        '''
        root_path = Firebase.root_path
        database_path = None
        match len(path):
            case 1: database_path = f'{root_path}/{path[0]}'
            case 3: database_path = f'{root_path}/{path[0]}/{path[1]}_{path[2]}'
            case 4: database_path = f'{root_path}/{path[0]}/{path[1]}_{path[2]}/{path[3]}'
            case 5: database_path = f'{root_path}/{path[0]}/{path[1]}_{path[2]}/{path[3]}/{path[5]}'
            case _: database_path = f'{root_path}'
        try:
            ref = db.reference(database_path)
            return ref.get()
        except Exception as e:
            return {"error": "An error occurred while retrieving data."}

    @staticmethod
    def upload_image(image_path: str, storage_path: str) -> bool:
        '''
        Uploads an image to Firebase Storage.

        :param image_path: The local path of the image to upload.
        :param storage_path: The path in Firebase Storage where the image will be uploaded.
        :return: True if the upload is successful, otherwise False.
        '''
        try:
            bucket = storage.bucket()
            blob = bucket.blob(storage_path)
            blob.upload_from_filename(image_path)
            return True
        except Exception as e:
            print(f"Error occurred while uploading image: {e}")
            return False

    @staticmethod
    def download_image(storage_path: str, local_path: str) -> bool:
        '''
        Downloads an image from Firebase Storage.

        :param storage_path: The path in Firebase Storage where the image is stored.
        :param local_path: The local path where the image will be saved.
        :return: True if the download is successful, otherwise False.
        '''
        try:
            bucket = storage.bucket()
            blob = bucket.blob(storage_path)
            blob.download_to_filename(local_path)
            return True
        except Exception as e:
            print(f"Error occurred while downloading image: {e}")
            return False