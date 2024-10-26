Nohal Asara XML Editor

Nohal Asara XML Editor is a GUI-based Python application designed to streamline the batch editing of XML files, allowing users to insert custom Hebrew and English notes and modify specific fields in each XML file. The tool creates a backup in a timestamped folder, ensuring original files remain unchanged.
Features

    Easy-to-Use GUI: Built with tkinter for an intuitive experience, allowing users to load files, edit fields, and manage file processing.
    Batch Processing: Select multiple XML files for editing at once.
    Custom Notes: Add Hebrew and English notes to specified XML fields.
    Optional Field Editing: Choose to modify fields like Title_Brief and Summary_Short.
    Backup and Organization: Saves modified files in a timestamped directory under C:/NohalAsara, preserving the original files.

Requirements

    Python 3.x
    tkinter (usually included with Python)

Installation

Clone the repository and navigate to the project directory:

bash

git clone https://github.com/yourusername/nohal_asara_xml_editor.git
cd nohal_asara_xml_editor

Usage

    Run the application:

    bash

    python nohal_asara_xml_editor.py

    In the GUI:
        Click Load Files to select XML files for processing.
        Enter notes in Hebrew and/or English.
        Check the Short Description box to modify Title_Brief if desired.
        Click Run to process the files.

    Modified files are saved in a timestamped directory under C:/NohalAsara.

Code Overview
Main Components

    File Loading: Select XML files for batch editing.
    Directory Creation: Timestamped output folder for storing modified files.
    XML Editing: Modifies Title_Brief and Summary_Short fields with the provided notes based on language (HE or EN).
    Backup: Copies files to the output directory before modification.

Example

bash

python nohal_asara_xml_editor.py

Load XML files, input custom notes, select optional fields, and process. The application handles file backup, edits, and saves all modified files in a timestamped folder.
