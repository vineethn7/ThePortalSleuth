import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import threading
import matplotlib.pyplot as plt

emotion_model = Sequential()
emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))
emotion_model.load_weights('model.h5')

show_text=[0]
# cap1 = cv2.VideoCapture(0,cv2.CAP_DSHOW)

emotion_dict = {0: "   Angry   ", 1: "Disgusted", 2: "  Fearful  ", 3: "   Happy   ", 4: "  Neutral  ", 5: "    Sad    ", 6: "Surprised"}


emoji_dist={0:"./emojis/angry.png",1:"./emojis/disgusted.png",2:"./emojis/fearful.png",3:"./emojis/happy.png",4:"./emojis/neutral.png",5:"./emojis/sad.png",6:"./emojis/surpriced.png"}




root=tk.Tk()
heading=Label(root,text="Emojify",pady=5, font=('arial',45,'bold'),bg='black',fg='white')
heading.pack()
lmain = tk.Label(master=root,padx=50,bd=10)
lmain2 = tk.Label(master=root,pady=10,bd=10)
root['bg']='grey'
root.geometry("1400x900+100+10")


exitbutton = Button(root, text='Quit',fg="black",command=root.destroy,font=('arial',25,'bold')).pack(side = BOTTOM)

while True:
    # ret,frame=cap1.read()
    frame=cv2.imread("t4.jpg")
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bounding_box = cv2.CascadeClassifier("C:/Users/hp/Documents/Projects/Emojify/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    num_faces = bounding_box.detectMultiScale(gray_frame,scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in num_faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
        prediction = emotion_model.predict(cropped_img)

        maxindex = int(np.argmax(prediction))
        cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        show_text[0]=maxindex


    pic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # pic=cv2.resize(pic,(500,500))
    frame2= cv2.imread(emoji_dist[show_text[0]])
    pic2=cv2.cvtColor(frame2,cv2.COLOR_BGR2RGB)
    img = Image.fromarray(pic)
    img2= Image.fromarray(pic2)
    imgtk = ImageTk.PhotoImage(image=img)
    imgtk2 = ImageTk.PhotoImage(image=img2)
    lmain.imgtk = imgtk
    lmain2.imgtk= imgtk2
    lmain.configure(image=imgtk)
    lmain2.configure(image=imgtk2)

    lmain.pack(side=LEFT)
    lmain.place(x=50,y=150)

    lmain2.pack(side=RIGHT)
    lmain2.place(x=900,y=150)
    root.update()


    if cv2.waitKey(1) == 27:
        break

cap1.release()
cv2.destroyAllWindows()
