from tkinter import *
from tkinter import ttk
import tkinter
from phrase_decryption import decrypt
#from phrase_decryption import decrypt_phrase

class DecryptionGUI(tkinter.Frame):
    def __init__(self) -> None:
        self.root_window()
        pass

    def root_window(self):
        self.root = Tk()
        self.root.title("Decryption Application")
        self.decryption_window = self.launch_widgets()
        self.root.geometry("450x300")
        return self.root
    
    ############################# Helper function(s)##################################
    def handle_OTP(self):
        self.OTP_length = len(self.phrase)
        self.pad = self.one_time_pad.get()
        self.pad.strip()
        try:
            self.clean_pad = [int(i) for i in self.pad.split(",")]
        except ValueError:
            self.clean_pad = [int(i) for i in self.pad.split(" ")]
        print(self.clean_pad, type(self.clean_pad))
    
        
    def decrypt_button_pressed(self):
        self.phrase = self.phrase_to_decrypt.get()
        self.otp = self.handle_OTP()
        self.decrypted_phrase.set("*" * len(self.phrase))
        return self.phrase, self.otp
    

    def clear_entry_fields(self):
        ''' (None)->None
        callback when the button is pressed.
        '''
        self.phrase_to_decrypt.set("")
        self.one_time_pad.set("")
        self.decrypted_phrase.set("")


    def reveal_button_pressed(self):
        self.window_contents = self.decrypted_phrase.get()
        i = 1
        while i < len(self.window_contents):
            if self.window_contents[i] == "*":
                self.decrypted_phrase.set(decrypt(self.phrase, self.clean_pad))
                i += len(self.window_contents)
                break
            else:
                self.decrypted_phrase.set(("*" * len(self.phrase)))
                i += len(self.window_contents)
                break

    ##################################################################################

    def launch_widgets(self):
        self.decryption_window = tkinter.Frame(self.root)
        self.title = self.header()
        self.title[0].pack()
        self.title[1].pack()
        self.left_window = ttk.Frame(self.decryption_window)
        self.left_window.pack(fill="both", side = LEFT, expand=True)
        #self.right_window = ttk.Frame(self.decryption_window)
        #self.right_window.pack(fill="both", side = RIGHT, expand=True)
        self.left_window_top = ttk.Frame(self.left_window)
        self.left_window_top.pack(fill="x", side = TOP, expand=True)
        self.left_window_bottom = ttk.Frame(self.left_window)
        self.left_window_bottom.pack(fill="x", side = BOTTOM, expand=True)
        self.decryption_entry_window = self.decrypt_enter()
        self.decryption_window.pack(fill="x", expand=True)
        self.one_time_pad_entry = self.OTP_pad_enter()
        self.decrypted_phrase_window = ttk.Frame(self.root)
        self.decrypted_phrase_window.pack(fill="x", side = TOP, expand=True)
        self.decrypted_phrase_UI = self.decryption_output()

        self.foot = self.footer()
 
    def header(self):
        '''(None)->list
        Creates the header. This is a window for displaying the title of the program.
        '''
        self.header_frame = ttk.Frame(self.root)
        self.header_frame.pack(side="top", fill="x")
        self.title = ttk.Label(self.header_frame, text="Decryption Application MVP")
        return self.header_frame, self.title

    def decrypt_enter(self):
        self.phrase_to_decrypt = tkinter.StringVar()
        self.phrase_to_decrypt_label = ttk.Label(self.left_window_bottom, text="Enter the phrase to decrypt:")
        self.phrase_to_decrypt_label.pack(fill="x", expand=True, side=TOP)
        self.phrase_to_decrypt_entry = ttk.Entry(self.left_window_bottom, textvariable=self.phrase_to_decrypt)
        self.phrase_to_decrypt_entry.pack(fill="x", side=LEFT, expand=True)
        self.decrypt_button = ttk.Button(self.left_window_bottom, text="Decrypt", command=self.decrypt_button_pressed)
        self.decrypt_button.pack(fill="x", side=RIGHT, expand=True)
    
    def OTP_pad_enter(self):
        self.one_time_pad = tkinter.StringVar()
        self.one_time_pad_label = ttk.Label(self.left_window_top, text="Enter the one time pad:")
        self.one_time_pad_label.pack(fill="x", side=TOP, expand=True)
        self.one_time_pad_entry = ttk.Entry(self.left_window_top, textvariable=self.one_time_pad)
        self.one_time_pad_entry.pack(fill="x", side=LEFT, expand=True)
        self.one_time_pad_button = ttk.Button(self.left_window_top, text="Clear", command=self.clear_entry_fields)
        self.one_time_pad_button.pack(fill="x", side= RIGHT, expand=True)
    
    def decryption_output(self):
        self.window = self.decrypted_phrase_window
        self.decrypted_phrase_label = ttk.Label(self.window, text="Decrypted phrase:")
        self.decrypted_phrase_label.pack(fill="x", expand=True)
        self.decrypted_phrase = tkinter.StringVar()
        self.decrypted_phrase_entry = ttk.Entry(self.window, textvariable=self.decrypted_phrase)
        self.decrypted_phrase_entry.pack(fill="x", side=LEFT, expand=True)
        self.reveal_button = ttk.Button(self.window, text="Reveal", command=self.reveal_button_pressed)
        self.reveal_button.pack(fill="x", side=RIGHT, expand=True)
        return self.decrypted_phrase_label, self.decrypted_phrase_entry, self.reveal_button
    
    def footer(self) -> list:
        '''(None)->list
        Creates the footer. This is a window for displaying the quit button.
        '''
        self.footer_frame = ttk.Frame(self.root)
        self.footer_frame.pack(side=BOTTOM, fill="x", padx = 3, pady = 3)
        self.button1 = ttk.Button(self.footer_frame, text="Quit", command = self.root.destroy)
        self.button1.pack(fill= "x")
       

def main():
    gui = DecryptionGUI()
    gui.root.mainloop()
main()