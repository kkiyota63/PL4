from bottle import default_app, route, run, request, template, static_file
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import os
import re

# 保存する画像の名前
WC_IMG_NAME = "wordcloud.png"

@route('/')
def index():
    return '''
    <h1>ワードクラウド生成アプリケーション</h1>
    <form action="/fetch" method="post">
        URL: <input type="text" name="url">
        <input type="submit" value="コンテンツを取得">
    </form>
    '''

@route('/fetch', method='POST')
def fetch_elements():
    # フォームからURLを取得する
    url = request.forms.get('url')

    if not url:
        return "URLを入力してください。"

    # 指定されたURLの内容を取得する
    response = requests.get(url)

    # レスポンスのステータスが200 (OK) でない場合、エラーを返す
    if response.status_code != 200:
        return f"URLの取得に失敗しました。ステータスコード: {response.status_code}"

    # Beautiful Soupでコンテンツを解析する
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    # 日本語の文字を除外する
    text_without_japanese = re.sub(r'[ぁ-んァ-ン一-龥]', '', text)

    # ワードクラウドを生成する
    wordcloud = WordCloud(background_color="white", width=800, height=800).generate(text_without_japanese)

    # 画像として保存する
    wordcloud.to_file(WC_IMG_NAME)

    # 保存した画像を表示するHTMLを返す
    return f'<img src="/{WC_IMG_NAME}" alt="ワードクラウド">'

@route('/' + WC_IMG_NAME)
def serve_image():
    return static_file(WC_IMG_NAME, root=os.getcwd(), mimetype='image/png')

application = default_app()
run(host='localhost', port=8080)
