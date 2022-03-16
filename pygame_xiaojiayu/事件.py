# 开发人：彭协宇
# 开发时间 ：2022/3/9 14:20

import pygame
import sys

#初始化
pygame.init()
size = width, height = 1200 ,600
bg = (0,0,0)
#创建指定大小的窗口
screen = pygame.display.set_mode(size)

font = pygame.font.Font(None,20)
line_height = font.get_linesize()
position = 0

#设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
        position += line_height
        if position>height:
            position = 0
            screen.fill(bg)
    pygame.display.flip()


