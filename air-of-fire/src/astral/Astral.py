"""The `Astral.py` module is a collection of classes and functions for working with astrological and planetary data.

@author nrosenthal
@version 1.0
@since 2024-10-28
"""

from Planets import     Planets, PlanetaryHour, PlanetaryHours;
from Timing import      Timing, Duration;
from Zodiacs import     Zodiacs, ZodiacalPosition;

class PositionedPlanet:
    """A `PositionedPlanet` is a `Planet` associated with a `ZodiacalPosition`. It should be understood as a planet at a specific position in the zodiacal sign.
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-29
    """
    def __init__(self, planet:Planets, position:ZodiacalPosition):
        self.planet = planet;
        self.position = position;
        
    def __str__(self):
        return f"{self.planet.name} {self.position.angle}degrees at {self.position.zodiac.name}";

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
    def __init__(self, *hours):
        super().__init__(*hours);
        self._max = 25;
        
        if len(self) > self._max:
            raise ValueError(f"Day cannot have more than {self._max} hours");
    
    def __str__(self):
        return f"Day of {len(self)} hours";
    
    def __repr__(self):
        return self.__str__();