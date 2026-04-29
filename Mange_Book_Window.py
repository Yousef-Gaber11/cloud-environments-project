from tkinter import *
from tkinter import ttk

red = "#C00000"
dark_red = "#8B0000"
green = "#25D366"
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
        self.frame = Frame(master)
        self.create_ui()

    def create_ui(self):

        # ***************************** books data entry ***************************
        books_data = Frame(self.frame, bg=color_frame)
        books_data.grid(row=0, column=0, rowspan=2, padx=50, sticky="nesw")

        title_frame = Frame(books_data, bg=color_frame)
        title_frame.grid(row=0, column=0, sticky="nesw", pady=20, padx=20)

        Label(
            books_data,
            text="Books Management",
            fg=color_txt,
            font=("Arial", 20),
            bg=color_frame,
        ).grid(pady=10, row=0, column=0, sticky="nesw")

        # ---------------- INPUTS ----------------
        form_frame = Frame(books_data, bg=color_frame)
        form_frame.grid(row=1, column=0)

        Label(
            form_frame, text="Title", font=("Arial", 10), bg=color_frame, fg=color_txt
        ).grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.title_entry = Entry(form_frame, font=("Arial", 10))
        self.title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")

        Label(
            form_frame, text="Author", font=("Arial", 10), bg=color_frame, fg=color_txt
        ).grid(row=1, column=0, padx=5, pady=5, sticky="nesw")
        self.author_entry = Entry(form_frame, font=("Arial", 10))
        self.author_entry.grid(row=1, column=1, padx=5, pady=5, sticky="nesw")

        Label(
            form_frame, text="Price", font=("Arial", 10), bg=color_frame, fg=color_txt
        ).grid(row=2, column=0, padx=5, pady=5, sticky="nesw")
        self.price_entry = Entry(form_frame, font=("Arial", 10))
        self.price_entry.grid(row=2, column=1, padx=5, pady=5, sticky="nesw")

        Label(
            form_frame,
            text="Quantity",
            font=("Arial", 10),
            bg=color_frame,
            fg=color_txt,
        ).grid(row=3, column=0, padx=5, pady=5, sticky="nesw")
        self.quantity_entry = Entry(form_frame, font=("Arial", 10))
        self.quantity_entry.grid(row=3, column=1, padx=5, pady=5, sticky="nesw")

        # ---------------- BUTTONS ----------------
        buttons_frame = Frame(books_data, bg=color_frame)
        buttons_frame.grid(row=2, column=0, pady=10, sticky="nesw")

        Button(
            buttons_frame,
            text="Add Book",
            bg=blue,
            fg="#ffffff",
            width=20,
            activebackground=dark_blue,
            activeforeground="#000000",
            command=lambda: None,
        ).grid(row=0, column=0, columnspan=2, pady=10, sticky="nesw")

        Button(
            buttons_frame,
            text="Update Book",
            bg=blue,
            fg="#ffffff",
            width=20,
            activebackground=dark_blue,
            activeforeground="#000000",
            command=lambda: None,
        ).grid(row=1, column=0, columnspan=2, pady=10, sticky="nesw")

        Button(
            buttons_frame,
            text="Delete Book",
            bg=red,
            fg="#ffffff",
            activebackground=dark_red,
            activeforeground="#000000",
            width=20,
            command=lambda: None,
        ).grid(row=2, column=0, columnspan=2, pady=10, sticky="nesw")

        Button(
            buttons_frame,
            text="Back to Home",
            bg=color_txt,
            fg="#ffffff",
            width=20,
            activebackground=light_grey,
            activeforeground="#000000",
            command=self.show_home,
        ).grid(pady=50, row=3, column=0, columnspan=2, sticky=S)

        # ***************************** SEARCH ***************************
        search_frame = Frame(self.frame, bg=color_frame)
        search_frame.grid(row=0, column=1, sticky="WE")

        Label(
            search_frame,
            text="Search",
            width=20,
            font=("Arial", 16),
            bg=color_frame,
            fg=color_txt,
        ).grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="WE")

        self.search_entry = Entry(search_frame, width=40, font=("Arial", 13))
        self.search_entry.grid(row=1, column=2, padx=10, pady=10, sticky="WE")

        Button(
            search_frame,
            text="Search For Book",
            width=20,
            bg=blue,
            fg="#ffffff",
            activebackground=dark_blue,
            activeforeground="#000000",
            command=lambda: None,
        ).grid(row=1, column=3, padx=10, pady=10, sticky="WE")

        Button(
            search_frame,
            text="Delete Results",
            width=20,
            bg=red,
            fg="#ffffff",
            activebackground=dark_red,
            activeforeground="#000000",
            command=lambda: None,
        ).grid(row=1, column=4, padx=10, pady=10, sticky="WE")

        # ***************************** TABLE ***************************
        self.tree = ttk.Treeview(
            self.frame,
            columns=("id", "title", "author", "price", "quantity"),
            show="headings",
            height=20,
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Title")
        self.tree.heading("author", text="Author")
        self.tree.heading("price", text="Price")
        self.tree.heading("quantity", text="Quantity")

        self.tree.grid(row=1, column=1)

        # dummy row just for UI
        self.tree.insert("", END, values=("", "", "", "", ""))

    def display(self):
        self.frame.pack(fill=BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()


if __name__ == "__main__":
    root = Tk()
    root.title("Manage Books - UI Only")
    root.geometry("900x600")

    app = ManageBooks(root, lambda: None)
    app.display()

    root.mainloop()
