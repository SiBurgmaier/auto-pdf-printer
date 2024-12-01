import os
import time
import win32api

# Paths to configure
onedrive_path = r"C:\Users\Silas\OneDrive\automatisch_drucken" # OneDrive folder
log_file_path = os.path.join(onedrive_path, "printed_files.txt")  # Log file

def print_pdf(pdf_path):
    """
    Prints a PDF file using the default printer.
    """
    try:
        # Send the file to the default printer
        result = win32api.ShellExecute(0, "print", pdf_path, None, ".", 0)

        print(f"Successfully printed: {pdf_path}")
        return True
    except Exception as e:
        print(f"Error printing {pdf_path}: {e}")
        return False

def load_printed_files(log_path):
    """
    Loads the list of already printed files from the log file.
    """
    if not os.path.exists(log_path):
        return set()
    with open(log_path, "r", encoding="utf-8") as file:
        return set(file.read().splitlines())

def save_printed_files(log_path, printed_files):
    """
    Saves the list of printed files to the log file.
    """
    with open(log_path, "w", encoding="utf-8") as file:
        file.write("\n".join(printed_files))

def monitor_and_print():
    """
    Monitors the folder and prints new PDFs.
    """
    printed_files = load_printed_files(log_file_path)

    while True:
        # List all PDF files in the target folder
        try:
            files = [f for f in os.listdir(onedrive_path) if f.endswith(".pdf")]
        except FileNotFoundError:
            print(f"Folder {onedrive_path} not found.")
            time.sleep(60)  # Wait 1 minute before retrying
            continue

        for file in files:
            full_path = os.path.join(onedrive_path, file)
            # If the file has not already been printed
            if file not in printed_files:
                if print_pdf(full_path):
                    printed_files.add(file)

        # Save the list of printed files
        save_printed_files(log_file_path, printed_files)

        # Wait 2 seconds before checking again
        time.sleep(2)

if __name__ == "__main__":
    print("Starting folder monitoring...")
    monitor_and_print()
