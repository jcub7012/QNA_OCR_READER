import subprocess
import platform
import tkinter as tk
from tkinterdnd2 import TkinterDnD
from tkinter import Frame
from main import main
import os

# Declare pdf_path at the global level (optional, you can also do this inside on_drop)
global pdf_path  # Declare that you're using the global variable
pdf_path = None

def on_drop(event):
    global pdf_path, confirmation_frame  # Declare that you're using the global variable
    pdf_path = event.data.strip("{}").strip()
    print(f"Debug: PDF Path from event = {pdf_path}")
    filename = os.path.basename(pdf_path)
    confirmation_label.config(text=f"Are you sure you want to process {filename}?")
    confirmation_frame.pack(expand=True)

def proceed():
    global pdf_path  # Declare that you're using the global variable
    if pdf_path is not None:
        print(f"Processing {pdf_path}")
        main(pdf_path)  # Run the main function, assuming it performs the desired operations
        root.destroy()  # This will destroy the Tkinter window
    else:
        print("Error: No PDF file selected.")

def show_confirmation_frame(pdf_path, pdf_directory):
    global root  # Declare root as global if it is not passed as an argument
    confirmation_frame = tk.Frame(root)
    confirmation_frame.pack(expand=True)
    
    confirmation_label = tk.Label(confirmation_frame, text=f"Are you sure you want to process {pdf_path}?")
    confirmation_label.pack(side="left")
    
    yes_button = tk.Button(confirmation_frame, text="Yes", command=lambda: proceed(pdf_directory))
    yes_button.pack(side="left")
    
    no_button = tk.Button(confirmation_frame, text="No", command=confirmation_frame.destroy)
    no_button.pack(side="left")

def cancel():
    confirmation_frame.pack_forget()

# Initialize main GUI window
root = TkinterDnD.Tk()
root.title("Q&A OCR Scanner")
root.configure(bg='lightblue')

# Assuming image_width and image_height are your image dimensions
# This is a placeholder; replace it with the actual dimensions of the image
image_width = 1920
image_height = 1080

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Maintain aspect ratio
image_aspect_ratio = image_width / image_height

# Calculate new dimensions
new_width = int(screen_width * 0.3)
new_height = int(new_width / image_aspect_ratio)

# Calculate position for centering
x_position = (screen_width - new_width) // 2
y_position = (screen_height - new_height) // 2

# Set window dimensions and position
root.geometry(f"{new_width}x{new_height}+{x_position}+{y_position}")

# Drag and drop label
label = tk.Label(root, text="Drag and Drop a PDF File Here", font=("Open Sans", 12))
label.pack(expand=True, padx=20, pady=20)
label_frame = tk.Frame(root, bg='lightblue', borderwidth=2, relief="solid")

# Options label
option_text = tk.StringVar()
option_text.set("Key Commands: [c] Continue, [n] New, [Ctrl+Z] Undo, [Ctrl+Y] Redo")
option_label = tk.Label(root, textvariable=option_text)
option_label.pack(expand=True, padx=20, pady=20)

# Create confirmation frame and pack it
confirmation_frame = tk.Frame(root)
confirmation_label = tk.Label(confirmation_frame, text="")
confirmation_label.pack(side="left")

yes_button = tk.Button(confirmation_frame, text="Yes", command=proceed)
yes_button.pack(side="left")

no_button = tk.Button(confirmation_frame, text="No", command=cancel)
no_button.pack(side="left")

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(side="bottom")

root.drop_target_register("DND_Files")
root.dnd_bind('<<Drop>>', on_drop)

root.mainloop()