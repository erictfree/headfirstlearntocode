from tkinter import *
import model

cell_size = 5



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
    option = OptionMenu(root, choice, 'Choose a Pattern', 'glider', 'glider gun', 'random')
    option.config(width=20)

    grid_view.grid(row=0, columnspan=3, padx=20, pady=20) 
    start_button.grid(row=1, column=0, sticky=W,padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)

if __name__ == '__main__':
    setup()
    mainloop()

