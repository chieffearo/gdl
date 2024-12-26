import requests
from tqdm import tqdm
import os
from tkinter import Tk, filedialog
import yt_dlp
import argparse
import signal
import sys

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

             Version 2.4 (creat by CHIƎF)
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

def handle_sigint_for_file(signum, frame):
    print(f"\n{PINK}File download canceled by user.{RESET}")
    sys.exit(0)

def handle_sigint_for_textfile(signum, frame):
    print(f"\n{PINK}Download from file canceled by user.{RESET}")
    sys.exit(0)

def handle_sigint_for_video(signum, frame):
    print(f"\n{PINK}Video download canceled by user.{RESET}")
    sys.exit(0)

def download_file(url, directory):
    signal.signal(signal.SIGINT, handle_sigint_for_file)
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
    signal.signal(signal.SIGINT, handle_sigint_for_textfile)
    with open(file_path, 'r') as file:
        links = file.readlines()
    for link in links:
        link = link.strip()
        if link:
            download_file(link, directory)

def download_video(url, directory):
    signal.signal(signal.SIGINT, handle_sigint_for_video)
    ydl_opts = {
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
        'format': 'best',
        'quiet': False,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"{PINK}Video downloaded successfully!{RESET}")
    except Exception as e:
        print(f"{BLACK}Error: {e}{RESET}")

def show_menu():
    print(f"{PINK}1. Download a Single Link{RESET}")
    print(f"{PINK}2. Download Multiple Links from a File{RESET}")
    print(f"{PINK}3. Download Video from Supported Platforms (Instagram, Aparat and ...){RESET}")
    print(f"{PINK}4. Exit{RESET}")
    choice = input(f"{PINK}Choose an option (1/2/3/4): {RESET}")
    return choice

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_logo()

    parser = argparse.ArgumentParser(description="Download utility")
    parser.add_argument("-u", "--url", type=str, help="Download a single file from the provided URL")
    parser.add_argument("-o", "--output", type=str, help="Download video from a supported platform (Instagram, Aparat, Pornhub)")

    args = parser.parse_args()

    if args.url:
        print(f"{PINK}Select download location.{RESET}")
        directory = select_directory()
        try:
            download_file(args.url, directory)
        except Exception as e:
            print(f"{BLACK}Error: {e}{RESET}")

    elif args.output:
        print(f"{PINK}Select download location.{RESET}")
        directory = select_directory()
        try:
            download_video(args.output, directory)
        except Exception as e:
            print(f"{BLACK}Error: {e}{RESET}")

    else:
        while True:
            choice = show_menu()

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
            elif choice == "3":
                url = input(f"{PINK}Enter the video URL: {RESET}")
                print(f"{PINK}Select download location.{RESET}")
                directory = select_directory()
                try:
                    download_video(url, directory)
                except Exception as e:
                    print(f"{BLACK}Error: {e}{RESET}")
            elif choice == "4":
                print(f"{PINK}Exiting the program...{RESET}")
                break
            else:
                print(f"{BLACK}Invalid option! Please try again.{RESET}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda signum, frame: sys.exit(0))
    main()
