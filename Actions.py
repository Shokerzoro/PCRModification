import matplotlib.pyplot as plt
from numpy import pi

from Samples import DefaultGeom, CreateGeom
from BasicFunctions import ArrowCreate

def ProfilRolling(angle, turns):
    
    for [Geom, Ep, Sat, pins] in CreateGeom(angle, turns):
        X, Y = Ep.Countor()
        plt.plot(X, Y, color="blue", linewidth="0.3")
        X, Y = Sat.Countor()
        plt.plot(X, Y, color="black", linewidth="0.6")
        for pin in pins:
            X, Y = pin.Countor()
            plt.plot(X, Y, color="black")
        
        plt.gca().set_aspect(1)
        plt.show()
        7
def Profil(angle, axes=True, markers=True):
    
    Geom, Ep, Sat, pins = DefaultGeom(angle)
    
    # ------- Настройка графика --------- #
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    ax.set_xticks([])
    ax.set_yticks([])

    # ------- Эпициклоида, сателлит, цевки ----------- #
    X, Y = Ep.Countor()
    ax.plot(X, Y, color="blue", linewidth="0.3", linestyle=":")
    X, Y = Sat.Countor()
    ax.plot(X, Y, color="black", linewidth="0.6")
    for pin in pins:
        X, Y = pin.Countor()
        ax.plot(X, Y, color="black", linewidth="0.6")
    
    # ------- Оси и аннотации ---------- #
    if axes:
        ax.plot([-60, 60], [0, 0], color="black", linestyle="-.", linewidth="0.5")
        ax.plot([0, 0], [-60, 60], color="black", linestyle="-.", linewidth="0.5")
    if markers:
        A = [0, 0]
        ax = ArrowCreate(ax, A, Geom.C(pi*1.7), 0.15)
        ax.text(22, 15, 'P(t)')
        ax = ArrowCreate(ax, A, Geom.P(pi/4.7), 0.15)
        ax.text(-22, 20, 'C(t)')