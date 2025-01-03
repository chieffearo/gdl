# Glyzo download manager
This utility allows you to download files and videos from the internet easily.

### 2.4
fix bug in 2.4

## Features

- Download files from a single URL or a text file containing multiple URLs.
- Download videos from platforms like Instagram, Aparat, Pornhub, etc.
- Automatic library installation with `requirements.txt`.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/chieffearo/gdl.git
   cd gdl-main
   ```

2. Install the required dependencies:
   - Using Python:
     ```bash
     python install_dependencies.py
     ```
   - Alternatively, install directly with pip:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

### Running the Utility

1. To run the main script:

   ```bash
   python gdl.py
   ```

2. If you'd like to specify a URL directly:

   ```bash
   python gdl.py -u <URL>
   ```

3. To download videos:
   ```bash
   python gdl.py -o <video URL>
   ```

### Menu Options

- **Option 1**: Download a single file by entering its URL.
- **Option 2**: Download multiple files using a text file containing URLs.
- **Option 3**: Download videos from supported platforms.

## Requirements

The script uses the following libraries:

- `requests`
- `tqdm`
- `yt-dlp`
- `tkinter`

These libraries are automatically installed when you run the `install_dependencies.py` script.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Use

you can download porn video with this script
   ```bash
   python gdl.py -o <video URL>
   ```
