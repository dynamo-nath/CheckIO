# o'reilly island

class Friends:
    
    def __init__(self):
        self.connections = []
        
    def add(self, buddy):
        count = 0
        for x in range(0, len(self.connections)):
            if buddy == self.connections[x]:
                count += 1
        if count == 0:
            self.connections.append(buddy)
            return True
        else:
            return False
        
    def connected(self):
        return self.connections
    
    def names(self):
        n = {}
        for x in range(1, len(self.connections)):
            n = self.connections[x-1] & self.connections[x]
            print(n)
    
    
f = {'a', 'c'}
g = {'x', 'p'}
g1 = {'p', 'x'}
h = {'c', 'd'}
a = Friends()
print(a.add(f))
print(a.add(g))
print(a.add(g1))
a.add(h)
print(a.connected())
print(a.names())