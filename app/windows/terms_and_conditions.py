'''
    This module defines the Terms and Conditions screen for the Real-Time Face Recognition Attendance System.
'''

# To initialize the screen, this module necessitates the inclusion of the following dependencies.
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from PIL import Image, ImageTk

from app.controllers.image_loader import ImageLoader
from app.controllers.file_manager import FileManager

from app.windows.create_account_screen import CreateAccountScreen

class TermsConditionsScreen:
    def __init__(self, master):
        '''
            Initializes the Terms and Conditions screen.

            :param master: The window of the application.
        '''
        self.master = master
        self.master.title("Terms and Conditions...")

        # Set the application icon
        self.master.iconbitmap(ImageLoader.app_icon())

        # # Define the size of the window
        # window_width = 550
        # window_height = 400

        # Focus the screen
        self.master.focus_force()

        # Get the dimensions of the screen
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Set the window size to approximately 650x400
        window_width = int(screen_width * (550 / screen_width))
        window_height = int(screen_height * (400 / screen_height))

        # Calculate coordinates to center the window on the screen
        position_x = (screen_width - window_width) // 2
        position_y = (screen_height - window_height) // 2

        # Set the geometry of the window
        self.master.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        # Apply custom styles
        style = ttk.Style()
        # Configure a new style for ttk.Frame
        style.configure('TFrame', background='white')

        # Configure a new style for ttk.Label
        style.configure("Tlabel1.TLabel", font=("Cascadia Code SemiBold", 10),background='white')
        style.configure("Tlabel2.TLabel", font=("Calibri", 9),background='white')

        # Frame 1: Header
        self.frame1 = ttk.Frame(self.master, width=window_width, height=int((window_height//7)*1.5), style='TFrame')
        self.frame1.pack(fill=tk.X)
        self.frame1.pack_propagate(False)

        ttk.Label(self.frame1, text='Terms and Conditions', style='Tlabel1.TLabel').pack(anchor=tk.NW, padx=10, pady=10)
        ttk.Label(self.frame1, text='Welcome to the Face Recognition Attendance System with Anti-Spoofing.' +
            '\nPlease read the following terms and conditions carefully before using this application.',
            style='Tlabel2.TLabel').pack(anchor=tk.NW, padx=12)

        ttk.Separator(self.master, orient='horizontal').pack(fill='x')

        # Frame 2: Terms and Conditions Text
        self.frame2 = ttk.Frame(self.master, width=window_width, height=int((window_height//7)*4.5), style='TFrame')
        self.frame2.pack()
        self.frame2.pack_propagate(False)

        # ScrolledText widget to display terms and conditions
        self.text_widget = tk.scrolledtext.ScrolledText(self.frame2, wrap=tk.WORD, width=int((window_width//2)*1.5), height=int((window_height//7)*4.3))
        self.text_widget.pack(padx=50,pady=10, expand=False)

        # Load the terms and conditions text
        self.load_terms_conditions()

        # Make the text widget read-only and disable copy, cut, paste, delete, and backspace
        self.text_widget.bind("<Control-c>", lambda e: "break")
        self.text_widget.bind("<Control-x>", lambda e: "break")
        self.text_widget.bind("<Control-v>", lambda e: "break")
        self.text_widget.bind("<Delete>", lambda e: "break")
        self.text_widget.bind("<BackSpace>", lambda e: "break")
        self.text_widget.config(state=tk.DISABLED)

        self.text_widget.tag_configure('header', font=('Cascadia Code SemiBold', 10))
        self.text_widget.tag_configure('body', font=('Calibri', 10))

        # Frame 3: Agree Button
        self.frame3 = ttk.Frame(self.master, width=window_width, height=int((window_height//7)), style='TFrame')
        self.frame3.pack(fill=tk.X)
        self.frame3.pack_propagate(False)

        ttk.Separator(self.frame3, orient='horizontal').pack(fill='x')

        ttk.Label(self.frame3, text='By clicking "I Agree", you agree to these terms and conditions.',
                  style='Tlabel2.TLabel').pack(side=tk.LEFT, anchor=tk.NW, padx=40, pady=15)

        self.agree_button_image = ImageLoader.load_image('agree', (16, 16))
        ttk.Button(self.frame3, text='I Agree', image=self.agree_button_image, compound=tk.LEFT,
                   command=self.open_create_account_screen).pack(side=tk.LEFT, anchor=tk.NE, pady=15)

    def load_terms_conditions(self):
        '''
            Loads the terms and conditions from a file and displays them in the text widget.
        '''
        terms_text = FileManager.read_terms_and_conditions_file()
        if isinstance(terms_text, list):
            for id, term in enumerate(terms_text):
                if id == 0:
                    self.text_widget.insert(tk.END, term, 'header')
                elif id in range(2, len(terms_text), 3):
                    self.text_widget.insert(tk.END, term, 'header')
                else:
                    self.text_widget.insert(tk.END, term, 'body')
        else:
            self.text_widget.insert(tk.END, terms_text, 'body')


    def open_create_account_screen(self):
        '''
            Closes the current screen and opens the Create Account screen.
        '''
        self.master.destroy()
        new_window = tk.Tk()
        CreateAccountScreen(new_window)
        new_window.mainloop()


# # Run the application
# if __name__ == "__main__":
#     root = tk.Tk()
#     TermsConditionsScreen(root)
#     root.mainloop()
