



#Convert an M4A file to MP3. Output file uses 'date modified' and location of source file.
 
#Draft version-- Documentation, codes style and refactoring are works in progress.
#For compatibility and backup purposes.



#Output --convert m4a to mp3 file with default settings.
#        Output file retains location and modification time of the source file.
#Input  -- Prompt user to select a m4a file, 
#Tested -- in python version python3.8
#For compatibility and backup purposes.
#Draft version-- Documentation, codes style and refactoring are works in progress.

#notes before uploading to GitHub
#     remove/refactor the line about sys variables  sys.path.insert since it links to an absolute path to my pip installation modules
#     remove the above line and this
#     OP was using a line that looked like sys.path.insert(0, '/Users/path-to/python3.8/site-packages')

import os

import sys
 
import tkinter as tk
from tkinter import filedialog

from pydub import AudioSegment


def is_m4a(file_path):
    # Check if the file extension is '.m4a'
    return file_path.lower().endswith('.m4a')

def convert_to_mp3(m4a_file_path, output_mp3_file_path):
    # Load the M4A file
    audio = AudioSegment.from_file(m4a_file_path, format="m4a")

    # Export as MP3
    audio.export(output_mp3_file_path, format="mp3")
    
    

def open_file_dialog():
    # Create a file dialog and store the selected file's path
    file_path = filedialog.askopenfilename()

    # Print the selected file's path to the console
    if file_path:
        print("Selected file: " + file_path)
        
        
        if is_m4a(file_path):
            # Create the output MP3 file path by replacing '.m4a' with '.mp3'
            output_mp3_file_path = os.path.splitext(file_path)[0] + '.mp3'

            # Convert to MP3
            convert_to_mp3(file_path, output_mp3_file_path)
            # Get the modification time of the source file
            source_mod_time = os.path.getmtime(file_path)
            # Set the modification time of the destination file to match the source file
            os.utime(output_mp3_file_path, (source_mod_time, source_mod_time))
            print(f'Conversion complete. MP3 file saved at: {output_mp3_file_path}')
            #point file_path at the new mp3
            file_path = output_mp3_file_path
        else:
            print('The input file is not in M4A format.')        
        
    else:
        print("No file selected.")

# Create the main application window
root = tk.Tk()
root.title("File Chooser Example")

# Create a button to trigger the file dialog
button = tk.Button(root, text="Open File", command=open_file_dialog)
button.pack(pady=20)

# Start the main event loop
root.mainloop()

