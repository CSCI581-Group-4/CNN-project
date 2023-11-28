import tkinter as tk
from tkinter import filedialog

# Define a class for app
class DrawingApp:
    def __init__(self, master):
        # Initialize app as master 
        self.master = master
        self.master.title("Drawing numbers")

        # Create widget for drawing
        self.canvas = tk.Canvas(master, bg="white", width=400, height=300)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # keybindings the left mouse button motion to the paint method
        self.canvas.bind("<B1-Motion>", self.paint)

        # Create a Save button
        save_button = tk.Button(master, text="Save", command=self.save_image)
        save_button.pack()

    # draw on the canvas during mouse movement
    def paint(self, events):
        x1, y1 = (events.x - 1), (events.y - 1)
        x2, y2 = (events.x + 1), (events.y + 1)
        # draws oval in black color or more accurate inking it in
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)

    # now save image
    def save_image(self):
        # will ask where user wants to store image
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        # checks for users pervided file path 
        if path:
            # Save as png 
            self.canvas.postscript(file=path, colormode="color")

# Entry point of the program
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Create an instance of the DrawingApp class, passing the main window
    app = DrawingApp(root)
    # Start the Tkinter event loop
    root.mainloop()
