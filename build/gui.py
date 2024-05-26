# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pytube import YouTube
import os
import threading

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *


# Define paths for the output and assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "build/assets/frame0/"

# Function to get the path relative to the assets directory
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to start video download in a separate thread
def start_download_video_thread(link):
    download_thread = threading.Thread(target=download_video, args=(link,))
    download_thread.start()

# Function to start audio download in a separate thread
def start_download_audio_thread(link):
    download_thread = threading.Thread(target=download_audio, args=(link,))
    download_thread.start()

# Function to download video
def download_video(link):
    yt = YouTube(link)
    os.makedirs("videos", exist_ok=True)
    
    # Select the best available stream
    stream = yt.streams.filter(progressive=True, resolution="720p").first()
    if not stream:
        stream = yt.streams.filter(progressive=True, resolution="480p").first()
    if not stream:
        stream = yt.streams.filter(progressive=True, resolution="360p").first()
    if not stream:
        stream = yt.streams.get_highest_resolution()
    
    # Download the selected stream
    if stream:
        try:
            stream.download('./videos/')
        except Exception as e:
            print(f"Unable to download video due to the following error: {e}")

# Function to download audio
def download_audio(link):
    yt = YouTube(link)
    os.makedirs("musics", exist_ok=True)
    
    # Select the audio stream
    stream = yt.streams.get_by_itag(140)
    
    # Download the selected stream
    if stream:
        try:
            stream.download('./musics/')
        except Exception as e:
            print(f"Unable to download audio due to the following error: {e}")

# Create the main window
window = Tk()

# Set window size and background color
window.geometry("280x310")
window.configure(bg = "#FFFFFF")

# Create a canvas widget
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 310,
    width = 280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Place the canvas widget
canvas.place(x = 0, y = 0)

# Create a title text on the canvas
canvas.create_text(
    36.0,
    35.0,
    anchor="nw",
    text="VIDEO DOWNLOADER",
    fill="#000000",
    font=("Inter", 20 * -1)
)

# Load and place the button for downloading video
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: start_download_video_thread(entry_1.get()),
    relief="flat"
)
button_1.place(
    x=26.0,
    y=192.0,
    width=101.0,
    height=44.0
)

# Load and place the button for downloading audio
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: start_download_audio_thread(entry_1.get()),
    relief="flat"
)
button_2.place(
    x=153.0,
    y=192.0,
    width=101.0,
    height=44.0
)

# Load and place the entry box background image
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    140.0,
    149.0,
    image=entry_image_1
)

# Create the entry box for the YouTube link
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=36.0,
    y=127.0,
    width=208.0,
    height=42.0
)

# Create a text label for the link entry box
canvas.create_text(
    35.0,
    110.0,
    anchor="nw",
    text="LINK:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

# Disable window resizing
window.resizable(False, False)

# Run the Tkinter main loop
window.mainloop()
