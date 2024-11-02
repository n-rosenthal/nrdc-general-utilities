import json;
import xml;
import csv;

class Storable:
    """The Storable interface provides abstract methods for storing objects
    """
        
    def json(self) -> dict:
        pass;
    
    def xml(self) -> str:
        pass;
    
    def csv(self) -> str:
        pass;

