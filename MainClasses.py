import numpy as np

import ReducerData as rd
from MainFunctions import MainFunctions

MF = MainFunctions()

########################################################################################################

class Geometry():
    
    def __init__(self, fi):
        self.fi = fi
        
    def T(self, t):
        return t + self.fi
    
    def C(self, t):
        Cx, Cy = MF.CDefault(self.T(t))
        return Cx, Cy
    
    def N(self, t):
        Nx, Ny = MF.NDefault(self.T(t))
        return Nx, Ny

    def P(self, t):
        Px, Py = MF.PDefault(self.T(t))
        return Px, Py        
    
    def Pmod(self, t):
        Pmodx, Pmody = MF.PModificated(t)
        return Pmodx, Pmody
    
    def Stiffnes(self, t):
        return MF.ContactStiffnes(t)
    
    def Intersecrion(self, pin1, pin2):
        N1x, N1y = self.N(pin1.t)
        Centr1x, Centr1y = pin1.centerX, pin1.centerY
        N2x, N2y = self.N(pin2.t) 
        Centr2x, Centr2y = pin2.centerX, pin2.centerY
        
        return MF.Intersection([[N1x, N1y], [N2x, N2y], [Centr1x, Centr1y], [Centr2x, Centr2y]])


##########################################################################################################

class Epicicloid():
    def __init__(self, geometry):
        self.geometry = geometry
        
    def Countor(self):
        X, Y = list(), list()
        N = np.linspace(0, 2*np.pi, 1000)
        for n in N:
            Xapp, Yapp = self.geometry.C(n)
            X.append(Xapp)
            Y.append(Yapp) 
        return X, Y            
 
 #########################################################################################################           
 
class Satellit():
    def __init__(self, geometry):
        self.geometry = geometry
        
    def Countor(self):
        X, Y = list(), list()
        n = np.linspace(0, 2*np.pi, 10000)
        for n in n:
            Xapp, Yapp = self.geometry.P(n)
            X.append(Xapp)
            Y.append(Yapp)
        return X, Y
            
###########################################################################################################    
    
class Pin():
    def __init__(self, geometry, i):
        self.geometry = geometry
        self.i = i
        self.t = (2*np.pi*i)/rd.z_p + (2*np.pi*0)/rd.z_p
        self.centerX, self.centerY = geometry.C(self.t)
        
    def Countor(self):
        n = np.linspace(0, 2*np.pi, 1000)
        X, Y = list(), list()
        for n in n:
            Xapp = self.centerX + np.cos(n)*rd.d_p/2
            Yapp = self.centerY + np.sin(n)*rd.d_p/2
            X.append(Xapp)
            Y.append(Yapp)
        return X, Y
    
    def Axes(self, geometry):
        Nx, Ny = geometry.N(self.t)
        NormalX = [self.centerX + Nx*rd.d_p/2, self.centerX - Nx*rd.d_p/2]
        NormalY = [self.centerY + Ny*rd.d_p/2, self.centerY - Ny*rd.d_p/2]
        
        Tx, Ty = Nx*np.cos(np.pi/2)+Ny*np.sin(np.pi/2), Ny*np.cos(np.pi/2)-Nx*np.sin(np.pi/2)
        TangenX = [self.centerX + Tx*rd.d_p/2, self.centerX - Tx*rd.d_p/2]
        TangenY = [self.centerY + Ty*rd.d_p/2, self.centerY - Ty*rd.d_p/2]
        
        return [NormalX, NormalY, TangenX, TangenY]
    
    def FSinusoudal(self):
        check = self.WorkCheck()
        if check:
            A = 4*rd.Ts/(rd.e*rd.z_p*rd.z_v)
            F = A*(np.sin(rd.z_v*self.t))*(1+rd.lam**2-2*rd.lam*np.cos(rd.z_v*self.t))**(-1/2)
            return F
            
    def WorkCheck(self):
        Px, Py = self.geometry.P(self.t)
        Nx, Ny = self.geometry.N(self.t)
        delta = (Px*Ny - Py*Nx)
        if delta >= 0:
            return True
        else:
            return False

    
        
      
    
    #####################################################################################################