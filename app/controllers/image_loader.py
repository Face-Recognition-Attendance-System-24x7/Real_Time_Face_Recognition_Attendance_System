'''
    This module contains a class designed to manage the loading of images
    required by various windows in the application.
'''

# This module requires the following dependencies to function properly.
from PIL import Image, ImageTk

class ImageLoader:
    '''
        This class provides static methods for retrieving and preparing images
        from the assets directory, including app icons, background images, arrows,
        and other visual elements needed for the application's interface.
    '''
    path = '../assets/images'

    @staticmethod
    def load_image(image_name: str, size: tuple[int, int]) -> ImageTk.PhotoImage:
        '''
            Loads and resizes an image from the assets directory.

            :param image_name: The name of the image file (excluding extension).
            :param size: A tuple (width, height) specifying the desired size of the image.
            :return: A resized image suitable for Tkinter.
        '''
        image_path = f'{ImageLoader.path}/{image_name}.png'

        try:
            # Load the image
            image = Image.open(image_path)
        except FileNotFoundError:
            return None

        # Resize the image
        resized_image = image.resize(size, Image.Resampling.LANCZOS)

        # Convert the image to a format suitable for Tkinter
        return ImageTk.PhotoImage(resized_image)

    @staticmethod
    def app_icon() -> str:
        '''
            Returns the path to the app icon.

            :return: The path to the app icon file.
        '''
        return f'{ImageLoader.path}/app_icon.ico'
