#!/usr/bin/env python
import PySimpleGUI as sg
import cv2
import numpy as np
import json
import time 

malls_dic={'Mall 1':[str(x) for x in range(76,85)],
           'Mall 2':[str(x) for x in range(85,94)],
           'Mall 3':[str(x) for x in range(30,40)],
           'Mall 4':[str(x) for x in range(40,50)],
           'Mall 5':[str(x) for x in range(50,60)],
           'Mall 6':[str(x) for x in range(60,70)]}

coordenadas = {0:(0,50),1:(256,50),2:(512,50),3:(768,50),4:(1024,50),5:(0,410),6:(256,410),7:(512,410),8:(768,410),9:(1024,410)}
#coordenadas = {0:(50,100),1:(100,150),2:(50,100),3:(50,100),4:(50,100),5:(50,100),6:(50,100),7:(50,100),8:(50,100),9:(50,100)}
#overlay = cv2.resize(cv2.imread('sirena.png'),(50,50),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)

def getIndex(mall_id, cam_id):
    return malls_dic[mall_id].index(str(cam_id))


def DrawAlert(event, frame, data):
    #cnt = 0

    if not data[event]: return frame
    for i in data[event]:
        index = getIndex(str(event), i)
        #frame[coordenadas[cnt][0]:coordenadas[cnt][1],coordenadas[cnt][0]:coordenadas[cnt][1]] = overlay
        frame = cv2.putText(frame, 'ALERTA ' + str(i), coordenadas[index], cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        #cnt+=1
    return frame

def buttonAlert(window,data,eventActual):
    for key in data.keys():
        if eventActual == key:
            window.FindElement(key).Update(button_color = ('black', 'white'))
        elif data[key] and eventActual != key:
            window.FindElement(key).Update(button_color = ('white', 'red'))

def main():

    sg.theme('Black')

    # define the window layout
    layout = [[sg.Image(filename='', key='image')],
              [sg.Button(button_text = 'Mall 1', key = 'Mall 1', 
                button_color = 'white', enable_events = True, 
                size=(10, 1), font='Any 14'), 
               sg.Button(button_text = 'Mall 2', key = 'Mall 2',
                button_color = 'white', enable_events = True,
                size=(10, 1), font='Any 14'),
               sg.Button(button_text = 'Mall 3', key = 'Mall 3', 
                button_color = 'white', enable_events= True, 
                size=(10, 1), font='Any 14')],
               [sg.Button(button_text = 'Mall 4', key = 'Mall 4', 
                   button_color = 'white', enable_events = True,
                   size=(10, 1), font='Any 14'),
               sg.Button(button_text = 'Mall 5', key = 'Mall 5', 
                   button_color = 'white', enable_events = True, 
                   size=(10, 1), font='Any 14'),
               sg.Button(button_text = 'Mall 6', key = 'Mall 6', 
                   button_color = 'white', enable_events = True,
                   size=(10, 1), font='Any 14')]]

    # create the window and show it without the plot
    window = sg.Window('OMIA - Visualizador de alertas',
                       layout)

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    eventActual = "Mall 1"
    #cap = cv2.VideoCapture("rtsp://192.168.0.13:4445/ds-test")
    cap = cv2.VideoCapture("rtsp://107.20.91.241:8554/ds-test")


    while(1):
        ret, frame = cap.read()
        
        
       
        #ret, frame = cap.read()
        if ret == True:
            with open('alarmas.json') as json_file:
                data = json.load(json_file)
            #frame_resize = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
            frame = DrawAlert(eventActual, frame,data)
            #buttonAlert(window,data,eventActual)
        cv2.imshow('VIDEO', frame)
        
        cv2.waitKey(1)

main() 

