from tkinter import *
from tkinter import ttk, messagebox


class ManageBooks:
    def __init__(self, master, show_home):
        self.master = master
        self.show_home = show_home
        self.frame = Frame(master)
        self.create_ui()

    def create_ui(self):

        # ================= HEADER =================
        header_frame = Frame(self.frame)
        header_frame.pack(fill=X, pady=10)

        Label(
            header_frame, text="Books Management", font=("Arial", 20, "bold"), pady=10
        ).pack()

        Button(
            header_frame,
            text="Back to Home",
            command=self.show_home,
            bg="gray",
            fg="white",
            cursor="hand2",
            relief=FLAT,
        ).pack(pady=5)

        # ================= MAIN BODY =================
        main_frame = Frame(self.frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # ---------- LEFT SIDE (FORM) ----------
        form_frame = Frame(main_frame)
        form_frame.grid(row=0, column=0, sticky="n")

        Label(form_frame, text="Title").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        self.title_entry = Entry(form_frame, width=25)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        Label(form_frame, text="Author").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        self.author_entry = Entry(form_frame, width=25)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        Label(form_frame, text="Price").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        self.price_entry = Entry(form_frame, width=25)
        self.price_entry.grid(row=2, column=1, padx=5, pady=5)

        Label(form_frame, text="Quantity").grid(
            row=3, column=0, padx=5, pady=5, sticky="w"
        )
        self.quantity_entry = Entry(form_frame, width=25)
        self.quantity_entry.grid(row=3, column=1, padx=5, pady=5)

        # ---------- BUTTONS ----------
        btn_frame = Frame(form_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)

        Button(
            btn_frame,
            text="Add Book",
            command=self.add_book,
            bg="gray",
            width=12,
            cursor="hand2",
            relief=FLAT,
        ).grid(row=0, column=0, padx=5)

        Button(
            btn_frame,
            text="Update Book",
            command=self.update_book,
            bg="gray",
            width=12,
            cursor="hand2",
            relief=FLAT,
        ).grid(row=0, column=1, padx=5)

        # ================= RIGHT SIDE (TABLE) =================
        table_frame = Frame(main_frame)
        table_frame.grid(row=0, column=1, padx=20)

        scrollbar = Scrollbar(table_frame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("id", "title", "author", "price", "quantity"),
            show="headings",
            height=12,
            yscrollcommand=scrollbar.set,
        )

        scrollbar.config(command=self.tree.yview)

        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Title")
        self.tree.heading("author", text="Author")
        self.tree.heading("price", text="Price")
        self.tree.heading("quantity", text="Quantity")

        self.tree.pack(fill=BOTH, expand=True)

        self.tree.bind("<ButtonRelease-1>", self.on_item_click)

        # ================= SEARCH SECTION =================
        search_container = Frame(self.frame)
        search_container.pack(pady=10, fill=X)

        search_inner = Frame(search_container)
        search_inner.pack()

        Label(search_inner, text="Search:", font=("Arial", 10)).grid(row=0, column=0)

        self.search_entry = Entry(search_inner, width=30)
        self.search_entry.grid(row=0, column=1, padx=5)

        Button(search_inner, text="Search", bg="gray", width=10).grid(
            row=0, column=2, padx=5
        )
        Button(search_inner, text="Clear", bg="gray", width=10).grid(
            row=0, column=3, padx=5
        )

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
            (2, "Book B", "Author B", 20.0, 5),
        ]

        for row in sample_books:
            self.tree.insert("", END, values=row)

    # ================= ACTIONS =================
    def add_book(self):
        if self.title_entry.get():
            messagebox.showinfo("Success", "Book added successfully")
            self.load_books()
            self.reset_form()
        else:
            messagebox.showerror("Error", "All fields are required")

    def update_book(self):
        selected = self.tree.selection()
        if selected:
            messagebox.showinfo("Success", "Book updated successfully")
            self.load_books()
            self.reset_form()
        else:
            messagebox.showerror("Error", "Select a book to update")

    # ================= VIEW CONTROL =================
    def display(self):
        self.frame.pack(fill=BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()


if __name__ == "__main__":
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry("800x500")

    app = ManageBooks(root, lambda: print("Back Home"))
    app.display()

    root.mainloop()
