class Connection:
    def __init__(self, upstream, name = ""):
        self.upstream = upstream;
        self.downstream = None;
        self.name = name;
            
    @property
    def X(self):
        return self.upstream.X;
    
    @property
    def Y(self):
        return self.upstream.Y;
    
    @property
    def T(self):
        return self.upstream.T;
    
    @property
    def P(self):
        return self.upstream.P;
    
    @property
    def P(self):
        return self.upstream.P;
    
    @property
    def h_mass_total(self):
        return self.upstream.h_mass_total;
    
    @property
    def h_mol_array(self):
        return self.upstream.h_mol_array;
    
    @property
    def mdot(self):
        return self.upstream.mdot;
    
    @property
    def soot(self):
        return self.upstream.soot;