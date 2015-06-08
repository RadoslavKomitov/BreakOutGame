from tkinter import *
import time
import random


tk = Tk()
tk.title("BreakOut")
canvas = Canvas(tk)
canvas.pack()
tk.geometry("500x400")

def lvl1():
    canvas.delete("all")
    Level_1()
# tk_img = PhotoImage(file = "C:/Users/Asus_K55VJ/Desktop/r.gif")
# canvas.create_image(225,180, image=tk_img)
def homescreen():
    level1_button = Button(tk, text = "Level 1", command = lvl1,width = 10)
    level2_button = Button(tk, text = "Level 2",width = 10)
    quit_button = Button(tk, text = "Quit", command=quit, width = 10)
    quit_button_window = canvas.create_window(225, 230, anchor='n', window=quit_button)            
    level1_button_window = canvas.create_window(225, 150, anchor='n', window=level1_button)
    level2_button_window = canvas.create_window(225, 190, anchor='n', window=level2_button)
    canvas.create_text(240, 100, text='Break Out',font=('Helvetica', 40))

homescreen()


def quit():
    tk.quit()

class Ball:
    def __init__(self,canvas,paddle,block,color):
        self.block = block
        self.paddle = paddle
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.id,285,300)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.hit_bottom = False
        
    def draw(self):
        global block_pos
        count = 0
        t = False
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 480:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 335:
            self.x = -3
        if self.hit_paddle(pos) == True:
            self.y = -3
        if self.hit_block(pos) == True:
            score = str(count)
            l = canvas.create_text(60,60, text = score,font = ("Helvetica",20) )
            count += 1
            
            self.y = 3
            t = True
            # w = canvas.create_text(90, 50, text = str(count) , font=('Courier', 20),fill = "red")

    def hit_blocka(self, pos):
        # for b in block
            # if self.hit_blocki(pos,b) == True:
             #    return True
        return False

            
    def hit_block(self,pos):
        global block_pos
        block_pos = self.canvas.coords(self.block.id)
        if pos[2] >= block_pos[0] and pos[0] <= block_pos[2]:
            if pos[3] >= block_pos[1] and pos[3] <= block_pos[3]:
                
                
                return True
        return False
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            
        return False
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,30,100,20,fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= 500:
            self.x = 0
        
    def turn_left(self, evt):
        self.x = -2
    def turn_right(self, evt):
        self.x = 2
    

class Blocks(Ball):
    def __init__(self,canvas,color,x,y):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x,y,x+35,y+10,fill = color)
    def draw(self):
        pos = self.canvas.coords(self.id)
    
        
def Level_1():
    tk.geometry("500x400")
    block = Blocks(canvas,"green",100,50)
    b2 = Blocks(canvas,"green",200,300)
    b4 = Blocks(canvas,"green",250,300)
    b5 = Blocks(canvas,"green",200,400)
    b1 = Blocks(canvas,"green",200,200)
    b3 = Blocks(canvas,"green",100,200)
    b0 = Blocks(canvas,"green",100,350)
    # global blo [b1, b2, b3, b4] 
    paddle = Paddle(canvas,"blue")
    ball = Ball(canvas,paddle,block,"red")
    leftWall = canvas.create_rectangle([-100,0,10,400], fill = "white")
    rightWall = canvas.create_rectangle([490,0,300,490], fill = "white")
    topWall = canvas.create_rectangle([10,-100,400,10], fill = "white")
    canvas.create_text(40,40,text = "Score: ", font = ("Helvetica",20))

    while True:
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()
            block.draw()
            
        else:
            canvas.create_text(250, 250, text='Game Over', font=('Courier', 30),fill = "red")
            tk.update_idletasks()
            tk.update()
            time.sleep(1)
            play_again_button = Button(tk, text = "Play Again",command = lvl1,width = 10)
            play_again_window = canvas.create_window(225, 180, anchor='n', window=play_again_button)
            quit_button2 = Button(tk, text = "Quit", command = quit, width = 10)
            quit_button_window2 = canvas.create_window(225, 290, anchor='n', window=quit_button2)            
            
            return
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

