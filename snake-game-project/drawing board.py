import tkinter as tk
root = tk.Tk()
root.title('Drawing board')
canvas = tk.Canvas(root,bg= 'white', width=500, height=500)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
canvas.grid(row=0,column=0,sticky='nsew')




now_color = 'black'
def color(set_color):
    global now_color
    now_color = set_color
brush_size = tk.IntVar()
size_slider = tk.Scale(root,from_=1,to=20,orient = 'vertical',variable=brush_size)
size_slider.grid(row=1,column=1)


def draw(event):
    size = size_slider.get()
    x , y = event.x, event.y
    canvas.create_rectangle(x-size,y-size,x+size,y+size,fill = now_color , outline = 'Black')

def delete():
   canvas.delete('all')

button = tk.Button(root,text='delete',command=delete )
button2 = tk.Button(root,text = 'red', command = lambda: color('red'))
button3 = tk.Button(root,text = 'orange', command = lambda: color('orange'))
button4 = tk.Button(root,text = 'yellow', command = lambda: color('yellow'))
button5 = tk.Button(root,text = 'green', command = lambda: color('green'))
button6 = tk.Button(root,text = 'blue', command = lambda: color('blue'))
button7 = tk.Button(root,text = 'purple', command = lambda: color('purple'))
button8 = tk.Button(root,text = 'black', command = lambda: color('black'))
button9 = tk.Button(root,text = 'white', command = lambda: color('white'))
button10 = tk.Button(root,text = 'pink', command = lambda: color('pink'))


button.grid(row=0,column=1)
button2.grid(row=0,column=2)
button3.grid(row=0,column=3)
button4.grid(row=0,column=4)
button5.grid(row=0,column=5)
button6.grid(row=0,column=6)
button7.grid(row=0,column=7)
button8.grid(row=0,column=8)
button9.grid(row=0,column=9)
button10.grid(row=0,column=10)





canvas.bind('<B1-Motion>',draw)
root.mainloop()
