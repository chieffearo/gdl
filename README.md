<p align="center">
  <h1 align="center">Glyzo Download Manager </h1>
  <p align="center">This utility allows you to download files and videos from the internet easily</p>
  <p align="center">
    <a href="/LICENSE.md">
      <img src="https://img.shields.io/badge/license-APGL-blue.svg">
    </a>
    <a href="https://github.com/chieffearo/gdl/releases">
      <img src="https://img.shields.io/badge/version-2.4-green.svg">
    </a>
  </p>
</p>


## Features

- Download files from a single URL or a text file containing multiple URLs.
- Download videos from platforms like Instagram, Aparat, Pornhub, etc.
- Automatic library installation with `requirements.txt`.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/chieffearo/gdl.git 
   cd gdl
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

This project is licensed under the GNU Affero General Public License v3.0. See the LICENSE file for details.
## Use

you can download porn video with this script
   ```bash
   python gdl.py -o <video URL>
   ```
# one line install
```bash
git clone https://github.com/chieffearo/gdl.git && cd gdl && pip install -r requirements.txt && python gdl.py
```

#### GDLM is coming soon 
Glyzo Download Manager for Mobile
