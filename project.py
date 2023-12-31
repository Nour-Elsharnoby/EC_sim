##############################################################الحمد لله##########################################################################

import tkinter as tk
from tkinter import simpledialog

#################################################################################################################################################

class Resistor_Class:
    def __init__(self, canvas):
        self.canvas = canvas
        x = 90
        y = 120
        self.points = [x, y, x+15, y, x+20, y+10, x+30, y-10, x+40, y+10, x+50, y-10, x+60, y+10, x+70,y-10 , x+75, y, x+90, y]
        self.body = None
        self.value = "10"
        self.color = None

        self.draw_resistor()
        
        # ربط حدث النقر والسحب
        self.canvas.tag_bind(self.body, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body, "<Button-3>", self.show_context_menu)

    def draw_resistor(self):
        self.body = self.canvas.create_line(self.points, smooth="false", width=3, fill=self.color, tags="resistor")

    def on_press(self, event):
        # حفظ موقع بداية السحب
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        self.start_x = cx*15
        self.start_y = cy*15

    def on_drag(self, event):
        # حساب التغيير في الموقع ونقل الخط المتعرج
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        evx = cx*15
        evy = cy*15
        delta_x = evx - self.start_x
        delta_y = evy - self.start_y
        self.canvas.move(self.body, delta_x, delta_y)
        self.start_x = evx
        self.start_y = evy

    def show_context_menu(self, event):
        menu = tk.Menu(self.canvas, tearoff=0)
        color_menu = tk.Menu(menu, tearoff=0)
        color_menu.add_command(label="blue", command=lambda: self.change_color("blue"))
        color_menu.add_command(label="red", command=lambda: self.change_color("red"))
        color_menu.add_command(label="yellow", command=lambda: self.change_color("yellow"))
        menu.add_cascade(label="color", menu=color_menu)
        menu.add_command(label="value", command=self.change_value)
        menu.add_command(label="rotate", command=self.rotate_resistor_right)
        menu.add_command(label="delete", command=self.delete_combo)
        menu.post(event.x_root, event.y_root)

    def change_color(self, new_color):
            self.color = new_color
            self.canvas.itemconfig(self.body, fill=self.color)

    def change_value(self):
        new_value = simpledialog.askstring("تغيير اسم الكرة", "الرجاء إدخال اسم جديد:", initialvalue=self.value)
        if new_value:
            self.value = new_value

    def rotate_resistor_right(self):
        a,A,b,B,c,C,d,D,e,E,f,F,g,G,h,H,i,I,j,J = self.canvas.coords(self.body)
        new_coords = [j,J-90,j,J-75,j-10,J-70,j+10,J-60,j-10,J-50,j+10,J-40,j-10,J-30,j+10,J-20,j,J-15,j,J]

        self.canvas.coords(self.body, *new_coords)
        

    def delete_combo(self):
        self.canvas.delete(self.body)

#################################################################################################################################################

class Capacitor_Class:
    def __init__(self, canvas):
        self.canvas = canvas
        x = 90
        y = 120
        self.points_r = [x, y, x+35, y, x+35, y+20, x+35, y-20]
        self.points_l = [x+55, y+20, x+55, y-20, x+55, y, x+90, y]
        self.body_r = None
        self.body_l = None
        self.value = "10"
        self.color = None

        self.draw_capacitor()
        
        # ربط حدث النقر والسحب
        self.canvas.tag_bind(self.body_r, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body_r, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body_r, "<Button-3>", self.show_context_menu)
        self.canvas.tag_bind(self.body_l, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body_l, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body_l, "<Button-3>", self.show_context_menu)

    def draw_capacitor(self):
        self.body_r = self.canvas.create_line(self.points_r, smooth="false", width=3, fill=self.color, tags="capacitor_r")
        self.body_l = self.canvas.create_line(self.points_l, smooth="false", width=3, fill=self.color, tags="capacitor_r")

    def on_press(self, event):
        # حفظ موقع بداية السحب
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        self.start_x = cx*15
        self.start_y = cy*15

    def on_drag(self, event):
        # حساب التغيير في الموقع ونقل الخط المتعرج
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        evx = cx*15
        evy = cy*15
        delta_x = evx - self.start_x
        delta_y = evy - self.start_y
        self.canvas.move(self.body_r, delta_x, delta_y)
        self.canvas.move(self.body_l, delta_x, delta_y)
        self.start_x = evx
        self.start_y = evy

    def show_context_menu(self, event):
        menu = tk.Menu(self.canvas, tearoff=0)
        color_menu = tk.Menu(menu, tearoff=0)
        color_menu.add_command(label="blue", command=lambda: self.change_color("blue"))
        color_menu.add_command(label="red", command=lambda: self.change_color("red"))
        color_menu.add_command(label="yellow", command=lambda: self.change_color("yellow"))
        menu.add_cascade(label="color", menu=color_menu)
        menu.add_command(label="value", command=self.change_value)
        menu.add_command(label="rotate", command=self.rotate_capacitor_right)
        menu.add_command(label="delete", command=self.delete_combo)
        menu.post(event.x_root, event.y_root)

    def change_color(self, new_color):
            self.color = new_color
            self.canvas.itemconfig(self.body_r, fill=self.color)
            self.canvas.itemconfig(self.body_l, fill=self.color)

    def change_value(self):
        new_value = simpledialog.askstring("تغيير اسم الكرة", "الرجاء إدخال اسم جديد:", initialvalue=self.value)
        if new_value:
            self.value = new_value

    def rotate_capacitor_right(self):
        a,A,b,B,c,C,d,D = self.canvas.coords(self.body_r)
        e,E,f,F,g,G,h,H = self.canvas.coords(self.body_l) 
        new_coords_r = [h,H-90,h,H-55,h+20,H-55,h-20,H-55]
        new_coords_l = [h+20,H-35,h-20,H-35,h,H-35,h,H]
        self.canvas.coords(self.body_r, *new_coords_r)
        self.canvas.coords(self.body_l, *new_coords_l)
        

    def delete_combo(self):
        self.canvas.delete(self.body_r)
        self.canvas.delete(self.body_l)

#################################################################################################################################################

class Inductance_Class:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 90
        self.y = 120
        self.body1 = None
        self.body2 = None
        self.body3 = None
        self.body4 = None
        self.body5 = None
        self.body6 = None
        self.points1 = [self.x,self.y, self.x+15, self.y]
        self.points2 = [self.x+75, self.y, self.x+90, self.y]
        self.value = "10"
        self.color = None

        self.draw_Inductance()
        
        # ربط حدث النقر والسحب
        self.canvas.tag_bind(self.body1, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body1, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body1, "<Button-3>", self.show_context_menu)
        self.canvas.tag_bind(self.body2, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body2, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body2, "<Button-3>", self.show_context_menu)
        self.canvas.tag_bind(self.body3, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body3, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body3, "<Button-3>", self.show_context_menu)
        self.canvas.tag_bind(self.body4, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body4, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body4, "<Button-3>", self.show_context_menu)
        self.canvas.tag_bind(self.body5, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body5, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body5, "<Button-3>", self.show_context_menu)

    def draw_Inductance(self):
        self.body1 = self.canvas.create_line(self.points1, smooth="false", width=3, fill=self.color, tags="inductance1")
        self.body2 = self.half_circle = self.canvas.create_oval(self.x+15, self.y-12, self.x+39, self.y+12, outline=self.color, width=3, tags="inductance2")
        self.body3 = self.half_circle = self.canvas.create_oval(self.x+33, self.y-12, self.x+57, self.y+12, outline=self.color, width=3, tags="inductance3")
        self.body4 = self.half_circle = self.canvas.create_oval(self.x+51, self.y-12, self.x+75, self.y+12, outline=self.color, width=3, tags="inductance4")
        self.body5 = self.canvas.create_line(self.points2, smooth="false", width=3, fill=self.color, tags="inductance5")

    def on_press(self, event):
        # حفظ موقع بداية السحب
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        self.start_x = cx*15
        self.start_y = cy*15

    def on_drag(self, event):
        # حساب التغيير في الموقع ونقل الخط المتعرج
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        evx = cx*15
        evy = cy*15
        delta_x = evx - self.start_x
        delta_y = evy - self.start_y
        self.canvas.move(self.body1, delta_x, delta_y)
        self.canvas.move(self.body2, delta_x, delta_y)
        self.canvas.move(self.body3, delta_x, delta_y)
        self.canvas.move(self.body4, delta_x, delta_y)
        self.canvas.move(self.body5, delta_x, delta_y)
        self.start_x = evx
        self.start_y = evy

    def show_context_menu(self, event):
        menu = tk.Menu(self.canvas, tearoff=0)
        color_menu = tk.Menu(menu, tearoff=0)
        color_menu.add_command(label="blue", command=lambda: self.change_color("blue"))
        color_menu.add_command(label="red", command=lambda: self.change_color("red"))
        color_menu.add_command(label="yellow", command=lambda: self.change_color("yellow"))
        menu.add_cascade(label="color", menu=color_menu)
        menu.add_command(label="value", command=self.change_value)
        menu.add_command(label="rotate", command=self.rotate_inductance_right)
        menu.add_command(label="delete", command=self.delete_combo)
        menu.post(event.x_root, event.y_root)

    def change_color(self, new_color):
            self.color = new_color
            self.canvas.itemconfig(self.body1, fill=self.color)
            self.canvas.itemconfig(self.body2, outline=self.color)
            self.canvas.itemconfig(self.body3, outline=self.color)
            self.canvas.itemconfig(self.body4, outline=self.color)
            self.canvas.itemconfig(self.body5, fill=self.color)

    def change_value(self):
        new_value = simpledialog.askstring("تغيير اسم الكرة", "الرجاء إدخال اسم جديد:", initialvalue=self.value)
        if new_value:
            self.value = new_value

    def rotate_inductance_right(self):
        a, b, c, d= self.canvas.coords(self.body5)
        n1=[c,d-90,c,d-75]
        n2=[c-12,d-75,c+12,d-51]
        n3=[c-12,d-57,c+12,d-33]
        n4=[c-12,d-39,c+12,d-15]
        n5=[c,d-15,c,d]

        self.canvas.coords(self.body1, n1)
        self.canvas.coords(self.body2, n2)
        self.canvas.coords(self.body3, n3)
        self.canvas.coords(self.body4, n4)
        self.canvas.coords(self.body5, n5)
        

    def delete_combo(self):
        self.canvas.delete(self.body1)
        self.canvas.delete(self.body2)
        self.canvas.delete(self.body3)
        self.canvas.delete(self.body4)
        self.canvas.delete(self.body5)

#################################################################################################################################################
        
class DC_Power_Class:
    def __init__(self, canvas):
        self.canvas = canvas
        x = 90
        y = 120
        self.points = []
        self.body = None
        self.value = "10"
        self.color = None

        self.draw_resistor()
        
        # ربط حدث النقر والسحب
        self.canvas.tag_bind(self.body, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body, "<Button-3>", self.show_context_menu)

    def draw_resistor(self):
        self.body = self.canvas.create_line(self.points, smooth="false", width=3, fill=self.color, tags="resistor")

    def on_press(self, event):
        # حفظ موقع بداية السحب
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        self.start_x = cx*15
        self.start_y = cy*15

    def on_drag(self, event):
        # حساب التغيير في الموقع ونقل الخط المتعرج
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        evx = cx*15
        evy = cy*15
        delta_x = evx - self.start_x
        delta_y = evy - self.start_y
        self.canvas.move(self.body, delta_x, delta_y)
        self.start_x = evx
        self.start_y = evy

    def show_context_menu(self, event):
        menu = tk.Menu(self.canvas, tearoff=0)
        color_menu = tk.Menu(menu, tearoff=0)
        color_menu.add_command(label="blue", command=lambda: self.change_color("blue"))
        color_menu.add_command(label="red", command=lambda: self.change_color("red"))
        color_menu.add_command(label="yellow", command=lambda: self.change_color("yellow"))
        menu.add_cascade(label="color", menu=color_menu)
        menu.add_command(label="value", command=self.change_value)
        menu.add_command(label="rotate", command=self.rotate_resistor_right)
        menu.add_command(label="delete", command=self.delete_combo)
        menu.post(event.x_root, event.y_root)

    def change_color(self, new_color):
            self.color = new_color
            self.canvas.itemconfig(self.body, fill=self.color)

    def change_value(self):
        new_value = simpledialog.askstring("تغيير اسم الكرة", "الرجاء إدخال اسم جديد:", initialvalue=self.value)
        if new_value:
            self.value = new_value

    def rotate_resistor_right(self):
        a,A,b,B,c,C,d,D,e,E,f,F,g,G,h,H,i,I,j,J = self.canvas.coords(self.body)
        new_coords = [j,J-90,j,J-75,j-10,J-70,j+10,J-60,j-10,J-50,j+10,J-40,j-10,J-30,j+10,J-20,j,J-15,j,J]

        self.canvas.coords(self.body, *new_coords)
        

    def delete_combo(self):
        self.canvas.delete(self.body)

#################################################################################################################################################
'''
class Resistor_Class:
    def __init__(self, canvas):
        self.canvas = canvas
        x = 90
        y = 120
        self.points = [x, y, x+15, y, x+20, y+10, x+30, y-10, x+40, y+10, x+50, y-10, x+60, y+10, x+70,y-10 , x+75, y, x+90, y]
        self.body = None
        self.value = "10"
        self.color = None

        self.draw_resistor()
        
        # ربط حدث النقر والسحب
        self.canvas.tag_bind(self.body, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body, "<Button-3>", self.show_context_menu)

    def draw_resistor(self):
        self.body = self.canvas.create_line(self.points, smooth="false", width=3, fill=self.color, tags="resistor")

    def on_press(self, event):
        # حفظ موقع بداية السحب
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        self.start_x = cx*15
        self.start_y = cy*15

    def on_drag(self, event):
        # حساب التغيير في الموقع ونقل الخط المتعرج
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        evx = cx*15
        evy = cy*15
        delta_x = evx - self.start_x
        delta_y = evy - self.start_y
        self.canvas.move(self.body, delta_x, delta_y)
        self.start_x = evx
        self.start_y = evy

    def show_context_menu(self, event):
        menu = tk.Menu(self.canvas, tearoff=0)
        color_menu = tk.Menu(menu, tearoff=0)
        color_menu.add_command(label="blue", command=lambda: self.change_color("blue"))
        color_menu.add_command(label="red", command=lambda: self.change_color("red"))
        color_menu.add_command(label="yellow", command=lambda: self.change_color("yellow"))
        menu.add_cascade(label="color", menu=color_menu)
        menu.add_command(label="value", command=self.change_value)
        menu.add_command(label="rotate", command=self.rotate_resistor_right)
        menu.add_command(label="delete", command=self.delete_combo)
        menu.post(event.x_root, event.y_root)

    def change_color(self, new_color):
            self.color = new_color
            self.canvas.itemconfig(self.body, fill=self.color)

    def change_value(self):
        new_value = simpledialog.askstring("تغيير اسم الكرة", "الرجاء إدخال اسم جديد:", initialvalue=self.value)
        if new_value:
            self.value = new_value

    def rotate_resistor_right(self):
        a,A,b,B,c,C,d,D,e,E,f,F,g,G,h,H,i,I,j,J = self.canvas.coords(self.body)
        new_coords = [j,J-90,j,J-75,j-10,J-70,j+10,J-60,j-10,J-50,j+10,J-40,j-10,J-30,j+10,J-20,j,J-15,j,J]

        self.canvas.coords(self.body, *new_coords)
        

    def delete_combo(self):
        self.canvas.delete(self.body)
'''
#################################################################################################################################################
'''
class Resistor_Class:
    def __init__(self, canvas):
        self.canvas = canvas
        x = 90
        y = 120
        self.points = [x, y, x+15, y, x+20, y+10, x+30, y-10, x+40, y+10, x+50, y-10, x+60, y+10, x+70,y-10 , x+75, y, x+90, y]
        self.body = None
        self.value = "10"
        self.color = None

        self.draw_resistor()
        
        # ربط حدث النقر والسحب
        self.canvas.tag_bind(self.body, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.body, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.body, "<Button-3>", self.show_context_menu)

    def draw_resistor(self):
        self.body = self.canvas.create_line(self.points, smooth="false", width=3, fill=self.color, tags="resistor")

    def on_press(self, event):
        # حفظ موقع بداية السحب
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        self.start_x = cx*15
        self.start_y = cy*15

    def on_drag(self, event):
        # حساب التغيير في الموقع ونقل الخط المتعرج
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        evx = cx*15
        evy = cy*15
        delta_x = evx - self.start_x
        delta_y = evy - self.start_y
        self.canvas.move(self.body, delta_x, delta_y)
        self.start_x = evx
        self.start_y = evy

    def show_context_menu(self, event):
        menu = tk.Menu(self.canvas, tearoff=0)
        color_menu = tk.Menu(menu, tearoff=0)
        color_menu.add_command(label="blue", command=lambda: self.change_color("blue"))
        color_menu.add_command(label="red", command=lambda: self.change_color("red"))
        color_menu.add_command(label="yellow", command=lambda: self.change_color("yellow"))
        menu.add_cascade(label="color", menu=color_menu)
        menu.add_command(label="value", command=self.change_value)
        menu.add_command(label="rotate", command=self.rotate_resistor_right)
        menu.add_command(label="delete", command=self.delete_combo)
        menu.post(event.x_root, event.y_root)

    def change_color(self, new_color):
            self.color = new_color
            self.canvas.itemconfig(self.body, fill=self.color)

    def change_value(self):
        new_value = simpledialog.askstring("تغيير اسم الكرة", "الرجاء إدخال اسم جديد:", initialvalue=self.value)
        if new_value:
            self.value = new_value

    def rotate_resistor_right(self):
        a,A,b,B,c,C,d,D,e,E,f,F,g,G,h,H,i,I,j,J = self.canvas.coords(self.body)
        new_coords = [j,J-90,j,J-75,j-10,J-70,j+10,J-60,j-10,J-50,j+10,J-40,j-10,J-30,j+10,J-20,j,J-15,j,J]

        self.canvas.coords(self.body, *new_coords)
        

    def delete_combo(self):
        self.canvas.delete(self.body)
'''
#################################################################################################################################################
########################################################--------the wire------------
class Wire_Class:
    def __init__(self, canvas):
        self.canvas = canvas
        self.points = []
        self.body = []
        self.m=[]
        self.z=[]
        self.color = None
        self.pin = 0
        self.bin = 0
        global z
        
        canvas.bind("<Double-Button-1>", self.get_index)
        canvas.bind("<Button-3>", self.stop)

        # ربط حدث النقر والسحب
        self.ev()

    def ev(self):
        global z
        for i in range(0, len(self.body)):
            self.canvas.tag_bind(f"wire{self.z[i]}", "<ButtonPress-1>", lambda event, i=i: self.on_press(event, i))
            self.canvas.tag_bind(f"wire{self.z[i]}", "<B1-Motion>", lambda event, i=i: self.on_drag(event, i))
            self.canvas.tag_bind(f"wire{self.z[i]}", "<Button-3>", lambda event, i=i: self.show_context_menu(event, i))

    def get_index(self, event):
        global z
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        a = cx*15
        b = cy*15
        if(self.pin>=2):
            if(abs(a-self.points[self.pin-2])<abs(b-self.points[self.pin-1])):
                a=self.points[self.pin-2]
            else:
                b=self.points[self.pin-1]
        self.points.append(a)
        self.points.append(b)
        self.pin +=2
        self.draw_wire()
    
    def draw_wire(self):
        global z
        m = None
        if(self.pin>=4):
            if((self.points[self.pin-4]==self.points[self.pin-2])and(self.points[self.pin-3]==self.points[self.pin-1])):
                self.bin += 0
            elif(self.points[self.pin-4]==self.points[self.pin-2]):
                m = 1 #رأسي
            elif(self.points[self.pin-3]==self.points[self.pin-1]):
                m = 0 #أفقي
            if(len(self.body)>=1):
                if(m==self.m[self.bin-1]):
                    a,b,c,d=self.canvas.coords(self.body[self.bin-1])
                    self.canvas.coords(self.body[self.bin-1], a,b,self.points[self.pin-2],self.points[self.pin-1])
                else:
                    self.body.append(self.canvas.create_line(self.points[self.pin-4],self.points[self.pin-3],self.points[self.pin-2],self.points[self.pin-1], smooth="false", width=3, fill=self.color, tags=f"wire{z}"))
                    self.m.append(m)
                    self.z.append(z)
                    self.bin += 1
                    z+=1
            else:
                self.body.append(self.canvas.create_line(self.points[self.pin-4],self.points[self.pin-3],self.points[self.pin-2],self.points[self.pin-1], smooth="false", width=3, fill=self.color, tags=f"wire{z}"))
                self.m.append(m)
                self.z.append(z)
                self.bin += 1
                z+=1


    def stop(self, event):
        canvas.unbind("<Double-Button-1>")
        self.ev()

    def on_press(self, event, i):
        global z
        # حفظ موقع بداية السحب
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        self.start_x = cx*15
        self.start_y = cy*15

    def on_drag(self, event, i):
        global z
        # حساب التغيير في الموقع ونقل الخط المتعرج
        y = x = None
        dex=event.x
        cx=dex//15
        dey=event.y
        cy=dey//15
        if(dex%15>7):
            cx=cx+1
        if(dey%15>7):
            cy=cy+1
        evx = cx*15
        evy = cy*15
        delta_x = evx - self.start_x
        delta_y = evy - self.start_y
        x = delta_x
        y = delta_y
        if(self.m[i]==0):
            delta_x=0
            self.canvas.move(f"wire{self.z[i]}", delta_x, delta_y)
            a,b,c,d=self.canvas.coords(self.body[i])
            if(i==0):
                e,f,g,h=self.canvas.coords(self.body[i+1])
                self.canvas.coords(self.body[i+1], c,d,g,h)
                self.canvas.coords(self.body[i], a+x,b,c,d)

            elif(i==len(self.body)-1):
                e,f,g,h=self.canvas.coords(self.body[i-1])
                self.canvas.coords(self.body[i-1], e,f,a,b)
                self.canvas.coords(self.body[i], a,b,c+x,d)
            elif((i>0)and(i<(len(self.body)-1))):
                e,f,g,h=self.canvas.coords(self.body[i+1])
                self.canvas.coords(self.body[i+1], c,d,g,h)
                j,k,l,m=self.canvas.coords(self.body[i-1])
                self.canvas.coords(self.body[i-1], j,k,a,b)
        else:
            delta_y=0
            self.canvas.move(f"wire{self.z[i]}", delta_x, delta_y)
            a,b,c,d=self.canvas.coords(self.body[i])
            if(i==0):
                e,f,g,h=self.canvas.coords(self.body[i+1])
                self.canvas.coords(self.body[i+1], c,d,g,h)
                self.canvas.coords(self.body[i], a,b+y,c,d)
            elif(i==len(self.body)-1):
                e,f,g,h=self.canvas.coords(self.body[i-1])
                self.canvas.coords(self.body[i-1], e,f,a,b)
                self.canvas.coords(self.body[i], a,b,c,d+y)
            elif((i>0)and(i<(len(self.body)-1))):
                e,f,g,h=self.canvas.coords(self.body[i+1])
                self.canvas.coords(self.body[i+1], c,d,g,h)
                j,k,l,m=self.canvas.coords(self.body[i-1])
                self.canvas.coords(self.body[i-1], j,k,a,b)

        # إعادة تحديد موقع البداية لكل عنصر
        self.start_x = evx
        self.start_y = evy

    def show_context_menu(self, event, i):
        global z
        menu = tk.Menu(self.canvas, tearoff=0)
        color_menu = tk.Menu(menu, tearoff=0)
        color_menu.add_command(label="blue", command=lambda: self.change_color("blue"))
        color_menu.add_command(label="red", command=lambda: self.change_color("red"))
        color_menu.add_command(label="yellow", command=lambda: self.change_color("yellow"))
        menu.add_cascade(label="color", menu=color_menu)
        menu.add_command(label="delete", command=self.delete_combo)
        menu.post(event.x_root, event.y_root)

    def change_color(self, new_color):
            global z
            self.color = new_color
            for a in range(0, len(self.body)):
                self.canvas.itemconfig(f"wire{self.z[a]}", fill=self.color)

    def delete_combo(self):
        global z
        for a in range(0, len(self.body)):
            self.canvas.delete(f"wire{self.z[a]}")
#################################################################################################################################################

def draw_grid(canvas, width, height, spacing):
    # رسم خطوط الشبكة الرأسية
    for x in range(0, width, spacing):
        canvas.create_line(x, 0, x, height, fill="lightgray", width=1)

    # رسم خطوط الشبكة الأفقية
    for y in range(0, height, spacing):
        canvas.create_line(0, y, width, y, fill="lightgray", width=1)

#################################################################################################################################################

def add_resistor(resistor_list):
    resistor_list.append(Resistor_Class(canvas))

def add_capacitor(capacitor_list):
    capacitor_list.append(Capacitor_Class(canvas))

def add_inductance(inductance_list):
    inductance_list.append(Inductance_Class(canvas))

def add_wire(wire_list):
    wire_list.append(Wire_Class(canvas))

#################################################################################################################################################
#################################################################################################################################################

root = tk.Tk()
root.title("FullScreen Tkinter App")
root.geometry("{0}x{1}+450+200".format(600, 400))

canvas = tk.Canvas(root, width=1530, height=780, bg="#FFFAFA")#the color is snow
canvas.pack()

draw_grid(canvas, 1530, 780, 15)

resistor_list = []
capacitor_list = []
inductance_list = []
wire_list = []
global z
z = 0

menu_bar = tk.Menu(root)

# إعداد قائمة الملف
tools_menu = tk.Menu(menu_bar, tearoff=0)
tools_menu.add_command(label="Resistor", command=lambda: add_resistor(resistor_list))
tools_menu.add_command(label="Capacitor", command=lambda: add_capacitor(capacitor_list))
tools_menu.add_command(label="Inductance", command=lambda: add_inductance(inductance_list))
tools_menu.add_separator()
tools_menu.add_command(label="DC_power", command=lambda: Resistor_Class(canvas))
tools_menu.add_command(label="AC_power", command=lambda: Resistor_Class(canvas))
tools_menu.add_separator()
tools_menu.add_command(label="Ground", command=lambda: Resistor_Class(canvas))
tools_menu.add_separator()
tools_menu.add_command(label="Wire", command=lambda: add_wire(wire_list))

# إضافة قائمة الملف إلى شريط القائمة
menu_bar.add_cascade(label="tools", menu=tools_menu)

# إعداد نافذة البرنامج
root.config(menu=menu_bar)

root.state('zoomed')
root.mainloop()
# 1536x793
