from tkinter import *
import model

cell_size = 5
is_running = False



def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice

    root = Tk()
    root.title('The Game of Life')

    grid_view = Canvas(root, width=model.width*cell_size,
                             height=model.height*cell_size,
                             borderwidth=0,
                             highlightthickness=0,
                             bg='white')

    start_button = Button(root, text='Start', width=12)
    clear_button = Button(root, text='Clear', width=12)

    choice = StringVar(root) 
    choice.set('Choose a Pattern')
    option = OptionMenu(root, choice, 'Choose a Pattern', 'glider', 'glider gun', 'random', command=option_handler)
    option.config(width=20)

    grid_view.grid(row=0, columnspan=3, padx=20, pady=20) 
    grid_view.bind('<Button-1>', grid_handler)
    start_button.grid(row=1, column=0, sticky=W,padx=20, pady=20)
    start_button.bind('<Button-1>', start_handler)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)
    clear_button.bind('<Button-1>', clear_handler)

def option_handler(event):
    global is_running, start_button, choice 

    is_running = False
    start_button.configure(text='Start')

    selection = choice.get()

    if selection == 'glider':
        model.load_pattern(model.glider_pattern, 10, 10)

    elif selection == 'glider gun':
        model.load_pattern(model.glider_gun_pattern, 10, 10)  

    elif selection == 'random':
        model.randomize(model.grid_model, model.width, model.height)

    update()

def start_handler(event):
   global is_running, start_button

   if is_running:
       is_running = False
       start_button.configure(text='Start')
   else:
       is_running = True
       start_button.configure(text='Pause')
       update()

def clear_handler(event):
   global is_running, start_button

   is_running = False
   for i in range(0, model.height):
       for j in range(0, model.width):
           model.grid_model[i][j] = 0

   start_button.configure(text='Start')
   update()

def grid_handler(event):
    global grid_view, cell_size

    x = int(event.x / cell_size)
    y = int(event.y / cell_size)
    
    if (model.grid_model[x][y] == 1):
        model.grid_model[x][y] = 0
        draw_cell(x, y, 'white')
    else:
        model.grid_model[x][y] = 1
        draw_cell(x, y, 'black')

def update():
   global grid_view, root, is_running

   grid_view.delete(ALL)

   model.next_gen()
   for i in range(0, model.height):
       for j in range(0, model.width):
           if model.grid_model[i][j] == 1:
                draw_cell(i, j, 'black')
   if (is_running):
       root.after(100,update)

def draw_cell(row, col, color):
    global grid_view, cell_size

    if color == 'black':
        outline = 'grey'
    else:
        outline = 'white'

    grid_view.create_rectangle(row*cell_size,
                               col*cell_size,
                               row*cell_size+cell_size,
                               col*cell_size+cell_size,
                               fill=color, outline=outline)

if __name__ == '__main__':
    setup()
    update()
    mainloop()
