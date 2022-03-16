# 开发人：彭协宇
# 开发时间 ：2022/3/9 14:20
#p18_1.py
import pygame
import sys

#初始化
pygame.init()

size = width, height = 1200 ,600
speed = [-2, 1]
bg = (255, 255, 255)

#创建指定大小的窗口
screen = pygame.display.set_mode(size)

#设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

kfc = pygame.image.load("lion.jfif")
#获得图像的位置矩形
position = kfc.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        #翻转图像
        kfc = pygame.transform.flip(kfc, True, False)
        #反方向移动
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    #填充背景
    screen.fill(bg)
    #更新图像
    screen.blit(kfc,position)
    #更新界面
    pygame.display.flip()
    #延时 10ms
    pygame.time.delay(10)

