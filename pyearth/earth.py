''' 
Constants and simple functions to compute
earth's parameters.

The constants are based on Jinbo Wang's popy toolbox.

'''

import numpy as np
from numpy import pi, sin, cos

class Constants():
    """ A class that represent earth constants """
    
    def __init__(self):

        self.radius_mean =             6371.0e3             # [m]
        self.radius_equatorial =       6378.0e3             # [m]
        self.radiu_polar =             6356.9e3             # [m]
        self.surface_area =            510072000.0e6        # [m^2]
        self.surface_area_land =       148940000.0e6        # [m^2]
        self.surface_area_water =      361132000.0e6        # [m^2]
        self.volume =                  1.08321e21           # [m^2]
        self.mass =                    5.9736e24            # [kg]
        self.density_mean =            5.515e3              # [km/m^3]
        self.rotation_period = 23.*3600 + 56.*60 + 4.1      # [s]
        self.omega = 2*pi/(23.*3600 + 56.*60 + 4.1)         # [rad/s]
        self.g = 9.780327                                   # [m/s^2]

class Betaplane():
    """ A class that represents parameters of the beta plane
        centered at lat"""

    def __init__(self,lat):

        const = Constants()
        self.f0 = 2.*const.omega*sin(lat*pi/180.)
        self.beta = 2*const.omega*cos(lat*pi/180)/const.radius_mean

