import time
from datetime import datetime
import serial
import tkinter as tk

class App():
    def __init__(self):
        self.root = tk.Tk()
        #self.logo = tk.PhotoImage(file="H:\public\dampa.gif")
        #self.w1 = tk.Label(image=self.logo).pack()

        self.logo = tk.PhotoImage(file="W:\public_html\dampa.gif")
        self.w1 = tk.Label(image=self.logo).pack()

        tk.Label (text='\nDigite o tempo de atualizacao (segundos):').pack()
        self.spin = tk.Spinbox(from_ = 1, to = 100)
        self.spin.pack()

        tk.Label (text='\n').pack()
        button1 = tk.Button(text ="Select",command=self.inicia).pack()

        self.root.mainloop()


    def inicia (self):
        self.root.withdraw()
        self.frame = tk.Toplevel()

        arquivo3 = open("capreserv.txt", "a+")
        arquivo3.write("capacidade")
        arquivo3.close()

        self.label1 = tk.Label (self.frame,text="Atualizado em:").pack()
        self.label2 = tk.Label(self.frame,text="")
        self.label2.pack()
        self.label3 = tk.Label (self.frame,text="Nivel:").pack()
        self.label4 = tk.Label(self.frame,text="")
        self.label4.pack()

        tk.Button(self.frame,text ="Exit",command=self.frame.quit).pack()

        self.update_clock()

        self.root.mainloop()

    def update_clock(self):

        aux = str(self.spin.get())
        aux2 = int (aux)
        time.sleep(aux2 - 1)

        arquivo = open("log.txt", "a+") #C:/path/to/file.txt
        arquivo2 = open("hora.txt", "a+")

        now = datetime.today()
        data = str(now.strftime("%d/%m/%y"))
        horario=str(now.strftime("%H:%M:%S"))
        now = data + " " + horario
        self.label2.configure(text=now)
        arquivo2.write(now + "\n")
        arquivo2.close()

        #Le os valores passados pelo arduino

        dist = objeto_porta.readline()
        dist2 = str(dist, encoding='UTF-8')
        self.label4.configure(text=dist2)
        arquivo.write(dist2)

        arquivo.close()

        self.frame.after(1000, self.update_clock)

#Cria o objeto_porta, limpa o buffer da serial,
objeto_porta = serial.Serial('COM3', 9600)
objeto_porta.flushInput();

app=App()
app.mainloop()

objeto_porta.close()


