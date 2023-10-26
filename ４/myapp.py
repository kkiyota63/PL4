from bottle import default_app, route, run, request, template

@route('/')
def index():
    return '''
    <h1>為替レート変換webアプリ</h1>
    <form action="/convert" method="post">
        金額 (USD): <input type="number" name="amount" step="0.01"><br>
        為替レート (1USD = ?JPY): <input type="number" name="rate" step="0.0001"><br>
        <input type="submit" value="JPYに変換">
    </form>
    <iframe src="https://www.smbc.co.jp/ex/ExchangeServlet?ScreenID=real" width="800" height="600"></iframe>
    '''

@route('/convert', method='POST')
def convert():
    # フォームから金額と為替レートを取得
    amount = float(request.forms.get('amount'))
    rate = float(request.forms.get('rate'))

    # 金額を変換
    converted_amount = amount * rate

    return f"{amount} USD は {converted_amount:.2f} JPY です。"

application = default_app()

# ローカルでアプリを実行
run(host='localhost', port=8080)
