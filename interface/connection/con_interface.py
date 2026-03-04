from abc import ABC, abstractmethod

class ConnectionInterface(ABC):
 
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
    
