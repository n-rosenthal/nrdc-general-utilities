"""The `Zodiacs` module contains enumerations for the 12 zodiac signs of the solar system.
It provides an interface for manipulating astrological and planetary data.

@author nrosenthal
@version 1.0
@since 2024-10-29
"""

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