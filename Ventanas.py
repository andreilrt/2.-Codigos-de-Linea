import tkinter
import numpy
import matplotlib.pyplot

tk = tkinter
Np = numpy
Plt = matplotlib.pyplot

class VentanaHome(tk.Frame):
    NoFigura = 0
    Xinicial = 550
    Yinicial = 30
    Alto = 400
    Ancho = 350

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(str(self.Ancho)+"x"+str(self.Alto)+"+"+str(self.Xinicial)+"+"+str(self.Yinicial))
        self.create_widgets()

    def create_widgets(self):
        self.Opcion = tk.IntVar()
        self.Anuncio = tk.Label(self.master,
        text="Ingrese la trama que quiere representar")
        self.Anuncio.place(x=30,y=10)
        self.Mensaje = tk.Entry(self.master,width=55)
        self.Mensaje.place(x=10,y=30)
        self.NRZBipolar = tk.Radiobutton(self.master,text="NRZ Bipolar ",variable=self.Opcion,value=1)
        self.NRZBipolar.place(x=120,y=60)
        self.AMINRZ = tk.Radiobutton(self.master,text="AMI NRZ ",variable=self.Opcion,value=2)
        self.AMINRZ.place(x=120,y=90)
        self.HDB3 = tk.Radiobutton(self.master,text="HDB3 ",variable=self.Opcion,value=3)
        self.HDB3.place(x=120,y=120)
        self.Generar = tk.Button(self.master, text="Generar", fg="blue",
                              command=self.MostrarSeleccion)
        self.Generar.place(x=150,y=150)
        self.Salir = tk.Button(self.master, text="Salir", fg="red",
                              command=self.master.destroy)
        self.Salir.place(x=160,y=180)
    
    def MostrarSeleccion(self):
        if self.Opcion.get() == 1:
            self.NRZBipolarCod()
        if self.Opcion.get() == 2:
            self.AMINRZCod()
        if self.Opcion.get() == 3:
            print("HDB3")
    
    def NRZBipolarCod(self):
        self.x = []
        self.y = []
        self.linea0x = []
        self.linea0y = []
        self.Trama = self.Mensaje.get()
        self.Longitud = len(self.Trama)
        for z in range(self.Longitud):
            self.x.append(z)
            self.x.append(z+1)
            self.linea0x.append(z)
            self.linea0x.append(z+1)
            self.linea0y.append(0)
            self.linea0y.append(0)
            if self.Trama[z]=='1':
                self.y.append(1)
                self.y.append(1)
            if self.Trama[z]=='0':
                self.y.append(-1)
                self.y.append(-1)

        self.NoFigura +=1
        Plt.figure(self.NoFigura)
        Plt.plot(self.x, self.y, 'r', label = "NRZ Bipolar")
        Plt.plot(self.linea0x, self.linea0y, 'g--')
        Plt.axis('scaled')
        Plt.legend()
        Plt.show()

    def AMINRZCod(self):
        self.x = []
        self.y = []
        self.linea0x = []
        self.linea0y = []
        self.Estado = True
        self.Trama = self.Mensaje.get()
        self.Longitud = len(self.Trama)
        for z in range(self.Longitud):
            self.x.append(z)
            self.x.append(z+1)
            self.linea0x.append(z)
            self.linea0x.append(z+1)
            self.linea0y.append(0)
            self.linea0y.append(0)
            if self.Trama[z]=='1':
                if self.Estado:
                    self.y.append(1)
                    self.y.append(1)
                    self.Estado=False
                else:
                    self.y.append(-1)
                    self.y.append(-1)
                    self.Estado=True
            if self.Trama[z]=='0':
                self.y.append(0)
                self.y.append(0)

        self.NoFigura +=1
        Plt.figure(self.NoFigura)
        Plt.plot(self.x, self.y, 'r', label = "NRZ Bipolar")
        Plt.plot(self.linea0x, self.linea0y, 'g--')
        Plt.axis('scaled')
        Plt.legend()
        Plt.show()

Raiz = tk.Tk()
app = VentanaHome(master=Raiz)
app.mainloop()