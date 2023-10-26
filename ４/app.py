from bottle import default_app, route, run
import tkinter as tk
from tkinter import scrolledtext
import requests


# GUI表示の関数
def show_web_content(url):
    response = requests.get(url)
    content = ""

    if response.status_code == 200:
        content = response.text
    else:
        content = "Error fetching URL."

    # GUIの初期化
    root = tk.Tk()
    root.title("Web Content Viewer")

    text_widget = scrolledtext.ScrolledText(root, width=80, height=20)
    text_widget.pack(padx=10, pady=10)

    text_widget.insert(tk.END, content)
    root.mainloop()

# Webサーバ側の処理
@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/view/<url:path>')
def fetch_and_view(url):
    show_web_content("http://" + url)
    return f"Displayed content from {url} in GUI."

application = default_app()

# ローカルで実行する場合には以下の行を使用
run(host='localhost', port=8080)
