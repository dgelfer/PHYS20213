import numpy as np

def pointPotential(x,y,q,posx,posy): 
  k = 9e9
  Vxy = ((k*q)/np.sqrt((x-posx)**2)+(y-posy)**2)
  return Vxy
  


def dipolePotential(x,y,q,d): # finds dipole potential at a certain distance d
    k = 9e9
    Vxy_2 = (k*q/(x**2+(y-(d/2))**2)**(1/2.)) - (k*q/(x**2+(y+(d/2))**2)**(1/2.))
    return Vxy_2

