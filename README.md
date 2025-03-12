# Screenshot Logger

## Overview
The Screenshot Logger is a CLI-based tool with a GUI interface that automatically captures screenshots at fixed intervals and saves them to a specified directory.

## Features
- Captures screenshots at a specified time interval.
- Saves images in a chosen format (PNG).
- Allows user-defined output directory.
- CLI arguments for interval, duration, and output directory.
- Optional GUI for easy interaction.
- Cross-platform support (Windows, Linux, macOS).

## Requirements
- Python 3.x
- Required Python packages: `pyautogui`, `pillow`, `tkinter`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Screenshot\ Logger
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Command Line
Run the script with default settings:
```bash
python screenshot_logger.py
```

### GUI
1. Run the script:
   ```bash
   python screenshot_logger.py
   ```
2. Enter the desired interval, total number of screenshots, and output directory.
3. Click "Start" to begin capturing screenshots.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 