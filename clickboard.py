import argparse
import os
import tkinter as tk
from pandas.io import clipboard


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, nargs='?', const="samplefile.txt", default="samplefile.txt")
    args = parser.parse_args()

    if os.environ.get('DISPLAY','') == '':
        os.environ.__setitem__('DISPLAY', '0.0')

    with open(args.filename, "r") as file:
        lines = [line.rstrip() for line in file if len(line.strip()) > 0]
        print(lines)

    def cbcopy(myword):
       clipboard.copy(myword)
    
    window = tk.Tk()
    for i, line in enumerate(lines):
        button = tk.Button(text=line, command=lambda x = line: cbcopy(x))
        button.pack()
    window.title("Clickboard")
    window.mainloop()