'''
Created on 
    July 20, 2022

Course work: 
    Python Randomizer

@author: Elakia

Source:
    
'''

# Import necessary modules
from flask import Flask, render_template,request 
import random

app = flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def startpy():
    pass


if __name__ == '__main__':
    startpy()