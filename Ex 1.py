# import des librairies

import tkinter as tk 


# constante

HEIGHT = 500
WIDTH = 500

# fonction global
couleur = "red"
restart = 1
# definition des fonctions 

def clic(event) : 
    global couleur
    if 150 < event.x < 350 and 150 < event.y < 350 : 
        if couleur == "red" :
            couleur = "blue"
        elif couleur == "blue" :
            couleur = "red"
        canvas.create_rectangle(150,150,350,350, fill = couleur)
    elif event.x > 350 or event.x < 150 or event.y < 150 or event.y > 350 :
        couleur = None

def recommencer() :
    global couleur
    couleur = "red"
    canvas.create_rectangle(150,150,350,350, fill = couleur)
        





# programme principal

root = tk.Tk()
root.title("Wargreymon")


# création des widgets 

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = "black" )
bouton = tk.Button(root, text = "Recommencer", command = recommencer)


# placement des widgets

canvas.grid()
bouton.grid()

# autre

rectangle = canvas.create_rectangle(150,150,350,350, fill = "red")
root.bind("<Button-1>", clic)

# fin

root.mainloop()