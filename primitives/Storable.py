class Storable:
    """The Storable interface provides abstract methods for storing objects
    """
    def __init__(self, *args):
        self._args = args;
        
    def json(self) -> dict:
        pass;
    
    def xml(self) -> str:
        pass;
    
    def csv(self) -> str:
        pass;