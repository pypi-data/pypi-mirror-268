import numpy as np

from reacnet.elements import ElementBase, FlowReactor
from reacnet.connectors import Connection

class Mixer(ElementBase):
    def __init__(self, soot_gas, name = ""):
        self.inlets = [];
        self.reactor_inlet = None;
        super().__init__(soot_gas, name);
        
    def add_inlet(self, inlet: Connection):
        self.inlets.append(inlet);
        inlet.downstream = self;
        if isinstance(inlet.upstream, FlowReactor):
            self.reactor_inlet = inlet;
        
    def check_inlets(self):
        if len(self.inlets) < 1:
            raise Exception("mixer needs at least one connected inlet!");
    
    def run(self):
        mdot_total = 0.0;
        species_mdot = np.zeros((self.soot_gas.n_species,));
        h_mol_array_combined = np.zeros((self.soot_gas.n_species,));
        h_mass_total = 0.0;
        P_max = 0.0;
        for inlet in self.inlets:
            mdot_total += inlet.mdot;
            species_mdot += inlet.Y * inlet.mdot;
            h_mass_total += inlet.h_mass_total * inlet.mdot;
            h_mol_array_combined += inlet.h_mol_array * inlet.mdot
            P_max = max(P_max, inlet.P);
                
        self._Y = species_mdot / mdot_total;
        self._P = P_max;
        self.mdot = mdot_total
        self._h_mass_total = h_mass_total / mdot_total;
        self._h_mol_array = h_mol_array_combined / mdot_total;
        
        self.soot_gas.HPY = self.h_mass_total, self.P, self.Y
        self._T = self.soot_gas.T;
        self._X = self.soot_gas.X;
        
        if self.reactor_inlet:
            self.soot = self.reactor_inlet.mdot * self.reactor_inlet.soot / mdot_total;
            
def check_reactor(inlet: Connection):
    if isinstance(inlet.upstream, FlowReactor):
        return 1;
    else:
        return 0;