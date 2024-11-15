import requests
from tqdm import tqdm
import os
from tkinter import Tk, filedialog

BLACK = "\033[30m"
PINK = "\033[95m"
RESET = "\033[0m"

def print_logo():
    logo = """
   ********   **                         
  **//////** /**  **   **                
 **      //  /** //** **  ******  ****** 
/**          /**  //***  ////**  **////**
/**    ***** /**   /**      **  /**   /**
//**  ////** /**   **      **   /**   /**
 //********  ***  **      ******//****** 
  ////////  ///  //      //////  //////  

             Version 1.0.0.0
    """
    print(f"{PINK}{logo}{RESET}")

def select_directory():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directory = filedialog.askdirectory(title="Select Download Directory")
    return directory

def select_file():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename(
        title="Select Text File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    return file_path

def download_file(url, directory):
    local_filename = url.split("/")[-1]
    filepath = os.path.join(directory, local_filename)
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024

    with open(filepath, 'wb') as file, tqdm(
        desc=f"{PINK}Downloading {local_filename}{RESET}",
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
        colour="magenta",
    ) as bar:
        for data in response.iter_content(block_size):
            file.write(data)
            bar.update(len(data))
    print(f"{PINK}Downloaded: {local_filename}{RESET}")

def download_from_file(file_path, directory):
    with open(file_path, 'r') as file:
        links = file.readlines()
    for link in links:
        link = link.strip()
        if link:
            download_file(link, directory)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print_logo()

    print(f"{PINK}1. Download a Single Link{RESET}")
    print(f"{PINK}2. Download Multiple Links from a File{RESET}")
    choice = input(f"{PINK}Choose an option (1/2): {RESET}")

    if choice == "1":
        url = input(f"{PINK}Enter the file URL: {RESET}")
        print(f"{PINK}Select download location.{RESET}")
        directory = select_directory()
        try:
            download_file(url, directory)
        except Exception as e:
            print(f"{BLACK}Error: {e}{RESET}")
    elif choice == "2":
        print(f"{PINK}Select the text file containing URLs.{RESET}")
        file_path = select_file()
        if not file_path:
            print(f"{BLACK}No file selected!{RESET}")
        else:
            print(f"{PINK}Select download location.{RESET}")
            directory = select_directory()
            try:
                download_from_file(file_path, directory)
            except Exception as e:
                print(f"{BLACK}Error: {e}{RESET}")
    else:
        print(f"{BLACK}Invalid option!{RESET}")
