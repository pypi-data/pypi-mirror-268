from reacnet.elements import ElementBase

class Tank(ElementBase):    
    def __init__(self, soot_gas, name = ""):
        super().__init__(soot_gas, name);
    
    @property
    def X(self):
        return self._X;
    
    @property
    def Y(self):
        return self._Y;

    @X.setter
    def X(self, X):
        soot_gas = self.soot_gas;
        soot_gas.X = X;
        self._X = soot_gas.X
        self._Y = soot_gas.Y
        
    @Y.setter
    def Y(self, Y):
        soot_gas = self.soot_gas;
        soot_gas.Y = Y;
        self._Y = soot_gas.Y
        self._X = soot_gas.X

    @property
    def TPX(self):
        return self._T, self._P, self._X;

    @TPX.setter
    def TPX(self, TPX):
        soot_gas = self.soot_gas;
        soot_gas.TPX = TPX;
        self._T = TPX[0];
        self._P = TPX[1];
        self._Y = soot_gas.Y;
        self._X = soot_gas.X;
        self._h_mol_array = self.soot_gas.h_mol_array;
        self._h_mass_total = self.soot_gas.h_mass_total;

    @property
    def TPY(self):
        return self._T, self._P, self._Y;

    @TPY.setter
    def TPY(self, TPY):
        soot_gas = self.soot_gas;
        soot_gas.TPY = TPY;
        self._T = TPY[0];
        self._P = TPY[1];
        self._Y = soot_gas.Y
        self._X = soot_gas.X
        self._h_mol_array = self.soot_gas.h_mol_array;
        self._h_mass_total = self.soot_gas.h_mass_total;