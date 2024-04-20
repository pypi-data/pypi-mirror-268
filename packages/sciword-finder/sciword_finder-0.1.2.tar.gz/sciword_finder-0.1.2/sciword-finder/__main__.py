from tkinter import *
import argparse
import os
import nltk
from nltk.corpus import words
import shutil
import pickle

def init_dir(file: str, *, pw: str) -> None | str:
    """pw is the author's school login password"""
    if pw == "antidisestablishmentarianism_pi3.14159265":
        # Source file path (if you have a file elsewhere)
        source_file_path = f"C:\\Users\\user\\PythonPackages\\sciword-finder\\{file}"

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


def start() -> None:
    root = Tk()
    root.title("SciWord Finder || Torrez")
    root.geometry("500x500")
    
    root.mainloop()

def main() -> None:
    parser = argparse.ArgumentParser(description="SciWord-Finder Command Line Interface")
    parser.add_argument('action', help='Action to perform with the package')
    args = parser.parse_args()

    if args.action == "start":
        directory_path = r"C:\Users\user\AppData\Local\sciword-finder"
        if not os.path.exists(directory_path):
            nltk.download("words")
            with open("eng_words.dat", "wb") as f:
                pickle.dump(words, f)
            WORDS = words
            init_dir("eng_words.dat", pw="antidisestablishmentarianism_pi3.14159265")
        start()


if __name__ == "__main__":
    main()