
import numpy as np

def pointPotential(x,y,q,posx,posy): 
    k = 9.e9
    Vxy = ((k*q)/np.sqrt( (x-posx)**2 +(y-posy)**2))
    return Vxy
  


def dipolePotential(x,y,q,d): # finds dipole potential at a certain distance d
    k = 9.e9
    Vxy_2 = (k*q/(y**2+(x-(d/2))**2)**(1/2.)) - (k*q/(y**2+(x+(d/2))**2)**(1/2.))
    return Vxy_2

def pointField(x,y,q,Xq,Yq):
     k = 9.e9
     Ex = (k*q)(x-Xq)/((((x-Xq)**2)+(y-Yq)**2))**(1./2.)
return Ex
     Ey = (k*q)(y-Yq)/((((x-Xq)**2)+(y-Yq)**2))**(1./2.)
return Ey
