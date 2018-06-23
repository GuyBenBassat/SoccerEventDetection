import numpy as np
import cv2
from tkinter import *

cap = cv2.VideoCapture('./data/21.08.2017.mancity.1.everton-regmo.blogspot.comSD.mp4')
framenum=0
master=Tk()

file = open('./data/21.08.2017.mancity.1.everton-regmo.blogspot.comSD.txt', 'w')

file.write('pass frames \n')

def label_frame():
    global framenum
    file.write(str(framenum)+'\n')
    print(framenum)


def forward():
    global framenum
    framenum += 1
    cap.set(1, framenum);  # Where framenum is the frame you want
    ret, frame = cap.read()
    rgbframe = frame
    cv2.destroyAllWindows()
    cv2.imshow('frame %d' % (framenum), rgbframe)
    cv2.moveWindow('frame %d' % (framenum),200,200)
    # if cv2.waitKey(1000000000) | 0xFF == ord('q'):
    #    end()

def forward10():
    global framenum
    framenum += 10
    cap.set(1, framenum);  # Where framenum is the frame you want
    ret, frame = cap.read()
    rgbframe = frame
    cv2.destroyAllWindows()
    cv2.imshow('frame %d' % (framenum), rgbframe)
    cv2.moveWindow('frame %d' % (framenum), 200, 200)
    # if cv2.waitKey(1000000000) | 0xFF == ord('q'):
    #    end()

def forward1000():
    global framenum
    framenum += 1000
    cap.set(1, framenum);  # Where framenum is the frame you want
    ret, frame = cap.read()
    rgbframe = frame
    cv2.destroyAllWindows()
    cv2.imshow('frame %d' % (framenum), rgbframe)
    cv2.moveWindow('frame %d' % (framenum), 200, 200)
    # if cv2.waitKey(1000000000) | 0xFF == ord('q'):
    #    end()


def end():
    cap.release()
    cv2.destroyAllWindows()
    file.close()
    exit()



label_bt = Button(master,text="label frame #%d" % (framenum) ,command=label_frame)
label_bt.grid()


for_bt = Button(master,text="forward" ,command=forward)
for_bt.grid()

for10_bt = Button(master,text="forward 10 frames" ,command=forward10)
for10_bt.grid()

for1000_bt = Button(master,text="forward 1000 frames" ,command=forward1000)
for1000_bt.grid()

end_bt = Button(master,text="end" ,command=end)
end_bt.grid()
master.mainloop()











