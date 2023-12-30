import os

# Create source file path
source_path = "C:/Users/infos/Desktop/source.txt"

# Create destination file path
destination_path = "C:/Users/infos/Downloads/dest.txt"

# Use os.rename() to rename the existing file
try:
    os.rename(source_path, destination_path)
    print(f"File successfully renamed from '{source_path}' to '{destination_path}'.")
except FileNotFoundError:
    print(f"Error: The file at '{source_path}' was not found.")
except FileExistsError:
    print(f"Error: A file already exists at '{destination_path}'. Rename failed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
