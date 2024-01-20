import os,pathlib
# Get the directory of the current file
current_file_path = pathlib.Path.cwd()

# Get the parent directory (one level up)
parent_directory = current_file_path.parent.parent

# Construct the path to the data folder
data_folder_path = os.path.join(parent_directory, 'data')
