import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Lõputöö")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.result_tree_frame = tk.Frame(self.main_frame)
        self.result_tree_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.result_tree = ttk.Treeview(self.result_tree_frame, columns=('Eesnimi', 'Perenimi', 'Sünniaeg', 'Sugu', 'Isikukood'))
        self.result_tree.heading('#0', text='Nr')
        self.result_tree.heading('Eesnimi', text='Eesnimi')
        self.result_tree.heading('Perenimi', text='Perenimi')
        self.result_tree.heading('Sünniaeg', text='Sünniaeg')
        self.result_tree.heading('Sugu', text='Sugu')
        self.result_tree.heading('Isikukood', text='Isikukood')
        self.result_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_y = ttk.Scrollbar(self.result_tree_frame, orient="vertical", command=self.result_tree.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_tree.configure(yscrollcommand=self.scrollbar_y.set)


        self.entry_label = tk.Label(self.main_frame, text="Sisesta tekst:")
        self.entry_label.pack(side=tk.TOP, padx=(10, 0), pady=(10, 0))

        self.entry = tk.Entry(self.main_frame)
        self.entry.pack(side=tk.TOP, padx=(10, 0))
        self.entry.bind("<Return>", lambda event: self.search())

        self.search_button = tk.Button(self.main_frame, text="Otsi", command=self.search)
        self.search_button.pack(side=tk.TOP)

        self.open_button = tk.Button(self.main_frame, text="Ava fail", command=self.open_file)
        self.open_button.pack(side=tk.TOP)

        self.status_label = tk.Label(self.main_frame, text="Ühtegi faili pole avatud!")
        self.status_label.pack(side=tk.TOP, padx=(10, 0), pady=(10, 0), anchor='w')

        self.loaded_filename = None

    def search(self):
        query = self.entry.get()

        if len(query) < 3:
            messagebox.showwarning("Hoiatus", "Otsing peab olema vähemalt 3 tähemärki pikk!")
            return

        search_terms = query.lower().split()
        self.result_tree.delete(*self.result_tree.get_children())

        matches = 0

        for idx, row in enumerate(self.model.data, start=1):
            if all(term in " ".join(row).lower() for term in search_terms):
                self.result_tree.insert("", "end", text=f"{idx}", values=row)
                matches += 1

        self.result_count_label.config(text=f"Leitud vasted: {matches}")

    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filename:
            self.loaded_filename = filename
            self.update_status()

    def on_close(self):
        if messagebox.askokcancel('Sulgemine', 'Kas oled kindel, et soovid sulgeda?'):
            self.root.destroy()
    def update_status(self):
        if self.loaded_filename:
            self.status_label.config(text=f"Avatud fail: {os.path.basename(self.loaded_filename)}")
        else:
            self.status_label.config(text="Ühtegi faili pole avatud!")


