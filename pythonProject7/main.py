import os

def replace_values_in_file(file_path, old_value, new_value):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Replace the old value with the new value
    new_content = file_content.replace(old_value, new_value)

    # Open the file in write mode and overwrite the content
    with open(file_path, 'w') as file:
        file.write(new_content)

def replace_values_in_directory(directory_path, old_value, new_value):
    # Iterate over all the files in the directory
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)

        # Check if the file is a regular file
        if os.path.isfile(file_path):
            replace_values_in_file(file_path, old_value, new_value)

# Example usage
directory_path = '/Users/ismart/Downloads'
old_value = 'old'
new_value = 'new'

replace_values_in_directory(directory_path, old_value, new_value)
