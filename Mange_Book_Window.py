from tkinter import *
from tkinter import ttk, messagebox

# ================= Colors =================
red = "#C00000"
dark_red = "#8B0000"
blue = "#128C7E"
dark_blue = "#075E54"
light_grey = "#D3D3D3"
color_txt = "#252525"
color_frame = "#E5E5E5"
yellow = "#ffe400"


class ManageBooks:
    def __init__(self, master, show_home):
        self.master = master
        self.show_home = show_home
        self.frame = Frame(master, bg=color_frame)
        self.create_ui()

    def create_ui(self):
        # ---------------- STYLE ----------------
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=32,
            fieldbackground="white",
        )
        style.configure(
            "Treeview.Heading",
            background=blue,
            foreground="white",
            font=("Arial", 10, "bold"),
        )
        style.map("Treeview", background=[("selected", dark_blue)])

        # ================= HEADER =================
        header_frame = Frame(self.frame, bg=color_frame)
        header_frame.pack(fill=X, pady=15)

        Label(
            header_frame,
            text="Books Management",
            font=("Arial", 22, "bold"),
            bg=color_frame,
            fg=color_txt,
        ).pack(pady=10)

        Button(
            header_frame,
            text="Back To Home",
            command=self.show_home,
            bg=color_txt,
            fg="white",
            activebackground=light_grey,
            activeforeground="black",
            relief=FLAT,
            cursor="hand2",
            padx=20,
            pady=8,
        ).pack()

        # ================= MAIN BODY =================

        main_frame = Frame(self.frame, bg=color_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # ========= LEFT FORM =========

        form_frame = Frame(main_frame, bg=color_frame)
        form_frame.grid(row=0, column=0, sticky="n", padx=30)

        labels = ["Title", "Author", "Price", "Quantity"]

        entries = []

        for i, text in enumerate(labels):

            Label(
                form_frame,
                text=text,
                bg=color_frame,
                fg=color_txt,
                font=("Arial", 11, "bold"),
            ).grid(row=i, column=0, pady=10, sticky="w")

            e = Entry(form_frame, width=28, font=("Arial", 11), relief=FLAT, bd=5)

            e.grid(row=i, column=1, padx=10, pady=10)

            entries.append(e)

        (self.title_entry, self.author_entry, self.price_entry, self.quantity_entry) = (
            entries
        )

        # ========= Buttons =========

        btn_frame = Frame(form_frame, bg=color_frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

        Button(
            btn_frame,
            text="Add Book",
            bg=blue,
            fg="white",
            activebackground=dark_blue,
            relief=FLAT,
            width=14,
            cursor="hand2",
        ).grid(row=0, column=0, padx=8)

        Button(
            btn_frame,
            text="Update Book",
            bg=blue,
            fg="white",
            activebackground=dark_blue,
            relief=FLAT,
            width=14,
            cursor="hand2",
        ).grid(row=0, column=1, padx=8)

        # ================= TABLE =================

        table_frame = Frame(main_frame, bg=color_frame)
        table_frame.grid(row=0, column=1, padx=20)

        scrollbar = Scrollbar(table_frame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("id", "title", "author", "price", "quantity"),
            show="headings",
            height=13,
            yscrollcommand=scrollbar.set,
        )

        scrollbar.config(command=self.tree.yview)
        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Title")
        self.tree.heading("author", text="Author")
        self.tree.heading("price", text="Price")
        self.tree.heading("quantity", text="Quantity")
        self.tree.column("id", width=60, anchor=CENTER)
        self.tree.column("title", width=180)
        self.tree.column("author", width=150)
        self.tree.column("price", width=80, anchor=CENTER)
        self.tree.column("quantity", width=80, anchor=CENTER)
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.bind("<ButtonRelease-1>", self.on_item_click)

        # ================= SEARCH =================

        search_container = Frame(self.frame, bg=color_frame)
        search_container.pack(pady=15, fill=X)
        search_inner = Frame(search_container, bg=color_frame)
        search_inner.pack()
        Label(
            search_inner,
            text="Search:",
            bg=color_frame,
            fg=color_txt,
            font=("Arial", 11, "bold"),
        ).grid(row=0, column=0)
        self.search_entry = Entry(search_inner, width=30, relief=FLAT, bd=4)
        self.search_entry.grid(row=0, column=1, padx=10)

        Button(
            search_inner,
            text="Search",
            bg=blue,
            fg="white",
            activebackground=dark_blue,
            relief=FLAT,
            width=12,
        ).grid(row=0, column=2, padx=8)

        Button(
            search_inner,
            text="Clear",
            bg=red,
            fg="white",
            activebackground=dark_red,
            relief=FLAT,
            width=12,
        ).grid(row=0, column=3, padx=8)

        self.load_books()

    # ================= UI ACTIONS =================
    def reset_form(self):
        self.title_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.quantity_entry.delete(0, END)

    def on_item_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            self.reset_form()
            item_data = self.tree.item(selected_item)
            self.title_entry.insert(0, item_data["values"][1])
            self.author_entry.insert(0, item_data["values"][2])
            self.price_entry.insert(0, item_data["values"][3])
            self.quantity_entry.insert(0, item_data["values"][4])

    # ================= DATA =================

    def load_books(self):
        self.tree.delete(*self.tree.get_children())
        sample_books = [
            (1, "Book A", "Author A", 15.5, 10),
            (2, "Book B", "Author B", 20, 5),
        ]
        for row in sample_books:
            self.tree.insert("", END, values=row)

    # ================= VIEW CONTROL =================
    def display(self):
        self.frame.pack(fill=BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()


if __name__ == "__main__":
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry("950x600")
    root.configure(bg=color_frame)
    app = ManageBooks(root, lambda: print("Back Home"))
    app.display()
    root.mainloop()
