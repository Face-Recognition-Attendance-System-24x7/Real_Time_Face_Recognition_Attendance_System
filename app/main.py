'''
    This script initializes the Real-Time Face Recognition Attendance System,
    starting with the display of the splash screen.
'''
# To initialize the screen, this module requires the inclusion of the following dependencies.
import tkinter as tk
from app.windows.splash_screen import SplashScreen

# Create the main window with the splash screen
if __name__ == "__main__":
    root = tk.Tk()
    splash = SplashScreen(root)
    root.mainloop()
