"""The `Planets` module provides information about the planets in the solar system as a tool for astrological and planetary data analysis.

@author nrosenthal
@version 1.0
@since 2024-10-29
"""

from enum import Enum;

class Planets(Enum):
    """Enumeration of the planets in the Chaldean Order, that is, from the slowest to the fastest, as seen from the Earth.
    The Sun and the Moon are included as planets in this system.
    """
    SATURN = 0;
    JUPITER = 1;
    MARS = 2;
    SUN = 3;
    VENUS = 4;
    MERCURY = 5;
    MOON = 6;

    def from_index(index: int):
        """Returns the `Planets` enumeration value at the given index.
        
        Args:
            index (int): The index of the enumeration value to be returned.
        
        Returns:
            Planets: The `Planets` enumeration value at the given index.
        
        Raises:
            ValueError: If the index is not valid for the `Planets` enumeration.
        """
        for planet in CHALDEAN_ORDER:
            if planet.value == index:
                return planet;
        raise ValueError(f"Invalid index: {index}");
    
    @staticmethod
    def from_name(name:str):
        """Returns the `Planets` enumeration value with the given name.
        
        Args:
            name (str): The name of the enumeration value to be returned.
        
        Returns:
            Planets: The `Planets` enumeration value with the given name.
        """
        return Planets[name.upper()];
    
    def __str__(self):
        """Returns a string representation of the `Planets` enumeration value.
        
        Returns:
            str: A string representation of the `Planets` enumeration value.
        """
        return self.name;
    
    def __repr__(self):
        """Returns a string representation of the `Planets` enumeration value.
        
        Returns:
            str: A string representation of the `Planets` enumeration value.
        """
        return self.name;
    
    def __int__(self):
        """Returns the integer value of the `Planets` enumeration value.
        
        Returns:
            int: The integer value of the `Planets` enumeration value.
        """
        return self.value;

    @staticmethod
    def from_weekday(weekday:int):
        """Returns the `Planets` enumeration value corresponding to the given weekday.
        
        Args:
            weekday (int): The weekday to be converted to a `Planets` enumeration value.
        
        Returns:
            Planets: The `Planets` enumeration value corresponding to the given weekday.
        """
        if weekday == 0:
            return Planets.SUN;
        elif weekday == 1:
            return Planets.MOON;
        elif weekday == 2:
            return Planets.MERCURY;
        elif weekday == 3:
            return Planets.VENUS;
        elif weekday == 4:
            return Planets.MARS;
        elif weekday == 5:
            return Planets.JUPITER;
        elif weekday == 6:
            return Planets.SATURN;
        else:
            raise ValueError(f"Invalid weekday: {weekday}");


#   Useful constants

CHALDEAN_ORDER:list[Planets] = [Planets.SUN, Planets.MOON, Planets.MERCURY, Planets.VENUS, Planets.MARS, Planets.JUPITER, Planets.SATURN];
"""`CHALDEAN_ORDER` is a list of the planets in the Chaldean Order, that is, from the slowest to the fastest, as seen from the Earth. The Sun and the Moon are included as planets in this system."""

WEEKDAY_TO_PLANET:dict[int, Planets] = {0: Planets.SUN, 1: Planets.MOON, 2: Planets.MERCURY, 3: Planets.VENUS, 4: Planets.MARS, 5: Planets.JUPITER, 6: Planets.SATURN};
"""`WEEKDAY_TO_PLANET` is a dictionary that maps each weekday to the corresponding planet in the Chaldean Order."""


#   Translation functions
def get_planet_name(planet:Planets) -> str:
    """Returns the name of the given `Planets` enumeration value.
    
    Args:
        planet (Planets): The `Planets` enumeration value to be translated.
        
    Returns:
        str: The name of the given `Planets` enumeration value.
    """
    match(planet.name):
        case "SATURN":
            return "Saturn";
        case "JUPITER":
            return "Jupiter";
        case "MARS":
            return "Mars";
        case "SUN":
            return "Sun";
        case "VENUS":
            return "Venus";
        case "MERCURY":
            return "Mercury";
        case "MOON":
            return "Moon";
        case _:
            raise ValueError(f"Invalid planet: {planet}");
        
def planet_to_pt_br(planet_name: str) -> str:
    """Returns the name of the given `Planets` enumeration value in Portuguese-Brazilian translation.
    
    Args:
        planet_name (str): The name of the `Planets` enumeration value to be translated.
        
    Returns:
        str: The name of the given `Planets` enumeration value in Portuguese-Brazilian translation.
    """
    match(planet_name):
        case "Saturn":
            return "Saturno";
        case "Jupiter":
            return "Júpiter";
        case "Mars":
            return "Marte";
        case "Sun":
            return "Sol";
        case "Venus":
            return "Venus";
        case "Mercury":
            return "Mercúrio";
        case "Moon":
            return "Lua";
        case _:
            raise ValueError(f"Invalid planet: {planet_name}");
   
def planet_to_en(planet_name: str) -> str:
    """Returns the name of the given `Planets` enumeration value in English translation.
    
    Args:
        planet_name (str): The name of the `Planets` enumeration value to be translated.
        
    Returns:
        str: The name of the given `Planets` enumeration value in English translation.
    """
    match(planet_name):
        case "Saturno":
            return "Saturn";
        case "Júpiter":
            return "Jupiter";
        case "Marte":
            return "Mars";
        case "Sol":
            return "Sun";
        case "Vênus":
            return "Venus";
        case "Mercúrio":
            return "Mercury";
        case "Lua":
            return "Moon";
        case _:
            raise ValueError(f"Invalid planet: {planet_name}");
        

#   Planetary hours
from Timing import Timing, Duration, HOUR_LENGTH, TimingError;
from datetime import datetime, timedelta;

class PlanetaryHour(Duration):
    """A `PlanetaryHour` is a subclass of `Duration` that represents a time interval in planetary hours.
    It provides a `planet` attribute that represents the planet in which the hour occurs.
    The `PlanetaryHour` adds a constraint over the start and end times of the `Duration` object: the duration between `start` and `end` must be less than 2 hours.
    If the duration between `start` and `end` exceeds 2 hours, a `TimingError` is raised.
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-29
    """
    def __init__(self, planet:Planets, start:datetime, end:datetime):
        self._chk(start, end);
        super().__init__(start, end);
        self.planet = planet;
    
    def _chk(self, start:datetime, end:datetime):
        super()._chk(start, end);
        duration = end - start;
        if duration.total_seconds() > (HOUR_LENGTH * 2):
            raise TimingError(f"Duration exceeds 2 hours: {duration}");
        
    def __str__(self):
        return f"{self.planet.name} {super().__str__()}";
    
    def __repr__(self):
        return f"{self.planet.name} {super().__repr__()}";
    
    def xml(self):
        return f"<planetary_hour><planet>{self.planet.name}</planet>{super().xml()}</planetary_hour>";
    
    def csv(self):
        return f"{self.planet.name},{super().csv()}";
    
    def json(self):
        return {
            "planet": self.planet.name,
            "start": super().json()["start"],
            "end": super().json()["end"],
            "duration": super().json()["duration"]
        };
    
class PlanetaryHours(list):
    """
    A `PlanetaryHours` is a subclass of `list` that represents a list of `PlanetaryHour` objects. It provides methods for creating and manipulating `PlanetaryHour` objects in several ways and formats.
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-29
    """
    def __init__(self, *hours:PlanetaryHour):        
        """Initializes a `PlanetaryHours` object with the given `PlanetaryHour` objects.
        
        @param *hours: The `PlanetaryHour` objects to be added to the `PlanetaryHours` object.
        """
        super().__init__(hours);
    
    def __str__(self):
        repr = "";
        for hour in self:
            repr += f"{hour}\n";
        return repr;
    
    def __repr__(self):
        repr = "";
        for hour in self:
            repr += f"{hour}\n";
        return repr;
    
    def csv(self):
        repr = "";
        for hour in self:
            repr += f"{hour.csv()}\n";
        return repr;
    
    def json(self):
        repr = [];
        for hour in self:
            repr.append(hour.json());
        return repr;
    
    def xml(self):
        repr = "<planetary_hours>\n";
        for hour in self:
            repr += f"\t{hour.xml()}\n";
        return repr + "</planetary_hours>\n";
    
    def from_csv(data:str):
        hours = [];
        for row in data.split("\n"):
            hours.append(PlanetaryHour.from_csv(row));
        return PlanetaryHours(*hours);
    
    def from_xml(data:str):
        hours = [];
        for row in data.split("\n"):
            hours.append(PlanetaryHour.from_xml(row));
        return PlanetaryHours(*hours);
    
    def from_json(data):
        hours = [];
        for row in data:
            hours.append(PlanetaryHour.from_json(row));
        return PlanetaryHours(*hours);
        
def getPlanetaryHours(sunrise: datetime, sunset: datetime) -> PlanetaryHours:
    planetary_hours:list[PlanetaryHour] = [];
    
    day_hour_length = (sunset - sunrise) / 12;
    night_hour_length = ((sunrise + timedelta(days=1)) - sunset) / 12;
    
    week_day:int    = sunrise.weekday();
    planet_day:int  = WEEKDAY_TO_PLANET[week_day];
    planet_index:int = planet_day.value;
    
    for i in range(12):
        start = sunrise + (day_hour_length * i);
        end = start + day_hour_length;
        planetary_hours.append(PlanetaryHour(Planets.from_index(planet_index), start, end));
        planet_index += 1;
        if planet_index == 7:
            planet_index = 1;
    for i in range(12):
        start = sunset + (night_hour_length * i);
        end = start + night_hour_length;
        planetary_hours.append(PlanetaryHour(Planets.from_index(planet_index), start, end));
        planet_index += 1;
        if planet_index == 7:
            planet_index = 1;
    return PlanetaryHours(*planetary_hours);

if __name__ == "__main__":
    import datetime;
    import json;
    import time;
    
    start = time.time();
    hours = getPlanetaryHours(datetime.datetime(2024, 10, 30, 6, 0, 0), datetime.datetime(2024, 10, 30, 18, 0, 0));
    end = time.time();
    print(end - start);
    
    
    