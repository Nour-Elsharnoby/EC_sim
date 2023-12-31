# # import pygame
# # import sys

# # # إعداد Pygame
# # pygame.init()

# # # إعداد الشاشة
# # width, height = 800, 600
# # screen = pygame.display.set_mode((width, height))
# # pygame.display.set_caption("سحب نقطة بالماوس")

# # # الألوان
# # black = (0, 0, 0)
# # white = (255, 255, 255)
# # blue = (0, 0, 255)
# # red = (255, 0, 0)

# # # إعداد النقطة
# # point_color = black
# # point_radius = 10
# # point_pos = pygame.Vector2(width // 2, height // 2)
# # point_poos = pygame.Vector2(width // 3, height // 3)
# # p1, p2, dif1, dif2 = pygame.Vector2(0, 0), pygame.Vector2(0, 0), pygame.Vector2(0, 0), pygame.Vector2(0, 0)


# # # دورة اللعبة
# # clock = pygame.time.Clock()
# # running = True
# # dragging = False
# # dd = False
# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #         elif event.type == pygame.MOUSEBUTTONDOWN:
# #             if event.button == 1:  # زر اليسار
# #                 mouse_pos = pygame.Vector2(event.pos)
# #                 if (mouse_pos - point_pos).length() < point_radius:
# #                     dragging = True
# #                     dif1 = point_pos - mouse_pos
# #                 elif (mouse_pos - point_poos).length() < point_radius:
# #                     dd = True
# #                     dif2 = point_poos - mouse_pos
# #         elif event.type == pygame.MOUSEBUTTONUP:
# #             if event.button == 1:
# #                 dragging = False
# #                 dd = False

# #     if dragging:
# #         mnow = pygame.mouse.get_pos()
# #         point_pos = mnow + dif1
    
# #     if dd:
# #         mnow = pygame.mouse.get_pos()
# #         point_poos = mnow + dif2

# #     # رسم النقطة
# #     screen.fill(white)
# #     pygame.draw.circle(screen, point_color, (int(point_pos.x), int(point_pos.y)), point_radius)
# #     pygame.draw.circle(screen, blue, (int(point_poos.x), int(point_poos.y)), point_radius)
# #     p1 =pygame.Vector2((((point_pos.x - point_poos.x) // 2)+point_poos.x), point_poos.y)
# #     p2 =pygame.Vector2((((point_pos.x - point_poos.x) // 2)+point_poos.x), point_pos.y)
# #     #liist = [point_poos.x, point_poos.y, p1.x, p1.y, p2.x, p2.y, point_pos.x, point_pos.y]
# #     #pygame.draw.lines(screen, red, False, liist, 5)
# #     liist = [point_poos, p1, p2, point_pos]
# #     pygame.draw.lines(screen, red, False, liist, 5)
# #     #pygame.draw.lines(screen, red, liist, 5)


# #     # تحديث الشاشة
# #     pygame.display.flip()

# #     # تحديث معدل الإطارات
# #     clock.tick(60)

# # # إغلاق Pygame
# # pygame.quit()
# # sys.exit()


        

   



# # import tkinter as tk

# # # Function to draw a line between the circles
# # def draw_line(event):
# #     canvas.create_line(circle1_coords[0], circle1_coords[1], circle2_coords[0], circle2_coords[1])

# # # Function to handle circle click
# # def circle_clicked(event):
# #     global circle_clicked_flag, circle1_coords, circle2_coords

# #     if not circle_clicked_flag:
# #         circle1_coords = (event.x, event.y)
# #         canvas.create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20, outline='black', width=2)
# #         circle_clicked_flag = True
# #     else:
# #         circle2_coords = (event.x, event.y)
# #         canvas.create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20, outline='black', width=2)
# #         circle_clicked_flag = False
# #         draw_line(event)

# # # Create the main window
# # root = tk.Tk()
# # root.title("Draw Line Between Circles")

# # # Create a canvas to draw on
# # canvas = tk.Canvas(root, width=400, height=400)
# # canvas.pack()

# # # Variables to keep track of circle coordinates and click state
# # circle1_coords = (0, 0)
# # circle2_coords = (0, 0)
# # circle_clicked_flag = False

# # # Bind mouse click events to circle_clicked function
# # canvas.bind("<Button-1>", circle_clicked)

# # # Start the main loop
# # root.mainloop()










# import tkinter as tk

# # Function to draw a line between the circles
# def draw_line():
#     canvas.create_line(circle1_coords[0], circle1_coords[1], circle2_coords[0], circle2_coords[1], width=3)

# # Function to handle circle click
# def circle_clicked(event):
#     global circle_clicked_flag, circle1_coords, circle2_coords

#     if not circle_clicked_flag:
#         circle1_coords = (event.x, event.y)
#         canvas.create_oval(event.x - 1.5, event.y - 1.5, event.x + 1.5, event.y + 1.5, outline='black', fill='black', width=2)
#         circle_clicked_flag = True
#     else:
#         circle2_coords = (event.x, event.y)
#         canvas.create_oval(event.x - 1.5, event.y - 1.5, event.x + 1.5, event.y + 1.5, outline='black', fill='black', width=2)
#         circle_clicked_flag = False
#         draw_line()

# # Create the main window
# root = tk.Tk()
# root.title("Draw Line Between Circles")

# # Create a canvas to draw on
# canvas = tk.Canvas(root, width=1200, height=1200)
# canvas.pack()

# # Variables to keep track of circle coordinates and click state
# circle1_coords = (0, 0)
# circle2_coords = (0, 0)
# circle_clicked_flag = False

# # Bind mouse click events to circle_clicked function
# canvas.bind("<Button-1>", circle_clicked)

# # Start the main loop
# root.mainloop()

import tkinter as tk

class CircuitSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Circuit Simulator")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.components = []   # List to store component IDs
        self.connections = []  # List to store connection IDs
        self.selected_connection_points = []  # List to store selected connection points for drawing wires

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Motion>", self.on_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # Create a clear button
        clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5)

        # Create a button to add components
        add_component_button = tk.Button(root, text="Add Component", command=self.add_component)
        add_component_button.pack(side=tk.LEFT, padx=5)

    def create_component(self, x, y):
        component_id = self.canvas.create_rectangle(x, y, x + 30, y + 30, fill="lightblue", tags="component")
        self.components.append(component_id)

        # Add connection points to the component (two on each side)
        connection_points = []
        for i in range(2):
            connection_x = x if i == 0 else x + 30
            connection_y = y + 15
            connection_point_id = self.canvas.create_oval(connection_x - 5, connection_y - 5,
                                                           connection_x + 5, connection_y + 5, fill="red", tags="connection")
            connection_points.append(connection_point_id)

        # Bind click event to connection points
        for connection_point_id in connection_points:
            self.canvas.tag_bind(connection_point_id, "<Button-1>", lambda event, id=connection_point_id: self.select_connection_point(id))

    def select_connection_point(self, connection_point_id):
        if connection_point_id not in self.selected_connection_points:
            self.selected_connection_points.append(connection_point_id)

            if len(self.selected_connection_points) == 2:
                # Draw wire between the selected connection points
                x1, y1 = self.canvas.coords(self.selected_connection_points[0])[0],self.canvas.coords(self.selected_connection_points[0])[1]
                x2, y2 = self.canvas.coords(self.selected_connection_points[1])[0],self.canvas.coords(self.selected_connection_points[1])[1]
                wire_id = self.canvas.create_line(x1+5, y1+5, x2+5, y2+5, fill="black", width=2, tags="wire")
                self.connections.append(wire_id)

                # Clear selected connection points
                self.selected_connection_points.clear()
                self.selected_connection_points = []

    def on_click(self, event):
        x, y = event.x, event.y
        clicked_connection = self.canvas.find_closest(x, y)
        
        if clicked_connection:
            connection_point_id = clicked_connection[0]
            self.select_connection_point(connection_point_id)

    def on_motion(self, event):
        pass  # No action on motion event

    def on_release(self, event):
        pass  # No action on release event

    def clear_canvas(self):
        self.canvas.delete("all")
        self.components = []
        self.connections = []
        self.selected_connection_points = []

    def add_component(self):
        # Add a component at a random position
        x = 50 + len(self.components) * 100
        y = 50
        self.create_component(x, y)

if __name__ == "__main__":
    root = tk.Tk()
    app = CircuitSimulatorApp(root)
    root.mainloop()