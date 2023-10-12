from turtle import *

def koch_snowflake_recursion(order, size):
    #分岐
    if order == 0:
        forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            #再起呼び出し
            koch_snowflake_recursion(order-1, size/3)
            left(angle)

def draw_koch_snowflake(order=3, size=200):

    # 雪片を3回描画して、完全なKochの雪片を形成する
    #繰り返し
    for _ in range(3):
        koch_snowflake_recursion(order, size)
        right(120)

    done()

#描画
draw_koch_snowflake()
