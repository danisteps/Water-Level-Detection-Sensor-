#-------------------------------------------------------------------------------
# Name:        Arquivo
# Purpose:      DAMPA
#
# Author:      Daniele Passos
#              Amintas Dutra
#              Matheus Monteiro
#              Pedro Souza
#              André Luiz Buarque
#
# Created:     04/09/2013
# Copyright:   (c) DAMPA 2013
# Licence:     DAMPA
#-------------------------------------------------------------------------------

from datetime import datetime
import serial
import time

#Cria o objeto_porta, limpa o buffer da serial,
objeto_porta = serial.Serial('COM3', 9600)
objeto_porta.flushInput();

#Fica em LOOP Infinito, para sair pressione
#Ctrl + c
while True:
        #Abre o arquivo para escrever os dados
        arquivo = open("LOG.txt", "a+")
        #Cria o objeto_hoje, pega os valores de
        #dia, mes, ano e horario, converte para string
        objeto_hoje = datetime.today()
        dia = str(objeto_hoje.day)
        mes = str(objeto_hoje.month)
        ano = str(objeto_hoje.year)
        horario = str(objeto_hoje.strftime("%X"))

        # Le os valores passados pelo arduino
        dist = objeto_porta.readline()
        dist2 = str(dist, encoding='UTF-8')

        #Escreve os dados de HORA, DATA e TEMPERATURA no arquivo
        arquivo.write("Leitura do sensor ultrasonico\n")
        arquivo.write("DATA: ")
        arquivo.write(dia)
        arquivo.write(" / ")
        arquivo.write(mes)
        arquivo.write(" / ")
        arquivo.write(ano)
        arquivo.write("\n")
        arquivo.write("HORA: ")
        arquivo.write(horario)
        arquivo.write("\n")
        arquivo.write(dist2)
        arquivo.write("\n-------------------------------\n")

        #Faz uma pausa de X (tempo informado) segundos para fazer o loop novamente
        time.sleep(1)
        #fecha o arquivo para abrir no proximo loop
        arquivo.close()

#Fecha o arquivo e a porta serial
arquivo.close()
objeto_porta.close()
