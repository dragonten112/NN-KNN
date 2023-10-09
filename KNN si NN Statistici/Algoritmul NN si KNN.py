
import cv2
from matplotlib import pyplot as plt
import numpy as np
from numpy import linalg as la
import statistics
import time
import os
import statistics as st

caleBD = 'C:\\Users\\razva\\OneDrive\\Desktop\\Facultate\\att_faces\\'

nrPozeAntrenare = 8
nrPers = 40
nrPixeli = 10304
poza_test='C:\\Users\\razva\\OneDrive\\Desktop\\Facultate\\att_faces\\s1\\9.pgm'
poza_test=cv2.imread(poza_test,0)
poza_test=np.array(poza_test)
poza_test=np.reshape(poza_test,(-1,))
nrPozaPers=10

def configurareA(caleBD):
    A = np.zeros ((nrPixeli, nrPozeAntrenare * nrPers))
    #cazul cel mai simplu: retin in A primele nrPozeAntrenare poze ale fiecarei persoane i
    for i in range(1, nrPers + 1):
        caleFolder = caleBD + 's' + str(i) + '\\'
        for j in range (1, nrPozeAntrenare + 1):
            cale_poza = caleFolder + str(j) + '.pgm'
            poza = cv2.imread(cale_poza, 0)
            poza = np.array(poza)
            pozaVect = np.reshape (poza, (nrPixeli, ))
            A[:,(i-1) * nrPozeAntrenare + (j-1)] = pozaVect
    print(np.shape(A))
    return A
A=configurareA(caleBD) 

def NN(A,poza_test,norma):
    z=np.zeros(len(A[0]))
    for i in range(0,len(A[0])):
        if(norma=='cos'):
            z[i]=1-np.dot(A[:,i],poza_test)/(la.norm(A[:,i])*la.norm(poza_test))
        else:
            z[i]=la.norm(A[:,i]-poza_test)
    pozitia=np.argmin(z)
    pozaGasita = np.reshape(A[:, pozitia], (112, 92))
    plt.imshow(pozaGasita, cmap='gray')
    plt.show()
    return pozitia



def KNN(A,poza_test,norma,k):
    z=np.zeros(len(A[0]))
    for i in range(0,len(A[0])):
        z[i]=la.norm(A[:,i]-poza_test)
    pozitii=np.argsort(z)
    pozitii=pozitii[:k]
    persoane=pozitii//8+1
    persoana=statistics.mode(persoane)
   
    
    return (persoana-1)*8

def rr_tmi(A, norma, k):
    timpiInterogare = []
    nrTotalTeste = nrPers * (10 - nrPozeAntrenare)
    nrRecunoasteriCorecte = 0
    for i in range(1, nrPers + 1):
        caleFolder = caleBD + 's' + str(i) + '\\'
        for j in range(nrPozeAntrenare + 1, nrPozaPers + 1):
            calePozaTest = caleFolder + str(j) + '.pgm'
            pozaTest = cv2.imread(calePozaTest, 0)
            pozaTest = np.array(pozaTest)
            pozaTest = np.reshape(pozaTest, (-1, ))
            
            t0 = time.perf_counter()
            pozitia = KNN(A, pozaTest, norma, k)
            t1 = time.perf_counter()
            t = t1 - t0
            timpiInterogare.append(t)
            
            persoana = pozitia // 8 + 1
            if persoana == i:
                nrRecunoasteriCorecte += 1
                
    rr = nrRecunoasteriCorecte/nrTotalTeste
    # print(f'Rata de recunoastere: {rr:.8f}')
    tmi = st.mean(timpiInterogare)
    # print(f'Timp mediu de interogare: {tmi:8f}')
    return rr, tmi

A = configurareA(caleBD)
pas = 2

valk = np.arange(3,10,pas)
norme = [1,2,np.inf,'cos']

RR = np.zeros((4,4))
TMI = np.zeros((4,4))

for k in valk:
    print(k)
    for norma in norme:
        if norma == 1:
            indiceCol = 0
        elif norma == 2:
            indiceCol = 1
        elif norma == np.inf:
            indiceCol = 2
        else:
            indiceCol = 3

        rr, tmi = rr_tmi(A, norma, k) 
        RR[k//pas - 1, indiceCol] = rr
        TMI[k//pas - 1, indiceCol] = tmi
        # print(f'Norma {norma} -> Rata de recunoastere: {rr:.8f}')
        # print(f'Norma {norma} -> Timp mediu de interogare: {tmi:8f}')
        # print()

valk = valk.reshape(-1,1)
RR = np.hstack((valk, RR))
TMI = np.hstack((valk, TMI))

RR_save = np.savetxt('ORL_8_KNN_RR.txt', RR, fmt='%10.9f')
TMI_save = np.savetxt('ORL_8_KNN_TMI.txt', TMI, fmt='%10.9f')    

print(NN(A,poza_test,'cos'))
pozitia=KNN(A,poza_test,1,3)

 
pozaGasita = np.reshape(A[:, pozitia], (112, 92))
plt.imshow(pozaGasita, cmap='gray')
plt.show()





































