import numpy as np
from omnisoot import SootGas
from reacnet.connectors import Connection

class ElementBase:    
    def __init__(self, soot_gas, name = ""):
        self.soot_gas = soot_gas
        self._Y = soot_gas.Y;
        self._X = soot_gas.X;
        self._T = soot_gas.T;
        self._P = soot_gas.P;
        self._h_mass_total = soot_gas.h_mass_total;
        self._h_mol_array = soot_gas.h_mol_array;
        self._soot = None;
        self._mdot = 0.0;
        self.name = name; 
        self.outlet = Connection(upstream = self);
        super().__init__()


    @property
    def mdot(self):
        return self._mdot;
        
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

    @property
    def soot(self):
        return self._soot;

    def __str__(self):
        return self.name;

    def run(self):
        pass;
    
    def _success_message(self):
        print(f"{self.name} was successfully run!");
    
    def _start_message(self):
        print(f"{self.name} was started!");

    def _run_upstream(self):
        if hasattr(self, "inlet"):
            self.inlet.upstream.run();
        elif hasattr(self, "inlets"):
            for inlet in self.inlets:
                inlet.upstream.run();
        else:
            pass;