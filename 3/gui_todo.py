import tkinter as tk
from tkinter import ttk, messagebox

class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ToDoリストアプリ")
        self.geometry("400x300")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # タスク追加エントリー
        self.task_entry = ttk.Entry(self)
        self.task_entry.pack(pady=20)

        # タスク追加ボタン
        self.add_button = ttk.Button(self, text="タスク追加", command=self.add_task)
        self.add_button.pack(pady=10)

        # タスク表示リストボックス
        self.task_listbox = tk.Listbox(self, height=10, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

        # タスク完了ボタン & タスク削除ボタン
        self.complete_button = ttk.Button(self, text="タスク完了/未完了", command=self.toggle_task)
        self.complete_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = ttk.Button(self, text="タスク削除", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("警告", "タスクが入力されていません")

    def toggle_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            if task.startswith("[完了] "):
                self.tasks[index] = task[6:]
            else:
                self.tasks[index] = "[完了] " + task
            self.update_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
