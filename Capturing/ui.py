# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pyscreenshot
import numpy as np
import PIL
import cv2
import wx
import ctypes
import pyautogui
import sys
from PyQt5.QtWidgets import *
import win32api
from tkinter import *
import pynput
from pynput import mouse

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
    html.H1(
        children='Graph',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Made with Dash', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div(dcc.Input(id='input-on-submit', type='text')),

    html.Button('Submit', id='submit-val', n_clicks=0),

    html.Div(id='container-button-basic',
             children='Enter a value of screenshots and press submit'),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }

    )
])

@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-on-submit', 'value')])
def update_output(n_clicks, value):
    if(n_clicks > 0):
        if (pyautogui.confirm('Now open window with data of rialto exchanges.\n'
                              'Then press OK and be ready to define the rectangular area.\n'
                              'Firstly, click on the point from top left angle\n'
                              'Then click on the point from bottom right angle') == 'OK'):
            with mouse.Listener(on_click=on_click) as listener:
                listener.join()
            windowRegion = (x1, y1, x2, y2)
            for i in range(int(value)):
                filename = "screen%s.png" % (i+1)
                im = pyscreenshot.grab(bbox=windowRegion)
                im.save(filename)
    return 'The input value was "{}" and the button has been clicked {} times'.format(value, n_clicks)


# def temp():
#     pyautogui.alert('This displays some text with an OK button.')
#     pyautogui.position()  # current mouse x and y
#     pyautogui.onScreen(x, y)  # True if x & y are within the screen.
#     pyautogui.PAUSE = 2.5   # Pause 2.5 s
#     pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
#     pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position
#     pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left') # The button keyword argument can be 'left', 'middle', or 'right'.
#     pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
#     pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
#     pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')
#     pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter
#     pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
#     pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
#     pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
#     pyautogui.alert('This displays some text with an OK button.')
#     pyautogui.confirm('This displays text and has an OK and Cancel button.')
#     pyautogui.prompt('This lets the user type in a string and press OK.')
#     pyautogui.screenshot('foo.png')  # returns a Pillow/PIL Image object, and saves it to a file
#     pyautogui.locateOnScreen('looksLikeThis.png')
#     pyautogui.locateCenterOnScreen('looksLikeThis.png')  # returns center x and y

# class Qscene(QGraphicsScene):
#
#     def __init__(self, parent=None):
#         super(Qscene, self).__init__(parent)
#
#
#
#     def mousePressEvent(self, event):
#         super(Qscene, self).mousePressEvent(event)
#
#         self.xRect = event.scenePos().x()
#         self.yRect = event.scenePos().y()
#
#
#     def mouseReleaseEvent(self, event):
#         super(Qscene, self).mouseReleaseEvent(event)
#
#         QGraphicsScene.clear(self)                        # +++
#
#         QGraphicsScene.addRect(self,self.xRect,self.yRect,self.endX-
#         self.xRect,self.endY-self.yRect)
#
#     def mouseMoveEvent(self, event):
#         super(Qscene, self).mouseMoveEvent(event)
#         self.endX = event.scenePos().x()
#         self.endY = event.scenePos().y()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     window = QWidget()
#     scene = Qscene()
#     view = QGraphicsView()
#     view.setScene(scene)
#
#     hbox = QGridLayout()
#     hbox.addWidget(view)
#
#     window.setLayout(hbox)
#     window.show()
#
#     sys.exit(app.exec_())

# def enable_mouseposition():
#     window.after(10, get_mouseposition)
#
#
# def get_mouseposition():
#     state_left = win32api.GetKeyState(0x01)
#     if state_left == -127 or state_left == -128:
#         xclick, yclick = win32api.GetCursorPos()
#         print(xclick, yclick)
#     else:
#         window.after(10, get_mouseposition)
#
#
# window = Tk()
# window.geometry("300x200")
# window.title("Testing")
#
#
# b = Button(window, text="OK", command=enable_mouseposition)
# b.grid(row=1, column=2, sticky=W)
#
#
# window.mainloop()

# if __name__ == '__main__':
#     if( pyautogui.confirm('This displays text and has an OK and Cancel button.') == 'OK'):
#         state_left = win32api.GetKeyState(0x01)
#         if state_left == -127 or state_left == -128:
#             xclick, yclick = win32api.GetCursorPos()
#             print(xclick, yclick)

    #print(pyautogui.size())
    # im = pyscreenshot.grab(bbox=(10, 10, 300, 300))
    # im.save('ss.png')

    # app.run_server(debug=True)
    # im = ImageGrab.grab(bbox=(10, 10, 300, 300))  # X1,Y1,X2,Y2
    # im.show()
    #
    # app = wx.App()
    #
    # SM_XVIRTUALSCREEN = 76
    # SM_YVIRTUALSCREEN = 77
    # SM_CXVIRTUALSCREEN = 78
    # SM_CYVIRTUALSCREEN = 79
    #
    # user32 = ctypes.windll.user32
    # width, height = user32.GetSystemMetrics(SM_CXVIRTUALSCREEN), user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)
    # x, y = user32.GetSystemMetrics(SM_XVIRTUALSCREEN), user32.GetSystemMetrics(SM_YVIRTUALSCREEN)
    #
    # screen = wx.ScreenDC()
    # bmp = wx.Bitmap(width, height)
    # mem = wx.MemoryDC(bmp)
    # mem.Blit(0, 0, width, height, screen, x, y)
    # del mem
    # bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
    #temp()
global counter, x1, y1, x2, y2
counter = 0
x1 = 0; y1 = 0; x2 = 0; y2 = 0
def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    global counter, x1, y1, x2, y2
    if pressed:
        if(counter < 2):
            if(counter == 0):
                x1 = x
                y1 = y
            if (counter == 1):
                x2 = x
                y2 = y
            counter += 1
            print('{0} at {1}'.format('Pressed', (x, y)), '\ncounter = ', counter, '\n')
            if(counter == 2): return False
            return True
        if(counter >= 2): return False
    if not pressed:
        # Stop listener
        return True

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

if __name__ == '__main__':
    app.run_server(debug=True)
    # if (pyautogui.confirm('Now open window with data of rialto exchanges.\n'
    #                       'Then press OK and be ready to define the rectangular area.\n'
    #                       'Firstly, click on the point from top left angle\n'
    #                       'Then click on the point from bottom right angle') == 'OK'):
    #     with mouse.Listener(on_click=on_click) as listener:
    #         listener.join()
    #     windowRegion = (x1, y1, x2, y2)
    #     filename = 'screen' + '.png'
    #     im = pyscreenshot.grab(bbox=windowRegion)
    #     im.save(filename)
