import tkinter as tk

class MyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_window()

    def create_window(self):
        #部品の作成や配置はここに書く
        self.grid(row=3, column=3)
        tk.Label(self, text="messageを入力してください").grid(row=0, column=0)

        self.taxtbook = tk.Entry(self)
        self.taxtbook.grid(row=0, column=1)

        self.button1 = tk.Button(self, text="入力")
        self.button1.bind("<Button-1>", self.btn1_clicked)
        self.button1.grid(row=1, column=0,columnspan=2)

        self.msgbox = tk.Label(self, text="massage: ")
        self.msgbox.grid(row=2, column=0, columnspan=2)
    def btn1_clicked(self, event):
        print("ボタンが押されました")
        self.msgbox["text"] = "massage: " + self.taxtbook.get()

app = MyApp()
app.mainloop()