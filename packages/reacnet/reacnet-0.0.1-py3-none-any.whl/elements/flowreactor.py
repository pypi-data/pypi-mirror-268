from omnisoot import PlugFlowReactor
from reacnet.connectors.connection import Connection

class FlowReactor:
    core: PlugFlowReactor
    inlet: Connection
        
    def __init__(self, reactor, run_callback):
        self.reactor = reactor;
        self.inlet = Connection(self);
        self.run = run_callback;
        
    @property
    def X(self):
        return self.reactor.X;

    @property
    def Y(self):
        return self.reactor.Y;
    
    @property
    def T(self):
        return self.reactor.T;

    @property
    def P(self):
        return self.reactor.P;
    
    @property
    def soot(self):
        return self.reactor.soot_array;