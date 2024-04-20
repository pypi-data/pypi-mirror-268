import cv2
import numpy as np
from robot_config import Device_Config
import time
def empty(img):
    pass
#False:不旋转屏幕（竖屏显示，上下会有白边）
#True：旋转屏幕（横屏显示）

conf=Device_Config('/root/unibot/robot_param_init.txt')
flag=0
colorflag=0
lh = 43
ls = 64
lv = 120
hh = 165
hs = 109
hv = 187

def onmouse(event, x, y, flags, param):  # 标准鼠标交互函数
    global lh,ls,lv,uh,us,uv,conf,flag,colorflag
    if event == cv2.EVENT_LBUTTONDOWN:  # 当鼠标移动时
        if(x<100 and y>250  and x>0 and y<320):
            #红色
            colorflag=0
            pass
        if(x<210 and y>250  and x>110 and y<320):
            #绿色
            colorflag=1
            pass
        if(x<320 and y>250  and x>220 and y<3320):
            #黄色
            colorflag=2
            pass
        if(x<480 and y>120  and x>320 and y<220):
            #测试
            if(flag==0):
                flag=1
            else:
                flag=0
        if(x<480 and y>240  and x>320 and y<340):
            #测试
            lls=[]
            print(colorflag)
            if(colorflag==0):
                lls=conf.readconfsectionvalue("RED")
            if(colorflag==1):
                lls=conf.readconfsectionvalue("GREEN")
            if(colorflag==2):
                lls=conf.readconfsectionvalue("YELLOW")
            cv2.setTrackbarPos('L_min', 'camera', lls[0])
            cv2.setTrackbarPos('L_max', 'camera', lls[3])
            cv2.setTrackbarPos('A_min', 'camera', lls[1])
            cv2.setTrackbarPos('A_max', 'camera', lls[4])
            cv2.setTrackbarPos('B_min', 'camera', lls[2])
            cv2.setTrackbarPos('B_max', 'camera', lls[5])

        if(x<480 and y>0  and x>320 and y<100):
            print(lh,uh,ls,us,lv,uv)
            if(colorflag==0):
                conf.setconf('RED','lh',lh)
                conf.setconf('RED','ls',ls)
                conf.setconf('RED','lv',lv)
                conf.setconf('RED','uh',uh)
                conf.setconf('RED','us',us)
                conf.setconf('RED','uv',uv)
            if(colorflag==1):
                conf.setconf('GREEN','lh',lh)
                conf.setconf('GREEN','ls',ls)
                conf.setconf('GREEN','lv',lv)
                conf.setconf('GREEN','uh',uh)
                conf.setconf('GREEN','us',us)
                conf.setconf('GREEN','uv',uv)
            if(colorflag==2):
                conf.setconf('YELLOW','lh',lh)
                conf.setconf('YELLOW','ls',ls)
                conf.setconf('YELLOW','lv',lv)
                conf.setconf('YELLOW','uh',uh)
                conf.setconf('YELLOW','us',us)
                conf.setconf('YELLOW','uv',uv)
            
        print(x, y)  # 显示鼠标所在像素坐标和数值，注意像素表示方法和坐标位置的不同

def set_object_color(robot,x,y,z,e1,e2,e3,e4):

    global lh,ls,lv,uh,us,uv,conf,flag,colorflag

    ls = conf.readconfsectionvalue('SERVO_GET_OBJECT')
    robot.gripper.action(0.3,0)
    robot.robotic_arm.xyz_Kinematic(1,x,y,z,e1,e2,e3,e4)

    cv2.setMouseCallback("camera", onmouse)  # 回调绑定窗口
    height_max = 320
    width_min = 480
    canvas1 = np.zeros((height_max, width_min,3), dtype=np.uint8)
    canvas2 = np.zeros((height_max, width_min), dtype=np.uint8)
    cv2.createTrackbar("L_min","camera",0,255,empty)
    cv2.createTrackbar("L_max","camera",255,255,empty)
    cv2.createTrackbar("A_min","camera",0,255,empty)
    cv2.createTrackbar("A_max","camera",255,255,empty)
    cv2.createTrackbar("B_min","camera",0,255,empty)
    cv2.createTrackbar("B_max","camera",255,255,empty)
    while True:
        img = robot.camera.get_frame()
        timg=cv2.medianBlur(img,5)
        hsv=cv2.cvtColor(timg,cv2.COLOR_BGR2LAB)

        lh=cv2.getTrackbarPos("L_min","camera")
        uh=cv2.getTrackbarPos("L_max","camera")
        ls=cv2.getTrackbarPos("A_min","camera")
        us=cv2.getTrackbarPos("A_max","camera")
        lv=cv2.getTrackbarPos("B_min","camera")
        uv=cv2.getTrackbarPos("B_max","camera")

        lower=np.array([lh,ls,lv])
        upper=np.array([uh,us,uv])
        mask=cv2.inRange(hsv,lower,upper)
        if(flag==0):
            canvas1[0:img.shape[0],0:320,0:3]=img
            
            cv2.rectangle(canvas1, (0,250), (100,320), (0,0,255), -1)
            cv2.rectangle(canvas1, (110,250), (210,320), (0,255,0), -1)
            cv2.rectangle(canvas1, (220,250), (320,320), (0,255,255), -1)
            cv2.rectangle(canvas1, (330,0), (480,100), (255,0,0), -1)
            cv2.putText(canvas1, "save", (350, 60), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), 5)
            cv2.rectangle(canvas1, (330,120), (480,220), (255,0,255), -1)
            cv2.putText(canvas1, "B&W", (350, 180), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), 5)
            cv2.rectangle(canvas1, (330,240), (480,340), (255,0,255), -1)
            cv2.putText(canvas1, "read", (350, 300), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), 5)
        else:
            canvas2[0:img.shape[0],0:320]=mask
            cv2.rectangle(canvas2, (0,250), (100,320), (0,0,255), -1)
            cv2.rectangle(canvas2, (110,250), (210,320), (0,255,0), -1)
            cv2.rectangle(canvas2, (220,250), (320,320), (0,255,255), -1)
            cv2.rectangle(canvas2, (330,0), (480,100), (255,0,0), -1)
            cv2.putText(canvas2, "save", (350, 60), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 0, 0), 5)
            cv2.rectangle(canvas2, (330,120), (480,220), (255,0,255), -1)
            cv2.putText(canvas2, "B&W", (350, 180), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 0, 0), 5)
            cv2.rectangle(canvas2, (330,240), (480,340), (255,0,255), -1)
            cv2.putText(canvas2, "read", (350, 300), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 0, 0), 5)
        if(colorflag==0):
            cv2.rectangle(canvas1, (140, 100), (180, 140), (0,0,255), 2)
        elif(colorflag==1):
            cv2.rectangle(canvas1, (140, 100), (180, 140), (0,255,0), 2)
        elif(colorflag==2):
            cv2.rectangle(canvas1, (140, 100), (180, 140), (0,255,255), 2)
        
        if(flag==0):
            cv2.imshow('camera', canvas1)
        else:
            cv2.imshow('camera', canvas2)
        if cv2.waitKey(5) & 0xFF == 27:
            break

