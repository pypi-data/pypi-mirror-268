from time import sleep
import os
import shutil

import win32com.client

def pdfConverter(sleep_time=2):
    ppttoPDF = 32  # PowerPoint format type for PDF
    input_folder = input('Enter Folder Directory\n>>> ')

    # Create a subfolder 'original' if it does not exist
    original_folder = os.path.join(input_folder, 'original')
    if not os.path.exists(original_folder):
        os.makedirs(original_folder)

    # Copy all PPTX and PPT files to the 'original' subfolder
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith((".pptx", ".ppt")):
                original_file_path = os.path.join(root, file)
                new_file_path = os.path.join(original_folder, file)
                if not os.path.exists(new_file_path):
                    shutil.copy(original_file_path, new_file_path)

    # Scan for files that need to be converted
    while any(f.endswith((".pptx", ".ppt")) for f in os.listdir(input_folder)):
        for root, dirs, files in os.walk(input_folder):
            if 'original' in root:  # Skip processing the 'original' subfolder
                continue
            for file in files:
                sleep(sleep_time)
                if file.endswith(".pptx") or file.endswith(".ppt"):
                    extension_length = 5 if file.endswith(".pptx") else 4
                    try:
                        # Open .ppt files
                        print(f'Trying to open {file}')
                        in_file = os.path.join(root, file)
                        powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                        deck = powerpoint.Presentations.Open(in_file)
                        sleep(sleep_time)

                        # Save the PDF
                        pdf_filename = file[:-extension_length] + ".pdf"
                        pdf_path = os.path.join(input_folder, pdf_filename)
                        deck.SaveAs(pdf_path, ppttoPDF)

                        # Close the .ppt file
                        deck.Close()
                        powerpoint.Quit()
                        print(f'Converted {file} successfully\n')

                        # Remove the original file
                        os.remove(in_file)
                    except Exception as e:
                        print(f'Failed to open {file}, will try again later.\n{e}\n')

    print('No more .ppt or .pptx files found')

if __name__ == '__main__':
    pdfConverter()
