import numpy as np
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def T(omega):
     return (1)/(1+1j*(omega)/(10))

array = np.logspace(-1, 3, 5) 
for i in array:
    print('Valeur', i)
    print (bcolors.WARNING, 'Module: ', round(np.abs(T(i)), 3), bcolors.ENDC)
    print ('Phase: ', round(np.angle(T(i)), 3))
    print('-----------------')