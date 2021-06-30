#!/usr/bin/env python
import PySimpleGUI as sg
import cv2
import numpy as np
import json
import time 
from retrieve import retrieve
import threading
import imutils
from elements import Button

malls_dic={'Mall 1':[str(x) for x in range(76,86)],
           'Mall 2':[str(x) for x in range(11,21)],
           'Mall 3':[str(x) for x in range(21,31)],
           'Mall 4':[str(x) for x in range(31,41)],
           'Mall 5':[str(x) for x in range(41,51)],
           'Mall 6':[str(x) for x in range(51,61)],
           'Mall 7':[str(x) for x in range(61,71)],
           'Mall 8':[str(x) for x in range(71,81)]}

coordenadas = {0:(0,50),1:(256,50),2:(512,50),3:(768,50),4:(1024,50),5:(0,410),6:(256,410),7:(512,410),8:(768,410),9:(1024,410)}
#coordenadas = {0:(50,100),1:(100,150),2:(50,100),3:(50,100),4:(50,100),5:(50,100),6:(50,100),7:(50,100),8:(50,100),9:(50,100)}
#overlay = cv2.resize(cv2.imread('sirena.png'),(50,50),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)

eventActual = "Mall 1"

cap = cv2.VideoCapture("rtsp://34.234.189.94:8559/ds-test")
#cap = cv2.VideoCapture("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov")
width  = cap.get(3)  # float `width`
height = cap.get(4)  # float `height`


separacion = 10

boton1 = Button((0,int(height-40)),(80,int(height)),(0,255,0), 'Mall 1' )
boton2 = Button((boton1.pos_2[0] + separacion,int(height-40)),(boton1.pos_2[0] + 100,int(height)),(0,255,0), 'Mall 2' )
boton3 = Button((boton2.pos_2[0] + separacion,int(height-40)),(boton2.pos_2[0] + 100,int(height)),(0,255,0), 'Mall 3' )
boton4 = Button((boton3.pos_2[0] + separacion,int(height-40)),(boton3.pos_2[0] + 100,int(height)),(0,255,0), 'Mall 4' )
boton5 = Button((boton4.pos_2[0] + separacion,int(height-40)),(boton4.pos_2[0] + 100,int(height)),(0,255,0), 'Mall 5' )
boton6 = Button((boton5.pos_2[0] + separacion,int(height-40)),(boton5.pos_2[0] + 100,int(height)),(0,255,0), 'Mall 6' )
boton7 = Button((boton6.pos_2[0] + separacion,int(height-40)),(boton6.pos_2[0] + 100,int(height)),(0,255,0), 'Mall 7' )
boton8 = Button((boton7.pos_2[0] + separacion,int(height-40)),(boton7.pos_2[0] + 100,int(height)),(0,255,0), 'Mall 8' )


botones={'Mall 1': boton1, 'Mall 2': boton2,
              'Mall 3': boton3, 'Mall 4': boton4,
              'Mall 5': boton5,'Mall 6': boton6,'Mall 7': boton7,'Mall 8': boton8}

def getIndex(mall_id, cam_id):
    return malls_dic[mall_id].index(str(cam_id))


def DrawAlert(event, frame, data):
    #cnt = 0

    if not data[event]: return frame, False
    for i in data[event]:
        index = getIndex(str(event), i)
        #frame[coordenadas[cnt][0]:coordenadas[cnt][1],coordenadas[cnt][0]:coordenadas[cnt][1]] = overlay
        frame = cv2.putText(frame, 'ALERTA ' + str(i), coordenadas[index], cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        #cnt+=1
    return frame, True

def buttonAlert(window,data,eventActual):
    for key in data.keys():
        if eventActual == key:
            window.FindElement(key).Update(button_color = ('black', 'white'))
        elif data[key] and eventActual != key:
            window.FindElement(key).Update(button_color = ('white', 'red'))

def creathread():
    x = threading.Thread(target=retrieve)
    data = x.start()
    return data



def change_camera(event,x,y,flags,param):
#     global color
    
    global cap 
    global eventActual

    if event == cv2.EVENT_LBUTTONDOWN:

        # print(boton1)
        if boton1.is_in(x,y):
            cap = cv2.VideoCapture("rtsp://34.234.189.94:8559/ds-test")
            eventActual = 'Mall 1'
        elif boton2.is_in(x,y):
            cap = cv2.VideoCapture("rtsp://34.234.189.94:8554/ds-test")
            eventActual = 'Mall 2'

        elif boton3.is_in(x,y):
            cap = cv2.VideoCapture("rtsp://34.234.189.94:8560/ds-test")
            eventActual = 'Mall 3'
        elif boton4.is_in(x,y):
            cap = cv2.VideoCapture("rtsp://34.234.189.94:8555/ds-test")
            eventActual = 'Mall 4'

        elif boton5.is_in(x,y):
            cap = cv2.VideoCapture("rtsp://34.234.189.94:8553/ds-test")
            eventActual = 'Mall 5'
        elif boton6.is_in(x,y):
            cap = cv2.VideoCapture("rtsp://34.234.189.94:8556/ds-test")
            eventActual = 'Mall 6'
        elif boton7.is_in(x,y):
            cap = cv2.VideoCapture("rtsp://34.234.189.94:8557/ds-test")
            eventActual = 'Mall 7'
        elif boton8.is_in(x,y):
            cap = cv2.VideoCapture("rtsp://34.234.189.94:8558/ds-test")
            eventActual = 'Mall 8'

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',change_camera)

def main():

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
   
    #cap = cv2.VideoCapture("rtsp://192.168.0.13:4445/ds-test")
    
    

    count = 30
    while(1):
        #ret, frame = cap.read()
        
        #--------------------------------------------------------

        ret, frame = cap.read()
        frame = imutils.resize(frame, width=1280, height=720)

        if ret == True and count%15 == 0:
            data = retrieve() #pasar el string a insertar
            # print(data)

        frame = boton1.draw_button(frame)
        frame = boton2.draw_button(frame)
        frame = boton3.draw_button(frame)
        frame = boton4.draw_button(frame)
        frame = boton5.draw_button(frame)
        frame = boton6.draw_button(frame)
        frame = boton7.draw_button(frame)
        frame = boton8.draw_button(frame)

        frame, estado = DrawAlert(eventActual, frame,data)
        #buttonAlert(window,data,eventActual)
        for key,value in data.items():
            if value:
                print('Alarm on ',key)
                botones[key].color_normal = botones[key].color_alarma
            else:
                #print('Normal button: ', key)
                botones[key].color_normal = (0,255,0)
        cv2.imshow('Frame', frame)
        count += 1
        cv2.waitKey(1)

main() 

