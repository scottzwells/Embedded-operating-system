#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# 引脚定义（物理引脚编号）
BtnPin = 11  # 物理引脚11
Gpin = 13    # 物理引脚13
Rpin = 12    # 物理引脚12

def setup():
    """初始化设置"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Gpin, GPIO.OUT)
    GPIO.setup(Rpin, GPIO.OUT)
    
    # 配置按钮引脚，启用内部上拉电阻
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    # 添加事件检测，双边沿触发
    GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)
    
    # 初始状态：绿灯亮
    GPIO.output(Gpin, GPIO.LOW)   # 绿灯亮
    GPIO.output(Rpin, GPIO.HIGH)  # 红灯灭

def Led(state):
    """根据按钮状态控制LED"""
    if state == 0:  # 按钮按下
        GPIO.output(Rpin, GPIO.LOW)   # 红灯亮
        GPIO.output(Gpin, GPIO.HIGH)  # 绿灯灭
        print("按钮按下 - 红灯亮")
    else:  # 按钮释放
        GPIO.output(Rpin, GPIO.HIGH)  # 红灯灭
        GPIO.output(Gpin, GPIO.LOW)   # 绿灯亮
        print("按钮释放 - 绿灯亮")

def Print(x):
    if x==0:
        print('************************')
        print('     Button Pressed!     ')
        print('************************')

def detect(chn):
    """按钮事件回调函数"""
    Led(GPIO.input(BtnPin))
    Print(GPIO.input(BtnPin))

def loop():
    """主循环"""
    while True:
        pass

def destroy():
    """清理函数"""
    GPIO.output(Gpin, GPIO.HIGH)
    GPIO.output(Rpin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()