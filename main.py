#coding:utf-8
from os import system
from sys import exit
from time import sleep
import random
import keyboard
from setup import *

layers = []
snakes = []
turn_point = []
turnable = True

def call_back(x):
    global turnable
    
    if turnable == False:
        return
    
    if snakes[0].direction == 1:
        if x.event_type == 'down' and x.name == 'up':
            turn_right()
        elif x.event_type == 'down' and x.name == 'down':
            turn_left()
    if snakes[0].direction == 2:
        if x.event_type == 'down' and x.name == 'left':
            turn_left()
        elif x.event_type == 'down' and x.name == 'right':
            turn_right()
    if snakes[0].direction == 3:
        if x.event_type == 'down' and x.name == 'up':
            turn_left()
        elif x.event_type == 'down' and x.name == 'down':
            turn_right()
    if snakes[0].direction == 4:
        if x.event_type == 'down' and x.name == 'left':
            turn_right()
        elif x.event_type == 'down' and x.name == 'right':
            turn_left()
            
    turnable = False
                
keyboard.on_press(call_back)

def init_board():
    def wall():
        layer = []
        for i in range(LENGTH+2):
            layer.append(4)
        layers.append(layer)
        
    wall()
    for i in range(HEIGHT):
        layer = [4]
        for i in range(LENGTH):
            layer.append(0)
        layer.append(4)
        layers.append(layer)
    wall()
        
def num_to_pic(num):
    if num == 0:
        return BLANK
    elif num == 1:
        return SNAKE_HEAD
    elif num == 2:
        return SNAKE_BODY
    elif num == 3:
        return BREAD
    elif num == 4:
        return WALL
        
#打印游戏面板
def print_board():
    system('cls')
    #上边界
    for i in layers:
        layer = ''
        for j in i:
            layer+=num_to_pic(j)
        print(layer)
    #下边界
    
#Snake_part类的两个字段：img为对象的图标所对应的数字，pos表示对象在面板中的位置
class Snake_part():
    def __init__(self,img_num,pos):
        self.img_num = img_num
        self.pos = pos
        if img_num == 1:
            snakes.insert(0,self)
        else:
            snakes.append(self)
        draw(self)
        
    direction = 3
    #默认初始运动方向为向右
    
    #move()的效果仅由对象的direction决定
    def move(self):
        #如果方向为向左
        if self.direction == 1:
            if self.img_num == 1:#如果是蛇头
                WHAT = self.detect(self.pos[0]-1,self.pos[1])
                if WHAT != 'blank':
                    return WHAT
                    
            layers[self.pos[1]][self.pos[0]] = 0
            self.pos = (self.pos[0]-1,self.pos[1])
            draw(self)
            
        #如果方向为向上
        elif self.direction == 2:
            if self.img_num == 1:#如果是蛇头
                WHAT = self.detect(self.pos[0],self.pos[1]-1)
                if WHAT != 'blank':
                    return WHAT
                    
            layers[self.pos[1]][self.pos[0]] = 0
            self.pos = (self.pos[0],self.pos[1]-1)
            draw(self)
        
        #如果方向向右
        elif self.direction == 3:
            if self.img_num == 1:#如果是蛇头
                WHAT = self.detect(self.pos[0]+1,self.pos[1])
                if WHAT != 'blank':
                    return WHAT
                    
            layers[self.pos[1]][self.pos[0]] = 0
            self.pos = (self.pos[0]+1,self.pos[1])
            draw(self)
        
        #如果方向为向下
        elif self.direction == 4:
            if self.img_num == 1:#如果是蛇头
                WHAT = self.detect(self.pos[0],self.pos[1]+1)
                if WHAT != 'blank':
                    return WHAT
                    
            layers[self.pos[1]][self.pos[0]] = 0
            self.pos = (self.pos[0],self.pos[1]+1)
            draw(self)

    
    def detect(self,num1,num2):
        if layers[num2][num1] == 4:#如果蛇头前面为墙
                return 'wall'
        elif layers[num2][num1] == 3:#如果吃面包
                    self.img_num = 2#原先的蛇头变为蛇身
                    draw(self)#更新贴图
                    dire = snakes[0].direction#记下原先蛇头的行进方向
                    head = Snake_part(1,(num1,num2))#新蛇头
                    head.direction = dire#新蛇头方向与原先蛇头方向一致
                    return 'bread'
        elif layers[num2][num1] == 2:#如果咬到自己
                return 'snake'
        else:#如果蛇头前仍然有空间
            return 'blank'
                        

#turn_left()函数使蛇头的方向顺时针转90度
def turn_right():
    turn_point.append(snakes[0].pos)
    if snakes[0].direction != 4:
        snakes[0].direction+= 1
    else:
        snakes[0].direction = 1

def turn_left():
    turn_point.append(snakes[0].pos)
    if snakes[0].direction != 1:
        snakes[0].direction-= 1
    else:
        snakes[0].direction = 4

#将某个物体绘入游戏面板
def draw(thing):
    layers[thing.pos[1]][thing.pos[0]] = thing.img_num
    
def init_snake():
    pos = (LENGTH_INIT,int(HEIGHT/2))
    head = Snake_part(1,pos)
    for i in range(LENGTH_INIT - 1):
        pos = (pos[0]-1,int(HEIGHT/2))
        snake = Snake_part(2,pos)
        
def try_add_bread():
    if random.random() <= BREAD_FRE:
        possible = []
        for i in range(HEIGHT):
            for j in range(LENGTH):
                if layers[i][j] == 0:
                    possible.append(i*LENGTH+j)
        NUM = random.choice(possible)
        layers[NUM//LENGTH][NUM%LENGTH] = 3

#每帧调用一次update()
def update():
    try_add_bread()
    if_turn = True
    for i in range(len(snakes)):
            if i != 0:#如果是蛇身
                snakes[i].move()
                            
            else:#如果是蛇头
                WHAT = snakes[i].move()
                if WHAT == 'bread':
                        if_turn = False
                        break
                elif WHAT == 'wall':
                        print('''
 蛇 撞 到 了 墙 ， 游 戏 结 束 ！

 页 面 将 在 3 秒 后 关 闭 ！''')
                        sleep(3)
                        exit()
                elif WHAT == 'snake':
                        print('''
 蛇 咬 到 了 自 己 ， 游 戏 结 束 ！

 页 面 将 在 3 秒 后 关 闭 ！''')
                        sleep(3)
                        exit()

    #转弯判断时的遍历须要逆序
    if if_turn == True:
        for i in range(len(snakes)-1,0,-1):
            if snakes[i].pos in turn_point:#如果蛇身处在转弯点
                snakes[i].direction = snakes[i-1].direction
                if i == len(snakes)-1:#蛇尾经过转弯点时，删除该转弯点
                    turn_point.remove(snakes[i].pos)

    print_board()
    
if __name__ == '__main__':  
    init_board()
    init_snake()
    while 1:
        sleep(SPEED)
        turnable = True
        update()
    input()
