'''
    This splash screen serves as the initial interface for the Real Time Face Recognition Attendance System,
    marking the starting point of the application's execution.
'''

# To initialize the screen, this module necessitates the inclusion of the following dependencies.
import tkinter as tk
from tkinter import ttk
import random

from app.controllers.image_loader import ImageLoader
from app.controllers.file_manager import FileManager

from app.windows.terms_and_conditions import TermsConditionsScreen

class SplashScreen:
    def __init__(self, master):
        '''
            Initializes the Splash screen.

            :param master: The main window of the application.
        '''
        self.master = master

        # Remove title bar
        self.master.overrideredirect(True)

        # # Set the size of the window
        # window_width = 350
        # window_height = 230

        # Get the screen width and height
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Set the window size to approximately 350x230
        window_width = int(screen_width * (350 / screen_width))
        window_height = int(screen_height * (230 / screen_height))

        # Calculate position x and y coordinates to center the window
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Set the geometry of the splash screen
        self.master.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        # Set the background image
        self.splash_background_image = ImageLoader.load_image('splash_background_image', (window_width, window_height))

        self.background_label = ttk.Label(self.master, image=self.splash_background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Wait for 2 to 5 seconds before opening new window
        self.master.after(random.randint(2000, 5000), self.open_new_window)
    def open_new_window(self):
        '''
           Closes the current screen and opens the new screen.
        '''
        self.master.destroy()

        # Check if the user preferences file exists
        if FileManager.check_file_exists():
            # Verify if the file format is correct
            file = FileManager()
            if file.check_correct_format():
                # Check if the user is logout or not
                if file.get_islogout() is not True:
                    print('User is not logout!')

                else:
                    # If the user is logout
                    # Open the Login window
                    new_window = tk.Tk()
                    TermsConditionsScreen(new_window)
                    new_window.mainloop()
            else:
                # If the format is incorrect, recreate the file with the default content
                FileManager.create_file()
                # Open the Terms and Conditions window
                new_window = tk.Tk()
                TermsConditionsScreen(new_window)
                new_window.mainloop()
        else:
            # If the file does not exist, create it with the default content
            FileManager.create_file()
            # Open the Terms and Conditions window
            new_window = tk.Tk()
            TermsConditionsScreen(new_window)
            new_window.mainloop()


# # Create the main window with the splash screen
# if __name__ == "__main__":
#     root = tk.Tk()
#     splash = SplashScreen(root)
#     root.mainloop()
