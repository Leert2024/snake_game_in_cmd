creator:leert2024
作者：leert2024

This program mainly uses the method of redrawing the screen (update) at regular intervals to achieve text-based snake eating
Required third-party Python library: keyboard, for implementing keyboard control




Gameplay: Press the directional keys on the keyboard to control the snake's direction
The snake will grow when eating bread, but will fail if it hits a wall or bites itself




Edit constant values in setup.py to customize game parameters or display methods, etc


Double click main.py to play the game in cmd without using a third-party environment




Possible bugs: There is a small probability of a snake biting itself when turning quickly twice

本程序主要使用间隔一定时间重绘屏幕（update）的方式，实现基于文本的贪吃蛇
需要的python第三方库：keyboard，用于实现键盘控制
游戏方式：按键盘上的方向键来控制蛇的转向，蛇吃面包就会增长，撞墙或咬到自己即会失败
在setup.py中编辑常量值以自定义游戏参数或显示方式等
双击main.py即可在命令行窗口进行游戏，无需使用第三方环境
可能存在的bug：快速转向两次时有小概率造成“蛇咬到自己”的情况