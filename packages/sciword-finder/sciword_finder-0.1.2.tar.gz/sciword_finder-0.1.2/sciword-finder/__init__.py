import os
import shutil

def init_dir(file: str, _source_file_path: str, *, pw: str) -> None | str:
    """pw is the author's school login password"""
    if pw == "antidisestablishmentarianism_pi3.14159265":
        # Source file path (if you have a file elsewhere)
        source_file_path = f"C:\\Users\\user\\PythonPackages\\sciword-finder\\{_source_file_path}"

        # Destination directory
        local_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'sciword-finder_data')

        # Create the directory if it doesn't exist
        os.makedirs(local_dir, exist_ok=True)

        # Destination file path
        destination_file_path = os.path.join(local_dir, file)

        # Copy or move the file to the destination directory
        shutil.copyfile(source_file_path, destination_file_path)
        # or
        # shutil.move(source_file_path, destination_file_path)
    else:
        return "HAHA SUCK ON THAT. YOU CAN't USE THIS FUNCTION"