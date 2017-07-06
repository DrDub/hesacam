# Hexbug Spider Arduino Camera

An arduino / PC controlled Hexbug Spider with a webcam on top. Useful
to videoconferencing.

This code is a simple hack on top of
https://github.com/xiam/arduino_hexbug_spider.  See that project for
instructions about how to wire the Arduino correctly.

See https://youtu.be/q4UUQbOghtY

Built at the Vancouver Hack Space, VHS (http://vanhack.ca).

## Website control.

The python code will use the serial communication to the Arduino to
expose the 4 commands (Left, Right, Forward, Backward) via a website.

You will need flask installed. Then do

```bash
FLASK_APP=start python -m flask run -h 0.0.0.0 -p 8080
```

If you go to http://localhost:8080/control and click on the text box,
you can control the Hexbug Spider using the arrow keys.

If you want to access the website remotely you'll need a way to
forward that port outside your firewall (if you are inside a
firewall).

