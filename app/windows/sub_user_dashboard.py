'''
    This module defines the Terms and Conditions screen for the Real-Time Face Recognition Attendance System.
'''

# To initialize the screen, this module necessitates the inclusion of the following dependencies.
import tkinter as tk
from tkinter import ttk

from app.controllers.image_loader import ImageLoader
from app.controllers.file_manager import FileManager

class SubUserDashboardScreen:
    def __init__(self, master):
        '''
            Initializes the Sub User Dashboard screen.

            :param master: The window of the application.
        '''
        self.master = master
        self.master.title("Sub User Dashboard")

        # Set the application icon
        self.master.iconbitmap(ImageLoader.app_icon())

        # Define the size of the window
        window_width = 500
        window_height = 300

        # Get the dimensions of the screen
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Calculate coordinates to center the window on the screen
        position_x = (screen_width - window_width) // 2
        position_y = (screen_height - window_height) // 2

        # Set the geometry of the window
        self.master.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
