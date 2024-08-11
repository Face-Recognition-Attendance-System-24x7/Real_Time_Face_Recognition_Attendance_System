'''
    This module defines the Create Account screen for user and subuser of the Real-Time Face Recognition Attendance System.
'''

# To initialize the screen, this module necessitates the inclusion of the following dependencies.
import tkinter as tk
from tkinter import ttk

from app.controllers.image_loader import ImageLoader
from app.controllers.file_manager import FileManager

class CreateAccountScreen:
    def __init__(self, master):
        '''
            Initializes the Create Account screen.

            :param master: The window of the application.
        '''
        self.master = master
        self.master.title("Create Account")

        # Remove title bar
        self.master.overrideredirect(True)

        # Set the application icon
        self.master.iconbitmap(ImageLoader.app_icon())

        self.master.configure(bg='white')

        # # Define the size of the window
        # window_width = 500
        # window_height = 300

        # Get the dimensions of the screen
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Set the window size to approximately 700x6400
        window_width = int(screen_width * (600 / screen_width))
        window_height = int(screen_height * (600 / screen_height))

        # Calculate coordinates to center the window on the screen
        position_x = (screen_width - window_width) // 2
        position_y = (screen_height - window_height) // 2

        # Set the geometry of the window
        self.master.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        # Color for text and background
        self.master.foreground_color = 'black'
        self.master.background_color = 'white'

        # Font for text
        self.master.font = ('helvatica', 12)

        # Frame on window that contains labelframe
        self.master.Frame = tk.Frame(self.master,
                                                  height=window_height,
                                                  width=window_width,
                                                  bg=self.master.background_color,
                                                  )
        self.master.Frame.pack(expand=True, fill=tk.BOTH)

        # Stop the frame from propagating the widget to be shrink or fit
        self.master.Frame.pack_propagate(False)

        # Label Frame on Frame
        self.master.Frame_LabelFrame = tk.LabelFrame(self.master.Frame,
                                                                  text='Create User Account',
                                                                  bd=1,
                                                                  font=self.master.font,
                                                                  foreground=self.master.foreground_color,
                                                                  background=self.master.background_color,
                                                                  height=window_height,
                                                                  width=window_width,
                                                                  relief='solid'
                                                                  )
        self.master.Frame_LabelFrame.pack(expand=True, padx=10, pady=10, sticky=tk.NSEW)

        # Stop the label frame from propagating the widget to be shrink or fit
        self.master.Frame_LabelFrame.pack_propagate(False)

        # Inner frame of label frame
        self.master.Frame_LabelFrame_innerFrame = tk.Frame(self.master.Frame_LabelFrame,
                                                                        height=window_height,
                                                                        width=window_width,
                                                                        background='blue'
                                                                        )
        self.master.Frame_LabelFrame_innerFrame.pack(expand=True, fill=tk.BOTH)

        # Stop the inner frame of label frame from propagating the widget to be shrink or fit
        self.master.Frame_LabelFrame_innerFrame.pack_propagate(False)

        # Configuring rows and columns of the inner frame of the label frame
        self.master.Frame_LabelFrame_innerFrame.rowconfigure(0, weight=1)
        self.master.Frame_LabelFrame_innerFrame.rowconfigure(1, weight=1)
        self.master.Frame_LabelFrame_innerFrame.rowconfigure(2, weight=1)
        self.master.Frame_LabelFrame_innerFrame.rowconfigure(3, weight=1)
        self.master.Frame_LabelFrame_innerFrame.rowconfigure(4, weight=2)
        self.master.Frame_LabelFrame_innerFrame.rowconfigure(5, weight=1)
        self.master.Frame_LabelFrame_innerFrame.rowconfigure(6, weight=1)
        self.master.Frame_LabelFrame_innerFrame.rowconfigure(7, weight=1)
        self.master.Frame_LabelFrame_innerFrame.columnconfigure(0, weight=2)
        self.master.Frame_LabelFrame_innerFrame.columnconfigure(1, weight=2)

        self.master.Frame_LabelFrame_innerFrame_Frame1 = ttk.Frame(
            self.master.Frame_LabelFrame_innerFrame, )
        self.master.Frame_LabelFrame_innerFrame_Frame1.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)

        self.master.Frame_LabelFrame_innerFrame_Frame1.rowconfigure(0, weight=1)
        self.master.Frame_LabelFrame_innerFrame_Frame1.rowconfigure(1, weight=1)
        self.master.Frame_LabelFrame_innerFrame_Frame1.columnconfigure(0, weight=1)
        self.master.Frame_LabelFrame_innerFrame_Frame1.columnconfigure(1, weight=1)
        #
        self.master.Frame_LabelFrame_innerFrame_Frame1_Label1 = ttk.Label(
            self.master.Frame_LabelFrame_innerFrame_Frame1,
            text='Name',
            font=self.master.font
        )
        self.master.Frame_LabelFrame_innerFrame_Frame1_Label1.grid(row=0, column=0, sticky='nw', padx=2,
                                                                                pady=2)
        self.master.Frame_LabelFrame_innerFrame_Frame1_Label1.pack(side=tk.LEFT)
        self.master.Frame_LabelFrame_innerFrame_Frame1_Entry = ttk.Entry(
            self.master.Frame_LabelFrame_innerFrame_Frame1,
            text='Name',
            font=self.master.font
        )
        self.master.Frame_LabelFrame_innerFrame_Frame1_Entry.grid(row=0, column=1, sticky=tk.NW, padx=2,
                                                                               pady=2)
        self.master.Frame_LabelFrame_innerFrame_Frame1_Entry.pack(side=tk.LEFT)
        self.master.Frame_LabelFrame_innerFrame_Frame2 = tk.Frame(
            self.master.Frame_LabelFrame_innerFrame,
            background='red')
        self.master.Frame_LabelFrame_innerFrame_Frame2.grid(row=1, column=0, sticky='nsew')

        self.master.Frame_LabelFrame_innerFrame_Frame3 = tk.Frame(
            self.master.Frame_LabelFrame_innerFrame,
            background='orange')
        self.master.Frame_LabelFrame_innerFrame_Frame3.grid(row=2, column=0, sticky='nsew')

        self.master.Frame_LabelFrame_innerFrame_Frame4 = tk.Frame(
            self.master.Frame_LabelFrame_innerFrame,
            background='green')
        self.master.Frame_LabelFrame_innerFrame_Frame4.grid(row=3, column=0, sticky='nsew')

        self.master.Frame_LabelFrame_innerFrame_Frame5 = tk.Frame(
            self.master.Frame_LabelFrame_innerFrame,
            background='green')
        self.master.Frame_LabelFrame_innerFrame_Frame5.grid(row=4, column=0, sticky='nsew', columnspan=2)

        self.master.Frame_LabelFrame_innerFrame_Frame6 = tk.Frame(
            self.master.Frame_LabelFrame_innerFrame,
            background='green')
        self.master.Frame_LabelFrame_innerFrame_Frame6.grid(row=5, column=0, sticky='nsew')

        self.master.Frame_LabelFrame_innerFrame_Frame7 = tk.Frame(
            self.master.Frame_LabelFrame_innerFrame,
            background='green')
        self.master.Frame_LabelFrame_innerFrame_Frame7.grid(row=6, column=0, sticky='nsew')

        self.master.Frame_LabelFrame_innerFrame_Frame8 = tk.Frame(
            self.master.Frame_LabelFrame_innerFrame,
            background='green')
        self.master.Frame_LabelFrame_innerFrame_Frame8.grid(row=7, column=0, sticky='nsew')


# # Run the application
# if __name__ == "__main__":
#     root = tk.Tk()
#     CreateAccountScreen(root)
#     root.mainloop()
