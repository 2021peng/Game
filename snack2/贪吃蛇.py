# 开发人：彭协宇
# 开发时间 ：2022/3/9 17:04

import time
from tkinter import *
import random

aaaa = []


# basic game configuration
def clicked(event):
    pass


def growSnake():
    global score

    score += 10

    txt = "score:" + str(score)
    mainpage_canvas.itemconfigure(scoreText, text=txt)

    lastElement = len(snake) - 1
    lastElementPos = mainpage_canvas.coords(snake[lastElement])

    snake.append(mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="#FDF3F3"))

    if (direction == "left"):
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0] + snakeSize, lastElementPos[1],
                               lastElementPos[2] + snakeSize, lastElementPos[3])
    elif (direction == "right"):
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0] - snakeSize, lastElementPos[1],
                               lastElementPos[2] - snakeSize, lastElementPos[3])
    elif (direction == "up"):
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] + snakeSize,
                               lastElementPos[2], lastElementPos[3] + snakeSize)
    else:
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] - snakeSize,
                               lastElementPos[2], lastElementPos[3] - snakeSize)
    print(type(score))
    if score != 0:
        print(score)
        if score % 20 == 0:
            placezhangai()
            aaaa.append(zuobiao)
            print(aaaa)
            za.append(zhangai)


def moveFood():
    global food, foodX, foodY

    mainpage_canvas.move(food, foodX * (-1), foodY * (-1))

    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)

    mainpage_canvas.move(food, foodX, foodY)


zhangai = 0
zhangaiX = 0
zhangaiY = 0
za = []

def movezhangai():
    global zhangai, zhangaiX, zhangaiY,za

    mainpage_canvas.move(zhangai, zhangaiX * (-1), zhangaiY * (-1))

    zhangaiX = random.randint(0, width - 2 * snakeSize)
    zhangaiY = random.randint(0, height - 2 * snakeSize)

    mainpage_canvas.move(zhangai, zhangaiX, zhangaiY)


def placezhangai():
    global zhangai, zhangaiX, zhangaiY, zuobiao
    a = random.randint(1, 2)
    kuai = 1
    chang = 1
    if a == 1:
        zhangai = mainpage_canvas.create_rectangle(25, 200, snakeSize, snakeSize, fill="white")
        kuai = 175
        chang = 10
    if a == 2:
        zhangai = mainpage_canvas.create_rectangle(200, 25, snakeSize, snakeSize, fill="white")
        kuai = 10
        chang = 175
    zhangaiX = random.randint(0, width - 2 * snakeSize)
    zhangaiY = random.randint(0, height - 2 * snakeSize)

    mainpage_canvas.move(zhangai, zhangaiX, zhangaiY)
    zuobiao = (zhangaiX, zhangaiY, zhangaiX + chang, zhangaiY + kuai)


def overlapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False


def moveSnake():
    global score
    mainpage_canvas.pack()
    positions = []

    positions.append(mainpage_canvas.coords(snake[0]))

    if (positions[0][0] < 0):
        mainpage_canvas.coords(snake[0], width, positions[0][1], width - snakeSize, positions[0][3])
    elif (positions[0][2] > width):
        mainpage_canvas.coords(snake[0], 0 - snakeSize, positions[0][1], 0, positions[0][3])
    elif (positions[0][1] < 0):
        mainpage_canvas.coords(snake[0], positions[0][0], height, positions[0][2], height - snakeSize)
    elif (positions[0][3] > height):
        mainpage_canvas.coords(snake[0], positions[0][0], 0 - snakeSize, positions[0][2], 0)

    positions.clear()

    positions.append(mainpage_canvas.coords(snake[0]))

    if (direction == "left"):
        mainpage_canvas.move(snake[0], -snakeSize, 0)
    elif direction == "right":
        mainpage_canvas.move(snake[0], snakeSize, 0)
    elif direction == "up":
        mainpage_canvas.move(snake[0], 0, -snakeSize)
    elif direction == "down":
        mainpage_canvas.move(snake[0], 0, snakeSize)

    sHeadPos = mainpage_canvas.coords(snake[0])

    foodPos = mainpage_canvas.coords(food)

    if (overlapping(sHeadPos, foodPos)):
        moveFood()
        growSnake()

    for i in range(1, len(snake)):
        if overlapping(sHeadPos, mainpage_canvas.coords(snake[i])):
            gameOver = True
            mainpage_canvas.create_text(width / 2, height / 2, fill="white", font="Times 20 italic bold",
                                        text="Game Over!")
    for k in aaaa:
        # if sHeadPos[0] in range(k[0], k[2]) and sHeadPos[1] in range(k[1],k[3]) and sHeadPos[2] in range(k[0],k[2] and sHeadPos[3] in range(k[1],k[3])):
        if sHeadPos[0] < k[2] and sHeadPos[2] > k[0] and sHeadPos[1] < k[3] and sHeadPos[3] > k[1]:
            gameOver = True
            mainpage_canvas.create_text(width / 2, height / 2, fill="white", font="Times 20 italic bold",
                                        text="Game Over!")


    for i in range(1, len(snake)):
        positions.append(mainpage_canvas.coords(snake[i]))

    for i in range(len(snake) - 1):
        mainpage_canvas.coords(snake[i + 1], positions[i][0], positions[i][1], positions[i][2], positions[i][3])

    if "gameOver" not in locals():
        mainpage.after(90, moveSnake)
    return score


def placeFood():
    global food, foodX, foodY

    food = mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="steel blue")
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)

    mainpage_canvas.move(food, foodX, foodY)


def leftKey(event):
    global direction
    direction = "left"


def rightKey(event):
    global direction
    direction = "right"


def upKey(event):
    global direction
    direction = "up"


def downKey(event):
    global direction
    direction = "down"


def rest():
    # for ada in aaaa:
    #     print(ada)
    #     mainpage_canvas.create_rectangle(ada[0], ada[1], ada[2], ada[3], fill="black")
    aaaa.clear()
    for wanmei in za:
        mainpage_canvas.delete(wanmei)




def hit_me():
    global width

    width = 1280
    global height
    height = 720
    global mainpage
    mainpage = Toplevel()
    ws = mainpage.winfo_screenwidth()
    hs = mainpage.winfo_screenheight()
    x = (ws / 2) - (width / 2)
    y = (hs / 2) - (height / 2)
    mainpage.geometry('%dx%d+%d+%d' % (width, height, x, y))
    mainpage.title("mainpage")
    global mainpage_canvas
    mainpage_canvas = Canvas(mainpage, bg="black", width=width, height=height)
    buttonBG = mainpage_canvas.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
    buttonTXT = mainpage_canvas.create_text(50, 15, fill="white")
    rest_button = Button(mainpage, text='Rest', font=("Arial", 12), bg='gray', width=10, height=1, command=rest)
    rest_button.place(x=0, y=0)

    mainpage_canvas.tag_bind(buttonBG, "<Button-1>", clicked)
    mainpage_canvas.tag_bind(buttonTXT, "<Button-1>", clicked)


    global snake
    snake = []
    global snakeSize
    snakeSize = 15
    snake.append(mainpage_canvas.create_rectangle(snakeSize, snakeSize, snakeSize * 2, snakeSize * 2, fill="white"))
    global score
    score = 0
    global txt
    txt = "Score:" + str(score)
    global scoreText
    scoreText = mainpage_canvas.create_text(width / 2, 10, fill="white", font="Times 20 italic bold", text=txt)

    mainpage_canvas.bind("<Left>", leftKey)
    mainpage_canvas.bind("<Right>", rightKey)
    mainpage_canvas.bind("<Up>", upKey)
    mainpage_canvas.bind("<Down>", downKey)
    mainpage_canvas.focus_set()
    global direction
    direction = "right"

    placeFood()
    moveSnake()
    print(1)


# config the welcome page
window = Tk()

window.title("My Game")
window.geometry("550x500")
canvas = Canvas(window, height=200, width=500)
background = PhotoImage(file="welcome.gif")

image = canvas.create_image(0, 0, anchor="nw", image=background)

canvas.pack(side="top")
# rest_button = Button(canvas, text='Rest',font=("Arial", 12),width=20, height=5)
# rest_button.pack(side='top')
play_button = Button(window, text="Play", font=("Arial", 12), width=20, height=5, command=hit_me)
Quit_button = Button(window, text="Quit", font=("Arial", 12), width=20, height=5, command=window.destroy)
play_button.pack()
Quit_button.pack()
window.mainloop()

