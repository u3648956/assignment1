
from math import atan2
import turtle

# 设置画布和画笔
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("patrickStar")

pen = turtle.Turtle()
pen.speed(10)
pen.pensize(3)
pen.color("pink")

# 绘制派大星的身体（五角星形状）
def draw_star(size):
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size/2)
        pen.right(144)
        pen.forward(size/2)
        pen.right(72)
    pen.end_fill()

# 绘制派大星的眼睛
def draw_eyes():
    # 左眼
    pen.penup()
    pen.goto(130, -10)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()
    
    # 左眼珠
    pen.penup()
    pen.goto(130, -10)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()
    
    # 右眼
    pen.penup()
    pen.goto(170, -10)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()
    
    # 右眼珠
    pen.penup()
    pen.goto(170, -10)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

# 绘制派大星的嘴巴
def draw_mouth():
    pen.penup()
    pen.goto(120, -40)
    pen.pendown()
    pen.color("black")
    pen.setheading(-60)
    pen.circle(30, 120)

# 绘制派大星的裤子
def draw_pants():
    # 设置起点
    pen.penup()
    pen.goto(170, -120)  # 从底部左端开始
    pen.setheading(0)
    pen.pendown()
    pen.color("blue")
    pen.begin_fill()
    # 计算两腰的长度
    # 利用勾股定理
    top_base = 180
    bottom_base = 120
    height = 40
    delta = (bottom_base - top_base) / 2
    leg_length = (delta**2 + height**2) ** 0.5

    # 绘制底边
    pen.forward(bottom_base)
    # 绘制左侧腰
    pen.left(atan2(height, delta) * 180 / 3.1415926)  # 转到左腰角度
    pen.forward(leg_length)
    # 绘制上底
    pen.left(180 - (atan2(height, delta) * 180 / 3.1415926))
    pen.forward(top_base)
    # 绘制右腰
    pen.left(180 - (atan2(height, delta) * 180 / 3.1415926))
    pen.forward(leg_length)
    pen.end_fill()

    # 裤子上的图案
    pen.penup()
    pen.goto(100, -100)
    pen.pendown()
    pen.color("green")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()
    # 裤子上的图案
    pen.penup()
    pen.goto(190, -110)
    pen.pendown()
    pen.color("green")
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()


# 主绘制函数
def draw_patrick():
    # 绘制身体
    pen.penup()
    pen.goto(120, 40)
    pen.pendown()
    pen.color("pink")
    draw_star(500)
    
    # 绘制眼睛
    draw_eyes()
    
    # 绘制嘴巴
    draw_mouth()
    
    # 绘制裤子
    draw_pants()
    
    # 隐藏海龟
    pen.hideturtle()

# 执行绘制
draw_patrick()

# 保持窗口打开
turtle.done()
