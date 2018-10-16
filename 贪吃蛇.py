#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame,sys,random

# 这个模块包含各种pygame中使用的常量
from pygame.locals import *

# 1 定义颜色的变量
# 目标方块的颜色 0 -255
redColour = pygame.Color(255,0,0)
# # 背景颜色 黑色
blackColour = pygame.Color(0,0,0)
# 贪吃蛇的颜色 白色
whiteColour = pygame.Color(255,255,255)

# 2 定义游戏结束的函数def关键字 定义函数
def gameOver():
    pygame.quit()
    sys.exit()

# 3 工作方式 贪吃蛇的逻辑
def main():

    # 3.1 初始化Pygame这个游戏库
    pygame.init()
    # 3.2 定义一个变量控制游戏的速度
    fpsClock = pygame.time.Clock()

    # 3.3 创建一个窗口 图形界面
    playSurface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("贪吃蛇")

    # 3.4 初始化变量 客户的要求
    # 贪吃蛇起始坐标位置（100,100）
    snakePosition = [100,100]

    snakeBody = [[100,100],[80,100],[60,100]]

    # 目标方块的起始位置
    targetPosition = [300,300]
    # 目标方块的标记 目的：用来判断是否吃掉了这个目标方块
    targetflag = 1

    # 初始化方向--> 往右
    direction = 'right'
    # 定义一个方向变量（方向是我们人为控制的 按键有关系）
    changeDirection = direction

    # 3.5pygame中所有的事件都是放在一个实时循环中完成的'a' 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:

                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
                    # 对应该键盘上的Esc键
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        # 3.6 确定方向 太多
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        # 3.7 根据方向移动蛇头坐标
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        # 3.8 增加蛇的长度
        snakeBody.insert(0,list(snakePosition))

        # 如果我们贪吃蛇的位置和目标方块的位置重合了 目标方块的标记为0
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targetflag = 0

        else:
            snakeBody.pop()

        if targetflag == 0:
            x = random.randrange(1,32) # 屏幕640 480
            y = random.randrange(1,24)
            targetPosition = [int(x*20),int(y*20)]
            targetflag = 1

        playSurface.fill(blackColour)#填充背景为黑色 x 水平y垂直

        for position in snakeBody:
            pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))#画蛇
            pygame.draw.rect(playSurface,redColour,Rect(targetPosition[0],targetPosition[1],20,20))
        pygame.display.flip()

        # 4 游戏结束
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver()
        elif snakePosition[1] > 460 or snakePosition[1] < 0:
            gameOver()

        # 控制游戏速度
        fpsClock.tick(6)

#５　启动程序
if __name__ == '__main__':
    main()
# VIP就业班 ---> 预科班（计算机的基础）














