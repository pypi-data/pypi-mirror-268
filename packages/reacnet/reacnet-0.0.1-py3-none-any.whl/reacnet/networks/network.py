from reacnet.elements import Tank, Mixer, FlowReactor

class Network:
    def __init__(self, first):
        self.elements = [];

    def add_element(self, element):
        self.elements.append(element);


    def check_elements(self):
        if len(self.elements) < 2:
            raise("Network needs at least two elements!");
    
        if not isinstance(self.elements[0], Tank):
            raise("The first element of network must be a Tank!");

        for i in range(len(self.elements)-1):
            if not (self.elements[i].outlet is self.elements[i+1].inlet):
                raise(f"element{i}: {self.elements[i]} is not connected to element{i+1}: {self.elements[i+1]}")