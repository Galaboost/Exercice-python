# import des librairies 

import tkinter as tk 

# constante 

HEIGHT = 500
WIDTH = 500

# variable global

clic = []
l1 = []
l2 = []
PAUSE = 1
# definition des fonction

def ligne(event) :
    global clic, l1, l2
    clic.append((event.x, event.y))
    if len(clic) == 2 :
        l1.append(canvas.create_line(clic[0], clic[1], fill = "blue"))
    if len(clic) == 4 :
        l2.append(canvas.create_line(clic[2], clic[3], fill = "red"))
    if len(clic) == 5 :
        canvas.delete(l1)
        canvas.delete(l2)
        clic = []
        l1 = []
        l2 = []

def pause() :
    global PAUSE
    if PAUSE == 1:
        bouton.config(text = "Restart")
    else :
        bouton.config(text = "Pause")
    PAUSE = 1 - PAUSE
   




# programme principal 

root = tk.Tk()
root.title("Wargreymon")

# création des widgets 

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = "white" )
bouton = tk.Button(root, text = "Pause", command = pause)

# placement des widgets

canvas.grid()
bouton.grid()

#autre

root.bind("<Button-1>", ligne)

# fin 

root.mainloop()