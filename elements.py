import cv2


class Button():
    def __init__(self, pos_1, pos_2, color_normal, text, font=cv2.FONT_HERSHEY_SIMPLEX, color_alarma=(255,0,0)):
        self.pos_1 = pos_1
        self.pos_2 = pos_2 
        self.color_normal = color_normal
        self.color_alarma = color_alarma
        self.text = text
        self.font = font
    def draw_button(self,frame):
       #cv2.rectangle(frame,(0,frame.shape[0]-40),(80,frame.shape[0]),color,-1)
        #print('self.pos_2', self.pos_2)
        #print('self.pos_1', self.pos_1)
        cv2.rectangle(frame,self.pos_1,self.pos_2,self.color_normal,-1)
        cv2.rectangle(frame,self.pos_1,self.pos_2,(0,0,0),3)
        cv2.putText(frame, self.text, (self.pos_1[0], self.pos_2[1]-8), self.font, .8, (0,0,0), 1, cv2.LINE_AA)
        
        return frame
    def is_in(self,x,y):
        if x < self.pos_2[0] and x > self.pos_1[0] and y < self.pos_2[1] and y > self.pos_1[1]:
            print('CLICK ON BUTTON: ', self.text)
            flag = True
        else:
            flag = False
        return flag
        # cv2.rectangle(frame,(90,frame.shape[0]-40),(170,frame.shape[0]),(0,255,0),-1)
    # cv2.rectangle(frame,(90,frame.shape[0]-40),(170,frame.shape[0]),(0,0,0),3)
    # cv2.putText(frame, 'Mall 2', (90,frame.shape[0]-5), font, .8, (255, 0, 0), 1, cv2.LINE_AA)