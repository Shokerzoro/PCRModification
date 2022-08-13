import MainClasses as mc
from numpy import linspace

#---- Создание геометрии ---------------------------------------------------------------

def DefaultGeom(angle):
    Geom = mc.Geometry(angle)
    Ep = mc.Epicicloid(Geom)
    Sat = mc.Satellit(Geom) 
    pins = [mc.Pin(Geom, i) for i in range(0, 25)]
    
    return Geom, Ep, Sat, pins

#---------- Генератор геометрии с поворотом обоймы ------------------------------------

def CreateGeom(angle, turns):
    
    Fi = linspace(0, angle, turns)
    for fi in Fi:
        Geom = mc.Geometry(fi)
        Ep = mc.Epicicloid(Geom)
        Sat = mc.Satellit(Geom) 
        pins = [mc.Pin(Geom, i) for i in range(0, 24)]
        
        yield [Geom, Ep, Sat, pins]
        
##### ------------- Получение данных для расчета --------- #############3        

def GetData(angle):
    
    Geom = mc.Geometry(angle)
    pins = [mc.Pin(Geom, i) for i in range(0, 25)]
    
    for pin in pins:
        if pin.WorkCheck():
            C = pin.centerX, pin.centerY
            N = Geom.N(pin.t)
            E = Geom.P(pin.t)
            Emod = Geom.Pmod(pin.t)
            f = ((Emod[0] - E[0])**2 + (Emod[1] - E[1])**2)**(1/2)
            k = Geom.Stiffnes(pin.t)
            
            yield C, N, E, f, k