import imageio.v3 as iio
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
filenames = filedialog.askopenfilenames(
    title='Select images for GIF', 
    filetypes=[('Images files', '*.png;8.jpg;*.jpeg;*.gif')]
)

if not filenames:
    print("No files selected.")
    exit()

images = [iio.imread(filename) for filename in filenames]

iio.imwrite('custom.gif', images, duration=500, loop=0)

print("GIF saved as output.gif")
