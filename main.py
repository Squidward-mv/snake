from tkinter import *
import random
import time
game = True
game_width = 1000
game_heigh = 1000
snake_item = 20
snake_bg = "red"
snake_bg1 = "yellow"

snake_x_nav = 0
snake_y_nav = 0
snake_list = []
snake_size = 5
sahar_list = []
sahar_size = 5
virg_x = game_width//snake_item
virg_y = game_heigh//snake_item
snake_x = virg_x//2
snake_y = virg_y//2
tk = Tk()
tk.title("Sweety dreams")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = game_width, height = game_heigh, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

sahar_bg = "blue"
sahar_bg1 = "black"
for i in range(sahar_size):
    x = random.randrange(virg_x)
    y = random.randrange(virg_y)
    id1 = canvas.create_oval(x * snake_item, y * snake_item, x * snake_item + snake_item,y * snake_item + snake_item, fill= sahar_bg1)
    id2 = canvas.create_oval(x * snake_item + 4, y * snake_item + 4, x * snake_item + snake_item - 4,y * snake_item + snake_item - 4, fill= sahar_bg)
    sahar_list.append([x,y,id1,id2])
print(sahar_list)

def snake_paint_item(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x * snake_item, y * snake_item, x * snake_item + snake_item,y * snake_item + snake_item, fill = snake_bg1)
    id2 = canvas.create_rectangle(x*snake_item+4,y*snake_item+4,x*snake_item+snake_item-4,y*snake_item+snake_item-4,fill = snake_bg)
    snake_list.append([x,y,id1,id2])
    print(snake_list)
snake_paint_item(canvas, snake_x, snake_y)

def check():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])
        print(temp_item)
def check_if_f():
    global snake_size
    for i in range(len(sahar_list)):
        if sahar_list[i][0] == snake_x and sahar_list[i][1] == snake_y:
            snake_size +=1
            canvas.delete(sahar_list[i][2])
            canvas.delete(sahar_list[i][3])



def snake_move(event):
    global snake_x
    global snake_y
    global snake_x_nav
    global snake_y_nav
    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
        check()
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
        check()
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
        check()
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
        check()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    check_if_f()



def game_over():
    global game
    game = False
def check_if_t():
    if snake_x > virg_x or snake_y > virg_y or snake_x < 0 or snake_y <0:
        game_over()

def check_if_ts(f_x,f_y):
    global game
    if (snake_x_nav == 0 and snake_y_nav == 0:)
        for i in range(len(snake_list)):
            if snake_list[i][0] == f_x and snake_list[i][1] == f_y:
                game = False

while game:
    check()
    check_if_f()
    check_if_t()
    check_if_ts(snake_x + snake_x_nav,snake_y + snake_y_nav)
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.25)

def fun_nothing(event):
    pass
canvas.bind_all("<KeyPress-Left>", fun_nothing)
canvas.bind_all("<KeyPress-Right>", fun_nothing)
canvas.bind_all("<KeyPress-Up>", fun_nothing)
canvas.bind_all("<KeyPress-Down>", fun_nothing)