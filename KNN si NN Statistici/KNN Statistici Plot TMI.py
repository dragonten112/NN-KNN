import numpy as np
import matplotlib.pyplot as plt

norme = [1,2,np.inf,'cos']
valk = np.arange(3,10,2)
font1 = {'weight': 'bold'}

TMI = np.loadtxt('ORL_8_KNN_TMI.txt')

plt.subplots(figsize=(8, 8))

plt.subplot(2,2,1)
plt.plot(norme, TMI[0,1:], marker = 'o', ms=10)
plt.title(f'K = {valk[0]}', font1)
plt.xlabel('Norme', font1)

plt.subplot(2,2,2)
plt.plot(norme, TMI[1,1:], marker = 'o', ms=10)
plt.title(f'K = {valk[1]}', font1)
plt.xlabel('Norme', font1)

plt.subplot(2,2,3)
plt.plot(norme, TMI[2,1:], marker = 'o', ms=10)
plt.title(f'K = {valk[2]}', font1)
plt.xlabel('Norme', font1)

plt.subplot(2,2,4)
plt.plot(norme, TMI[3,1:], marker = 'o', ms=10)
plt.title(f'K = {valk[3]}', font1)
plt.xlabel('Norme', font1)

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
plt.suptitle('Timpi de interogare', fontweight = 'bold', fontsize = 16)
plt.show()
