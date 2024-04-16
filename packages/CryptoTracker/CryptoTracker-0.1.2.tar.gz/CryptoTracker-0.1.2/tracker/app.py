import pandas as pd
from tkinter import *
from tkinter import ttk

# Model for storing and manipulating data
class CryptoModel:
    def __init__(self):
        self.data = pd.DataFrame(columns=["Name", "Link", "Deadline", "Market Cap", "Twitter", "Discord"])

    def add_project(self, name, link, deadline, market_cap, twitter, discord):
        new_entry = pd.DataFrame([[name, link, deadline, market_cap, twitter, discord]],
                                 columns=["Name", "Link", "Deadline", "Market Cap", "Twitter", "Discord"])
        self.data = pd.concat([self.data, new_entry], ignore_index=True)

    def get_data(self):
        return self.data

# GUI for the application
class CryptoView:
    def __init__(self, root, model):
        self.model = model
        self.root = root
        self.root.title("Crypto Project Tracker")
        self.frame = Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        Label(self.frame, text="Name").grid(row=0, column=0)
        self.name = Entry(self.frame)
        self.name.grid(row=0, column=1)
        
        Label(self.frame, text="Link").grid(row=1, column=0)
        self.link = Entry(self.frame)
        self.link.grid(row=1, column=1)
        
        Label(self.frame, text="Deadline").grid(row=2, column=0)
        self.deadline = Entry(self.frame)
        self.deadline.grid(row=2, column=1)
        
        Label(self.frame, text="Market Cap").grid(row=3, column=0)
        self.market_cap = Entry(self.frame)
        self.market_cap.grid(row=3, column=1)
        
        Label(self.frame, text="Twitter").grid(row=4, column=0)
        self.twitter = Entry(self.frame)
        self.twitter.grid(row=4, column=1)
        
        Label(self.frame, text="Discord").grid(row=5, column=0)
        self.discord = Entry(self.frame)
        self.discord.grid(row=5, column=1)
        
        self.submit_button = Button(self.frame, text="Add Project", command=self.submit)
        self.submit_button.grid(row=6, columnspan=2)
        
        self.treeview = ttk.Treeview(self.root, columns=("Name", "Link", "Deadline", "Market Cap", "Twitter", "Discord"), show="headings")
        for col in self.treeview["columns"]:
            self.treeview.heading(col, text=col)
        self.treeview.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.update_display()

    def submit(self):
        self.model.add_project(self.name.get(), self.link.get(), self.deadline.get(), self.market_cap.get(), self.twitter.get(), self.discord.get())
        self.update_display()

    def update_display(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for index, row in self.model.get_data().iterrows():
            self.treeview.insert("", "end", values=list(row))

# Main application logic
if __name__ == "__main__":
    root = Tk()
    model = CryptoModel()
    view = CryptoView(root, model)
    root.mainloop()