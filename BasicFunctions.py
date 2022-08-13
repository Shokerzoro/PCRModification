from numpy import linspace, pi, cos, sin
from scipy.interpolate import interp1d
import ReducerData as rd

    
def Modification(self, t):
    return 0.5*cos((t+pi/rd.z_v)*rd.z_v)

def VectorTurn(A, B, fi, Percent):
    x = B[0] - A[0]
    y = B[1] - A[1]
    
    Xrotated = (x*cos(fi) - y*sin(fi))*Percent
    Yrotated = (x*sin(fi) + y*cos(fi))*Percent
    
    return Xrotated, Yrotated

def ArrowCreate(ax, A, B, Percent):
    ArrowAngle = pi/12
    Ax, Ay = A[0], A[1]
    Bx, By = B[0], B[1]
    X, Y = [Ax, Bx], [Ay, By]
    ax.plot(X, Y, color="black") 
    
    X, Y = VectorTurn(A, B, -ArrowAngle, Percent)
    ax.plot([Bx - X, Bx], [By - Y, By], color="black")
    
    X, Y = VectorTurn(A, B, ArrowAngle, Percent)
    ax.plot([Bx - X, Bx], [By - Y, By], color="black")
   
    return ax

def line(self, p1, p2):
        A = (p1[1] - p2[1])
        B = (p2[0] - p1[0])
        C = (p1[0]*p2[1] - p2[0]*p1[1])
        return A, B, -C
        
def intersection(self, L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

def SplineInterpolationParametric(self, Xlist, Ylist):
    t = linspace(0, 2*pi, 2*len(Xlist))
    
    f_cubic_x = interp1d(t, Xlist, kind='cubic')
    f_cubic_y = interp1d(t, Ylist, kind='cubic')        
    x_int = f_cubic_x(t)
    y_int = f_cubic_y(t)
    
    return x_int, y_int

def RandomAddiction(self):
    pass
    
