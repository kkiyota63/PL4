import tkinter as tk

class CalculatorApp(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        # 入力と結果を表示するテキストボックス
        self.entry = tk.Entry(self, font=("Arial", 24), justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # ボタンの定義
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        #初期の行と列を設定
        row = 1
        col = 0

        # ボタンの配置
        for button in buttons:
            tk.Button(self, text=button, font=("Arial", 18)).grid(row=row, column=col,
                                                                  sticky="nsew", padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # 各行と列のサイズ調整
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)
            self.grid_rowconfigure(4, weight=1)

class ExtendedCalculatorApp(CalculatorApp):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        # 平方根のボタンを追加
        self.sqrt_button = tk.Button(self, text="√", font=("Arial", 18), fg="blue")
        self.sqrt_button.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

        # 5行目のサイズ調整
        self.grid_rowconfigure(5, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓アプリ")
    root.geometry("300x400")
    app = ExtendedCalculatorApp(root)
    root.mainloop()
