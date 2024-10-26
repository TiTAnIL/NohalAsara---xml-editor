import os
from pathlib import Path
import shutil
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from datetime import datetime

class NohalAsaraApp:
    def __init__(self, root):
        self.root = root
        self.root.title('נוהל הסרה')
        self.root.geometry('400x200')
        self.root.resizable(0, 0)

        self.files = []
        self.root_dir = Path('C:/NohalAsara')
        self.output_dir = None

        # Tkinter Variables
        self.checkbox_var = tk.IntVar()
        self.hebrew_note_var = tk.StringVar()
        self.english_note_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # File Loading Button
        load_button = tk.Button(self.root, text="Load Files", command=self.load_files)
        load_button.pack(anchor=tk.NW)

        # Checkbox
        check_button = tk.Checkbutton(self.root, text="Short Description too?", variable=self.checkbox_var)
        check_button.place(x=80, y=120, width=150)

        # Labels and Entry for Hebrew and English notes
        tk.Label(self.root, text="Hebrew:").place(x=15, y=50)
        tk.Label(self.root, text="English:").place(x=15, y=90)

        tk.Entry(self.root, textvariable=self.hebrew_note_var, bd=5).place(x=70, y=50, width=300)
        tk.Entry(self.root, textvariable=self.english_note_var, bd=5).place(x=70, y=90, width=300)

        # Run Button
        run_button = tk.Button(self.root, text="Run", command=self.process_files)
        run_button.place(x=30, y=170, width=340)

    def load_files(self):
        self.files = filedialog.askopenfilenames(filetypes=[("XML Files", "*.xml")])
        if self.files:
            print(f"Loaded files: {self.files}")

    def create_output_dir(self):
        date_time = datetime.now().strftime('%d%m%y_%H%M%S')
        self.output_dir = self.root_dir / date_time
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def copy_files(self):
        copied_files = []
        for file in self.files:
            file_path = Path(file)
            if file_path.is_file():
                destination = self.output_dir / file_path.name
                shutil.copy(file_path, destination)
                copied_files.append(destination)
        return copied_files

    def edit_xml(self, files):
        hebrew_note = self.hebrew_note_var.get()
        english_note = self.english_note_var.get()

        for file in files:
            tree = ET.parse(file)
            root = tree.getroot()

            # Iterate over XML elements
            for app_data in root.iter("App_Data"):
                name = app_data.get("Name")
                value = app_data.get("Value")
                lang_suffix = value[-2:]

                # Modify Title_Brief if checkbox is selected
                if self.checkbox_var.get() and name == "Title_Brief":
                    new_value = self.modify_value(value, lang_suffix, hebrew_note, english_note)
                    app_data.set("Value", new_value)

                # Modify Summary_Short
                if name == "Summary_Short":
                    new_value = self.modify_value(value, lang_suffix, hebrew_note, english_note)
                    app_data.set("Value", new_value)

            # Save the modified XML
            tree.write(file, encoding="UTF-8")
    
    def modify_value(self, value, lang_suffix, hebrew_note, english_note):
        if lang_suffix == "HE":
            return f"{hebrew_note} HE"
        elif lang_suffix == "EN":
            return f"{english_note} EN"
        return value

    def process_files(self):
        if not self.files:
            print("No files selected!")
            return

        self.create_output_dir()
        copied_files = self.copy_files()
        self.edit_xml(copied_files)
        print(f"Processed files: {copied_files}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NohalAsaraApp(root)
    root.mainloop()

