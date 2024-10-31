"""The `Zodiacs` module contains enumerations for the 12 zodiac signs of the solar system.
It provides an interface for manipulating astrological and planetary data.

@author nrosenthal
@version 1.0
@since 2024-10-29
"""

import datetime
from enum import Enum;


class Zodiacs(Enum):
    """The `Zodiacs` class represents the 12 zodiac signs of the solar system.
    """
    ARIES = 1;
    TAURUS = 2;
    GEMINI = 3;
    CANCER = 4;
    LEO = 5;
    VIRGO = 6;
    LIBRA = 7;
    SCORPIO = 8;
    SAGITTARIUS = 9;
    CAPRICORN = 10;
    AQUARIUS = 11;
    PISCES = 12;
    

    def __str__(self):
        return self.name;
    
    def __repr__(self):
        return self.__str__();
    
    @staticmethod
    def from_index(index:int):
        """Returns the `Zodiacs` enumeration value at the given index.
        
        Args:
            index (int): The index of the enumeration value to be returned.
        
        Returns:
            Zodiacs: The `Zodiacs` enumeration value at the given index.
        
        Raises:
            ValueError: If the index is not valid for the `Zodiacs` enumeration.
        """
        if index < 1 or index > 12:
            raise ValueError(f"Invalid index: {index}");
        return Zodiacs(index);
    
    @staticmethod
    def from_name(name:str):
        """Returns the `Zodiacs` enumeration value with the given name.
        
        Args:
            name (str): The name of the enumeration value to be returned.
        
        Returns:
            Zodiacs: The `Zodiacs` enumeration value with the given name.
        
        Raises:
            ValueError: If the name is not valid for the `Zodiacs` enumeration.
        """
        for zodiac in Zodiacs:
            if zodiac.name == name:
                return zodiac;
        raise ValueError(f"Invalid name: {name}");
        
    @staticmethod
    def from_english_name(name:str):
        """Returns the `Zodiacs` enumeration value with the given English name.
        
        Args:
            name (str): The English name of the enumeration value to be returned.
        
        Returns:
            Zodiacs: The `Zodiacs` enumeration value with the given English name.
        
        Raises:
            ValueError: If the name is not valid for the `Zodiacs` enumeration.
        """
        for zodiac in Zodiacs:
            if zodiac.name.lower() == name.lower():
                return zodiac;
        raise ValueError(f"Invalid name: {name}");
    
class ZodiacalPosition:
    """The `ZodiacalPosition` class represents the position of a celestial body in the zodiacal system.
    It provides a `zodiac` attribute that represents the zodiac sign of the body,
    and an `angle` attribute that represents the angle of the body relative to the zodiac sign.
    The `ZodiacalPosition` adds a constraint over the `angle` attribute: it must be between 0 and 360 degrees.
    """
    def __init__(self, zodiac:Zodiacs, angle:float):
        """Initializes a `ZodiacalPosition` object with the given `zodiac` and `angle`.
        
        Args:
            zodiac (Zodiacs): The zodiac sign of the celestial body.
            angle (float): The angle of the celestial body relative to the zodiac sign.
        
        Raises:
            ValueError: If the angle is not valid, i.e. not between 0 and 360 degrees.
        """
        self.zodiac = zodiac;
        self.angle = angle;
        
        if self.angle < 0 or self.angle > 360:
            raise ValueError(f"Invalid angle: {angle}");
        
        self.angle = self.angle % 360;
    
    def __str__(self):
        return f"{self.zodiac} ({self.angle}°)";
    
    def __repr__(self):
        return self.__str__();
    
    def xml(self):
        return f"<zodiac>{self.zodiac}</zodiac><angle>{self.angle}</angle>";
    
    def csv(self):
        return f"{self.zodiac},{self.angle}";
    
    def json(self):
        return {"zodiac":self.zodiac, "angle":self.angle};
    
    
#   INTERVAL OF SIGNS IN THE ZODIACAL SYSTEM
CURR_YEAR:int = None;

def setSignsInterval():
    """Sets the global variable `CURR_YEAR` to the current year. This is used in the creation of the `SIGNS` dictionary.
    """
    
    global CURR_YEAR;
    CURR_YEAR = datetime.datetime.now().year;
    
    
setSignsInterval();


SIGNS:dict[Zodiacs, tuple[datetime.datetime, datetime.datetime]] = {
    Zodiacs.ARIES: (datetime.datetime(CURR_YEAR, 3, 21), datetime.datetime(CURR_YEAR, 4, 19)),
    Zodiacs.TAURUS: (datetime.datetime(CURR_YEAR, 4, 20), datetime.datetime(CURR_YEAR, 5, 20)),
    Zodiacs.GEMINI: (datetime.datetime(CURR_YEAR, 5, 21), datetime.datetime(CURR_YEAR, 6, 20)),
    Zodiacs.CANCER: (datetime.datetime(CURR_YEAR, 6, 21), datetime.datetime(CURR_YEAR, 7, 22)),
    Zodiacs.LEO: (datetime.datetime(CURR_YEAR, 7, 23), datetime.datetime(CURR_YEAR, 8, 22)),
    Zodiacs.VIRGO: (datetime.datetime(CURR_YEAR, 8, 23), datetime.datetime(CURR_YEAR, 9, 22)),
    Zodiacs.LIBRA: (datetime.datetime(CURR_YEAR, 9, 23), datetime.datetime(CURR_YEAR, 10, 23)),
    Zodiacs.SCORPIO: (datetime.datetime(CURR_YEAR, 10, 24), datetime.datetime(CURR_YEAR, 11, 21)),
    Zodiacs.SAGITTARIUS: (datetime.datetime(CURR_YEAR, 11, 22), datetime.datetime(CURR_YEAR, 12, 21)),
    Zodiacs.CAPRICORN: (datetime.datetime(CURR_YEAR, 12, 22), datetime.datetime(CURR_YEAR, 1, 19)),
    Zodiacs.AQUARIUS: (datetime.datetime(CURR_YEAR + 1, 1, 20), datetime.datetime(CURR_YEAR + 1, 2, 18)),
    Zodiacs.PISCES: (datetime.datetime(CURR_YEAR + 1, 2, 19), datetime.datetime(CURR_YEAR + 1, 3, 20))
};


def whichSign(date:datetime.datetime) -> Zodiacs:
    """Returns the zodiac sign of the given date.
    
    Args:
        date (datetime.datetime): The date to be used to determine the zodiac sign.
    
    Returns:
        Zodiacs: The zodiac sign of the given date.
    """
    
    for sign in SIGNS:
        if SIGNS[sign][0] <= date <= SIGNS[sign][1]:
            return sign;
        
    raise ValueError(f"Invalid date: {date}");
 
def computeAngle(date:datetime.datetime) -> float:
    """Returns the angle of the Sun in the (astrological; [0, 360]) range for the given date.
    
    Args:
        date (datetime.datetime): The date to be used to determine the angle of the Sun.
    
    Returns:
        float: The angle of the Sun in the (astrological; [0, 360]) range for the given date.
    """
    
    zodiac = whichSign(date);
    sign_start: datetime.datetime = SIGNS[zodiac][0];
    sign_end: datetime.datetime = SIGNS[zodiac][1];
    
    return (date - sign_start).total_seconds() * 360 / (sign_end - sign_start).total_seconds() + 8;

def main():
    #   Module initalization:
    setSignsInterval();         #   Sets the global variable `CURR_YEAR` to the current year
                                #   Runs twice to ensure that the global variable is set correctly
                                #       (i.e. its an artifact)

    #   Guess sign:
    print(whichSign(datetime.datetime.now()));
    
    #   Sun position
    print(computeAngle(datetime.datetime.now()));

    #   Testing:
    print(Zodiacs.ARIES);
    print(Zodiacs.from_index(1));
    print(Zodiacs.from_name("ARIES"));
    
    print(SIGNS);
    
    


    
    

if __name__ == "__main__":
    main();