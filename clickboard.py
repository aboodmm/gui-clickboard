import argparse
import os
import tkinter as tk


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    args = parser.parse_args()

    if os.environ.get('DISPLAY','') == '':
        os.environ.__setitem__('DISPLAY', '0.0')

    with open(args.filename, "r") as file:
        lines = [line.rstrip() for line in file if len(line.strip()) > 0]
        print(lines)

    window = tk.Tk()

    for line in lines:
        button = tk.Button(text=line)
        button.bind("", None)
        button.pack()
    window.title("Clickboard")
    window.mainloop()