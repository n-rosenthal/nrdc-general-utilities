"""The `Astral.py` module is a collection of classes and functions for working with astrological and planetary data.

@author nrosenthal
@version 1.0
@since 2024-10-28
"""

from Planets import     Planets, PlanetaryHour, PlanetaryHours;
from Timing import      Timing, Duration;
from Zodiacs import     Zodiacs, ZodiacalPosition
import datetime;

class AstralError(Exception):
    """Base class for all exceptions raised by the `Astral` module."""
    pass;
    

class PositionedPlanet:
    """A `PositionedPlanet` is a `Planet` associated with a `ZodiacalPosition`. It should be understood as a planet at a specific position in the zodiacal sign.
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-29
    """
    def __init__(self, planet:Planets, position:ZodiacalPosition, direction: str = "ascendant"):
        self.planet = planet;
        self.position = position;
        self.direction = direction;
        
    def __str__(self):
        return f"{self.planet.name} {self.direction} {self.position.angle}degrees at {self.position.zodiac.name}";

    def __repr__(self):
        return self.__str__();
    
    def xml(self):
        return f"<PPlanet>\n\t<planet>{self.planet.name}</planet>\n\t<zodiac>{self.position.zodiac.name}</zodiac>\n\t<angle>{self.position.angle}</angle>\n</PPlanet>";
    
    def csv(self):
        return f"{self.planet.name},{self.position.zodiac.name},{self.position.angle}";
    
    def json(self):
        return {"planet":self.planet, "zodiac":self.position.zodiac, "angle":self.position.angle};
    
    def __call__(self):
        return self.position, self.planet;
    
    @staticmethod
    def from_xml(xml):
        planet = Planets.from_xml(xml.find("planet").text);
        zodiac = Zodiacs.from_xml(xml.find("zodiac").text);
        angle = float(xml.find("angle").text);
        return PositionedPlanet(planet, ZodiacalPosition(zodiac, angle));
    
    @staticmethod
    def from_csv(csv):
        planet, zodiac, angle = csv.split(",");
        return PositionedPlanet(Planets.from_csv(planet), ZodiacalPosition(Zodiacs.from_csv(zodiac), float(angle)));

    @staticmethod
    def from_json(json):
        return PositionedPlanet(Planets.from_json(json["planet"]), ZodiacalPosition(Zodiacs.from_json(json["zodiac"]), json["angle"]));
    
    
def test_PositionedPlanet():
    test = PositionedPlanet(Planets.MERCURY, ZodiacalPosition(Zodiacs.SCORPIO, 0));
    assert test() == (ZodiacalPosition(Zodiacs.SCORPIO, 0), Planets.MERCURY);
    assert test.xml() == "<PPlanet>\n\t<planet>MERCURY</planet>\n\t<zodiac>SCORPIO</zodiac>\n\t<angle>0</angle>\n</PPlanet>";
    assert test.csv() == "MERCURY,SCORPIO,0";
    assert test.json() == {"planet":Planets.MERCURY, "zodiac":Zodiacs.SCORPIO, "angle":0}    

    test = PositionedPlanet.from_xml("<PPlanet>\n\t<planet>MERCURY</planet>\n\t<zodiac>SCORPIO</zodiac>\n\t<angle>0</angle>\n</PPlanet>");
    assert test() == (ZodiacalPosition(Zodiacs.SCORPIO, 0), Planets.MERCURY);
    

class PlanetaryDay(PlanetaryHours):
    """A `PlanetaryDay` is a subclass of `PlanetaryHours` list that represents a day of planetary hours.
    Its maximum length is 25.
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-29
    """
    def verify(self):
        if len(self) > 25:
            raise AstralError("PlanetaryDay exceeds maximum length of 25 hours");
    
    def __init__(self, *hours):
        super().__init__(*hours);
        
    
    def append(self, hour):
        if len(self) >= 25:
            pass;
        else:
            super().append(hour);
    
    def __str__(self):
        return "\n".join([str(hour) for hour in self]);
    
    def __repr__(self):
        return self.__str__();
    
    def xml(self):
        repr = "<planetary_day>\n";
        for hour in self:
            repr += f"\t{hour.xml()}\n";
        return repr + "</planetary_day>\n";
    
    def csv(self):
        return "\n".join([hour.csv() for hour in self]);
    
    def json(self):
        return [hour.json() for hour in self];
    
def test_PlanetaryDay():
    import datetime;
    import random;
    
    pday = PlanetaryDay();
    
    for i in range(100):
        start = datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 100));
        end = start + datetime.timedelta(minutes=random.randint(0, 100));
        pday.append(PlanetaryHour(Planets.MERCURY, start, end));

class ZodiacalSky:
    """A `ZodiacalSky` is a list of `PositionedPlanet` objects.
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-29
    """
    def __init__(self, *planets):
        self.planets = planets;
    
    def __str__(self):
        sky: str = "";
        
        for planet in self.planets:
            if(planet.direction == "retrograde"):
                sky += f"{planet.planet.name:<10} (R) at {planet.position.angle:>3}° {planet.position.zodiac:>14}\n";
            else:
                sky += f"{planet.planet.name:<14} at {planet.position.angle:>3}° {planet.position.zodiac:>14}\n";
        
        return sky;
    
    def __repr__(self):
        return self.__str__();

ZODIACAL_SKY__30_10_2024:ZodiacalSky = ZodiacalSky(
    PositionedPlanet(Planets.SUN, ZodiacalPosition(Zodiacs.SCORPIO,         8)),
    PositionedPlanet(Planets.MOON, ZodiacalPosition(Zodiacs.LIBRA,          20)),
    PositionedPlanet(Planets.MERCURY, ZodiacalPosition(Zodiacs.SCORPIO,     25)),
    PositionedPlanet(Planets.VENUS, ZodiacalPosition(Zodiacs.SAGITTARIUS,   15)),
    PositionedPlanet(Planets.MARS, ZodiacalPosition(Zodiacs.CANCER,         28)),
    PositionedPlanet(Planets.JUPITER, ZodiacalPosition(Zodiacs.GEMINI,      20),     "retrograde"),
    PositionedPlanet(Planets.SATURN, ZodiacalPosition(Zodiacs.PISCES,       12),     "retrograde"),
);


if __name__ == "__main__":
    print(ZODIACAL_SKY__30_10_2024);