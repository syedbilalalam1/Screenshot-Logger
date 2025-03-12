try:
    import pyautogui
    import time
    import os
    import argparse
    import tkinter as tk
    from tkinter import filedialog
except ImportError as e:
    print(f"Error: {e}. Please ensure all dependencies are installed.")
    exit(1)

# Set up argument parser
parser = argparse.ArgumentParser(description="Screenshot Logger")
parser.add_argument("-i", "--interval", type=int, default=10, help="Time interval between screenshots (seconds)")
parser.add_argument("-d", "--duration", type=int, default=60, help="Total duration to run (seconds)")
parser.add_argument("-o", "--output", type=str, default="screenshots", help="Output directory")
args = parser.parse_args()

# Validate CLI arguments
if args.interval <= 0:
    print("Error: Interval must be a positive integer.")
    exit(1)

if args.duration <= 0:
    print("Error: Duration must be a positive integer.")
    exit(1)

if not os.path.isdir(args.output):
    try:
        os.makedirs(args.output, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {args.output}: {e}")
        exit(1)

# Function to start screenshot capture
def start_capture():
    interval = int(interval_entry.get())
    total_screenshots = int(total_screenshots_entry.get())
    output_dir = output_entry.get()

    # Calculate duration
    duration = interval * total_screenshots

    # Validate inputs
    if interval <= 0 or total_screenshots <= 0:
        status_label.config(text="Interval and total screenshots must be positive integers.")
        return

    if not os.path.isdir(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
        except OSError as e:
            status_label.config(text=f"Error creating directory: {e}")
            return

    # Capture screenshots
    start_time = time.time()
    for _ in range(total_screenshots):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{output_dir}/screenshot_{timestamp}.png"
        pyautogui.screenshot().save(filename)
        status_label.config(text=f"[+] Screenshot saved: {filename}")
        root.update()
        time.sleep(interval)

# Create the main window
root = tk.Tk()
root.title("Screenshot Logger")

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

# Interval input
interval_label = tk.Label(root, text="Interval (seconds):")
interval_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
interval_entry = tk.Entry(root)
interval_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Total screenshots input
total_screenshots_label = tk.Label(root, text="Total Screenshots:")
total_screenshots_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
total_screenshots_entry = tk.Entry(root)
total_screenshots_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Output directory input
output_label = tk.Label(root, text="Output Directory:")
output_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
output_entry = tk.Entry(root)
output_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Browse button for output directory
browse_button = tk.Button(root, text="Browse", command=lambda: output_entry.insert(0, filedialog.askdirectory()))
browse_button.grid(row=2, column=2, padx=10, pady=5)

# Start button
start_button = tk.Button(root, text="Start", command=start_capture)
start_button.grid(row=3, column=0, columnspan=3, pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=3, pady=10)

# Run the GUI
root.mainloop() 