import numpy as np
import matplotlib.pyplot as plt

font1 = {'weight': 'bold'}

RR = np.loadtxt('ORL_8_NN_RR.txt')
norme = [1,2,np.inf,'cos']

plt.subplots(figsize=(8, 8))

plt.subplot(2,1,1)
plt.plot(norme, RR * 100, marker = 'o', ms=10)
plt.xlabel('Norme', font1)
plt.ylabel('Rata de recunoastere(%)', font1)
plt.title('Rata de recunoastere pentru NN', font1)

TMI = np.loadtxt('ORL_8_NN_TMI.txt')
norme = [1,2,np.inf,'cos']

plt.subplot(2,1,2)
plt.plot(norme, TMI, marker = 'o', ms=10)
plt.xlabel('Norme', font1)
plt.ylabel('Timpii de interogare(s)', font1)
plt.title('Timpii de interogare pentru NN', font1)

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
plt.show()