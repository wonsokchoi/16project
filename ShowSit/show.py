from tkinter import Tk as makescreen, Canvas, font
from sql import *

# MACROS
ON = 'ON'
OFF = 'OFF'
RUN = 'RUN'

screen = makescreen()
canvas = Canvas(screen, width=500, height=500)
screen.update()
canvas.pack()

rect = canvas.create_rectangle(100, 100, 400, 400, fill='yellow')

status_font = font.Font(family="맑은 고딕", size=30)
status_text = canvas.create_text(250, 200, text='status', font=status_font)
time_font = font.Font(family="맑은 고딕", size=40)
time_text = canvas.create_text(250, 300, text='time', font=time_font)

seatnumber = '0'
building = "'Soongsil Univ'"
def update_canvas() :
    global rect, status_text, time_text
    sql = SQL()

    data = sql.select_where('ssu_table', 'seat_number='+seatnumber+" AND name="+building)
    status = data[1]
    print(data)
    canvas.itemconfig(status_text, text=data[1])
    canvas.itemconfig(time_text, text="{} min".format(data[3]))

    if status == ON :
        canvas.itemconfig(rect, fill='yellow')
    else :
        canvas.itemconfig(rect, fill='gray')

    screen.after(200, update_canvas)

update_canvas()
screen.mainloop()