from tkinter import *

class VentInicio(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)       
        self.pack()
        
 # Creacion de Frames

        p1Frame=Frame(self,height=450,width=425,bg="#ebfce8")
        p1Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=(5,0),pady=5)
        p1Frame.grid_propagate(False)

        p2Frame=Frame(self,height=450,width=425,bg="#ebfce8")
        p2Frame.grid(row=0,column=1,columnspan=1,rowspan=1,padx=(0,5),pady=5)
        p2Frame.grid_propagate(False)

        p3Frame=Frame(p1Frame,height=70,width=415,bg="#089970")
        p3Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,3))
        p3Frame.pack_propagate(False)

        p4Frame=Frame(p1Frame,height=365,width=415,bg="#ebfce8")
        p4Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(3,5))
        p4Frame.pack_propagate(False)

        p5Frame=Frame(p2Frame,height=100,width=415,bg="yellow")
        p5Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,3))
        p5Frame.pack_propagate(False)

        p6Frame=Frame(p2Frame,height=335,width=335,bg="#089970")
        p6Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(3,5))
        p6Frame.grid_propagate(False)

 # Creacion de Frames
        mensaje="Hola, bienvenido al sistemas de matricula de materias Z.I.A"
        mensajeBienv = Label(p3Frame,text=mensaje,font=("arial", 18, "bold"),bg="#089970",wraplength=415,fg="#ebfce8")
        mensajeBienv.pack(expand=True)

        
        
        bibi1="Soy Jhoan Alexis Rúa García, estudiante de Ingeniería de Sistemas e Informática. Apasionado por las matemáticas y el desarrollo web. Soy una persona persistente, que nunca se rinde ante las dificultades. Además, soy un gran fanático del fútbol y disfruto enfrentando nuevos desafíos"
        bibi2="Mi nombre es Tomas Velasquez, tengo 22 años y estudio ingeniería de sistemas e informática. De esta carrera me gustan los retos lógicos que se presentan constantemente, por otra parte me apasiona la música y el futbol. "
        bibi3="Soy Lina, mi color favorito es el morado, me gusta la torta de red velvet, amo los gatos, a mi hermanito, mi familia y mi mejor amiga. Soy feliz jugando con mis gatas, estudiando y trabajando, mi esencia radica en hacer todo con amor"
        bibi4="Hola, soy Stiven Rosero, tengo 19 años y soy un apasionado por el ciclismo y la vida al aire libre. Mi familia es mi motivacion para trabajar. Mi filosofía de vida es simple: 'Con amor y con esfuerzo, nos ganaremos el almuerzo'"
        bibi5="Soy Sergio Morales y estudio Ingeniería de sistemas. Me gusta el basket, la ciencia y la programacion. Aprovecho mi tiempo libre en aprender cosas nuevas y hacer deporte. En el futuro me gustaria dedicarme al desarrollo de videojuegos, que es lo que me apasiona"

        self.biblios = [bibi1,bibi2,bibi3,bibi4,bibi5]

        self.punteroIntergrante =1
        def cambiarTextoEImagenF6(evento):
            i=self.punteroIntergrante

# Cambio de texto      
            evento.widget["text"]=self.biblios[i]

# Cambio de imagenes
            
            imag1=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\Foto{i+1}_1.png")     
            imag2=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\Foto{i+1}_2.png")     
            imag3=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\Foto{i+1}_3.png")     
            imag4=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\Foto{i+1}_4.png")     
            
            global lisImagenes 
            lisImagenes=[imag1,imag2,imag3,imag4]
            
            setCuatroImagenes(lisImagenes)
            
# Cambio de puntero  
            i+=1
            n =5 # numero de grupo de fotos en la carpeta imagenes
            if i ==n:
                self.punteroIntergrante= 0
            else:
                self.punteroIntergrante=i
            

        biblioTexto = Label(p5Frame,text=bibi1,font=("arial", 10),bg="#ebfce8",wraplength=405,highlightbackground="#089970",highlightthickness=2)
        biblioTexto.pack(expand=True,fill="both")
        biblioTexto.bind("<Button-1>",cambiarTextoEImagenF6)



        def setCuatroImagenes(packImagenes):
            img1.config(image=packImagenes[0])
            img2.config(image=packImagenes[1])
            img3.config(image=packImagenes[2])
            img4.config(image=packImagenes[3])

        tam=157

        self.image1 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\Foto1_1.png")
        self.image2 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\Foto1_2.png")
        self.image3 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\Foto1_3.png")
        self.image4 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\Foto1_4.png")


        img1 = Label(p6Frame,image=self.image1,height=tam,width=tam)
        img1.grid(row=0,column=0,columnspan=1,rowspan=1,padx=3,pady=3)

        img2 = Label(p6Frame,image=self.image2,height=tam,width=tam)
        img2.grid(row=0,column=1,columnspan=1,rowspan=1,padx=3,pady=3)

        img3 = Label(p6Frame,image=self.image3,height=tam,width=tam)
        img3.grid(row=1,column=0,columnspan=1,rowspan=1,padx=3,pady=3)

        img4 = Label(p6Frame,image=self.image4,height=tam,width=tam)
        img4.grid(row=1,column=1,columnspan=1,rowspan=1,padx=3,pady=3)
        
# Frame 4
        
        # Imagen:
        self.punteroImagen=2
        def cambiarTextoEImagenF4(evento):
            i=self.punteroImagen

            # Cambio de imagenes
            global imagF4
            imagF4=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\Funcion{i}.png")     
   
            ImagenF4.config(image=imagF4)
            
# Cambio de puntero  
            i+= 1
            n = 5 
            if i ==(n+1):
                self.punteroImagen= 1
            else:
                self.punteroImagen=i
        
        self.imagenF41 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\Funcion1.png")
        
        ImagenF4 = Label(p4Frame,image=self.imagenF41,width=300,wraplength=160,highlightbackground="#089970",highlightthickness=4)
        ImagenF4.pack(side="top",pady=3)
        ImagenF4.bind("<Enter>",cambiarTextoEImagenF4)
        
# Texto descripcion
        
        descripTexto = Label(p4Frame,text="",font=("arial", 10, "bold"),bg="#ebfce8",wraplength=400)
        descripTexto.pack(side="top",fill="x",pady=10)
        
# Boton para pasar
        
        def cambioVentana():
            self.destroy()           
            ventana.abrirLog()
            
        
        botonIngreso=Button(p4Frame,text="Ingresar",command=cambioVentana,bg="#089970",font=("arial", 12, "bold"),fg="#cedae0")
        botonIngreso.pack(side="top",pady=(10,20))
           
        
# Creacion del menu :U
        ventana.menuBar = Menu(ventana)
        ventana.option_add("*tearOff",  False)
        ventana.config(menu=ventana.menuBar)
        menu1= Menu(ventana.menuBar)
        ventana.menuBar.add_cascade(label="Inicio",menu=menu1)
        menu1.add_command(label="Salir",command=lambda:ventana.destroy())
        
        textDescrip="Z.I.A es un sistema de gestión académica diseñado para mejorar la administración de asignaturas en instituciones educativas. Está dirigido exclusivamente a coordinadores y tiene el proposito de facilitar los diferentes procesos relacionados."
        menu1.add_command(label="Descripcion",command=lambda: descripTexto.config(text=textDescrip))
        