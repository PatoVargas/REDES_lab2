"""
Codigo elaborado por Patricio Vargas Pino, rut : 18455204-3 y que se desarrolla 
para completar la experiencia correspondiente al laboratorio dos de redes de computadores 
en la cual se debe procesar una señal de audio utilizando un filtro FIR.
La construcción de este programa se realiza reutilizando código del primer laboratorio pertenenciente al propio estudiante.
"""
#Importaciones
import numpy as np
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt
from funciones import *

#Datos del audio#
rate,info=read("beacon.wav") 
plt.rcParams['agg.path.chunksize'] = 100000 #se ajusta para visualizar los datos

#Primer grafico#
primerGrafico(info,rate)

#transformada fe fourier#
signal =info[:,1]
transformada = transformadaFourier(signal,rate)
#print(transformada)

#Parametros que se modifican para cambiar el filtro#
lowcut = 20000.0
highcut = 22000.0

#Filtro de la señal
y = aplicarFiltro(lowcut,highcut,transformada,rate)

#Transformada inversa despues del filtro 
W = np.fft.ifft(y)
graficarNuevoEspectro(W,rate)

#Para guardar la señal filtrada en un audio de extensión wav
data2 = np.array(W, dtype=np.int16)
write('prueba_20000_22000.wav', rate, data2)