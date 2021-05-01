#agentsframework.py

import random                                 #Original, unprotected

class Agent():
    def __init__(self, environment, agents, y , x):
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
        self.environment = environment
        self.agents = agents
        self.store = 0                          

               
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    def eat(self):                                      
        if self.environment[self.y][self.x] > 10:            #if this is true, - 10 and add 10 to the store (initially 0 see above)
            self.environment[self.y][self.x] -= 10           #agents interact with environment and 'eat' it away (remove value)
            self.store += 10                              


    def distance_between(self, agents):
        return (((self.x - agents.x)**2) +
        ((self.y - agents.y)**2))**0.5


    def shared_with_neighbours(self, neighbourhood):
        for agents in self.agents:
            distance = self.distance_between(agents)
            if distance <= neighbourhood:
                if distance > 0:
                    average = ((self.store + agents.store) / 2)
                    self.store = average
                    agents.store = average
                    #print("sharing " + str(distance) + " " + str(average))
            
                
            
            
            
                                                 #Below not working yet
'''import random                                 #New, protected version (using property and get-set)

class Agent():
    def __init__(self):
        self._x = None
        self._y = None
                
    def getx(self):
        return self._x
        
    def gety(self):
        return self._y
        
    def setx(self, value):
        self._x = random.randint(0,99)
        
    def sety(self, value):
        self._y = random.randint(0,99)
        
    def delx(self):
        del self._x
        
    def dely(self):
        del self._y
        
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
    x = property(getx, setx, delx, "X Value")
    y = property(gety, sety, dely, "Y Value")'''
