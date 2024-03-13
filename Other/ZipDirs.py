import os
import zipfile

def zip_subfolders(main_folder):
    for item in os.listdir(main_folder):  # List everything in the main folder
        item_path = os.path.join(main_folder, item)  # Get the full path of the item
        if os.path.isdir(item_path):  # Check if this item is a directory
            zip_file_name = f"{item_path}.zip"  # Name of the zip file to create
            with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        # Create a relative path for files to maintain the directory structure
                        rel_path = os.path.relpath(os.path.join(root, file), os.path.join(item_path, '..'))
                        zipf.write(os.path.join(root, file), rel_path)
            print(f"Zipped {item_path} to {zip_file_name}")

# Replace 'your_main_folder_path' with the path to your main folder
zip_subfolders('/mnt/306deddd-38b0-4adc-b1ea-dcd5efc989f3/MaterialsDataset/MatSegDataset_Split/')
