from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from gestorAplicacion.usuario.Usuario import Usuario
from gestorAplicacion.usuario.Coordinador import Coordinador
from gestorGrafico.ventPrincipal import VentPrincipal
from excepciones.ObjetoInexistente import *
from excepciones.ErrorManejo import *

class VentLog(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Matricula de Materias")
        self.resizable(0,0)
        self.geometry("865x460")
        self.config(bg="#ebfce8",highlightbackground="#089970",highlightthickness=5)
        self.iconbitmap("Python\src\gestorGrafico\Imagenes\icono.ico")

        frame = Frame(self, width=400, height=200,bg="#ebfce8",highlightbackground="#089970",highlightthickness=5)
        frame.pack(expand=True)

        def mostrarContraseña():
            if entrada2.cget('show') == '*':
                entrada2.config(show='')
            else:
                entrada2.config(show='*')

        def limpiar():
            entrada1.delete(0, last= END)
            entrada2.delete(0, last= END)

        def cambiarVentana():
            self.destroy()
            VentPrincipal()

        def verificar():
            try:
                exist = False
                esCoo = False
                pw = False
                coordi = None
                
                if entrada1.get() == "" and entrada2.get() == "":
                    raise CampoVacio
                
                for usuario in Usuario.getUsuariosTotales():
                    if usuario.getId() == int(entrada1.get()):
                        coordi = usuario
                        exist = True
                        break

                if exist:
                    if not isinstance(usuario, Coordinador):
                        return messagebox.showwarning("Error", "El usuario ingresado no corresponde a un coordinador")
                    else:
                        esCoo = True

                if esCoo:
                    if str(usuario.getPw()) == entrada2.get():
                        pw = True
                    else:
                        return messagebox.showwarning("Error", "La contrasena es incorrecta. Intentelo nuevamente")
                else:
                    return messagebox.showwarning("Error", "El id ingresado no corresponde a ningún usuario")
                if pw:
                    Coordinador.setUsuarioIngresado(coordi)
                    cambiarVentana()
            except CampoVacio:
                messagebox.showerror("Error",CampoVacio().mostrarMensaje())
            except ValueError:
                messagebox.showerror("Error",CampoInvalido().mostrarMensaje())
             
        usuar = Label(frame,text="Usuario",bg="#ebfce8",font=("arial", 11, "bold"))
        entrada1 = Entry(frame)
        cont = Label(frame,text="Contraseña",bg="#ebfce8",font=("arial", 11, "bold"))
        entrada2 = Entry(frame, show="*")
        boton_ingresar = Button(frame, text="Iniciar Sesion", command= verificar,bg="#089970",font=("arial", 11, "bold"),fg="#ebfce8")
        boton_limpiar = Button(frame, text="Limpiar", command= limpiar,bg="#089970",font=("arial", 11, "bold"),fg="#ebfce8")
        revisar = Checkbutton(frame, text="Mostrar contraseña", command= mostrarContraseña,bg="#ebfce8",font=("arial", 11))        
        
        usuar.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        entrada1.grid(row=0,column=1,columnspan=2,padx=10,pady=10)
        cont.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        entrada2.grid(row=1,column=1,columnspan=2,padx=10,pady=10) 
        boton_ingresar.grid(row=3,column=0, columnspan=2, padx=10,pady=10,sticky="w")
        boton_limpiar.grid(row=3,column=1, columnspan=2, padx=10,pady=10,sticky="w")
        revisar.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        
        self.mainloop()
        
    @classmethod
    def getCoordinadorIngresado(cls):
        return cls.coordinadorIngresado
    
    @classmethod
    def setCoordinadorIngresado(cls, coordinador):
        cls.coordinadorIngresado = coordinador
       
        
