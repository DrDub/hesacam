## This file is part of hesacam https://github.com/DrDub/hesacam

## Copyright (c) 2017 Pablo Duboue <pablo.duboue@gmail.com>, http://duboue.net

## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:

## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.


import serial
from flask import Flask, session, redirect, url_for, escape, request, Response


ser = serial.Serial('/dev/ttyUSB0', 9600)
app = Flask("hexcam")
app.secret_key = '<CHANGE ME BEFORE DEPLOYING>'

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form['action']
        if action is not None:
            print "Received", repr(action)
            ser.write((action + "\n").encode('ascii'))
    return '''
        <html><body><h1>HexCam</h1>
        <form method="post">
            <p><input name="action" type="submit" value="R">
        </form>
        <form method="post">
            <p><input name="action" type="submit" value="L">
        </form>
        <form method="post">
            <p><input name="action" type="submit" value="F">
        </form>
        <form method="post">
            <p><input name="action" type="submit" value="B">
        </form>
    </body></html>
    '''

@app.route("/do/<action>")
def do(action=None):
    if action is None:
            return 'missing action'
        
    print "Received", repr(action)
    ser.write((action + "\n").encode('ascii'))
    return 'done'

@app.route("/control",methods=['GET'])
def control():
    return '''
        <html>
        <head>
        <script>
        var running = false;
document.addEventListener('keyup', (event) => {
  const keyName = event.key;

    if(running)
      return;
    //alert(`Key pressed ${keyName}`);
    var toSend = null;
    if(keyName === 'ArrowUp'){
      toSend = 'F';
    }else if(keyName === 'ArrowDown'){
      toSend = 'B';
    }else if(keyName === 'ArrowLeft'){
      toSend = 'L';
    }else if(keyName === 'ArrowRight'){
      toSend = 'R';
    } // else ignore

    if(toSend){
       //alert(toSend);
       var xhttp = new XMLHttpRequest();
       xhttp.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {
           running = false;
         }
       };
       xhttp.open("GET", "/do/" + toSend, true);
       xhttp.send();
       running = true;
    }

    }, false);
        </script>
        </head>
        <body><h1>HexCam</h1>
        
        Control the camera by using arrows on this textbox:
        <input type="text">
    </body></html>
'''
    
