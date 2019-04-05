import numpy as np

def pseudorapidity(x, y, z):
    mag = np.sqrt(x**2 + y**2 + z**2)
    costheta = np.ones_like(x)
    costheta = np.divide(z, mag, out=costheta, where=mag!=0)
    frac = np.full_like(x, np.nan)
    frac = np.divide(1-costheta, 1+costheta, out=frac, where=np.abs(costheta)<1)
    return -0.5 * np.log(frac)
