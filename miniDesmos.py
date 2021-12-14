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

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def plotter(img):
    strs = []
    pts = []
    for ele in res:
        x = []
        y = []
        for k in ele:
            x+=k[0][0]
            y+=k[0][1]
        if len(x)%2 == 1:
            x.pop()
        if len(y)%2 == 1:
            y.pop() 
        g = list(chunks(x,2))
        h = list(chunks(y,2))
        pts.append(tuple(x))
        pts.append(tuple(y))
        pts.append(random.choice(['r','g','b']))
        pts.append
        for i in range(len(g)):
            try:
                m, b = np.polyfit(g[i], h[i], 1)
                st = 'y ='+str(m)+'*x+'+str(b)+'{'+str(min(h[i]))+'<y<'+str(max(h[i]))+'}'+'{'+str(min(g[i]))+'<x<'+str(max(g[i]))+'}'
                strs.append(st)
            except:
                continue
    return strs, pts

st.header("Generate plots for anything")
st.write("Choose any image and get corresponding equations for plotting the image. This is inspired by www.desmos.com")

img = st.file_uploader("Choose an image...")
#st.write(type(img))
strs = []
pts = []
res = []
s = 0
x = []
y = []


if st.button('Generate plot'):
    #img = cv.imread(img)
    img = Image.open(img)
    img = np.array(img)
    img = cv.flip(img, 0)
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edged = cv.Canny(imgray, 40, 200)
    ret, thresh = cv.threshold(edged, 50, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    
    r = cv.drawContours(img, contours, -1, (0,255,0), 3)
    #cv.imshow('img',r)
    #cv.waitKey(0)
    
    st.image(r)
    
    for i in contours:
        if len(i)>3:
            res.append(i)
            s+=len(i)
    r = cv.drawContours(img, res, -1, (0,255,0), 3)
    for ele in res:
        
        for k in ele:
            x+=k[0][0]
            y+=k[0][1]
        if len(x)%2 == 1:
            x.pop()
        if len(y)%2 == 1:
            y.pop() 
        g = list(chunks(x,2))
        h = list(chunks(y,2))
        pts+=tuple(x)
        pts+=tuple(y)
        pts.append(random.choice(['r','g','b']))
        pts.append
        for i in range(len(g)):
            try:
                m, b = np.polyfit(g[i], h[i], 1)
                st = 'y ='+str(m)+'*x+'+str(b)+'{'+str(min(h[i]))+'<y<'+str(max(h[i]))+'}'+'{'+str(min(g[i]))+'<x<'+str(max(g[i]))+'}'
                strs.append(st)
                x.clear()
                y.clear()
            except:
                x.clear()
                y.clear()
                continue
    #st.pyplot.figure(figsize=(10, 10))
    #st.pyplot.grid()
    
st.write(pts)    
if st.button('gen'):    
    st.pyplot(*pts);
    
    
   
   
