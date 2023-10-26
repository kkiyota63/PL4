from bottle import default_app, route, run, request, template
import requests
from bs4 import BeautifulSoup

@route('/')
def index():
    return '''
    <form action="/fetch" method="post">
        URL: <input type="text" name="url">
        <input type="submit" value="コンテンツを取得">
    </form>
    '''

@route('/fetch', method='POST')
def fetch_elements():
    # フォームからURLを取得します
    url = request.forms.get('url')

    if not url:
        return "URLを入力してください。"

    # 指定されたURLの内容を取得します
    response = requests.get(url)

    # レスポンスのステータスが200 (OK) でない場合、エラーを返します
    if response.status_code != 200:
        return f"URLの取得に失敗しました。ステータスコード: {response.status_code}"

    # Beautiful Soupでコンテンツを解析します
    soup = BeautifulSoup(response.content, 'html.parser')

    # 要素を抽出して表示します（テキストのみを取得します）
    return soup.get_text()

application = default_app()

# ローカルで実行する場合に以下を使用
run(host='localhost', port=8080)
