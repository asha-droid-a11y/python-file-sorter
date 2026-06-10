# Python File Sorter
# Organizes files in a directory based on file extension
import os, shutil

# path defined =>
path = r"C:\Users\ASHA\Downloads"
print(path)

folder_names = [
    "Images",
    "PDF Files",
    "Excel Files",
    "CSV Files",
    "Word Files",
    "EXE Files",
    "MSI Files",
    "ZIP Files",
    "RAR_7Z Files"
]

# folders created =>

for folder in folder_names:
  folder_path = os.path.join(path, folder)

  if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("files created")

file_types = {
    ".pdf": "PDF Files",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".webp": "Images",
    ".csv": "CSV Files",
    ".xlsx": "Excel Files",
    ".doc": "Word Files",
    ".docx": "Word Files",
    ".exe": "EXE Files",
    ".msi": "MSI Files",
    ".zip": "ZIP Files",
    ".rar": "RAR_7Z Files",
    ".7z": "RAR_7Z Files"
}
 
#  files moves =>

moved_count = 0

for file in os.listdir(path):
    
    if os.path.isdir(os.path.join(path, file)):
        continue
    
    extension = os.path.splitext(file)[1].lower()

    if extension in file_types:
        

        folder = file_types[extension]

        source = os.path.join(path, file)

        destination = os.path.join(path, folder, file)

        if not os.path.exists(destination):
          shutil.move(source, destination)
          moved_count += 1
          print(f"Moved: {file}")

print(f"\nTotal files moved: {moved_count}")


