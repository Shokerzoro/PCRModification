import ReducerData as rd
import BasicFunctions as bf
import numpy as np

class MainFunctions():
    
    def CDefault(self, t):
        Cx = np.sin(t)*rd.a_p/2 - rd.e*np.sin(rd.z_p*t)
        Cy = np.cos(t)*rd.a_p/2 - rd.e*np.cos(rd.z_p*t)
        return Cx, Cy
    
    def NDefault(self, t):
        A = (1+rd.lam**2-2*rd.lam*np.cos(rd.z_v*t))**(-1/2)
        Nx = A*(-np.sin(t)+rd.lam*np.sin(rd.z_p*t))
        Ny = A*(-np.cos(t)+rd.lam*np.cos(rd.z_p*t))
        return Nx, Ny
    
    def PDefault(self, t):
        Cx, Cy = self.CDefault(t)
        Nx, Ny = self.NDefault(t)
        Px = Cx + Nx*(rd.d_p/2)
        Py = Cy + Ny*(rd.d_p/2)
        return Px, Py
    
    def PModificated(self, t):
        Px, Py = self.PDefault(t)
        Nx, Ny = self.NDefault(t)
        PMx = Px + Nx*(bf.Modification(t%(2*np.pi/rd.z_v)))
        PMy = Py + Ny*(bf.Modification(t%(2*np.pi/rd.z_v)))
        return PMx, PMy
    
    def ContactStiffnes(self, t):
        pass

    
    def Intersection(self, points):
        [[N1x, N1y], [N2x, N2y], [Centr1x, Centr1y], [Centr2x, Centr2y]] = points
        A1, A2 = [Centr1x, Centr1y], [Centr1x + N1x, Centr1y + N1y]
        B1, B2 = [Centr2x, Centr2y], [Centr2x + N2x, Centr2y + N2y]
        return bf.intersection(bf.line(A1, A2), bf.line(B1, B2))
            
    
##############---------------------------------------------########################3

MF = MainFunctions()  