import tkinter as tk
from Controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.protocol("WM_DELETE_WINDOW", app.view.on_close)
    root.mainloop()
