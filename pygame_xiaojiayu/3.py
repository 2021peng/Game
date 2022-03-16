# 开发人：彭协宇
# 开发时间 ：2022/3/9 15:13
import pygame
from pygame.locals import *
import sys #退出程序需要

#初始化pygame
pygame.init()

clock = pygame.time.Clock()
size = (width,height) = (1000,600)
#一帧移动速度
speed = [2,1]
#三原色值都为255时为白色
bg = (255,255,255)

#全屏按钮
fullscreen = False

#设置窗口为size大小，返回的是Surface对象
screen = pygame.display.set_mode(size,RESIZABLE)
#设置窗口标题
pygame.display.set_caption("小狮子")

#加载图片，返回的是Surface对象
turtle = pygame.image.load("lion.jfif")
#获得图像位置矩形
position = turtle.get_rect()

l_head = turtle
r_head = pygame.transform.flip(turtle,True,False)
while True:
    #事件循环
    for event in pygame.event.get():
        #如果事件为点了窗口的关闭
        if event.type ==pygame.QUIT:
            sys.exit()
        #如果事件为按键盘
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-1,0]
                turtle = l_head
            if event.key == pygame.K_RIGHT:
                speed = [1,0]
                turtle = r_head
            if event.key == pygame.K_UP:
                speed = [0,-1]
            if event.key == pygame.K_DOWN:
                speed = [0,1]
            if event.key == K_ESCAPE:  # 按Esc退出游戏
                sys.exit()
            #全屏按钮
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1920,1080),FULLSCREEN | HWSURFACE)
                    width, height = 1920,1080
                    #超边界可能是因为win10显示内容%125放大了
                else:
                    screen = pygame.display.set_mode(size)
        #用户调制窗口尺寸大小
        if event.type == VIDEORESIZE:
            size = event.size
            width,height = size
            print(size)
            screen = pygame.display.set_mode(size, RESIZABLE)

    #以speed速度移动图像
    position = position.move(speed)


    #如果位置矩形左右碰到边界
    if position.left < 0 or position.right > width:
        #图像水平方向翻转，垂直方向不变
        turtle = pygame.transform.flip(turtle,True,False)
        #反方向移动，碰到左边界往右移动，碰到右边界往左移动
        speed[0] = -speed[0]

    #如果位置矩形上下碰到边界
    if position.top < 0 or position.bottom > height:
        #反方向移动就行了
        speed[1] = -speed[1]

    #填充背景
    screen.fill(bg)
    #绘制图像，此步和上一步在内存中完成，图做出来后再贴出来
    screen.blit(turtle,position)
    #更新界面
    pygame.display.flip()
    #帧切换延迟10毫秒
    #pygame.time.delay(10)
    #帧率不高于100帧
    clock.tick(200)
