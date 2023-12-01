import matplotlib.pyplot as plt
import numpy as np

def fft(x):
    N= len(x)
    #caso base
    if N==1:
        return x
    else: 
        #dividir
        pares = fft(x[::2])
        impares = fft(x[1::2])
        #conquistar
        factor = np.exp(-2j*np.pi*np.arange(N)/N)
        X =np.concatenate([pares+factor[:int(N/2)]*impares,impares+factor[int(N/2)]*impares])
        return X 
factor_muestreo=128
tasa_muestreo = 1.0/factor_muestreo  
freq=1
t=np.arange(0,1, tasa_muestreo)
x=3*np.sin(2*np.pi*freq*t)

X=fft(x)
N=len(X)
i= np.arange(N)
T=N/factor_muestreo
freq=i/T


plt.figure(figsize=(8,6))
plt.plot(t, x,'r')
plt.ylabel('Amplitud')
plt.show

plt.figure(figsize=(8,6))
plt.subplot(121)
plt.stem(freq, np.asb(X),'b')
plt.xlabel('frecuencia Hz')
plt.ylabel('Amplitud FFT')
plt.show
