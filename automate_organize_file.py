#AUTOMATION WITH PYTHON SCRIPTS


import os
import shutil

# Define the file type categories and their corresponding extensions
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh"],
}

def organize_files(directory):
    """
    Organizes files in a directory into predefined categories based on file extensions.

    Args:
        directory (str): Path to the directory containing the files to organize.
    """
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine the file's extension
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Find the category for the file extension
        moved = False
        for category, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                category_path = os.path.join(directory, category)
                os.makedirs(category_path, exist_ok=True)  # Create category directory if it doesn't exist
                shutil.move(file_path, os.path.join(category_path, filename))  # Move the file to the category directory
                print(f"Moved {filename} to {category}")
                moved = True
                break
        
        # If the file type is unknown, move it to 'Others' directory
        if not moved:
            others_path = os.path.join(directory, "Others")
            os.makedirs(others_path, exist_ok=True)  # Create 'Others' directory if it doesn't exist
            shutil.move(file_path, os.path.join(others_path, filename))  # Move the file to 'Others' directory
            print(f"Moved {filename} to Others")

if __name__ == "__main__":
    # Define the directory to organize
    directory_to_organize = r"C:\Users\admin\OneDrive\文件"  # Replace with the actual directory path

    # Call the function to organize files
    organize_files(directory_to_organize)
