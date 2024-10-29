"""The `Timing` module provides classes and functions for working with time intervals and durations.
It provides an interface for manipulating astrological and planetary data.

@author nrosenthal
@version 1.0
@since 2024-10-28
"""

from dataclasses import dataclass;
from datetime import datetime;
from zoneinfo import ZoneInfo;
from air-of-fire.src.primitives.Timing import Timing


#   Useful constants
EPOCH:datetime      = datetime(1970, 1, 1, 0, 0, 0, 0, ZoneInfo("UTC"));
HOUR_LENGTH:float   = 3600.0;

#   Error handling
class TimingError(Exception):
    """`TimingError` is a general error class for the `Timing` module.
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-28
    """
    def __init__(self, message:str):
        super().__init__(message);
        
    def __str__(self):
        return self.message;
    
    def __repr__(self):
        return self.message;



#   Utilities
def check_planetary_hour_duration(start: datetime, end: datetime) -> bool:
    """Checks if the given `start` and `end` times are a valid planetary hour.
    The start time must be before the end time and the duration must not exceed 2 hours.
    
    Args:
        start (datetime): The start time of the planetary hour.
        end (datetime): The end time of the planetary hour.
        
    Returns:
        bool: `True` if the given `start` and `end` times are a valid planetary hour, `False` otherwise.
    """
    try:
        planetary_hour_duration = Duration(start, end);
        return planetary_hour_duration >= HOUR_LENGTH * 2;
    except ValueError:
        return False;

@dataclass
class Timing:
    """`Timing` is the base class. It provides an interface for manipulating time intervals and durations.
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-28
    """
    def _chk(self, start:datetime, end:datetime):
        if(start > end):
            raise ValueError("Start time must be before end time");
    
    def __init__(self, start:datetime, end:datetime):
        """Initializes a `Timing` object with the given `start` and `end` timestamps.
        
        @param start: The start timestamp of the `Timing` object.
        @param end: The end timestamp of the `Timing` object.
        """
        self._chk(start, end);
        self.start = start;
        self.end = end;
        
    def __str__(self):
        return f"{self.start} - {self.end}";
    
    def __repr__(self):
        return self.__str__();
    
    def __call__(self) -> tuple[datetime, datetime]:
        return (self.start, self.end);
    
    def xml(self):
        return f"<timing><start>{self.start}</start><end>{self.end}</end></timing>";
    
    def csv(self):
        return f"{self.start},{self.end}";
    
    def json(self):
        return {
            "start": self.start,
            "end": self.end
        };
        
    @staticmethod
    def from_dict(data):
        return Timing(
            datetime.fromisoformat(data["start"]),
            datetime.fromisoformat(data["end"])
        );
        
    @staticmethod
    def from_csv(data):
        return Timing(
            datetime.fromisoformat(data[0]),
            datetime.fromisoformat(data[1])
        );
        
    @staticmethod
    def from_xml(data):
        return Timing(
            datetime.fromisoformat(data.find("start").text),
            datetime.fromisoformat(data.find("end").text)
        );
        
class Duration(Timing):
    def __init__(self, start:datetime, end:datetime):
        super().__init__(start, end);
        
    def __str__(self):
        return f"{self.end - self.start}";
    
    def __repr__(self):
        return self.__str__();
    
    def __call__(self):
        return super().__call__()[1] - super().__call__()[0];
    

      
        