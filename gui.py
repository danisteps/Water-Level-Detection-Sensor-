import Tkinter as tk
import time
from datetime import datetime
#import serial

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.logo = tk.PhotoImage(file="C:\Python27\dampa2.gif")
        self.w1 = tk.Label(image=self.logo).pack()
        self.label1 = tk.Label (text="Atualizado em:").pack()
        self.label2 = tk.Label(text="")
        self.label2.pack()
        self.label3 = tk.Label (text="Nivel:").pack()
        self.label4 = tk.Label(text="")
        self.label4.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        #arquivo = open("LOG.txt", "a+") #C:/path/to/file.txt
        now = datetime.today()
        self.label2.configure(text=now)

        # Le os valores passados pelo arduino
        #dist = objeto_porta.readline()
        #dist2 = str(dist, encoding='UTF-8')
        #self.label4.configure(text=dist2)
        #arquivo.write(dist2)
        #arquivo.close()

        self.root.after(1000, self.update_clock)


#Cria o objeto_porta, limpa o buffer da serial,
#objeto_porta = serial.Serial('COM3', 9600)
#objeto_porta.flushInput();
app=App()
app.mainloop()
#objeto_porta.close()