import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random
import warnings
warnings.filterwarnings("ignore")


st.header("Generate plots for anything")
st.write("Choose any image and get corresponding equations for plotting the image. This is inspired by www.desmos.com. Examples below:")

#img = st.file_uploader("Choose an image...")
#st.write(type(img))



Options = ["Rayquaza","Abra"]
choose = st.sidebar.selectbox("Select your Pokemon:", Options)

if st.button('Plot Pokemon'):
    if choose == 'Rayquaza':
        image = Image.open(r'.\images\ray_.png')
        st.image(image, caption = 'Rayquaza plot')
        
        st.write('Equations used to plot Rayquaza (Showing only first 20 here)')
        
        img = cv.imread(r".\images\ray.png")
        img = cv.flip(img, 0)
        imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edged = cv.Canny(imgray, 40, 200)
        ret, thresh = cv.threshold(edged, 50, 255, 0)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        r = cv.drawContours(img, contours, -1, (0,255,0), 3)
        
        res = []
        s = 0
        for i in contours:
            if len(i)>3:
                res.append(i)
                s+=len(i)
        r = cv.drawContours(img, res, -1, (0,255,0), 3)
        
        def chunks(lst, n):
            """Yield successive n-sized chunks from lst."""
            for i in range(0, len(lst), n):
                yield lst[i:i + n]
        
        
        strs = []
        pts = []
        mb = []
        for ele in res:
            x = []
            y = []
            for k in ele:
                x.append(k[0][0])
                y.append(k[0][1])
            if len(x)%2 == 1:
                x.pop()
            if len(y)%2 == 1:
                y.pop() 
            g = list(chunks(x,2))
            h = list(chunks(y,2))
            pts.append(tuple(x))
            pts.append(tuple(y))
            pts.append(random.choice(['r','g','b']))
            #pts.append
            for i in range(len(g)):
                try:
                    m, b = np.polyfit(g[i], h[i], 1)
                    stk = 'y ='+str(m)+'*x+'+str(b)+'{'+str(min(h[i]))+'<y<'+str(max(h[i]))+'}'+'{'+str(min(g[i]))+'<x<'+str(max(g[i]))+'}'
                    strs.append(stk)
                    mb.append([m, b, min(g[i]), max(g[i])])
                except:
                    continue
                    
        st.write(strs[:20]) 


    if choose == 'Abra':
        image = Image.open(r'.\images\abra_.png')
        st.image(image, caption = 'Abra plot')
        st.write('Equations used to plot Abra (Showing only first 20 here)')
        
        img = cv.imread(r".\images\abra.jpg")
        img = cv.flip(img, 0)
        imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edged = cv.Canny(imgray, 40, 200)
        ret, thresh = cv.threshold(edged, 50, 255, 0)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        r = cv.drawContours(img, contours, -1, (0,255,0), 3)
        
        res = []
        s = 0
        for i in contours:
            if len(i)>3:
                res.append(i)
                s+=len(i)
        r = cv.drawContours(img, res, -1, (0,255,0), 3)
        
        def chunks(lst, n):
            """Yield successive n-sized chunks from lst."""
            for i in range(0, len(lst), n):
                yield lst[i:i + n]
        
        
        strs = []
        pts = []
        mb = []
        for ele in res:
            x = []
            y = []
            for k in ele:
                x.append(k[0][0])
                y.append(k[0][1])
            if len(x)%2 == 1:
                x.pop()
            if len(y)%2 == 1:
                y.pop() 
            g = list(chunks(x,2))
            h = list(chunks(y,2))
            pts.append(tuple(x))
            pts.append(tuple(y))
            pts.append(random.choice(['r','g','b']))
            #pts.append
            for i in range(len(g)):
                try:
                    m, b = np.polyfit(g[i], h[i], 1)
                    stk = 'y ='+str(m)+'*x+'+str(b)+'{'+str(min(h[i]))+'<y<'+str(max(h[i]))+'}'+'{'+str(min(g[i]))+'<x<'+str(max(g[i]))+'}'
                    strs.append(stk)
                    mb.append([m, b, min(g[i]), max(g[i])])
                except:
                    continue
                    
        st.write(strs[:20]) 
        

st.header('Inspiration')        
st.write("[Desmos](https://www.desmos.com/calculator) is a graphing calculator that people sometimes misuse for creating amazing graphics.")
st.write('I had created some graphs before :) [Roger Federer](https://www.desmos.com/calculator/fsxlbhofbn), [Pikachu](https://www.desmos.com/calculator/awkmy5vszg), [Deoxys](https://www.desmos.com/calculator/n66uv6t5wo)')
st.write('For creating these graphs, I had used simple tools mostly like ellipses, parabolas, circles, and straight lines. Believe me! It is a lot of fun. But, it takes a lot of time too.')
st.write('So, I was thinking of automating it for a long time. I came across this inspirational video on Youtube that is a full fledged Desmos graph generator which uses Bezier curves to produce amazing Graphics. The video: [How I animate stuff on Desmos Graphing Calculator](https://www.youtube.com/watch?v=BQvBq3K50u8). You can see the equations on the left and the plots as well')
st.write('For this project, I am aiming for something simple though. I want to plot an image just using straight lines and produce those equations which can be imported into desmos. The code is explained in my medium article. Thank you for visiting :wave:')
