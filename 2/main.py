# turtleモジュールから全ての関数とクラスをインポート
from turtle import *

def koch_snowflake_recursion(order, size):
    """
    与えられた深さの順序でKochの雪片の一辺を描画する関数。
    order: 再帰の深さ（0の場合、直線を描画）
    size: 描画する線の長さ
    """

    # 分岐: 再帰の深さが0の場合とそれ以外の場合で処理を分ける
    if order == 0:
        forward(size)  # 直線を描画
    else:
        # 各段階のKochのカーブを描画
        for angle in [60, -120, 60, 0]:
            # 再帰呼び出し: 関数を自身を呼び出して、次の段階のカーブを描画
            koch_snowflake_recursion(order - 1, size / 3)
            left(angle)  # 指定した角度だけ左に回転

def draw_koch_snowflake(order=3, size=200):
    """
    指定された深さの順序で完全なKochの雪片を描画する関数。
    order: 再帰の深さ
    size: 雪片の一辺の長さ
    """

    # 繰り返し: 3つの辺を描画して、完全なKochの雪片を形成
    for _ in range(3):
        koch_snowflake_recursion(order, size)  # 雪片の一辺を描画
        right(120)  # 120度右に回転して、次の辺の開始位置に移動

    done()  # タートルの描画を完了

# 描画: 定義した関数を呼び出してKochの雪片を描画
draw_koch_snowflake()
