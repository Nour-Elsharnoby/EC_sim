# import tkinter as tk
# import math

# class RotatableLine:
#     def __init__(self, canvas, x1, y1, x2, y2):
#         self.canvas = canvas
#         self.line = canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
#         self.angle = 0  # زاوية الدوران

#         # ربط حدث النقر بالزر
#         self.canvas.tag_bind(self.line, "<Button-1>", self.rotate_line)

#     def rotate_line(self, event):
#         # تحديث زاوية الدوران إلى 90 درجة
#         self.angle += 90
#         self.angle %= 360  # للتأكد من أن الزاوية لا تتجاوز 360 درجة

#         # حساب إحداثيات نقطة الدوران
#         x, y, a, b = self.canvas.coords(self.line)
#         # print(x)
#         # print(y)
#         # print(a)
#         # print(b)

#         # حساب الإحداثيات الجديدة بعد الدوران
#         new_x = a
#         new_y = b-(a-x)

#         # تحديث إحداثيات الخط
#         self.canvas.coords(self.line, a, b, new_x, new_y)

# def main():
#     root = tk.Tk()
#     root.title("دوران الخط 90 درجة")

#     canvas = tk.Canvas(root, width=200, height=200, bg="white")
#     canvas.pack()

#     # إنشاء الخط الأول
#     line1 = RotatableLine(canvas, x1=100, y1=100, x2=150, y2=100)


#     root.mainloop()

# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import simpledialog

class DraggableCurve:
    def __init__(self, canvas):
        self.canvas = canvas
        self.points = [90, 120, 102, 120, 107, 130, 117, 110, 127, 130, 137, 110, 147, 130, 157,110 , 167,130 , 177,110 ,182, 120, 195, 120]
        self.line = None
        self.value = "10"
        self.color = None

        self.draw_curve()
        
        # ربط حدث النقر والسحب
        self.canvas.tag_bind(self.line, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.line, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.line, "<Button-3>", self.show_context_menu)

    def draw_curve(self):
        self.line = self.canvas.create_line(self.points, smooth="false", width=3, fill=self.color, tags="curve")

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
        self.canvas.move(self.line, delta_x, delta_y)
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
        menu.add_command(label="rotate", command=self.rotate_combo)
        menu.add_command(label="delete", command=self.delete_combo)
        menu.post(event.x_root, event.y_root)

    def change_color(self, new_color):
            self.color = new_color
            self.canvas.itemconfig(self.line, fill=self.color)

    def change_value(self):
        new_value = simpledialog.askstring("تغيير اسم الكرة", "الرجاء إدخال اسم جديد:", initialvalue=self.value)
        if new_value:
            self.value = new_value

    def delete_combo(self):
        self.canvas.delete(self.line)

    def rotate_combo(self):
        self.canvas.delete(self.line)
        self.draw_curve()


def draw_grid(canvas, width, height, spacing):
    # رسم خطوط الشبكة الرأسية
    for x in range(0, width, spacing):
        canvas.create_line(x, 0, x, height, fill="lightgray", width=1)

    # رسم خطوط الشبكة الأفقية
    for y in range(0, height, spacing):
        canvas.create_line(0, y, width, y, fill="lightgray", width=1)

root = tk.Tk()
root.title("FullScreen Tkinter App")
root.geometry("{0}x{1}+450+200".format(600, 400))

canvas = tk.Canvas(root, width=1530, height=780, bg="#FFFAFA")#the color is snow
canvas.pack()

draw_grid(canvas, 1530, 780, 15)

menu_bar = tk.Menu(root)

# إعداد قائمة الملف
tools_menu = tk.Menu(menu_bar, tearoff=0)
tools_menu.add_command(label="Resistor", command=lambda: DraggableCurve(canvas))
tools_menu.add_command(label="Capacitor", command=lambda:DraggableCurve(canvas))
tools_menu.add_command(label="Inductance", command=lambda: DraggableCurve(canvas))
tools_menu.add_separator()
tools_menu.add_command(label="DC_power", command=lambda:DraggableCurve(canvas))
tools_menu.add_command(label="AC_power", command=lambda: DraggableCurve(canvas))
tools_menu.add_separator()
tools_menu.add_command(label="Ground", command=lambda: DraggableCurve(canvas))

# إضافة قائمة الملف إلى شريط القائمة
menu_bar.add_cascade(label="tools", menu=tools_menu)

# إعداد نافذة البرنامج
root.config(menu=menu_bar)

root.state('zoomed')
root.mainloop()
# 1536x793
