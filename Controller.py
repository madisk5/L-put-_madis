import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from View import View
from Model import Model
import os

class Controller:
    def __init__(self, root):
        self.root = root
        self.model = Model()
        self.view = View(root)

        self.view.open_button.config(command=self.load_file)
        self.view.search_button.config(command=self.search)
        self.view.entry.bind("<Return>", self.search)

        self.loaded_filename = None
        self.loaded = False


        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filename:
            self.model.load_file(filename, delimiter=';')
            self.loaded_filename = filename
            self.loaded = True
            self.update_status()

    def search(self, event=None):
        if not self.loaded:
            return

        query = self.view.entry.get().lower()
        if len(query) < 3:
            messagebox.showwarning("Hoiatus", "Otsing peab olema vähemalt 3 tähemärki pikk!")
            return

        if query:
            self.view.result_tree.delete(*self.view.result_tree.get_children())
            search_terms = query.split()
            matches = 0
            for idx, row in enumerate(self.model.data, start=1):
                if all(term in " ".join(row).lower() for term in search_terms):
                    self.view.result_tree.insert("", "end", text=f"{idx}", values=row)
                    matches += 1
            messagebox.showinfo("Otsingutulemused", f"Leitud vasted: {matches}")
        else:
            self.view.result_tree.delete(*self.view.result_tree.get_children())
            for idx, row in enumerate(self.model.data, start=1):
                self.view.result_tree.insert("", "end", text=f"{idx}", values=row)

    def update_status(self):
        if self.loaded_filename:
            filename = os.path.basename(self.loaded_filename)
            self.view.status_label.config(text=f"Avatud fail: {filename}")
        else:
            self.view.status_label.config(text="Ühtegi faili pole avatud!")

    def on_close(self):
        if messagebox.askokcancel('Sulgemine', 'Kas oled kindel, et soovid sulgeda?'):
            self.root.destroy()
