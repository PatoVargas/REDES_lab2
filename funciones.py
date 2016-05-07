from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt
import numpy as np

"""
Entrada: arreglo con la información de la señal y la frecuencia de muestreo de esta
Salida: grafico amplitud versus tiempo
Funcion: a partir de las entradas la funcion grafica la señal
"""
def primerGrafico(signal,frecuencia):
	plt.title('Amplitud vs Tiempo')
	plt.xlabel('Tiempo (s)')
	plt.ylabel('f(t)')
	Tiempo=np.linspace(0, len(signal)/frecuencia, num=len(signal))
	plt.plot(Tiempo,signal)
	plt.show()


"""
Entrada: info del audio y la frecuencia
Salida: gráfico de la transformada de fourier
Funcion: realizar la transformada de fourier, guardar en Z y posteriormente graficar
"""
def transformadaFourier(signal,frecuencia):
	largo_n = signal.size 
	k = arange(largo_n) #crear un arreglo del tamaño de la señal
	T = largo_n/frecuencia #Periodo es igual al largo partido la frecuencia
	frq = k/T #Se asigna una frecuencia a cada elemento de k
	Y = fft(signal) #Transformada de fourier de la señal
	plot(frq,Y,'g') #Grafico de la transformada dejando solo la parte positiva
	title('Transformada de fourier con y sin ruido')
	xlabel('Freq (Hz)') #nombre de los ejes
	ylabel('F (w)')
	#show()
	return Y


"""
Entrada: valor minimo y maximo para el corte, la frecuencia de muestreo y el orden para el filtro
Salida: a y b, el minimo y el maximo para el corte
Funcion: encontrar los límites del corte
"""
def butter_bandpass(lowcut, highcut, rate, order=5):
    nyq = 0.5 * rate
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

"""
Entrada: valor minimo y maximo para el corte, la frecuencia de muestreo, el orden para el filtro y la señal
Salida: señal filtrada
Funcion: realizar el filtro a la señal original. Requiere de los servicios de butter_bandpass
"""
def butter_bandpass_filter(data, lowcut, highcut, rate, order=5):
    b, a = butter_bandpass(lowcut, highcut, rate, order=order)
    y = lfilter(b, a, data)
    return y

"""
Entrada: info del audio
Salida: grafico del espectro truncado
Funcion: graficar el escpectro después de aplicar el filtro
"""
def graficarNuevoEspectro(signal,frecuencia):
	plt.title('Señal filtrada en el dominio del tiempo')
	plt.xlabel('Tiempo (s)')
	plt.ylabel('f(t)')
	Tiempo=np.linspace(0, len(signal)/frecuencia, num=len(signal))
	plt.plot(Tiempo,signal)
	plt.show()

"""
Entrada: minimo, maximo, señal y frecuencia de muestreo
Salida: señal filtrada
Funcion: llamar a las funciones que filtran la señal
"""
def aplicarFiltro(lowcut,highcut,signal,rate):
	largo_n = signal.size 
	k = arange(largo_n) #crear un arreglo del tamaño de la señal
	T = largo_n/rate #Periodo es igual al largo partido la frecuencia
	frq = k/T #Se asigna una frecuencia a cada elemento de k
	y = butter_bandpass_filter(signal, lowcut, highcut,rate, order=1)
	plt.plot(frq, y)
	plt.grid(True)
	plt.axis('tight')
	plt.legend(loc='upper left')
	plt.show()
	return y
