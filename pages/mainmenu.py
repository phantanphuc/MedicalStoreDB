try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2


class MainmenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=300, height=200)
        self.controller = controller

        # self.bg = tk.PhotoImage(file="resources/test.png")
        # self.bg_label = tk.Label(self, image=self.bg)
        # self.bg_label.place(x=0, y=0)


        # self.root = tk.Tk()
        # self.geometry("300x200")

        self.label1 = tk.Label(self, text="Username")
        self.label1.place(x=50, y=50)

        self.entry1 = tk.Entry(self)
        self.entry1.place(x=150, y=50)

        self.label2 = tk.Label(self, text="Password")
        self.label2.place(x=50, y=100)

        self.entry2 = tk.Entry(self, show="*")
        self.entry2.place(x=150, y=100)

        self.button1 = tk.Button(self, text="Login", command=self.login)
        self.button1.place(x=150, y=150)
