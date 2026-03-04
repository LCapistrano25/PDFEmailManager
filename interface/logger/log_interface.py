import logging

class ControlLogInterface(ABC):
    def __init__(self, log_level):
        self.log = logging.basicConfig(level=log_level)
    
    @abstractmethod
    def log_info(self, message):
        pass
        
    @abstractmethod
    def log_error(self, message):
        pass

    @abstractmethod 
    def log_warning(self, message):
        pass

    @abstractmethod 
    def log_debug(self, message):
        pass