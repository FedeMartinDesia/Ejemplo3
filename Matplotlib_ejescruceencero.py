import matplotlib.pyplot as plt
import numpy as np

#Crear figura Axes
fig, ax = plt.subplots()

#cambiando la posicion del eje x y para qe se crucen en 0
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))

#eliminando borde superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

#agregando la flecha al final del eje x e y


ax.plot(1, 0, 
        ">k", 
        transform=ax.get_yaxis_transform(), 
        clip_on=False)
ax.plot(0, 1,
        "^k", 
        transform=ax.get_xaxis_transform(), 
        clip_on=False)

#generando datos para graficar la funcion
#100 samples entre -0.5 y 1
x = np.linspace(-0.5, 1., 100)

#plot de la funcion
ax.plot(x, np.sin(x*np.pi))

#mostrar plot
plt.show()
