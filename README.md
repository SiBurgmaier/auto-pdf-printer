# Auto PDF Printer

This Python script monitors a folder for new PDF files, automatically prints them using the default printer, and logs the printed files to avoid duplicates.

## Features
- Monitors a specified folder for new PDF files.
- Automatically sends new PDFs to the default printer.
- Keeps a log of printed files to prevent re-printing.
- Handles filenames with spaces and special characters (e.g., umlauts).

## Requirements
- Python 3.x
- [pywin32](https://github.com/mhammond/pywin32)

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/auto-pdf-printer.git
   cd auto-pdf-printer
2. Install dependencies:
   ```bash
   pip install pywin32
   ```
   
   Edit the onedrive_path variable in the script to match the folder you want to monitor.
  
3. Run the script:
   ```bash
   python auto_pdf_printer.py
   ```

## Configuration
  Folder Path:
  Set the onedrive_path variable to the folder you want to monitor.

## Log File:
  The script creates a log file (printed_files.txt) in the monitored folder to keep track of printed PDFs.

## Notes
  Ensure your printer is set as the default printer on your system.
  Test the script with filenames that contain spaces or special characters (e.g., ä, ö, ü).
