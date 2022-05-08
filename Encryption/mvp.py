from tkinter import *
from tkinter import ttk
import tkinter

from phrase_encryption import encrypt_phrase

class EncryptionGUI(tkinter.Frame):
    def __init__(self) -> None:
        self.root_window()
        pass
    
    def root_window(self) -> None:
        self.root = Tk()
        self.root.title("Encryption Application")
        self.encrypt_window = self.launch_widgets()
        self.root.geometry("500x300")
        return self.root
    
    ############################# Helper function(s)##################################
    def encryption_button_pressed(self):
        ''' (None)->None
        callback when the button is pressed.
        '''
        self.script = encrypt_phrase(self.phrase.get())
        self.encrypted_phrase_placeholder.set(self.script[0])
        print(self.script[0])
        self.one_time_pad = self.script[1]
        self.one_time_pad_placeholder.set("*" * len(self.one_time_pad))
        print(self.one_time_pad_placeholder.get())

    def clear_entry_fields(self):
        ''' (None)->None
        callback when the button is pressed.
        '''
        print(f"{self.phrase.get()} -> Empty")
        self.phrase.set("")
        print(f"{self.encrypted_phrase_placeholder.get()} -> Empty")
        self.encrypted_phrase_placeholder.set("")
        print(f"{self.one_time_pad_placeholder.get()} -> Empty")
        self.one_time_pad_placeholder.set("")
        return self.phrase, self.encrypted_phrase_placeholder, self.one_time_pad_placeholder
     
    def reveal_OTP(self): 
        self.contents_of_OTP_entry_window = self.one_time_pad_placeholder.get()
        key = self.one_time_pad
        self.one_time_pad_placeholder.set(key)
        print(self.one_time_pad_placeholder.get())

    def hide_OTP(self):
        self.contents_of_OTP_entry_window = self.one_time_pad_placeholder.get()
        key = "*"*len(self.one_time_pad)
        self.one_time_pad_placeholder.set(key)
        print(self.one_time_pad_placeholder.get())

    def reveal_pad_button_pressed(self):
        '''(None)->None
        Callback when the button is pressed. Checks if the pad is hidden or not.
        If the hidden, the reveal_OTP() function is called. If not, the hide_OTP() function is called.
        '''
        self.current = self.one_time_pad_placeholder.get()
        search = True
        while search == True:
            if self.current[0] == "*":
                print("---BEGIN PRIVATE KEY---")
                self.reveal_OTP()
                print("---END PRIVATE KEY---")
                search = False
            else:
                self.hide_OTP()
                print("the OTP has been hidden")
                search = False

    ##################################################################################

    def launch_widgets(self) -> None:
        '''(None) -> None
        Creates the main window for the application and loads the widgets into the window.
        '''
        self.encrypt_window = ttk.Frame(self.root) # create a frame for the encrypt window
        self.title = self.header()
        self.title[0].pack()
        self.title[1].pack()
        self.encrypt_window.pack(pady=10,fill="x", expand=True)
        self.enter_window = self.encrypt_text_enter() # load the phrase entry window (this includes the phrase entry field, label, and the encryption button)
        self.enter_window[0].pack(fill="x", expand=True)
        self.enter_window[1].pack(fill="x", expand=True)
        self.enter_window[3].pack(fill="x", expand=True)
        self.area_for_encrypted_phrase = self.encrypted_phrase_window() # load the encrypted phrase window (includes the encrypted phrase label, entry, and button)
        self.area_for_encrypted_phrase[0].pack(fill="x", expand=True)
        self.area_for_encrypted_phrase[2].pack(fill="x", expand=True)
        self.area_for_encrypted_phrase[1].pack(fill="x", expand=True)
        self.OTP_area = self.one_time_pad_window() # load the one time pad window (includes the one time pad label, area where the OTP will be displayed, and button to reveal/hide the OTP)
        self.OTP_area[0].pack(expand=True)
        self.OTP_area[1].pack(expand=True)
        self.OTP_area[3].pack(expand=True)
        self.footer_area = self.footer() # load the footer
        self.footer_area[0].pack()
        self.footer_area[1].pack()

    def encrypt_text_enter(self) -> list:
        '''(None)->list
        Creates the window for entering a phrase to be encrypted. This window includes the phrase entry field, label, and the encryption button.
        Returns the phrase entry window as a list which is then called by the launch_widgets() function.
        '''
        self.phrase = tkinter.StringVar()
        self.encrypt_label = ttk.Label(self.encrypt_window, text="Enter a phrase to encrypt: ")#.grid(column=0, row=0, columnspan=2, sticky=(N, W), padx=5)
        self.encrypt_label.pack(fill="x", expand=True)
        self.encrypt_entry = ttk.Entry(self.encrypt_window, textvariable=self.phrase, style="TEntry")#.grid(column=0, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
        self.encrypt_entry.pack(fill="x", side = LEFT, expand=True)
        self.encryption_button = ttk.Button(self.encrypt_window, text="Encrypt", command=self.encryption_button_pressed, style="TButton")#.grid(column=2, row=1, pady=5, padx=5)#.pack(fill="x", expand=True)
        self.encryption_button.pack(fill="x", side= RIGHT, expand=True)
        return self.encrypt_label, self.encrypt_entry, self.phrase, self.encryption_button
    
    def encrypted_phrase_window(self)-> list:
        '''(None)->list
        Creates the window for displaying the encrypted phrase. This window includes the encrypted phrase label, entry, and button.
        Returns the encrypted phrase window as a list which is then called by the launch_widgets() function.
        '''
        self.encrypted_phrase_placeholder = tkinter.StringVar()
        self.en_phrase_window = ttk.Frame(self.root)
        self.en_phrase_window.pack(fill="x", expand=True)
        self.phrase_label = ttk.Label(self.en_phrase_window, text="Encrypted phrase:")
        self.phrase_label.pack(fill="x", expand=True)
        self.encrypted_phrase_entry = ttk.Entry(self.en_phrase_window, textvariable=self.encrypted_phrase_placeholder)#.pack(fill="x", expand=True)
        self.encrypted_phrase_entry.pack(fill="x", side = LEFT, expand = True)
        self.clear_button = ttk.Button(self.en_phrase_window, text="Clear", command=self.clear_entry_fields)#.grid(column=3, row=3, sticky=(N, S, E, W))
        self.clear_button.pack(fill="x", side= RIGHT, expand=True)
        #self.encrypt_button = ttk.Button(self.encrypt_window, text="Encrypt", command=self.encryption_button_pressed, style="TButton").grid(column=2, row=2)
        return self.phrase_label, self.clear_button, self.encrypted_phrase_entry, self.encrypted_phrase_placeholder, self.en_phrase_window

    def one_time_pad_window(self) -> list:
        '''(None)->list
        Creates the window for displaying the one time pad. This window includes the one time pad label, area where the OTP will be displayed, and button to reveal/hide the OTP.
        Returns the one time pad window as a list, which is then called by the launch_widgets() function.
        '''
        self.one_time_pad_placeholder = tkinter.StringVar()
        self.OTP_window = ttk.Frame(self.root)
        self.OTP_window.pack(fill="x", expand=True)
        self.one_time_pad_label = ttk.Label(self.OTP_window, text="One-time pad: ")
        self.one_time_pad_label.pack(fill="x", expand=True)
        self.one_time_pad_entry = ttk.Entry(self.OTP_window, textvariable=self.one_time_pad_placeholder)
        self.one_time_pad_entry.pack(fill= "x", side=LEFT, expand=True)
        self.reveal_pad_button = ttk.Button(self.OTP_window, text="Reveal", command=self.reveal_pad_button_pressed)
        self.reveal_pad_button.pack(fill= "x", side=RIGHT, expand=True)
        return self.one_time_pad_label, self.one_time_pad_entry, self.one_time_pad_placeholder, self.reveal_pad_button, self.OTP_window

    def footer(self) -> list:
        '''(None)->list
        Creates the footer. This is a window for displaying the quit button.
        '''
        self.footer_frame = ttk.Frame(self.root)
        self.footer_frame.pack(side=BOTTOM, fill="x", padx= 6, pady=6)
        self.button1 = ttk.Button(self.footer_frame, text="Quit", command = self.root.destroy)
        self.button1.pack(fill= "x")
        return self.footer_frame, self.button1
    
    def header(self) -> list:
        '''(None)->list
        Creates the header. This is a window for displaying the title of the program.
        '''
        self.header_frame = ttk.Frame(self.root)
        self.header_frame.pack(side="top", fill="x")
        self.title = ttk.Label(self.header_frame, text="Encryption Application MVP")
        return self.header_frame, self.title

def test_function():
    gui = EncryptionGUI()
    gui.root.mainloop()

test_function()
