import numpy as np
from omnisoot import SootGas
from reacnet.connectors import Connection

class ElementBase:
    _X: np.ndarray
    _Y: np.ndarray
    _h_mass_total: float
    _h_mol_array: np.ndarray
    _T: float
    _P: float
    mdot: float
    outlet: object
    soot_gas: SootGas
    soot_array: np.ndarray
    name: str
        
    
    def __init__(self, soot_gas, name = ""):
        self.soot_gas = soot_gas
        self._Y = soot_gas.Y;
        self._X = soot_gas.X;
        self._T = soot_gas.T;
        self._P = soot_gas.P;
        self._h_mass_total = soot_gas.h_mass_total;
        self._h_mol_array = soot_gas.h_mol_array;
        self.name = name  
        self.outlet = Connection(upstream = self);
        super().__init__()
        
    @property
    def T(self):
        return self._T;
    
    @property
    def P(self):
        return self._P;
        
    @property
    def h_mass_total(self):
        return self._h_mass_total;
    
    @property
    def h_mol_array(self):
        return self._h_mol_array
    
    @property
    def X(self):
        return self._X;
    
    @property
    def Y(self):
        return self._Y;
