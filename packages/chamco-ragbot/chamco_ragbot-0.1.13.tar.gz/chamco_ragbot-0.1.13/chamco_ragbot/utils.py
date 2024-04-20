


def parse_file_url(file_url):
    # Split the path into folder and file parts
    parts = file_url.split('/')
    
    # Extract the folder name (without file name)
    folder_full = '/'.join(parts[:-1])
    folder_name = parts[-2]
    
    # Extract the file name
    file_name = parts[-1]
    
    return folder_full, folder_name, file_name




import re

def sanitize_folder_name(folder_name):
    # Convert to lowercase
    folder_name = folder_name.lower()
    
    # Remove non-alphanumeric characters and replace spaces with dashes
    folder_name = re.sub(r'[^a-z0-9\s-]', '', folder_name)
    
    # Replace multiple spaces with a single dash
    folder_name = re.sub(r'\s+', '-', folder_name)
    
    # Remove leading and trailing dashes
    folder_name = folder_name.strip('-')
    
    # Limit to 128 characters
    folder_name = folder_name[:128]
    
    return folder_name
